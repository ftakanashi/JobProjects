# OSI七层模型
七层模型以及各层代表性的协议分别是
```text
应用层     HTTP, FTP, DNS, TELNET, DHCP, POP3...
表示层     JPEG, ASCII...
会话层
传输层     TCP, UDP
网络层     IP, ICMP...
数据链路层   MAC
物理层
```
在更加简化的五层模型中，"表示层"和"会话层"被合并到应用层。

而在更看重TCP/IP协议的四层模型中，"链路层"和"物理层"被更进一步地合并成"链路物理层"。

使用七层模型可以描述两台不同主机中的两个进程进行网络通信的。
发送进程将一段数据从上至下传输，每经过一层就加套一层头报文啥的。

然后在最底层的物理层变成01比特流，进行传输，传输到目标主机后，再从下至上一层层剥开报文，
最终得到发出的数据。

![](https://bkimg.cdn.bcebos.com/pic/b21bb051f8198618b8f0ae2b40ed2e738ad4e6ee?x-bce-process=image/watermark,image_d2F0ZXIvYmFpa2U5Mg==,g_7,xp_5,yp_5/format,f_auto)
