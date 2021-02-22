---
title: 部署Hexo
date: 2021-02-22 13:20:54
tags:
---
> 原文地址 [easyhexo.com](https://easyhexo.com/1-Hexo-install-and-config/1-4-deploy-hexo.html#%E9%83%A8%E7%BD%B2%E5%88%B0-centos-servers)

[#](#部署到-github) 部署到 GitHub
---------------------------

### [#](#准备工作) 准备工作

1.  如果没有账号，请点此前往 [GitHub](https://github.com/) 注册一个 GitHub 账号。
2.  新建一个公开仓库，仓库名格式为 `your_username.github.io` 例如你的 GitHub 用户名是 `easyhexo` ，那么你的仓库地址名称就应该是 `easyhexo.github.io`
3.  创建完成后记下该仓库的 HTTPS/SSH 地址，一般格式为 `https://github.com/your_username/your_reponame.git` 在下一步会用到。

### [#](#安装部署插件) 安装[部署插件](https://github.com/hexojs/hexo-deployer-git)

### [#](#配置-git) 配置 Git

如果你只是安装好了 Git 但没有配置过你的 Git ，那么现在需要做的第一件事情就是设置你的 Git 用户名和邮箱。 在 Git Bash 中执行以下两条命令配置你的用户名和邮箱，这里建议用户名和邮箱与你的 GitHub 用户名和邮箱保持一致。

提醒

每次 Git 提交时都会附带这两条信息，用于记录是谁提交的更新，并且会随更新内容一起被记录到历史记录中。简单说，是用来标记的你的身份的～

### [#](#配置站点-config-yml-文件) 配置站点 `_config.yml` 文件

### [#](#发布到-github) 发布到 GitHub

在本地的 Hexo 站点根目录下，执行如下命令即可部署到 GitHub Pages 上。

提醒

如果是第一次使用，会弹出一个登录框，需要登录你的 GitHub 账号。

### [#](#自定义域名) 自定义域名

1.  如果你拥有个人域名，请用 A 记录解析到以下 IP 中的任意一个。如果使用 CNAME 请解析到你的 GitHub 仓库名称。

**参考表格**

<table><thead><tr><th>记录类型</th><th>主机记录</th><th>解析路线</th><th>记录值</th><th>MAX 优先级</th><th>TTL（秒）</th></tr></thead><tbody><tr><td>A</td><td>@</td><td>默认</td><td>185.199.110.153</td><td>-</td><td>600</td></tr><tr><td>CNAME</td><td>@</td><td>默认</td><td>GitHub 博客仓库名称</td><td>-</td><td>600</td></tr></tbody></table>

2.  打开仓库设置，找到 GitHub Pages 项目，修改 Custom domain 选项的值为你的自定义域名（不带 http 等前缀）
3.  勾选 Custom domain 选项下的 Enforce HTTPS 选项，强制开启 Https 。如果遇到 `Enforce HTTPS` 选项无法打开，可以稍等一会儿再尝试。

提醒

同时需要在本地的 `source` 目录新建一个 CNAME 文件，内容为你的自定义域名（不带 http 等前缀）。否则无法使用自定义域名功能（ `hexo d` 生成的文件没有 CNAME 文件，导致仓库的自定域名设置失效）

[#](#部署到-netlify) 部署到 Netlify
-----------------------------

Netlify 是一个可以部署静态网站的平台，也可以从 GitHub/GitLab/Bitbucket 的项目中快速构建你的网站。相比 GitHub Pages 更加专业、便捷，即使在国内的访问速度也不错，百度也能收录。

### [#](#准备工作-2) 准备工作

1.  如果没有账号，请点此前往 [GitHub](https://github.com/) 注册一个 GitHub 账号。
2.  新建一个公开仓库，仓库名格式为 `your_username.github.io` 例如你的 GitHub 用户名是 `easyhexo` ，那么你的仓库地址名称就应该是 `easyhexo.github.io`
3.  创建完成后记下该仓库的 HTTPS/SSH 地址，一般格式为 `https://github.com/your_username/your_reponame.git` 在下一步会用到。

### [#](#配置-git-2) 配置 Git

提醒

配置 Git 也和部署到 GitHub 一样。

如果你只是安装好了 Git 但没有配置过你的 Git ，那么现在需要做的第一件事情就是设置你的 Git 用户名和邮箱。 在 Git Bash 中执行以下两条命令配置你的用户名和邮箱，这里建议用户名和邮箱与你的 GitHub 用户名和邮箱保持一致。

提醒

每次 Git 提交时都会附带这两条信息，用于记录是谁提交的更新，并且会随更新内容一起被记录到历史记录中。简单说，是用来标记的你的身份的～

### [#](#配置本地和远程仓库) 配置本地和远程仓库

在博客根目录打开终端并执行以下命令：

这样就将你的 Hexo 博客 push 上 GitHub 仓库了。以后更新博客只需要 `git push origin master` 即可。

### [#](#配置-netlify) 配置 Netlify

1.  首先打开 [Netlify 官网](https://www.netlify.com/) ，用 GitHub 帐号登录。
2.  点击 **New site from Git**，进入 **Create a new site** 页面。
    1.  **Connect to Git provider** 页面，选择 GitHub。
    2.  **Pick a repository** 页面，选择你刚刚创建的博客存储库。
    3.  最后一步 **Build options, and deploy!**，Netlify 会检测到是 Hexo 项目，自动配置好了。点击 **Deploy site** 按钮即可。 ![](https://easyhexo.com/assets/img/1.83db3e4f.png)

最后出现如下界面：

![](https://easyhexo.com/assets/img/2.c8fd4268.png)

可以看到 Netlify 自动分配了一个域名，在这个网站中是 `https://nifty-noyce-b98546.netlify.com` 。

如果你有自己的域名并想要绑定它，请点击 **Set up a custom domain** 链接。这里不再赘述，详细步骤请见 [Netlify Docs: custom-domains](https://www.netlify.com/docs/custom-domains) 。

关于 HTTPS 的设置，Netlify Docs 中也有详细教程。请自行阅读。

[#](#部署到-coding) 部署到 CODING
---------------------------

### [#](#准备工作-3) 准备工作

CODING or dev.tencent.com?

~CODING = dev.tencent.com~

2019 年 12 月 25 日，CODING 个人版与腾讯云开发者平台升级至全新 CODING。也就是说，这两个平台回合并成 CODING 了。

1.  如果没有账号，请点此前往 [CODING](https://coding.net/) 注册 CODING 账号。
2.  新建一个公开仓库，仓库名格式为 `your_username.coding.me` 例如你的 CODING 用户名 (username) 是 `easyhexo` ，那么你的仓库名称就应该是 `easyhexo.coding.me`
3.  创建完成后记下该仓库的 HTTPS/SSH 地址 一般格式为 `https://coding.net/your_username/your_reponame.git` 在下一步会用到。
4.  如果您没有配置 `Git` 和 `hexo-deployer-git` 请参阅前文配置方法配置。

### [#](#配置站点-config-yml-文件-2) 配置站点 `_config.yml` 文件

### [#](#发布到-coding) 发布到 CODING

在本地 Hexo 站点根目录下，执行如下命令即可部署到 CODING Pages 上。

提醒

如果是第一次使用，会弹出一个登录框，需要登陆你的 CODING 账号。

### [#](#自定义域名-2) 自定义域名

1.  如果你拥有个人域名，请添加 CNAME 记录。
2.  绑定前请在域名 DNS 设置中添加一条 CNAME 记录指向 xxxx.coding.me。将 @ 和 www 记录都解析到这个即可。

**参考表格**

<table><thead><tr><th>记录类型</th><th>主机记录</th><th>解析路线</th><th>记录值</th><th>MAX 优先级</th><th>TTL（秒）</th></tr></thead><tbody><tr><td>CNAME</td><td>www</td><td>默认</td><td>xxxx.coding.me</td><td>-</td><td>600</td></tr><tr><td>CNAME</td><td>@</td><td>默认</td><td>xxxx.coding.me</td><td>-</td><td>600</td></tr></tbody></table>

2.  打开仓库设置，找到 代码 - Pages 服务，在绑定新域名下的文本框内输入你的自定义域名（不带 http 等前缀）。
3.  勾选 强制 HTTPS 访问。

提醒

出于 SEO 的考虑，我们建议您绑定一个 www 域名即可，如果您使用的域名 DNS 解析服务不支持添加 CNAME 记录，建议更换 Nameservers 到其他支持该功能的域名提供商（如 腾讯云）。如果遇到自定义域名失效，请参照前文 GitHub 配置方案解决。

详细内容请参阅 [CODING 官方文档](https://coding.net/help/) 。

[#](#部署到-centos-servers) 部署到 CentOS Servers
-------------------------------------------

### [#](#预先准备) 预先准备

*   确保你的 PC 已经安装好 Hexo 主程序的并且生成站点文件夹。安装 Hexo，请参阅[安装 Hexo](chrome-extension://ijllcpnolfcooahcekpamkbidhejabll/1-Hexo-install-and-config/1-2-install-hexo.html)
*   一台搭载 CentOS 7.4 64bit 的 ECS 服务器实例，其他 Linux 系统也可以
*   你至少应该掌握一丢丢的 Linux 命令

### [#](#安装部署插件-2) 安装[部署插件](https://github.com/hexojs/hexo-deployer-git)

### [#](#服务器环境配置) 服务器环境配置

#### [#](#更新服务器的软件包) 更新服务器的软件包

#### [#](#安装-git) 安装 Git

#### [#](#新建-git-用户) 新建 Git 用户

#### [#](#设置-gituser-的密码) 设置 gituser 的密码

#### [#](#配置-ssh-免密登陆) 配置 SSH 免密登陆

我们在使用 SSH 访问服务器时每一次连接都需要验证相应用户的密码，十分繁琐，所以我们通过一组密匙来进行授权访问。 在 `Git Bash` 中使用 `ssh-keygen` 命令在你的电脑上生成一组密匙，这个过程中 `ssh-keygen` 会确认密钥的存储位置（ Windows 下默认是 `c:users/username/.ssh/id_rsa` ），然后它会要求你输入两次密钥口令。如果你不想在使用密钥时输入口令，将其留空。

使用 `ssh-copy-id -i` 命令将公钥也就是 `id_rsa.pub` 添加到服务器上。这个过程中需要验证你所添加的用户的密码，如果你的服务器上存在多个用户，你需要逐一添加。添加完成后可以通过 `ssh your_user_name@HostIP` 命令来验证是否添加成功。

#### [#](#禁止-git-用户-shell-登陆权限) 禁止 Git 用户 Shell 登陆权限

出于安全考虑，禁用 Git 用户的 shell 权限 (必须先验证是否可以免密码登陆，可以后再禁用 shell 权限，否则无法通过 `ssh-copy-id -i` 添加 SSH 公钥)，使用 `vim /etc/passwd` 命令修改 `~/etc/` 下的 passwa 文件

#### [#](#ssh-免密登陆无效问题排查) SSH 免密登陆无效问题排查

检查 `/etc/ssh/` 目录下的 `sshd_config` 文件，确认以下关键选项是否正常

若还是不能正常工作，则检查用户权限和组权限

关于 SSH 的更多问题可查阅[这里](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/#platform-windows)

#### [#](#初始化-git-仓库) 初始化 Git 仓库

新建 `/var/repo` 目录，并在该目录下，使用 `git init --bare` 创建一个名为 `blog.git` 裸仓库，并改变该目录的所有者为 git 用户。

> 裸仓库可以直接作为服务器仓库供各开发者 push、pull 数据，实现数据共享和同步，不保存文件，只保存历史提交的版本信息。

#### [#](#配置-git-hooks) 配置 Git Hooks

使用 vim 命令在 `/var/repo/blog.git/hooks` 目录下创建 `post-receive` 文件

并且在 `post-receive` 文件中写入以下内容

提升 `post-receive` 的可执行权限

#### [#](#安装-nginx) 安装 Nginx

> Nginx 是一个高性能的 HTTP 和反向代理服务，也是一个 IMAP/POP3/SMTP 服务。外网用户访问服务器的 Web 服务由 Nginx 提供，Nginx 需要配置静态资源的路径信息才能通过 url 正确访问到服务器上的静态资源。

在安装之前我们先创建用于存放静态资源的目录 `/home/www/hexo` ，并更改其所有者，稍后将其设置为 Nginx 的默认静态资源目录。

#### [#](#配置静态服务器访问路径) 配置静态服务器访问路径

修改 Nginx 默认静态资源路径，打开 Nginx 的默认配置文件 `/etc/nginx/nginx.conf` ，将默认的 `root /usr/share/nginx/html;` 修改为: `root /home/www/hexo;` 如下所示。

如果你拥有 `SSL,TSL` 证书，需要配置 `HTTPS` 访问或者添加 `HTTP` 强制转换 `HTTPS` 访问功能，请参照以下代码进行配置。

### [#](#配置-config-yml文件) 配置 `_config.yml` 文件

在 `_config.yml` 文件中设置 deploy 选项

#### [#](#发布站点) 发布站点

在你的 Hexo 站点根目录下，执行如下命令即可发布你的站点到服务器上。

[#](#其他问题) 其他问题
---------------

### [#](#hooks-失效) Hooks 失效

如果部署成功，但是 `/home/www/hexo` 目录的资源文件并未更新，请检查 `post-receive` 是否有执行权限，以及 `/home/www/hexo` 文件所有者是否为 Git 用户，以及是否具有读写权限。

### [#](#部署后，部分页面-404) 部署后，部分页面 404

部分情况下，在初次部署之后，部分文章或者页面路径大小如果更改了，会导致新部署上去的页面出现 404 错误。 这是由于 Git 没有区分大小写导致的文件路径错误。修改 `hexo根目录/.deploy_git/.git/` 下的 `config` 文件

[#](#视频) 视频
-----------