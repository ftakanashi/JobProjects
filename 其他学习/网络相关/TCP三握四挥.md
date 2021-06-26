# 关于TCP的报文格式
![](https://img-blog.csdn.net/20180717201939345?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4OTUwMzE2/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

其中需要知道的是SYN，ACK，FIN等这些是01标志位。
而序号和确认号是占用4个字节的大一点的数。

# TCP三次握手
![](https://img-blog.csdn.net/20180717202520531?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4OTUwMzE2/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

# TCP四次挥手
![](https://img-blog.csdn.net/20180717204202563?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzM4OTUwMzE2/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

挥手相比于握手，其麻烦的地方在于两点。

第一，服务器断开连接需要一定时间并且有可能无法关闭。也就是CLOSE_WAIT这一块的幺蛾子。
换句话说，如果将上图中第二、三根线给合并在一起，那么挥手就和握手是一个意思，只不过SYN换成了FIN而已。

第二，客户端在发出最后一次ACK之后不能直接断开，而是需要等两个最大报文生存周期（Maximum Segment Lifetime）。
这是因为现在是在结束通信，而通信通道中此时可能鱼龙混杂，说不定这个 ACK没送到服务端，那么服务端就永远挂起了。
而等待2MSL的意义就在于，如果最后一个ACK没被服务端收到，那么服务端会再次送出一个FIN+ACK报文。
这一来一回恰好是2MSL。而如果在这段时间内客户端收到了新的FIN+ACK，说明上一个ACK发送失败了，所以就再发一个并再等2MSL。

