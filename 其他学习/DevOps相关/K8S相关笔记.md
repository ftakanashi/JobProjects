> (1) 深入剖析Kubernetes系列

# K8S基础

> 小小的前情提要：
> 本质上，Docker容器内容可以分成两个部分，一个是由联合挂载等技术得到的镜像层只读rootfs；另一个是通过Cgroup、Namespace等技术实现隔离后的一个可读写的容器层。这两者又分别被称为容器的静态视图（Image）和动态视图（Runtime）。

Kubernetes，简称K8S是Google和RedHat共同主导开发的Docker容器编排管理的项目，其推出主要是为了对抗Docker公司官方的Compose+Swarm。后者虽然和Docker原生结合得更加紧密，但是由于Docker公司政策失误以及项目定位不明确等原因，最终在竞争中败下阵来。
现在，业界容器编排的绝对王者，已经变成了K8S。

## K8S架构

K8S的前身是谷歌内部开发并使用了较久的集群管理与任务调度组件Borg。其基础设计理念也如出一辙。
一般来说，一个K8S的架构是这样的：

<img src="/Users/wyzypa/Pictures/TyporaImages/K8S相关笔记.asset/8ee9f2fa987eccb490cfaa91c6484f67.png" alt="img" style="zoom: 33%;" />

最大的层面，K8S中将主机分成Master和Node两种角色。Master作为控制节点，Node作为计算节点。
Master中主要的组件有三个，分别是

- 负责容器编排管理的kube-controller-manager
- 负责调度的kube-scheduler
- 负责API服务的kube-apiserver

Master负责保存的一些整个集群的meta持久化信息，则通过kube-apiserver保存到etcd中。

在Node中最核心的部分是一个称为kubelet的组件。其主要负责与容器的运行时（Runtime）部分打交道。这主要是通过kubelet访问CRI（Container Runtime Interface）接口完成。
同时，kubelet会通过CNI（Container Network Interface）调用网络插件为容器配置网络，通过CSI（Container Storage Interface）调用存储插件对容器数据进行持久化存储。

需要注意，上面提到的容器是广义的，并非一定是Docker容器。这也是继承了Borg项目的K8S的一个特点，其将关注的重点放在了“工作单位的编排和管理调度”上，至于底层工作的单位是容器还是其他说明他并不关心，只要实现了相关的接口就可以。这也是其理念上和Docker原生的compose+swarm项目不同之处。

## Pod

k8s中，Pod是进行调度的最小单位，也是最小的API对象。
由于容器的本质是进程，而k8s作为调度管理系统，更像是一个轻型的操作系统在管理这些进程。由于进程之间的特殊关系，自然我们就希望能有进程组，而这个进程组就对应到这里的Pod。



# kubeadm部署工具

K8S无论是Master节点还是Node节点，都需要很多组件。因为K8S用了Go语言编写，所以这些组件本质上都是一些二进制文件。
因此，在部署一个K8S集群的时候，最朴素简单的方法，就是将相关的二进制文件传送到服务器上，然后用脚本控制参数，启动这些二进制文件即可。事实上大厂的生产环境也大多使用ansible或者saltstack等工具做这件事。

另一方面，最开始由开源作者贡献，后来逐渐被融入到了K8S原生的kubeadm项目是一个很好的替代品。其实现了快捷简单的k8s部署。

在使用kubeadm前，应该保证机器上已经安装了k8s的完整组件。
安装`kubeadm`很简单，很多包管理软件可以直接安装。如`apt-get install kubeadm`。事实上如果你的机器没有安装k8s相关组件，这个命令也会分析依赖然后自动安装上k8s组件如kubelet, kubectl等二进制文件。

## kubeadm工作原理

抛开k8s的功能不看，单纯将其视为一个软件，部署软件的麻烦，本身就可以通过容器化来解决。即，将每个k8s组件都当成一个容器在相关服务器上启动，这样就可以很大限度的减少环境搭建、配置等工作。
所以这就是个套娃思路，用容器化的方式部署容器管理软件k8s。

在k8s诸多组件中，kubelet是一个比较难以容器化的东西。因为容器化就意味着容器内部的进程无法看到宿主机上的一些内容，而kubelet有时会需要调用如CNI，CSI等接口直接操作宿主机。
作为解决方案，kubeadm做了一个妥协，将kubelet直接运行在宿主机上，其余组件使用容器部署。

接着在master节点上，只要输入命令`kubeadm init`，就可以初始化一个master节点，即部署一个master节点了。
若有需要使用非默认的部署参数（通常都是需要的），则可以写一个yaml文件然后通过`kubeadm init --config xxx.yaml`来实现。

### kubeadm init

简单介绍一下这个命令的工作流程。

- preflight check

  由于这个命令是在初始化master节点，也是部署整个k8s集群的最开始的步骤，所以其会先对当前机器做一个检查称为preflight check。
  检查项包括比如内核版本是否在3.10以上；Cgroup是否可用；kubeadm版本与kubelet版本是否匹配等等。

- 证书生成

  完成preflight check后，kubeadm会生成k8s对外提供服务需要的各种证书与相关目录。
  对集群外的，默认情况下，k8s集群对外服务（入口为kube-apiserver）默认走HTTPS协议。因此需要准备相关的CA证书放到特定的目录下。
  对集群内的，有时master需要通过kube-apiserver向kubelet发起请求，比如查看某些node上的日志等，此时为了保证安全性还需apiserver本身有相关证书。

  当然，如果想要手动配置证书，则可以跳过自动生成证书阶段，手动放入证书到`/etc/kubernetes/pki`中即可。

- 生成apiserver配置文件

  这里，配置文件指其他组件访问apiserver时服务端需要的一些配置文件，全部形如`/etc/kubernetes/xxx.conf`。主要包括了下面四个：

  ```
  admin.conf
  controller-manager.conf
  kubelet.conf
  scheduler.conf
  ```

- 生成master组件配置文件

  之前说过，master上的组件主要是kube-apiserver, kube-controller-manager和kube-scheduler。kubeadm会以pod的形式启动这些组件，在那之前要先生成pod的配置文件。这些文件都是yaml格式，并且被存放在`/etc/kubernetes/manifests`中。

  至于什么是pod，怎么启动pod等，都会在后面详细说。现在只要将pod理解为简单的一个容器即可。

  上面三个组件各自名称`.yaml`，以及一个`etcd.yaml`，这四个文件就是这步的结果。

- 生成Bootstrap token

  生成token后，任何安装了k8s和kubeadm的机器都可以通过持有这个token后发起特定命令而加入到本master下属集群中。

  为什么要这个token呢？因为在最开始的时候，一个新节点想要加入集群，为了保证后续通信安全性，它必须先拿到master的apiserver的相关证书。但是如果要你手动复制证书过去的话又与kubeadm自动化部署的初衷违背。

  所以这里用这个token做一个妥协，复制个token不算大事。而它的作用就是保证了第一次node和master的通信的安全性。

- 安装默认插件

  这是kubeadm init的最后一步，主要是安装kube-proxy和DNS两个插件。本质上这两个插件也是两个pod，所以就直接创建两个pod就完事了。

`kubeadm init`命令执行完后，程序会在控制台上输出包括下面这些信息：

```
kubeadm join 10.168.0.2:6443 --token 00bwbx.uvnaa2ewjflwu1ry --discovery-token-ca-cert-hash sha256:00eb62a...
...
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
```

上面的那个是`kubeadm join`命令，用于在node节点上执行从而加入本集群。可以记下来待会儿在node节点执行。

下面三行，则是提示你手动执行一些配置命令。这些命令在做的事，主要是为将master访问集群必须的配置文件放置到k8s默认的位置`~/.kube`中去，这样本用户就可以直接访问集群了。

现在，我们可以运行`kubectl get nodes`查询集群信息。当前集群只有一个master节点，并且你可能看到，master的状态是Not Ready：

```shell
$ kubectl get nodes
NAME      STATUS     ROLES     AGE       VERSION
master    NotReady   master    1d        v1.11.1
```

运行`kubectl describe node master`查看详细的报错情况：

```shell
$ kubectl describe node master
...
Conditions:
...
Ready   False ... KubeletNotReady  runtime network not ready: NetworkReady=false reason:NetworkPluginNotReady message:docker: network plugin is not ready:...
```

看到提示是网络插件没有准备好。
运行命令`kubectl apply -f https://git.io/weave-kube-1.6`可以启动网络插件（不要问为什么，现在不知道…

至此，master节点算是正式启动好了。

### kubeadm join

node或者说worker节点，和master节点一样的地方，是都运行一个kubelet组件，但是master上还有那老三样管理组件的pod要启动。所以不需要那么多复杂步骤。

只要保证worker上已经安装了k8s和kubeadm，只要单纯将上面`kubeadm init`生成的那条`kubeadm join`命令复制过来，执行一下即可。