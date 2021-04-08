---
layout: post
title: Android Termux 安装 Linux
date: 2021年4月8日17:57:58
tags: Linux
---



> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 [www.sqlsec.com](https://www.sqlsec.com/2020/04/termuxlinux.html)

Termux 在安装好 proot 的情况下，是可以运行 Linux 系统的，利用这个原理，国光写出了 Termux 一键安装 Linux 脚本，让你的 Termux 折腾之路更加简单。

**项目地址**: [https://github.com/sqlsec/termux-install-linux](https://github.com/sqlsec/termux-install-linux)

因为本脚本使用的是 Python3 编写，所以除了 proot 需要安装以外，还需要基本的 Python 环境，Python 相对于 sh 脚本的优点是更灵活，可操作性更强，人生苦短，我用 Python，另外觉得好用的话 不点点个 star 再走吗。

执行如下命令安装基本依赖:

Bash

```
pkg install proot git python -y
```

Bash

```
git clone https://github.com/sqlsec/termux-install-linux
cd termux-install-linux
python termux-linux-install.py
```

![](https://image.3001.net/images/20200423/15876456241183.jpg)

0 学习成本，安装和卸载 Linux 都很方便。

Bash

```
cd ~/Termux-Linux/Ubuntu
./start-ubuntu.sh
```

![](https://image.3001.net/images/20200423/1587646427613.png)

这个 Kali 是轻量级的，大家要安装完整的 Kali Nethunter 的话 ，可以参考我的 Termux 文章里面的操作细节:

[Termux 高级终端安装使用配置教程: Kali NetHunter](https://www.sqlsec.com/2018/05/termux.html#toc-heading-120)

Bash

```
cd ~/Termux-Linux/Kali
./start-kali.sh
```

![](https://image.3001.net/images/20200423/15876474958738.png)

Bash

```
cd ~/Termux-Linux/Debian
./start-debian.sh
```

![](https://image.3001.net/images/20200423/15876484859724.png)

CentOS 也完美支持，这样理论上用 Termux 跑个宝塔面板应该也不是不可能的了，虽然感觉这样很蛋疼，但评论区真的有人想要这么搞，不是很能理解，手机建站需要端口转发到外网，端口转发到外网需要外网服务器，那么问题来了，既然有外网服务器了，为什么不直接在外网的服务器上建站呢？？？

Bash

```
cd ~/Termux-Linux/CentOS
./start-centos.sh
```

![](https://image.3001.net/images/20200423/15876497487617.png)

这个国光已经更换过源了，但是貌似还是有点慢，感兴趣的朋友可以自己再折腾一下，平时国光很少使用 Fedora，基本上就是 CenotOS、Ubuntu、Kali 用的比较多 …

Bash

```
cd ~/Termux-Linux/Fedora
./start-fedora.sh
```

启动完成之后手动输入如下命令，重建缓存:

Bash

```
yum clean all
yum makecache
```

![](https://image.3001.net/images/20200423/1587654547348.png)

以上操作系统安装与卸载国光均一一测试成功，理论上不会出现安装不了的情况了，日后除非有大的改动，否则 Termux 这一块应该不再更新了，我得去搞我的安全研究去了，路漫漫其修远兮，吾将上下而求索。另外给那些还在读初中或者高中的同学一些忠告：少把时间花在那些工具与系统安装上，多花时间在计算机原理与代码上，有条件的同学还是在电脑上编程比较好，Termux 只是一个玩具性质的工具，只是电脑不在身边的临时替代品，不知不觉又扯多了，溜了溜了。

如果你喜欢这篇文章的话 不防点一下网站最下方不起眼的广告表示支持！Thanks♪(･ω･)ﾉ

发现一个尴尬的问题，看我这篇文章大人大多数是极客玩家，你们的浏览器自带去广告插件，尽管我的章中的广告位置已经很不起眼了，但是你们可能连点的机会都没有…

博客我也写了快 4 年了，文章广告到现在的收益只有 8 美元，有图有真相:

![](https://image.3001.net/images/20200421/15874495233711.jpg)

本文可能实际上也没有啥技术含量，但是写起来还是比较浪费时间的，在这个喧嚣浮躁的时代，个人博客越来越没有人看了，写博客感觉一直是用爱发电的状态。如果你恰巧财力雄厚，感觉本文对你有所帮助的话，可以考虑打赏一下本文，用以维持高昂的服务器运营费用（域名费用、服务器费用、CDN 费用等），对博客用 CDN 了，否则访客不会有这么快速友好的体验。

![](https://image.3001.net/images/20200421/1587449920128.jpg)

**微信**

![](https://image.3001.net/images/20200421/15874503376388.jpg)

**支付宝**

没想到文章加入打赏列表没几天 就有热心网友打赏了 于是国光我用 Bootstrap 重写了一个页面 用以感谢 支持我的朋友，详情请看 [打赏列表 | 国光](https://www.sqlsec.com/dashang.html)