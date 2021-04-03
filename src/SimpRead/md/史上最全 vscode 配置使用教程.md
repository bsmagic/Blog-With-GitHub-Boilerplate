\> 本文由 \[简悦 SimpRead\](http://ksria.com/simpread/) 转码， 原文地址 \[zhuanlan.zhihu.com\](https://zhuanlan.zhihu.com/p/113222681)

工欲善其事，必先利其器。想要优雅且高效的编写代码，必须熟练使用一款前端开发工具。但前端开发工具数不胜数，像 HBuilder、Sublime Text、WebStorm、Visual Studio Code...... 等等, 其中 VSCode 以其轻量且强大的代码编辑功能和丰富的插件生态系统，独受前端工师的青睐。网上有很多 vscode 的配置以及使用博客，但都没有本篇那么详细且全面。

![](https://pic2.zhimg.com/v2-f49196c75f2d84da6334e0eeed8c1413_b.jpg)![](https://pic2.zhimg.com/v2-f49196c75f2d84da6334e0eeed8c1413_r.jpg)

软件下载
----

直接在官网进行下载，需要的也可以留言给你发软件包

[Visual Studio Code - Code Editing. Redefined​code.visualstudio.com![图标](https://pic4.zhimg.com/v2-beaba009c542a9f6fe1d2034a7ed568b_180x120.jpg)](https://code.visualstudio.com/)

首页

![](https://pic4.zhimg.com/v2-0f049e5f50eb1175eea793f15fa95b08_b.jpg)![](https://pic4.zhimg.com/v2-0f049e5f50eb1175eea793f15fa95b08_r.jpg)

vscode 设置成中文
------------

vscode 默认的语言是英文，对于英文不好的小伙伴可能不太友好。简单几步教大家如何将 vscode 设置成中文。

1.  按快捷键 “Ctrl+Shift+P”。
2.  在 “vscode” 顶部会出现一个搜索框。
3.  输入 “configure language”，然后回车。
4.  “vscode” 里面就会打开一个语言配置文件。
5.  将 “en-us” 修改成“zh-cn”。
6.  按 “Ctrl+S” 保存设置。
7.  关闭 “vscode”，再次打开就可以看到中文界面了。

当然如果你不愿意设置，也可以直接安装它的中文插件，还是很人性化的。

![](https://pic3.zhimg.com/v2-ddbfa1f88bf57ffe6a2cee34a973243f_b.jpg)![](https://pic3.zhimg.com/v2-ddbfa1f88bf57ffe6a2cee34a973243f_r.jpg)

VScode 用户设置
-----------

1\. 打开设置

文件 -- 首选项 -- 设置，打开用户设置。VScode 支持选择配置，也支持编辑 setting.json 文件修改默认配置。个人更倾向于编写 json 的方式进行配置，下面会附上我个人的配置代码

这里解析几个常用配置项：

（1）editor.fontsize 用来设置字体大小，可以设置 editor.fontsize : 14;

（2）files.autoSave 这个属性是表示文件是否进行自动保存，推荐设置为 onFocusChange——文件焦点变化时自动保存。

（3）editor.tabCompletion 用来在出现推荐值时，按下 Tab 键是否自动填入最佳推荐值，推荐设置为 true;

（4）editor.codeActionsOnSave 中的 source.organizeImports 属性，这个属性能够在保存时，自动调整 import 语句相关顺序，能够让你的 import 语句按照字母顺序进行排列，推荐设置为 true, 即 "editor.codeActionsOnSave": {"source.organizeImports": true}；

（5）editor.lineNumbers 设置代码行号, 即 editor.lineNumbers ：true；

我的个人配置，供参考：

```
{
  "files.associations": {
  "\*.vue": "vue",
  "\*.wpy": "vue",
  "\*.wxml": "html",
  "\*.wxss": "css"
  },
  "terminal.integrated.shell.windows": "C:\\\\Windows\\\\System32\\\\cmd.exe",
  "git.enableSmartCommit": true,
  "git.autofetch": true,
  "emmet.triggerExpansionOnTab": true,
  "emmet.showAbbreviationSuggestions": true,
  "emmet.showExpandedAbbreviation": "always",
  "emmet.includeLanguages": {
  "vue-html": "html",
  "vue": "html",
  "wpy": "html"
  },
  //主题颜色 
  //"workbench.colorTheme": "Monokai",
  "git.confirmSync": false,
  "explorer.confirmDelete": false,
  "editor.fontSize": 14,
  "window.zoomLevel": 1,
  "editor.wordWrap": "on",
  "editor.detectIndentation": false,
  // 重新设定tabsize
  "editor.tabSize": 2,
  //失去焦点后自动保存
  "files.autoSave": "onFocusChange",
  // #值设置为true时，每次保存的时候自动格式化；
  "editor.formatOnSave": false,
   //每120行就显示一条线
  "editor.rulers": \[
  \],
  // 在使用搜索功能时，将这些文件夹/文件排除在外
  "search.exclude": {
      "\*\*/node\_modules": true,
      "\*\*/bower\_components": true,
      "\*\*/target": true,
      "\*\*/logs": true,
  }, 
  // 这些文件将不会显示在工作空间中
  "files.exclude": {
      "\*\*/.git": true,
      "\*\*/.svn": true,
      "\*\*/.hg": true,
      "\*\*/CVS": true,
      "\*\*/.DS\_Store": true,
      "\*\*/\*.js": {
          "when": "$(basename).ts" //ts编译后生成的js文件将不会显示在工作空中
      },
      "\*\*/node\_modules": true
  }, 
  // #让vue中的js按"prettier"格式进行格式化
  "vetur.format.defaultFormatter.html": "js-beautify-html",
  "vetur.format.defaultFormatter.js": "prettier",
  "vetur.format.defaultFormatterOptions": {
      "js-beautify-html": {
          // #vue组件中html代码格式化样式
          "wrap\_attributes": "force-aligned", //也可以设置为“auto”，效果会不一样
          "wrap\_line\_length": 200,
          "end\_with\_newline": false,
          "semi": false,
          "singleQuote": true
      },
      "prettier": {
          "semi": false,
          "singleQuote": true
      }
  }
}
```

**最近经常有人微信问我，这个配置代码写在哪里？**

新版的 vscode 设置默认为 UI 的设置，而非之前的 json 设置。如果你想复制我上面这段代码进行配置，可以进行下面的修改

文件 > 首选项 > 设置 > 搜索 workbench.settings.editor，选中 json 即可改成 json 设置；

**禁用自动更新**

文件 > 首选项 > 设置（macOS：代码 > 首选项 > 设置，搜索 update mode 并将设置更改为 none。

常用的快捷键
------

高效的使用 vscode, 记住一些常用的快捷键是必不可少的，我给大家罗列了一些日常工作过程中用的多的快捷键。

以下以 Windows 为主，windows 的 Ctrl，mac 下换成 Command 就行了

对于 **行** 的操作：

*   重开一行：光标在行尾的话，回车即可；不在行尾，ctrl `+ enter` 向下重开一行；ctrl+`shift + enter` 则是在上一行重开一行
*   删除一行：光标没有选择内容时，ctrl `+ x` 剪切一行；ctrl +`shift + k` 直接删除一行
*   移动一行：`alt + ↑` 向上移动一行；`alt + ↓` 向下移动一行
*   复制一行：`shift + alt + ↓` 向下复制一行；`shift + alt + ↑` 向上复制一行
*   ctrl + z 回退

对于 **词** 的操作：

*   选中一个词：ctrl `+ d`

搜索或者替换：

*   ctrl `+ f` ：搜索
*   ctrl `+ alt + f`： 替换
*   ctrl `+ shift + f`：在项目内搜索

通过 **Ctrl + \`** 可以打开或关闭终端

Ctrl+P 快速打开最近打开的文件

Ctrl+Shift+N 打开新的编辑器窗口

Ctrl+Shift+W 关闭编辑器

Home 光标跳转到行头

End 光标跳转到行尾

Ctrl + Home 跳转到页头

Ctrl + End 跳转到页尾

Ctrl + Shift + \[ 折叠区域代码

Ctrl + Shift + \] 展开区域代码

Ctrl + / 添加关闭行注释

Shift + Alt +A 块区域注释

插件安装
----

在输入框中输入想要安装的插件名称，点击安装即可。安装后没有效果，可以重启 vscode

![](https://pic3.zhimg.com/v2-4e57c8d10598038ba80642446e7ea698_b.jpg)![](https://pic3.zhimg.com/v2-4e57c8d10598038ba80642446e7ea698_r.jpg)

**必备插件**

**1、View In Browser**

在浏览器里预览网页必备。运行 html 文件

![](https://picb.zhimg.com/v2-69b3dfead6052e0702f5970ae9f232d9_b.gif)![](https://picb.zhimg.com/v2-69b3dfead6052e0702f5970ae9f232d9_b.gif)

### 2、vscode-icons

改变编辑器里面的文件图标

### 3、Bracket Pair Colorizer

给嵌套的各种括号加上不同的颜色。

### 4、Auto Rename Tag

自动修改匹配的 HTML 标签。

![](https://picb.zhimg.com/v2-304d2802620974eeb369a6302f50cfc0_b.gif)![](https://picb.zhimg.com/v2-304d2802620974eeb369a6302f50cfc0_b.gif)

### 5、Path Intellisense

**智能路径提示**，可以在你输入文件路径时智能提示。

![](https://picb.zhimg.com/v2-304d2802620974eeb369a6302f50cfc0_b.gif)![](https://picb.zhimg.com/v2-304d2802620974eeb369a6302f50cfc0_b.gif)

### 6、Markdown Preview

实时预览 markdown。

### 7、stylelint

CSS / SCSS / Less 语法检查

### 8、Import Cost

引入包大小计算, 对于项目打包后体积掌握很有帮助

![](https://picb.zhimg.com/v2-2db7c8e03f575e26584b54a5c2ccace6_b.gif)![](https://picb.zhimg.com/v2-2db7c8e03f575e26584b54a5c2ccace6_b.gif)

### 9、Prettier

比 Beautify 更好用的代码格式化插件  

Vue 插件
------

### vetur

语法高亮、智能感知、Emmet 等

![](https://pic3.zhimg.com/v2-8abdcb8f10bcd6009ffcad29ebdfe576_b.jpg)![](https://pic3.zhimg.com/v2-8abdcb8f10bcd6009ffcad29ebdfe576_r.jpg)

### VueHelper

snippet 代码片段

![](https://pic4.zhimg.com/v2-e7396a249f4ad2b6c68e94a37cb49ff5_b.gif)![](https://pic4.zhimg.com/v2-e7396a249f4ad2b6c68e94a37cb49ff5_b.gif)

其它插件
----

**1、CSScomb**

CSS 书写顺序规则，这里我推荐腾讯 AollyTeam 团队的规范：

[http://alloyteam.github.io/CodeGuide/#css-declaration-order​alloyteam.github.io](http://alloyteam.github.io/CodeGuide/#css-declaration-order)

简单说下这个插件怎么用：

在项目的根目录下创建一个名为 csscomb.json 的文件，然后添加一些配置项。也可以将配置项写入项目的 package.json 文件中的 csscombConfig 字段。

至于添加的配置项，CSScomb 提供了示例配置文件：

[https://github.com/csscomb/csscomb.js/blob/master/config/csscomb.json​github.com](https://github.com/csscomb/csscomb.js/blob/master/config/csscomb.json)

其中的 sort-order 就是 CSS 属性书写顺序，可以按照自己遵循的规范设置，所以我直接替换成了腾讯的。

这个配置文件里面各个字段的作用可以戳这里查看：

[csscomb/csscomb.js​github.com](https://github.com/csscomb/csscomb.js/blob/master/doc/options.md)

**2、Turbo Console Log**

快捷添加 console.log，一键 注释 / 启用 / 删除 所有 console.log。这也是我最常用的一个插件

![](https://pic1.zhimg.com/v2-b14aec7821adc57a3f41ac746a5689a7_b.gif)![](https://pic1.zhimg.com/v2-b14aec7821adc57a3f41ac746a5689a7_b.gif)

简单说下这个插件要用到的快捷键:

```
ctrl + alt + l 选中变量之后，使用这个快捷键生成 console.log
alt + shift + c 注释所有 console.log
alt + shift + u 启用所有 console.log
alt + shift + d 删除所有 console.log
```

**3、GitLens**

详细的 Git 提交日志。

Git 重度使用者必备，尤其是多人协作时：哪一行代码，何时、何人提交都有记录。

妈妈再也不用担心我背锅了！

![](https://picb.zhimg.com/v2-5e020466c135639aa33ba9a26e8ed2fa_b.png)![](https://picb.zhimg.com/v2-5e020466c135639aa33ba9a26e8ed2fa_r.jpg)

### 4、css-auto-prefix

**自动添加 CSS 私有前缀**。

![](https://pic3.zhimg.com/v2-01d42a4fb0039acb17ff5a7b708d1030_b.gif)![](https://pic3.zhimg.com/v2-01d42a4fb0039acb17ff5a7b708d1030_b.gif)

### 5、change-case

**转换命名风格**。  

![](https://pic1.zhimg.com/v2-1085adfd3dc66da8ed6b40c5961a786e_b.gif)![](https://pic1.zhimg.com/v2-1085adfd3dc66da8ed6b40c5961a786e_b.gif)

**6、CSS Peek**

**定位 CSS 类名**。  

![](https://pic4.zhimg.com/v2-247271ae745aaffee6497624e335b7b9_b.gif)![](https://pic4.zhimg.com/v2-247271ae745aaffee6497624e335b7b9_b.gif)

**7、vscode-json**

处理 JSON 文件，用法看图：

![](https://pic3.zhimg.com/v2-5a6867c294dafe411cc58a43de69875d_b.gif)![](https://pic3.zhimg.com/v2-5a6867c294dafe411cc58a43de69875d_b.gif)

### 8、Regex Previewer

**实时预览正则表达式的效果**。  

![](https://picb.zhimg.com/v2-ff1f00be77163d4e24b146211c618212_b.gif)![](https://picb.zhimg.com/v2-ff1f00be77163d4e24b146211c618212_b.gif)

设置同步
----

花了一天终于把 vscode 配置成自己满意的样子，如果每换一次电脑就要重新来一次，大家一定会手撕了我。放心，早就帮大家准备好了。Settings Sync，在不同电脑间同步你的插件。

首先要想在不同的设备间同步你的插件, 需要用到 Token 和 Gist id

Token 就是你把插件上传到 github 上时, 让你保存的那段字符，Gist id 在你上传插件的那台电脑上保存着。

先给大家来三个快捷键，后面会用到

```
1、CTRL+SHIFT+P 我也不知道叫什么，暂且就叫它功能搜索功能吧
2、ALT+SHIFT+D 下载配置
3、ALT+SHIFT+U 上传配置
```

现在手把手教大家配置：

1、安装 Settings Sync  
2、登陆 Github>settings>Developer settings>personal access tokens>generate new token，输入名称，勾选 Gist，提交

![](https://pic3.zhimg.com/v2-9898e9d1d90e227fdb6da88a829b01d2_b.jpg)![](https://pic3.zhimg.com/v2-9898e9d1d90e227fdb6da88a829b01d2_r.jpg)

3、保存 Github Access Token  
4、打开 vscode，Ctrl+Shift+P 打开命令框 --> 输入 sync--> 选择高级设置 --> 编辑本地扩展设置 --> 编辑 token

5、Ctrl+Shift+P 打开命令框 --> 输入 sync--> 找到 update/upload settings，上传成功后会返回 Gist ID，保存此 Gist ID.

![](https://pic1.zhimg.com/v2-76ae0fd6b07c5c7949fc3a6e02dff2c1_b.gif)![](https://pic1.zhimg.com/v2-76ae0fd6b07c5c7949fc3a6e02dff2c1_b.gif)

6、在 VSCode 里，依次打开: 文件 -> 首选项 -> 设置，然后输入 Sync 进行搜索: 能找到你 gist id

![](https://picb.zhimg.com/v2-86515bfd4e5aada27c7f998dcdaf1dfa_b.jpg)![](https://picb.zhimg.com/v2-86515bfd4e5aada27c7f998dcdaf1dfa_r.jpg)

7、若需在其他机器上 DownLoad 插件的话，同样，Ctrl+Shift+P 打开命令框，输入 sync，找到 Download settings，会跳转到 Github 的 Token 编辑界面，点 Edit，regenerate token，保存新生成的 token，在 vscode 命令框中输入此 Token，回车，再输入之前的 Gist ID，即可同步插件和设置  

开启一个本地服务
--------

**第一种方式**

1\. 安装 Debugger for Chrome 插件

![](https://pic3.zhimg.com/v2-80a0108d05009387f257d9b70226c3c4_b.jpg)![](https://pic3.zhimg.com/v2-80a0108d05009387f257d9b70226c3c4_r.jpg)

2\. 使用 ctrl+\` 快捷键打开终端，然后输入 npm install -g live-server

3\. 在命令行里输入 live-server 即可

**第二种方式**

在写前端页面中，经常会在浏览器运行 HTML 页面，从本地文件夹中直接打开的一般都是 file 协议，当代码中存在 http 或 https 的链接时，HTML 页面就无法正常打开，为了解决这种情况，需要在在本地开启一个本地的服务器。 本文是利用 node.js 中的 http-server，开启本地服务，步骤如下：

_1\. 安装 http-server_

在终端输入： $ npm install http-server -g

_2\. 开启 http-server 服务_

终端进入目标文件夹，然后在终端输入：

```
$ http-server -c-1   （⚠️只输入http-server的话，更新了代码后，页面不会同步更新）
Starting up http-server, serving ./
Available on:
  http://127.0.0.1:8080
  http://192.168.8.196:8080
Hit CTRL-C to stop the server
```

_3\. 关闭 http-server 服务_

按快捷键 CTRL-C 终端显示 ^Chttp-server stopped. 即关闭服务成功。

**❤️关注 + 点赞 + 收藏 + 评论 + 转发❤️**，原创不易，鼓励笔者创作更好的文章

关注公众号_**前端码头**_，获取独家学习路线 + 精品课程，更多前端小干货等着你喔