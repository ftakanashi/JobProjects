## 问题描述
你的朋友正在使用键盘输入他的名字 name。偶尔，在键入字符 c 时，按键可能会被长按，而字符可能被输入 1 次或多次。

你将会检查键盘输入的字符 typed。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），那么就返回 True。

示例 1：
>
>输入：name = "alex", typed = "aaleex"
>输出：true
>
>解释：'alex' 中的 'a' 和 'e' 被长按。

示例 2：
>输入：name = "saeed", typed = "ssaaedd"
输出：false
>
>解释：'e' 一定需要被键入两次，但在 typed 的输出中不是这样。

示例 3：
>输入：name = "leelee", typed = "lleeelee"
>
>输出：true

示例 4：
>输入：name = "laiden", typed = "laiden"
输出：true
>
>解释：长按名字中的字符并不是必要的。
 

提示：

name.length <= 1000
typed.length <= 1000
name 和 typed 的字符都是小写字母。


### 解法
重建typed的办法就不说了，空间上不太行。
要空间行，显然就需要走双指针的套路了。

name和typed分别一个指针，然后往前扫描，如果扫描到一样的，各自往前移动，
如果扫描到不一样的，则看typed当前的字符是否和上一个字符一样。因为既然能走到
这一步，说明name和typed各自上一个字符应该是一致的，如果typed当前字符和上一个
一致，那么当前字符就是长按得到的，因此此时typed指针前移，而name的不动即可。

本身思路不难，不过代码有一些边界问题需要处理，需要注意一下。