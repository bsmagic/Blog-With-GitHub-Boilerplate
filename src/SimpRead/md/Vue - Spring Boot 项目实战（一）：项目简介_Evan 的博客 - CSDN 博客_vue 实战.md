> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 [blog.csdn.net](https://blog.csdn.net/Neuf_Soleil/article/details/88925013)

![](https://img-blog.csdnimg.cn/20191215205052258.png)

GitHub 地址：[https://github.com/Antabot/White-Jotter](https://github.com/Antabot/White-Jotter)  
![](https://img-blog.csdnimg.cn/20191215210150398.png)

教程目录
====

第一部分
----

[Vue + Spring Boot 项目实战（一）：项目简介](https://learner.blog.csdn.net/article/details/88925013)  
[Vue + Spring Boot 项目实战（二）：搭建 Vue.js 项目](https://learner.blog.csdn.net/article/details/88926242)  
[Vue + Spring Boot 项目实战（三）：前后端结合测试（登录页面开发）](https://learner.blog.csdn.net/article/details/88955387)  
[Vue + Spring Boot 项目实战（四）：数据库的引入](https://learner.blog.csdn.net/article/details/89294300)  
[Vue + Spring Boot 项目实战（五）：使用 Element 辅助前端开发](https://learner.blog.csdn.net/article/details/89298717)  
[Vue + Spring Boot 项目实战（六）：前端路由与登录拦截器](https://learner.blog.csdn.net/article/details/89422585)  
[Vue + Spring Boot 项目实战（七）：导航栏与图书页面设计](https://learner.blog.csdn.net/article/details/89853305)  
[Vue + Spring Boot 项目实战（八）：数据库设计与增删改查](https://learner.blog.csdn.net/article/details/92413933)  
[Vue + Spring Boot 项目实战（九）：核心功能的前端实现](https://learner.blog.csdn.net/article/details/95310666)  
[Vue + Spring Boot 项目实战（十）：图片上传与项目的打包部署](https://learner.blog.csdn.net/article/details/97619312)

第二部分
----

[Vue + Spring Boot 项目实战（十一）：用户角色权限管理模块设计](https://learner.blog.csdn.net/article/details/100849732)  
[Vue + Spring Boot 项目实战（十二）：访问控制及其实现思路](https://learner.blog.csdn.net/article/details/101121899)  
[Vue + Spring Boot 项目实战（十三）：使用 Shiro 实现用户信息加密与登录认证](https://learner.blog.csdn.net/article/details/102690035)  
[Vue + Spring Boot 项目实战（十四）：用户认证方案与完善的访问拦截](https://learner.blog.csdn.net/article/details/102788866)  
[Vue + Spring Boot 项目实战（十五）：动态加载后台菜单](https://learner.blog.csdn.net/article/details/103114893)  
[Vue + Spring Boot 项目实战（十六）：功能级访问控制的实现](https://learner.blog.csdn.net/article/details/103250775)  
[Vue + Spring Boot 项目实战（十七）：后台角色、权限与菜单分配](https://learner.blog.csdn.net/article/details/103603726)  
[Vue + Spring Boot 项目实战（十八）：博客功能开发](https://learner.blog.csdn.net/article/details/104033436)

第三部分
----

[Vue + Spring Boot 项目实战（十九）：Web 项目优化解决方案](https://learner.blog.csdn.net/article/details/104763090)  
[Vue + Spring Boot 项目实战（二十）：前端优化实战](https://learner.blog.csdn.net/article/details/105594069)  
[Vue + Spring Boot 项目实战（二十一）：缓存的应用](https://learner.blog.csdn.net/article/details/107028816)

前言
==

之前写了一些关于 Java EE 的文章，主要是理论性质的，目的是帮助大家快速了解 Java EE 的核心内容，早日爬出这个陈旧又绕不开的坑，进入 Java Web 开发的新天地。当然只有理论是不够的，有很多细节需要在实践中理解，所以我决定做一个实践教程。

这个项目十分简单，是一个纯粹为教程而生的原型，可以视为一个简陋的带后台的**门户网站**。所以学习时不用有什么压力，估计你们学的比我写的快很多。

我的目标是根据这个教程，可以帮助 **新入行的或是刚开始学习相关技术** 的小伙伴们把一个完整的项目还原出来，建立起对前后端分离式 Web 开发的整体认知。

一开始，我会尽量详细地描述开发的过程，帮助大家快速上手。随着项目进展，曾经讲到过的、比较容易搜索到的内容会适当省略。

当然，每个人的理解方式不同，可能有些重要的细节没讲到位，欢迎大家在评论区提问。受限于个人水平，一定有很多说的不对的地方，大家理解一下，友善白嫖哈。

一、项目概述
======

这个项目我把它命名为 **“白卷”**，估摸着很多同学会拿它做课程设计之类，建议你们尽量加点自己的东西在里面，直接交白卷，你的良心不会痛吗？（狗头保命）

开个玩笑，叫白卷是因为它随着教程进展逐渐完善，象征着知识的从无到有，从有到多。

另外我还给它起了一个英文名字，叫 **White Jotter**（白色笔记本），纯粹是为了谐音。

项目遵循敏捷开发原则，会根据大家反馈的意见整理出新的需求，动态扩展、调整、优化。初始阶段按照简单的分层架构设计，具体见下图：

*   **应用架构**  
    ![](https://img-blog.csdnimg.cn/20200524211402855.JPG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L05ldWZfU29sZWls,size_16,color_FFFFFF,t_70#pic_center)
    
*   **技术架构**  
    ![](https://img-blog.csdnimg.cn/20200524211507112.JPG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L05ldWZfU29sZWls,size_16,color_FFFFFF,t_70#pic_center)
    

项目需要在前后端之间不断穿梭，但在做教程的时候，我会尽量模块化地去讲解。

此外，我把教程分为了几个阶段，是为了循序渐进、由易到难地讲解知识点。

各个阶段的主要内容如下（随教程进展更新）：

（一）第一部分
-------

这个项目的第一部分以图书信息管理为示例，主要帮助大家理解以下内容：

*   如何从 0 开始搭建 Web 项目？
*   什么是前后端分离？如何实现前后端分离？
*   单页面应用有哪些特点？
*   如何在 Web 项目中使用数据库并利用网页实现增删改查？
*   在开发中如何利用各种辅助手段？
*   Vue.js 的基本概念与用法
*   简单的前端页面设计
*   如何部署 Web 应用？

各个页面的效果大致如下：

**登录页面**：  
![](https://img-blog.csdnimg.cn/20191209210208815.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9sZWFybmVyLmJsb2cuY3Nkbi5uZXQ=,size_16,color_FFFFFF,t_70)  
**首页**：  
![](https://img-blog.csdnimg.cn/20191209210530763.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9sZWFybmVyLmJsb2cuY3Nkbi5uZXQ=,size_16,color_FFFFFF,t_70)  
**图书馆页面**：  
![](https://img-blog.csdnimg.cn/20191209210256344.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9sZWFybmVyLmJsb2cuY3Nkbi5uZXQ=,size_16,color_FFFFFF,t_70)

（二）第二部分
-------

项目的第二部分是后台管理模块的开发，主要包括以下内容：

*   后台管理模块的常见功能与布局（内容管理、用户 \ 权限管理、运维监控）
*   用户身份验证、授权、会话管理与信息加密存储
*   Shiro 框架的使用
*   实现不同粒度的访问控制（动态菜单、功能控制、数据控制）
*   结合内容管理，实现文章的编写与展示

后台基本结构如下：  
![](https://img-blog.csdnimg.cn/20191209211442519.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9sZWFybmVyLmJsb2cuY3Nkbi5uZXQ=,size_16,color_FFFFFF,t_70)  
后台页面效果：

**Dashboard（from PanJiaChen / vue-element-admin）**：  
![](https://img-blog.csdnimg.cn/20191209211530410.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9sZWFybmVyLmJsb2cuY3Nkbi5uZXQ=,size_16,color_FFFFFF,t_70)

**图书管理**：  
![](https://img-blog.csdnimg.cn/20191209211611897.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9sZWFybmVyLmJsb2cuY3Nkbi5uZXQ=,size_16,color_FFFFFF,t_70)  
**用户管理**：  
![](https://img-blog.csdnimg.cn/20191209211632331.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9sZWFybmVyLmJsb2cuY3Nkbi5uZXQ=,size_16,color_FFFFFF,t_70)  
笔记本页面效果：

**文章列表：**  
![](https://img-blog.csdnimg.cn/20200121212242241.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9sZWFybmVyLmJsb2cuY3Nkbi5uZXQ=,size_16,color_FFFFFF,t_70)  
**文章详情：**  
![](https://img-blog.csdnimg.cn/20200121212950872.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9sZWFybmVyLmJsb2cuY3Nkbi5uZXQ=,size_16,color_FFFFFF,t_70)

（三）第三部分
-------

第三部分是在前面的基础上，分析项目存在的不足，并对其进行由点及面的优化。

当简单的优化无法达到我们想要的目的时，就需要从架构层面进行整体的升级改造，那就是下一套教程的事情了。

此外，这个教程还有姐妹篇，也就是我正在更新的信息安全方面的教程。在攻防实践阶段，会把我们这个项目当作一号靶机，对黑客技术有兴趣的同学可以走一波关注：

[【信息安全系列文章地址】](https://learner.blog.csdn.net/category_10482034.html)

二、技术栈
=====

参考技术架构图，项目使用的主要技术如下：

1. 前端技术栈
--------

1.Vue.js  
2.ElementUI  
3.axios

2. 后端技术栈
--------

1.Spring Boot  
2.Apache Shiro  
3.Apache Log4j2  
4.Spring Data JPA  
5.Spring Data Redis

3. 数据库
------

1.MySQL  
2.Redis

在开发过程中还会不断用到一些新的技术，有必要的我会增添上去。

三、主要参考内容
========

*   [How2J.cn - Java 全栈学习网站](https://how2j.cn?p=50613)
*   [Vue.js - 渐进式 JavaScript 框架](https://cn.vuejs.org/)
*   [Element - 网站快速成型工具](http://element-cn.eleme.io/#/zh-CN)

下一篇：[Vue + Spring Boot 项目实战（二）：搭建 Vue.js 项目](https://learner.blog.csdn.net/article/details/88926242)

有兴趣听我扯技术之外的故事的同学可以关注我的公众号。不定期更新，权当和大家聊聊天，图个乐子。  
![](https://img-blog.csdnimg.cn/20191125154730664.jpg#pic_center)