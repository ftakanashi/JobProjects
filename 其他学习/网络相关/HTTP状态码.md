F# HTTP状态码
总的表格：
![](https://pic3.zhimg.com/v2-7ed37fe236c6d4af96aa32d93adda926_b.jpg)

## 100-199

## 200-299 请求正常处理

【200 OK】
服务端正常处理了客户端发来的请求，服务端返回了对应的请求所要求的的资源。

【204 No Content】
服务端正常处理了客户端发来的请求，但不返回任何资源

【206 Partial Content】
服务端正常处理了客户端发来的请求，只返回一部分要求的资源。
执行范围由响应报文中的Content-Range指定。

## 300-399 重定向

【301 Moved Permenently】
请求的资源的URI已经更新，以后应当使用新的URI

【302 Found】
请求的资源的URI已经更新，但是这个更新是临时性的，希望本次访问可以访问新的URI。
但不代表以后都是这个URI。

【303 See Other】
请求的资源的URI已经更新，但是这个更新是临时性的，希望本次访问可以**用GET方法**访问新的URI。
303和302的区别在于，303明确希望客户端用GET方法访问新URI。

【304 Not Modified】
该状态码表示客户端发送附带条件的请求时，服务器端允许请求访问资源，但未满足条件的情况。

304虽然被划分在3XX类别中，但是和重定向没有关系。

附带条件的请求是指采用 GET 方法的请求报文中包含 If-Match，If-Modified-Since，If-None-Match，If-Range，If-Unmodified-Since 中任一首部

【307 Temporary Redirect】
同302

## 400-499 客户端错误
【400 Bad Request】
报文中存在语法错误。需要修改请求内容后再次发送。

【401 Unauthorized】
发送的请求需要通过HTTP认证。
返回含有 401 的响应必须包含一个适用于被请求资源的 WWW-Authenticate 首部用以质询(challenge)用户信息。

当浏览器初次接收到 401 响应，会弹出认证用的对话窗口。

【403 Forbidden】
对请求资源的访问被服务器拒绝。返回主体内容可包含拒绝的理由。

【404 Not Found】
服务端没有请求的资源。

【405 Method Not Allowed】
服务端可以识别客户端请求的方法类型，但是服务端禁止使用该方法。

客户端可以通过OPTIONS方法来查看服务器允许的访问方法。

## 500-599 服务端错误
【500 Internal Server Error】
服务端执行请求时发生故障。通常是web应用的bug等情况。

【502 Bad Gateway】
返回502的服务端通常不是应用服务器而是网关、代理。当其无法从上游服务器获取正确信息时返回502。

【503 Service Unavailable】
服务端处于超负荷或者停机维护中，无法处理请求。
