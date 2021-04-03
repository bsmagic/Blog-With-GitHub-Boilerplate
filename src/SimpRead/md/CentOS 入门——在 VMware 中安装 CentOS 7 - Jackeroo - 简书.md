> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 [www.jianshu.com](https://www.jianshu.com/p/e31534077185)

![](http://upload-images.jianshu.io/upload_images/1906922-33374de68ac927b5.png)

CentOS、VMware 双剑合壁

CentOS（Community ENTerprise Operating System）是目前最流行的 Linux 的发行版本之一。它是在 RedHat Enterprise Linux（RHEL）依照开源协议分享的源代码编译而成，天生具备 RedHat Linux 的稳定性，又可以免费使用。

一、VMware 简介
-----------

VMware 是一个虚拟机软件，可以在现有的操作系统中虚拟出一个新的硬件环境。从而在不影响现在系统的基础上，轻松体验 Linux 操作系统。  
VMware 主要特点：

*   不需要分区或者重新启动就可以在同一台电脑上同时使用几种操作系统
*   主机或者几台虚拟机可以组成虚拟网络，甚至组成服务器集群
*   虚拟主机的硬件设施：CPU、内存、硬盘大小可以随时动态调整

### 1. Windows 版

VMware Workstation Pro 14 官方下载： [http://download3.vmware.com/software/wkst/file/VMware-workstation-full-14.1.3-9474260.exe](http://download3.vmware.com/software/wkst/file/VMware-workstation-full-14.1.3-9474260.exe)

和谐码：

> ZY5H0-D3Y8K-M89EZ-AYPEG-MYUA8  
> FF590-2DX83-M81LZ-XDM7E-MKUT4

### 2. Mac 版

VMware Fushion 10 官方下载：  
[https://download3.vmware.com/software/fusion/file/VMware-Fusion-10.1.3-9472307.dmg?PubCID=3848409](https://download3.vmware.com/software/fusion/file/VMware-Fusion-10.1.3-9472307.dmg?PubCID=3848409)

和谐码：

> FG3TU-DDX1M-084CY-MFYQX-QC0RD

### 3. Linux 版本

VMware Workstation Pro 官方下载： [http://download3.vmware.com/software/wkst/file/VMware-Workstation-Full-14.1.3-9474260.x86_64.bundle](http://download3.vmware.com/software/wkst/file/VMware-Workstation-Full-14.1.3-9474260.x86_64.bundle)

和谐码：

> VF19H-8YY5L-48DQY-JEWNG-YPKF6

二、 CentOS 简介
------------

当前国内的 Linux 服务器市场，RHEL/CentOS 占据了很大的份额，所以学习 Linux 当然要从 CentOS 入手。它的最新版本为 CentOS 7——建议大家都从这个版本开始，不要再试图安装老版本，毕竟 CentOS 6 与新版有很大的差别。

CentOS 官方网站： [传送门](http://www.centos.org/)  
CentOS 7 国内镜像： [http://mirrors.163.com/centos/7/isos/x86_64/CentOS-7-x86_64-Minimal-1804.iso](http://mirrors.163.com/centos/7/isos/x86_64/CentOS-7-x86_64-Minimal-1804.iso)

三、新建虚拟机
-------

在 VMware 中安装 CentOS，步骤十分简单，大家只需要跟着我走下去就 OK。

### 1、新建虚拟机

打开安装好的 VMware Workstation Pro 14，选择 “文件”→“新建虚拟机” 打开“新建虚拟机向导”。

  

![](http://upload-images.jianshu.io/upload_images/1906922-d7f8952f5200206c.png)

打开新建虚拟机向导

### 2、选择虚拟机硬件兼容性

如果你只是在本机上使用，则尽管选择最新的 Workstation 14，点击 “下一步” 继续。  
需要注意的是，如果你需要把虚拟机拷贝到安装有其他版本 VMware Workstation 的电脑上使用，则最好选择二者之间的低版本。

  

![](http://upload-images.jianshu.io/upload_images/1906922-5d368c23d270505f.png)

选择 VMware Workstation 兼容版本

### 3、安装客户机操作系统

选择 “安装程序光盘映像文件(iso)”，再点击“浏览” 选中刚才下载的 CentOS 安装镜像。点击 “下一步” 继续。

  

![](http://upload-images.jianshu.io/upload_images/1906922-d514cf794f3f8be8.png)

挂载 CentOS 安装镜像

### 4、命名虚拟机

给虚拟机起个名字吧。最好结合虚拟机的实际用途和系统版本命名，比如我要在其中安装 Hadoop，就起名为： hadoop@CentOS7。  
再点击 “位置” 后的 “浏览” 按钮，选择一个足够大的硬盘分区，保存虚拟机配置信息。

  

![](http://upload-images.jianshu.io/upload_images/1906922-22cc945c6234dc00.png)

虚拟机配置信息保存位置

### 5、处理器配置

指定虚拟机的 CPU（处理器）的数量和核心数，根据自己的需求设置，也可以直接点击 “下一步” 继续。

  

![](http://upload-images.jianshu.io/upload_images/1906922-f155a099e298371f.png)

CPU 设置

### 6、内存设置

设置 CentOS 需要的内存。我一般安装的是服务器，所以内存会比较大点，比如 2048MB。

  

![](http://upload-images.jianshu.io/upload_images/1906922-878131e578e525cc.png)

设置内存大小

### 7、网络设置

VMware 支持三种网络配置，一般情况下，选择默认的 “使用网络地址转换（NAT）” 就可以了：虚拟机中的系统可以上网，主机也可以访问虚拟机的网络。

  

![](http://upload-images.jianshu.io/upload_images/1906922-97c6c91c8e34b7b9.png)

网络设置

### 8、I/O 控制器类型

选择默认的 “LSI Logic” 就可以很好地支持 CentOS 7，不用更改。

  

![](http://upload-images.jianshu.io/upload_images/1906922-52f6e880e1901e96.png)

SCSI 控制器选择

### 9、虚拟磁盘类型

默认的 “SCSI（S）(推荐）” 就可以，不用更改。

  

![](http://upload-images.jianshu.io/upload_images/1906922-8e7831e0484d406a.png)

选择 SCSI 接口硬盘

### 10、选择磁盘

默认是 “创建新虚拟磁盘”，不用更改。

  

![](http://upload-images.jianshu.io/upload_images/1906922-2f1cb95274592ddd.png)

新建虚拟硬盘

### 11、指定磁盘容量

默认设置的 20GB 不够大，我们直接指定 100GB。不过放心，它是按需分配，不会直接就占用了 100GB 的硬盘空间。

  

![](http://upload-images.jianshu.io/upload_images/1906922-2b526315cdf57644.png)

设置硬盘大小

### 12、指定磁盘文件

选择我们刚才指定保存虚拟机的位置，并且给磁盘文件起个名字就 OK。

  

![](http://upload-images.jianshu.io/upload_images/1906922-84c51408975d02ee.png)

指定磁盘文件保存位置和名称

四、安装 CentOS
-----------

虚拟机新建成功之后，我们在 VMware Workstation Pro 的主界面，点击启动按钮，就很快来到了 CentOS 7 的安装界面。

### 1、开始安装

第一个界面，简单无比的英文，只能选择”Install CentOS 7“。

  

![](http://upload-images.jianshu.io/upload_images/1906922-1424379ddfd9f3cd.png)

开始安装 CentOS 7

### 2、启用中文界面安装

对英文界面不感冒的朋友，可以在这里选择” 中文 “，在安装过程中使用中文界面。

  

![](http://upload-images.jianshu.io/upload_images/1906922-39a860873f64719f.png)

CentOS 支持中文安装界面

### 3、安装信息配置

在” 安装信息摘要 “界面，我们可以在安装 CentOS 之前进行一些简单的配置。包括本地化、软件、系统等。  
CentOS 安装已经尽可能做得友好，你甚至只需要做以下两个设置，就可以完成配置。

  

![](http://upload-images.jianshu.io/upload_images/1906922-d923ec0cbac278a8.png)

需要确认安装位置

#### 3.1 安装位置——分区配置

点击”安装位置 “，在新打开的” 安装位置 “配置界面，你所需要做的就是点击” 完成“确认一下硬盘分区。  

!

![](http://upload-images.jianshu.io/upload_images/1906922-4f374b81b90d503f.png)

确认下，采用自动配置的硬盘分区即可

#### 3.2 网络和主机名——网络配置

点击”网络和主机名 “，点击右侧的” 滑块“，让 CentOS 安装向导帮助我们自动配置好网络。

  

![](http://upload-images.jianshu.io/upload_images/1906922-2fd6486b7fe52e61.png)

启用网络——自动配置

#### 3.3 自动安装中

返回”安装信息摘要 “界面，点击” 开始安装“……

### 4、给 root 用户设置个密码

在安装的过程中，我们不要忘记做两件事情：

  

![](http://upload-images.jianshu.io/upload_images/1906922-1948b70fbd9996b3.png)

给 root 设置密码

> *   点击”root 密码 “，给系统管理员 root 设置密码。
> *   点击” 创建用户 “，新建一个用来登录的用户和密码。

![](http://upload-images.jianshu.io/upload_images/1906922-cd5f6e7546bf0e1d.png)

设置 root 密码

接下来，就是去喝杯咖啡，10 分钟不到——CentOS 7 就成功安装了。