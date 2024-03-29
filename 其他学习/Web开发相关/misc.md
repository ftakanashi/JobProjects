### 关于CSRF
CSRF全称Cross Site Request Forgery，即跨站请求伪造。
是一种常见的攻击手段。

举一个简单的例子，比如我在电商网站上开店，别人给我打钱是通过发起一个POST请求到
`/pay/wyzypa`这个URI，顺便带上金额。

如果不带任何校验，我可以做一个钓鱼网站，让电商网站的买家点击一个能够发送POST请求到上述URI的链接。
这样我就可以白拿钱了。

而一个简单的避免CSRF攻击的办法是这样的：
按照正常流程，买家在发起POST前肯定先要GET一个付款的界面。
在渲染这个付款界面的时候，电商后台生成一个随机数，将其记录下来并将其埋入GET请求返回的页面中。
通常是通过一个`<input>`保存这个随机数。

当买家GET请求完成后，可以安排将上述这个随机数（此后称为csrf token）保存到cookie或者session中。

随后，要求买家在POST的时候请求中带上这个随机数。只有其与后台保存的随机数一致时才校验通过。
这样，由于我不知道买家页面上的随机数是多少，就没法实施攻击了。

注意，使用CSRF验证请求的合法性应该尽量放在POST请求上。
因为GET请求时csrf token会写在URL里，如果被第三方截取那么csrf验证机制也就没用了。