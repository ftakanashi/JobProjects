> 参考资料：https://zhuanlan.zhihu.com/p/136345843
> 这个作者的公众号【Python Web与Django开发】是个宝藏！

# Django基本

## Django的优缺点

Python的开发框架，最主流的也就Django和Flask两种，而两种框架的价值取向又几乎是相反的，所以Django的优缺点反过来说基本上就是Flask的缺优点。

Django优点：

- 框架功能完善、有完整的开发文档和活跃的社区、有强大的ORM组件、自带admin管理系统等

Django的缺点：

- 过于重型，自带许多轻量级应用不需要的模块、封装层次较高，导致二次开发难度较大、与传统静态语言相比性能较差（当然基于python天生就慢）

## Django请求的处理流程

1. [wsgi] 接收请求，解析并封装请求内容成一个请求对象，交给Django。封装请求对象，更具体的，发生在WSGIHandler类中。
2. [中间件] Django中间件对请求对象中的内容进行校验，为请求对象添加一些额外的相关数据
3. [路由] 根据Django配置的路由，将请求分发给相关的视图函数
4. [视图函数] 视图函数进行相关逻辑处理（比如与数据库的沟通，渲染模板等），返回响应对象。
5. [中间件] 对响应对象进行校验处理
6. [wsgi] 将响应对象解析成相应格式的内容（HTTP，JSON等），返回给客户端

如图所示：

<img src="https://localblog-1258020778.cos.ap-shanghai.myqcloud.com/uPic/2022/03/18/image-20210721203731807.png" alt="image-20210721203731807" style="zoom:67%;" />

上述流程是开发或者说调试时的逻辑，如果放到生产环境上，往往需要更多组件如nginx，uwsgi等。下面是一个生产环境的示意图：

![image-20210721204152294](https://localblog-1258020778.cos.ap-shanghai.myqcloud.com/uPic/2022/03/18/image-20210721204152294.png)

这个流程，简单来说，浏览器发起HTTP请求后先到nginx。nginx会对请求url做分析，如果请求的是静态文件，nginx直接返回；若不是，则将请求通过socket交给uWSGI。
之后就和上面描述过的流程一样了。

## FBV与CBV

这两个词的意思分别是Function Based View和Class Based View。于是两者分别说的是什么，区别是什么就一目了然了。

这里主要想说的是，CBV可以利用很多类的特性如多态、继承、多继承等，从而使得视图函数的编写更加简单清晰。
FBV和CBV一个很明显的不同在于，当和URL进行绑定的时候，CBV需要通过类调用`as_view()`方法才能有效绑定。

`as_view()`这个方法到底干了什么？简单来说，这个方法用于返回一个函数，而返回什么函数则是通过了View类中的`dispatch`方法对request进行解析，得到`request.method`的值，然后查询类的相关处理方法并返回。

### 如何给CBV方法加装饰器

除了把方法当做函数，普通地加装饰器外，还可以通过如下的方式，在类外面对若干个方法加若干个装饰器：

```python
from django.utils.decorators import method_decorator

decorators = [login_required, check_user_permission]

@method_decorator(decorators, name='get')
@method_decoratro(decorators, name='post')
class XXXView(View):
    # ...
```

### 【TODO】CBV中的通用视图类

>https://mp.weixin.qq.com/s?__biz=MjM5OTMyODA4Nw==&mid=2247483764&idx=1&sn=f0756dbb9887a05280e6464194477e1d&chksm=a73c614c904be85a8380a0d93155a5f70b9cdecf716f452ff9274a9ebeac1c194001beed7b23&scene=21#wechat_redirect

CBV如果只是简单地把原来分散的函数给整合到一个类里并取名get, post等，那其实并不是很有意义。Django在`django.views.generics`中准备了很多预先定义好的通用视图类。前人Web开发时发现前后端数据交互总是那么几个固定的模式，而这些通用的视图类，就事先帮我们把这些模式实现好，我们只要做很少的配置，就可以开箱即用。十分方便。

这些类主要包括下面几种：

- ListView

  用于展示某个模型在数据库中保存的所有对象。

# Django中间件

> 官方文档： https://docs.djangoproject.com/en/1.11/topics/http/middleware/

注意区分App和中间件，两者都在settings.py中注册，一个在INSTALLED_APPS中注册，一个在MIDDLEWARE中注册。

==Django中间件的本质，是一个实现了Django中间件规范部分或者全部接口方法的类==。官方文档对中间件的定义是，其是一个接受`get_response`方法作为参数的callable，同时调用中间件时应该要返回一个response。
那么接口方法是干什么的呢？简单来说，中间件的接口方法，就是一些处理HTTP请求中的钩子函数。正如上面所说，当wsgi包装完请求，Django进行请求路由之前，中间件可以对请求内容进行校验等。这个工作就是由中间件类的钩子函数完成的。

实际开发中间件的过程中，通常不会选择自己从头写，而是继承`django.utils.deprecation.MiddlewareMixin`。

## 中间件接口方法（钩子）

中间件常用的接口方法有下面几个：

- `process_request(self, request)`
  顾名思义，这个方法在中间件层接到请求，传递给路由层之前被运行。比如==FTKBlog项目中对IP进行应用层面的白黑名单访问限制的时候，就用到了这个钩子==。彼时在中间件类中重载了这个方法，检查request.META.REMOTE_ADDR是否存在于黑名单中。

- `process_response(self, response)`
  这个和process_request相对，是在视图函数返回了response给中间件，中间件继续返回给wsgi层之前被执行。用于对响应的后处理。

以上两个钩子中间件处理阶段最主要的钩子，分别对应了请求处理流程中中间件工作的两个阶段。
除了上面两个时机外，其实还有其他一些时机，也存在中间件可以埋的钩子。如：

- `process_view(self, request, view_func, view_args, view_kwargs)`
  process_view钩子在路由层处理完成，已经找到视图函数之后；在视图函数被执行之前，被执行。因此这个钩子的参数除了request对象，还有view函数对象，view函数的参数等。
  例如管理CSRF的中间件就重载了process_view并在其中做了CSRF token的校验。
  注意process_view可以返回两类东西。如果返回None，则Django继续转而执行其他中间件的process_view，若没有剩余的中间件有process_view，则最终去执行view函数。如果返回的是一个HttpResponse，则Django不会再去执行视图函数，而是直接将这个response返回给中间件的process_response处理，并最终将这个结果返回给客户端。

- `process_exception(self, request, exception)`
  当视图函数处理请求时发生异常，就会转入实现了这个钩子的中间件进行处理。当然，如果没有实现了这个钩子的中间件，则进入Djanog的默认异常处理模式（使用相应HTTP Error的Error Handler）

- `process_template_response(self, request, response)`
  这个钩子会在试图函数处理完成后，并且返回的不是一般的response对象而是一个TemplateReponse对象（其特点是带有render方法）时。
  因为没有怎么返回过TemplateResponse对象，所以就不多说了。

## 中间件的执行顺序

settings中MIDDLEWARE是一个列表，而这个列表中注册的中间件是有顺序的。
在某个时间节点要进行中间件处理时，很有可能多个中间件都实现了这个节点对应的钩子函数。那么这些钩子函数就会有一个处理的顺序问题。

官方文档这样描述这个问题：可以将各个中间件视为包裹视图函数的洋葱皮，而视图函数是洋葱心。
显然，process_request和process_view这两个钩子发生在视图函数被调用前，因此中间件执行顺序是MIDDLEWARE列表的正序。
相反，process_template_response和process_response都发生在视图函数被调用后，因此中间件执行顺序是反过来的，即MIDDLEWARE列表的逆序。
至于process_exception，由于其发生在视图函数被调用时，实际上已经进入视图函数，只不过没执行完，所以返回的时候，中间件是按照response的逆序来执行，处理这个异常的。

另外还需要提一句，==中间件可以做到“短路”。比如上面说的，在process_view中直接返回HttpResponse对象的话，就可以让Django不去执行视图函数了。==

## 常见的（内建）中间件

我们知道Django项目初始化时就有一些中间件被注册了。主要是下面这些：

| 中间件名称               | 作用                                                         |
| ------------------------ | ------------------------------------------------------------ |
| SecurityMiddleware       | 为request/response提供了一些安全的加固                       |
| SessionMiddleware        | 开启了会话session支持，必须要注册这个中间件才能使用会话机制  |
| CommonMiddleware         | 一些基础的中间件要做的事，比如禁止User-Agents是特定值的访问、重写非标准格式的URL等 |
| CsrfViewMiddleware       | 添加CSRF保护，对于有POST等写操作请求的时候一定要加上         |
| AuthenticationMiddleware | 视图函数执行前对每个请求，通过会话检验用户的有效情况，为request.user赋值 |
| MessageMiddleware        | 开启基于Cookie和Session的会话保持机制。上述Authentication中间件就是基于这种机制才能工作 |
| XFrameOptionsMiddleware  | 对点击劫持的保护                                             |

### 关于CsrfViewMiddleware提供的CSRF保护

CSRF是什么这里就不说了，可以看网络那篇中提的。
Django利用这个中间件进行CSRF攻击防止的原理是这样的：

1. 客户端第一次访问时，csrf中间件会在response返回前在其中加上一个随机生成的csrf token，并在后台缓存中保存下这个token。这个token被放在response的头中，要求客户端将其存为cookie。
2. 返回给客户端的表单中，都含有一个csrf token的隐藏字段，模板中以`{% csrf_token %}`形式出现。
3. 要求客户端进行POST等请求时必须带上这个隐藏字段。如果提交POST的是Django原生的一些比如FormView之类生成的界面，那么Django会处理好一切，如果是程序员通过其他手段提交，则需要手动加上这个token。
4. 校验客户端提交的token和后台保存的token是否一致，只有一致才认为没有CSRF攻击风险，否则返回403 Forbidden。

### ajax如何提交token

几种方法。若ajax代码写在模板里了，则可以

```javascript
data: {
  csrfmiddlewaretoken: {{ csrf_token }}
}
```

也可以通过jQuery等框架手动取值：

```javascript
data:{
  csrfmiddlewaretoken: $('[name="csrfmiddlewaretoken"]').val()
}
```

或者用jquery.cookies.js或者其他库，直接去cookies中取token。

# Django ORM

## QuerySet的特点

通过Django ORM获取数据之后，得到的最直观的是一个QuerySet对象。这个对象有两个特点：==惰性查询、自带缓存==。

==惰性查询，是指生成QuerySet的表达式写完，并可能将其赋值给某个代表了QuerySet的变量后。此时其实ORM并不会真的去数据库取数据。只有当这个QuerySet在后续的代码里被用到时，ORM才会去取数据，称之为QuerySet的执行（evaluation)==。例：

```python
articles = Article.objects.filter(title__contains='django')
# 此时ORM还没去数据库取数
for article in articles:
  print(article.author)    # 第一次循环到这里，真的要用数据了，采取取数
```

自带缓存也很好理解。在Django这个层面，会对从数据库中取来的结果做一些简单的缓存。当然这个缓存需要代码中以变量的形式主动保存，比如上面的代码。
换言之，每执行一次ORM，都会可能去连数据库取数。但如果你将第一次取回来的数据用变量保存下来，之后访问那个变量就行了。很简单的思想。

另外提一个小的优化点。很多时候通过ORM取数得到的QuerySet是个空集。此时如果用`if articles`或者`if len(articles) > 0`之类的表达去判断是否是空集，还是会出发ORM去执行取数。此时可以使用`articles.exists()`方法。这个方法只会通过QuerySet的接口判断是否有结果，返回True和False，而不至于触发取数过程。

## ORM执行效率问题

> 资料：https://stackoverflow.com/questions/25696120/why-is-django-orm-so-much-slower-than-raw-sql

通常认为，ORM的执行速度比原生的 raw SQL 要慢很多。这通常可以归结为以下几点原因。

- 在数据检索前，ORM需要将你的一长串代码逻辑给转换成一个SQL，这本身就需要耗费一定时间，逻辑越复杂，耗费的时间肯定就越长。更不用说有些复杂逻辑ORM无法生成，或者说要写出符合逻辑的ORM代码不如直接写raw SQL。
- 在数据检索时，注意ORM并没有我们想象的那么智能，很多时候他只负责生成能用的SQL而不是最优的。所以检索时可能ORM的SQL效率不够好。
- 在数据检索后，这也是很明显的一个拖慢ORM的地方。ORM会将检索出来的数据全部都包装成相关类的对象（否则也不会叫ORM了），而这个新建对象的过程会耗费大量时间空间。

话分两头，资料中的回答评论中也有人提到，有人用Django 1.8做过实验，发现优化的不错，基本上不必raw SQL差多少了。当然这种评论毫无价值毕竟没提供数据量等信息。

总体来说，当ORM的效率过于拉胯时，就可以考虑用raw SQL来做。raw SQL一方面可以通过独立地用mysqldb模块建立连接获取数据，另一方面，Django内部其实也维护了这个连接，可以通过`django.db.connection`来调用。
和mysqldb的调用方式一样，需要通过`connection`中的`cursor`属性代表的游标来fetch数据，如：

```python
from django.db import connection
cursor = connection.cursor()
cursor.execute('SELECT * FROM xxx;')
data = cursor.fetchall()
```

## 【TODO】select_related和prefetch_related

> https://mp.weixin.qq.com/s?__biz=MjM5OTMyODA4Nw==&mid=2247484306&idx=1&sn=48a89cdf74edff43d727c61ac14b480a&chksm=a73c63aa904beabc1975f9e38bafb36ac9fff041b0a468fa66c82279b03c1fdbf9364731e0c6&scene=21#wechat_redirect



## ORM获取随机值

有时候可能需要通过ORM取某个模型的一个随机值，可以这么干：

```python
Model.objects.order_by('?').first()
```

Order by的参数写问号，即随机排序，然后取第一个结果，就是随机取值了。

## 【TODO】annotate与aggragate

# Django 模板

## 如何自定义模板标签以及模板过滤器

在相关app下新建`templatetags`目录（一定得是这个名字），并在其中新建`__init__.py`文件（说明这是一个Python包了）。
接着可以在其中建立任意名字的.py文件，然后在其中进行自定义tag或者过滤器的注册。注册器是下面这个：

```python
from django import template
register = template.Library()
```

下面来举个例子，比如我想在模板中自定义一个`{% get_user_name id %}`的tag，其功能是在前端模板写一个id，就可以直接显示出后台User模型对应用户的用户名：

```python
class UsernameNode(template.Node):
  def __init__(self, uid):
    self.uid = uid
  
  def render(self, context):
    try:
      u = User.objects.get(user_id=self.uid)
    except User.DoesNotExists as e:
      return ''
    return u.username

@register.tag(name='get_user_name')
def get_uesr_name_tag_handler(parser, token):    # parser和token两个参数是Django要求的
  try:
    tag, uid = token.split_contents()    # split_contents是token对象自带的方法，可以返回模板调用的tag名与参数
  except ValueError as e:
    raise template.TemplateSyntaxError('Tag takes at least one argument.')
  uid = uid.strip('\'')    # 默认参数用单引号包着，去掉单引号

  return UsernameNode(uid)

​```
在模板中的调用可能是这样的：
<p>Name: {% get_user_name 1 %}
​```
```

需要注意的是，自定义tag函数返回的必须是一个节点类，而节点类必须实现了render方法，其可以接收context并返回一串字符串。

自定义tag和过滤器很灵活，不多说了，更多资料建议看官方文档。

# restful规范与rest_framework框架

restful规范是一种软性的，推荐性的规定。即你可以用Django不遵循这个规定实现一个网站或者api，但是遵循这个规范会各种意义上很省事并且容易维护。

## restful规范的要求

- url中应该可以体现API版本号。具体的可以写在域名中或者uri中如：

  ```
  https://api.v1.wyzypa.cn/xxx
  https://wyzypa.cn/api/v1/xxx
  ```

- url中可以添加条件进行筛选匹配如:

  ```
  https://wyzypa.cn/api/v1/servers?page=3
  ```

- 各种操作都由一个HTTP方法和特定的URL格式进行规定，如

  | URL格式     | HTTP方法 | 操作说明                                           |
  | ----------- | -------- | -------------------------------------------------- |
  | models/     | GET      | 获取所有model记录                                  |
  | models/     | POST     | 新增一条model记录，请求中带有各个字段的初始化值    |
  | models/uuid | GET      | 获取主键为uuid的这条model记录                      |
  | models/uuid | PUT      | 全量更新主键uuid记录，请求中带有各个字段的更新值   |
  | models/uuid | PATCH    | 部分更新主键uuid记录，请求中带有需要更新的字段的值 |
  | models/uuid | DELETE   | 删除主键uuid记录                                   |

  在设计URL和方法时要时刻牢记，URL是名词，而方法是动词。

- 要有统一的返回数据格式（通常API犯不着返回HTML，而选择JSON），返回数据中要有统一的状态码字段（不一定要与HTTP的状态码统一）与信息字段。如果发生错误，则要返回错误信息。如：

  ```
  {code: 1000, msg: 'success'}
  {code: 1001, msg: 'xxx not found'}
  ```

### restfulAPI与普通API的区别

普通的API，通常对于特定的一个谓语都要安排一个特定的接口。比如对于product模型的增删查改，可能需要

```
/getproduct.aspx
/createproduct.aspx
/updateproduct.aspx
/deleteproduct.aspx
```

四个接口。

而显然，restfulAPI只需要一个`/product`接口，然后根据不同的HTTP方法作为谓语与其组合即可。

此外，还需要考虑到众多浏览器也已经遵循了restful协议。比如浏览器通常默认GET方法是幂等的，因此失败会自动重发。但是普通API的写操作也是GET方法，这就引起了数据不一致的风险。

## rest_framework插件的基本组件

- 视图组件 ViewSet

  Web开发，最关键的，当然就是View怎么写了。而rest framework提供了一些叫做ViewSet的类给程序员。这些类中封装好了标准的restful操作。只要继承这些类，就可以轻松地实现restful风格的接口。

  这些类处于`rest_framework.generics`中，比如`ListCreateAPIView`这个类就实现了上面提到的对于`models/`这个URL的GET和POST两种方法。类似的，`RetrieveUpdateDestroyAPIView`则是实现了后面四种针对某特定uuid记录的方法。

  在views中继承完上述类之后，还需要将其与某个ORM模型关联起来，通常是通过指定这个类的雷属性`queryset = Model.objects.all()`来进行。

  除了`queryset`，这个类中还可以指定各种各样的rest framework的组件，从而实现功能强大的API。下面会重点说些有用的组件。

  写完这个类后，只需要再urls的路由中，将符合上述URL规范的url与类绑定（写成`url('models/', XXView.as_view())`即可），这样访问相关URL的时候后端的rest framework的视图就会工作了。

- 序列化器serializer

  （反序列化）对于写操作，序列化器将前台传来的数据进行校验，并且转换成后台可以理解的python数据。
  （序列化）对于读操作，序列化器将后台得到的数据经过组织拼装，以序列化后的格式交给前台。
  `ModelSerializer`是个和ORM结合很好的序列化器，只要将其和一个ORM模型关联，并且指定好各个字段的处理方式（比如外键字段该怎么处理等，通常可以用各种Field类来实现个性化的序列/反序列化），他就能很好地完成ORM模型的序列化与反序列化相关工作。

- 认证组件

  View中有authentication_classes属性，这就是指出了这个View要不要有认证，可以允许通过哪些途径认证。例：

  ```python
  authentication_classes = (SessionAuthentication,TokenAuthentication)
  ```

- 权限组件

  View中有permission_classes，通常和认真组件配合起来使用。决定某个View是否有权限控制，若有哪些人有权限。例：

  ```python
  permission_classes = (IsAuthenticatedOrReadOnly,)
  ```

- 过滤器组件

  rest framework原生带有过滤器组件，但是也可以用更好用一点的`django_filter`，这个插件和rest framework原生兼容性也不错。

  ```
  filter_backends = (DjangoFilterBackend,OrderingFilter)
  filter_class = ServerFilter
  ```

- 分页组件

  pagination_class指出分页组件采取什么策略。常用的是:

  ```python
  pagination_class = LimitOffsetPagination
  ```

除了上述组件外还有其他很多一些组件，这里就不一一写了。

# 【TODO】Django与Celery

# wsgi与uwsgi与uWSGI

==wsgi全称 (Python) Web Server Gateway Interface，其描述的是一个协议，这个协议规定了Web服务器如何与Python程序进行交互，从而使得Python代码也可以作为Web的后端代码工作==。
wsgi协议架构包括两部分实体，server（或者叫gateway）与application。
server通常是指web服务器。支持wsgi协议的web服务器并不多。Apache装上mod_wsgi模块之后可以算一个，而更多的时候采用Python自己实现的uWSGI服务器。
application指那些通过Django、Flask等框架写成的Web应用本身。

如上所说，==uWSGI是一个具体的软件，即用Python写成的一个Web服务器==。因为其要基于wsgi协议与web应用通信，因此其肯定实现了wsgi协议。作为web服务器，uWSGI当然也实现了HTTP协议可进行通信。因此，uWSGI如果使用HTTP协议启动监听，那么外部访问者可以直接访问到uWSGI的端口上从而得到HTTP内容。

另一方面，==uWSGI还实现了uwsgi协议。这个协议是uWSGI自带的，可以定义传输数据类型的传输协议==。
由于用户的浏览器没有实现uwsgi协议，所以为了能通过uwsgi访问到uWSGI中的应用内容，还需要前置一个同样实现了uwsgi协议的Nginx。（顺便一提，因为Nginx也实现了HTTP协议，所以Nginx和uWSGI之间也可以用HTTP进行通信。只需要双方协商好，配置一致即可。彼时Nginx就充当一个转发代理的角色）。

以上三者的关系，带上周边的一些概念，所有关系可以表示如下：

<img src="https://localblog-1258020778.cos.ap-shanghai.myqcloud.com/uPic/2022/03/18/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTQ1NTAxNQ==,size_16,color_FFFFFF,t_70.png" alt="在这里插入图片描述" style="zoom: 67%;" />

==总结一下，就是uWSGI这个软件实现了wsgi协议的server部分，从而可以通过wsgi协议与Django App进行通信；同时也实现了uwsgi协议，可以与前端实现了uwsgi协议的服务器如Nginx进行通信。==

# 其他

## 常用的/用过的第三方库

- django-filter：更好用的过滤器
- rest framework: 构建restful API神器
- django-debug-toolbar: django框架调试debug工具
- django-redis: 不解释…
- django-ratelimit: 进行访问频率限制的组件
- django-crontab: 不解释…
- django-elasticsearch-dsl: 用来和ES交互的组件

## 如何进行Django的高并发调优

可以从下面几个角度来考虑：

- 使用nginx进行负载均衡以及静态文件发布
- 数据库读写分离、主从复制
- 用redis等进行热点数据的缓存
- 耗时任务交给celery等组件进行异步处理
- 使用gzip、django-compressor等进行静态文件压缩
- CDN加速静态文件访问