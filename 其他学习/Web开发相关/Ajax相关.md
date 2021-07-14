# Ajax原理
Ajax全称是Asynchronous JavaScript and XML。

Ajax的核心在于，他允许了Javascript单独像服务器发起请求，收到回应，期间不阻塞用户继续浏览页面。Ajax通过向服务端发出一个XmlHttpRequest对象作为请求。这个对象有以下这些字段：

| 字段               | 含义                                                         |
| ------------------ | ------------------------------------------------------------ |
| raedyState         | 该对象的一个状态值。选择有<br />0： 表示对象已建立但未初始化（未调用open方法）<br />1：对象已初始化但未发送（未调用send方法）<br />2：数据发送开始，未收到响应<br />3：已经开始接收响应，但未接收完全<br />4：完成，可以通过相关字段获取响应的信息 |
| status             | 服务端返回的HTTP状态码                                       |
| statusText         | 服务端返回的伴随状态码的文本信息                             |
| responseText       | 服务端返回的字符串信息                                       |
| responseXml        | 服务端返回的XML格式信息                                      |
| onreadystatechange | 当readyState的值发生变化时的回调函数。                       |

上面也提到了，这个对象主要的方法是`open`，`send`两个。调用方法大概是这样：

```javascript
xlmhttp = new XmlHttpRequest();
xmlhttp.open("POST", url, false);
xmlhttp.onreadystatechange = function(){
  // 这里是回调函数，最关键
  if (xmlhttp.readyState == 4){
    // 完成了请求，可以做一些事情比如显示得到的数据等
  }
}
xmlhttp.send();
```

