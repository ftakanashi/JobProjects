## 题目描述
给定一个字符串 queryIP。如果是有效的 IPv4 地址，返回 "IPv4" ；如果是有效的 IPv6 地址，返回 "IPv6" ；如果不是上述类型的 IP 地址，返回 "Neither" 。

有效的IPv4地址 是 “x1.x2.x3.x4” 形式的IP地址。 其中 0 <= xi <= 255 且 xi 不能包含 前导零。例如: “192.168.1.1” 、 “192.168.1.0” 为有效IPv4地址， “192.168.01.1” 为无效IPv4地址; “192.168.1.00” 、 “192.168@1.1” 为无效IPv4地址。

一个有效的IPv6地址 是一个格式为“x1:x2:x3:x4:x5:x6:x7:x8” 的IP地址，其中:
```
1 <= xi.length <= 4
xi 是一个 十六进制字符串 ，可以包含数字、小写英文字母( 'a' 到 'f' )和大写英文字母( 'A' 到 'F' )。
在 xi 中允许前导零。
例如 "2001:0db8:85a3:0000:0000:8a2e:0370:7334" 和 "2001:db8:85a3:0:0:8A2E:0370:7334" 是有效的 IPv6 地址，而 "2001:0db8:85a3::8A2E:037j:7334" 和 "02001:0db8:85a3:0000:0000:8a2e:0370:7334" 是无效的 IPv6 地址。
```

示例 1：
```
输入：queryIP = "172.16.254.1"
输出："IPv4"
解释：有效的 IPv4 地址，返回 "IPv4"
```
示例 2：
```
输入：queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
输出："IPv6"
解释：有效的 IPv6 地址，返回 "IPv6"
```
示例 3：
```
输入：queryIP = "256.256.256.256"
输出："Neither"
解释：既不是 IPv4 地址，又不是 IPv6 地址
```

提示：
```
queryIP 仅由英文字母，数字，字符 '.' 和 ':' 组成。
```

### 解法 模拟
没啥可说的。
虽然整体的检查地址合法性的规则看上去很复杂，但是一条一条写，慢慢套每个规则即可。
因此方案有很多很多。

比如我的办法就是，定义了一个`checkIPv4`和`checkIPv6`两个方法，分别用于检查两类地址。

其中，用于检查IPv4的方法就是先以`"."`为分隔符切割字符串，保证片段数量是4个，然后依次检查每个片段。
要求是每个片段必须是一个不带前导零（除非其本身就是0）的合法的0到255间的数字。

检查IPv6的方法则是以`":"`为分隔符，保证片段有8个，并且检查片段。
每个片段的字符长度最多为4个，并且必须可以转化为合法的16进制数字。

按照上述逻辑写代码即可。