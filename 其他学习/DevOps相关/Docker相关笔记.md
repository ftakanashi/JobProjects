# 容器与虚拟机

容器和虚拟机都是用来做环境隔离的基本单位。通常我们都把容器看做一种轻型的虚拟机，因为容器和虚拟机的架构区别如下：

![img](https://upload-images.jianshu.io/upload_images/12979420-a562cd670f2b8b02?imageMogr2/auto-orient/strip|imageView2/2/w/529/format/webp)

不论是用什么隔离体系，最终我们的目的都是要让程序利用硬件进行计算。而利用硬件都要通过操作系统内核。
这里，虚拟机的做法，是带起一个自己的操作系统，通过自身操作系统的内核去访问硬件。而硬件本身也不是直接暴露给虚拟机OS，而是通过虚拟机管理软件，即上图中的hypervisor进行了虚拟化。
另一方面，容器的做法是所有容器共享宿主机操作系统的内核，从而访问硬件。因此容器内部不需要自己的OS。容器通过Docker Engine管理程序与宿主机OS内核打交道。

开启一个新虚拟机时，需要加载庞大的虚拟机的操作系统，同时虚拟机运行时其操作系统肯定也要运行，因此会占据较多的CPU、内存资源。
而启动一个容器很快，往往只要几毫秒即可。容器通过Namespace技术将不同容器的各种资源隔离开，但由于容器专注于应用代码本身，没有多余的操作系统等，因此占用资源也不多。

# 容器虚拟化技术泛谈

容器的虚拟化技术主要包括了Cgroup, Namespace, rootfs和容器引擎。
可以说一个容器就是由这四项技术共同作用构成的。这四种技术分别实现了Docker容器的：

Cgroup：资源控制
Namespace：访问隔离
rootfs：文件系统隔离（镜像的本质就是一个rootfs文件）
容器引擎：生命周期控制

## Cgroup

全程Control Group，是Linux内核本身就提供的一种机制。Cgroup将若干个进程组成一个控制组。
针对一个控制组，Cgroup机制可以控制组内所有进程可以使用的资源。
可以使用，即可指可以使用哪些资源（比如指定CPU，指定内存段等），也可以指可以使用多少资源（即指定资源使用上限值）。

Cgroup机制中有很多子系统，分别用来控制不同的资源，如图：

<img src="https://img2020.cnblogs.com/blog/1977753/202004/1977753-20200412224046852-870716976.png" alt="img" style="zoom:50%;" />

## Namespace

Namespace也是Linux内核自带的一个机制。其作用是，将原来在内核看来是一个整体的系统（比如网络资源、用户系统、进程系统等），分成若干个互相独立的部分，使之互相之间不影响对方。

Linux内核中实现的Namespace总共有下面这几种：

| Namespace | 作用                                    |
| --------- | --------------------------------------- |
| IPC       | 隔离进程通信的共享内存以POSIX消息队列等 |
| Network   | 隔离网络资源                            |
| Mount     | 隔离文件系统挂载点，即文件系统隔离      |
| PID       | 隔离进程PID，即隔离进程系统             |
| UTS       | 隔离主机以及域名                        |
| User      | 隔离用户以及用户组，即隔离用户系统      |

## rootfs

在Linux启动的时候，初始化文件系统时，最开始会建立一个叫做rootfs的文件系统。这个系统内容与磁盘中整个文件系统一样，但是只有读权限。之后，Linux会将rootfs的权限修改为读写，于是文件系统初始化就完成了。

而在Docker中借鉴了类似的思路。==第一步先启动挂载一个只读的rootfs，这个文件系统中只包括一些保证系统可以运行的最基本的内容。之后，和Linux不同的是，容器中的rootfs一直保持只读状态，在此基础上容器内部新创建一个空的读写的文件系统==。

<img src="/Users/wyzypa/Pictures/TyporaImages/Docker相关笔记.asset/image-20210722110433707.png" alt="image-20210722110433707" style="zoom:50%;" />

每当容器内试图对某些文件作出修改时，Docker会发挥COW（Copy on Write）机制，将文件从只读的rootfs中复制到读写文件系统并修改后保存在读写文件系统中。
多个容器可以共享同个只读rootfs，而各自维护自己的读写文件系统。由于共享，所以可以大幅度节省磁盘、内存空间。

# 容器的网络模式

> https://www.jianshu.com/p/22a7032bb7bd

docker容器总共有四种网络模式

| 网络模式           | 命令                      | 描述                                                         |
| ------------------ | ------------------------- | ------------------------------------------------------------ |
| host模式           | -net=host                 | 容器与宿主机共享网络Namespace                                |
| container模式      | -net=container:NAME_OR_ID | 容器与其他容器共享网络Namespace，如k8s的一个pod内的容器就是container模式，互相共享网络namespace |
| none模式           | -net=none                 | 容器自身有独立的网络Namespace，但需要手动对其进行配置        |
| 【默认】bridge模式 | -net=bridge               | 容器自身有独立的网络Namespace，将其通过一个宿主机统一指定的网关接入一个docker子网络。类似虚拟机的桥接模式。 |

- host模式
  host模式就是将docker容器看做一个宿主机内的特别进程，其文件系统、进程系统等于宿主机隔离，但是网络和宿主机共享。换言之，如果docker容器监听端口，那么是直接在宿主机IP上监听，外部访问这个端口也就访问了容器内部；反过来，容器内部也可以利用宿主机的IP访问外部网络。

  host模式可以最大限度地提升网络传输效率，并且配置直接方便，但是安全性、隔离性方面不好。

  <img src="https://upload-images.jianshu.io/upload_images/13618762-a892da42b8ff9342.png?imageMogr2/auto-orient/strip|imageView2/2/w/698/format/webp" alt="img" style="zoom:50%;" />

- container模式
  container模式下，容器建立时需要指定另一个已经配置好网络的容器。新容器与该容器共享网络Namespace。通常被指定的这个容器是桥接模式的，即处于宿主机建立的docker0网络中。新容器可以通过该容器的IP与外界交互信息。而两个容器之间通信则可以通过local网卡

  显然，此时新容器与既存容器形成一个容器集群。因此k8s等集群服务中采用这种模式。

  <img src="https://upload-images.jianshu.io/upload_images/13618762-790a69a562a5b358.png?imageMogr2/auto-orient/strip|imageView2/2/w/695/format/webp" alt="img" style="zoom:50%;" />

- none模式
  none模式下建立起的新容器，只有一个lo网卡。即在网络上其不与宿主机或其他容器有关联。可以通过手动配置进行关联。

  none模式可以保证容器在网络方面的绝对安全和绝对隔离。

  <img src="https://upload-images.jianshu.io/upload_images/13618762-3fd41778faebcef5.png?imageMogr2/auto-orient/strip|imageView2/2/w/723/format/webp" alt="img" style="zoom:50%;" />

- bridge模式（默认）

  默认情况下，docker采用bridge模式进行容器网络配置。docker主进程启动时，虚拟一个叫做docker0的网卡，并以此为网关建立一个docker子网。
  之后每个容器建立时，都从这个子网中分得一个IP。宿主机内的所有容器都处于该子网中。容器间通信时，docker0被视作交换机进行通信中继服务，容器向外网访问时，则将宿主机视作路由器进行访问。

  <img src="https://upload-images.jianshu.io/upload_images/13618762-f1643a51d313a889.png?imageMogr2/auto-orient/strip|imageView2/2/w/1083/format/webp" alt="img" style="zoom:50%;" />



# 【TODO】K8S

> https://blog.csdn.net/u012140251/article/details/114646671
>
> https://blog.csdn.net/u012140251/article/details/115294353



# 其他

## 关于数据卷

我们知道启动容器时`-v`参数可以绑定宿主机目录与容器内目录，即挂载数据卷。

`-v`参数的值中可以最后再加上`:ro`或者`:rw`这两个flag，分别标识只读挂载卷和读写挂载卷。如`-v test_con:/home/back:/root:ro`。

当有容器A挂载了若干个数据卷，此时通过`docker run`启动容器B，可以指定参数`--volumns-from A`来挂载和A中一模一样的几个数据卷。
在创建很多容器进行容器集群创建的时候，给所有容器都加上这个参数，便可以让多个容器有共同的挂载卷。==这也是一种实现容器间通信的办法==。

在容器内，写入挂载卷和写入非挂载卷目录的性能是有区别的。
写入挂载卷，由于和宿主机的目录直接同步，因此会直接写磁盘。
写入非挂载卷目录，根据上面说过的 rootfs + 可读写fs 的架构，首先要将相关文件从rootfs中复制到可读写fs中，再进行修改。因此步骤比直接写挂载卷多，因此性能稍差一些。