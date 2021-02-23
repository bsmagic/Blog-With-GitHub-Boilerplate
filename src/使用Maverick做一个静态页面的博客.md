---
layout: post
title: 使用Maverick做一个静态页面的博客
slug: Use Maverick to make a static page blog
date: 2021-2-23 13:13:43
status: publish
author: 穿山甲叔叔
categories: 
  - Maverick
tags:
  - Blog
  - 日记
  - GitHub
excerpt: blog
---

[TOC]



> 　　这几天一直想要做一个自己的个人网站，于是跟着网上的教学使用Hexo做了一个使用GitHub的穿山甲小窝，却出了各种问题(生成的静态页面没有样式、为了解决没有样式的问题修改配置文件后样式有了却因为重定向的问题无法预览、皮肤不能用等等一些问题)。

# 为什么使用Maverick来制作？

其实是想要放弃调试Hexo了抱着试一试的想法就去咕咕了一下，一个标题为[用 GitHub 搭建静态博客太繁琐？用这个小工具实现「傻瓜式」发布](https://sspai.com/post/58013)

的文章让我虎躯一震，两目大放精光自豪地想我就是个笨蛋！于是就点了进去。

## 什么是Maverick？

[Maverick](https://github.com/AlanDecode/Maverick)

同样是由刚刚那篇文章的博主开发的基于Python的静态博客生成器

## Maverick吸引我的地方(博主说的) 

1. 方便的图片管理
2. 博客版本管理
3. 在任何设备上写博客，包括浏览器
4. 无需值守的自动化构建
5. 免费、超快的全球 CDN

因为这些看上去就很方便，所以对我这种懒人来说有着致命的吸引力

# 遇到的问题

只能说我是傻逼，在克隆项目后我在本地使用VS code直接Push马克蛋文件到github导致自动部署错误，开始还以为是项目本身的问题让项目背了锅。。。隔天继续查看博主博文的时候才发现博主早就把路铺好了让我走，结果我走歪了罢。项目中的update_site文件就是本地编辑Push的文件，本来轻轻松松的事让我给搞复杂了

![](images\bbs1.png)

# 参考链接

[Maverick](https://github.com/AlanDecode/Maverick)

[自动部署仓](https://github.com/AlanDecode/Blog-With-GitHub-Boilerplate)