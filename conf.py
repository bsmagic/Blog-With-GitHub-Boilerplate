# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    # "name": "Galileo",
    # "type": "local",
    # "path": "../Galileo"
    # "name": "Kepler",
    # "type": "git",
    # "url": "https://github.com/AlanDecode/Maverick-Theme-Kepler.git",
    # "branch": "latest"
    "name": "Galileo",
    "type": "git",
    "url": "https://github.com/1244919208/Maverick-Theme-Galileo.git",
    "branch": "latest"
}
enable_jsdelivr = {
    "enabled": True,
    "repo": "1244919208/1244919208.github.io@gh-pages"
}

# 站点设置
site_name = "穿山甲老窝"
site_logo = "${static_prefix}logo.png"
site_build_date = "2021-2-22 12:51+08:00"
author = "穿山甲叔叔"
email = "ztfword@foxmail.com"
author_homepage = "csjss.top/"
description = "回收废旧大老婆二老婆"
key_words = ['Maverick', '穿山甲叔叔', 'Galileo', 'blog']
language = 'zh-CN'
external_links = [
    {
        "name": "听点啥",
        "url": "https://wyy.csjss.top",
        "brief": "Yes"
    },
    {
        "name": "网盘",
        "url": "https://demo.csjss.top",
        "brief":"OneManager"
    }
     
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    },
    {
        "name": "Todo",
        "url": "${site_prefix}Todo/",
        "target": "_self"
    },
    {
        "name": "公众号",
        "url": "${site_prefix}wechat/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Twitter",
        "url": "https://twitter.com/2233word",
        "icon": "gi gi-twitter"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/1244919208",
        "icon": "gi gi-github"
    },
    {
        "name": "Weibo",
        "url": "https://weibo.com/u/6774943340/home",
        "icon": "gi gi-weibo"
    }
    ,
    {
        "name": "bilibili",
        "url": "https://space.bilibili.com/18700960",
        "icon": "gi gi-bilibili"
    }
    
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
<link rel="stylesheet" href="/assets/live2d/css/live2d.css" />
'''

footer_addon = '''
<script>
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "https://hm.baidu.com/hm.js?3ed3a5739644e280369cd2d33d6490e2";
  var s = document.getElementsByTagName("script")[0]; 
  s.parentNode.insertBefore(hm, s);
})();
</script>
'''

body_addon = '''
<div id="landlord">
    <div class="message" style="opacity:0"></div>
    <canvas id="live2d" width="280" height="250" class="live2d"></canvas>
    <div class="hide-button">隐藏</div>
</div>
<script type="text/javascript">
    var message_Path = '/assets/live2d/'
    var home_Path = 'https://csjss.top/'  //此处修改为你的域名，必须带斜杠
</script>
<script type="text/javascript" src="/assets/live2d/js/live2d.js"></script>
<script type="text/javascript" src="/assets/live2d/js/message.js"></script>
<script type="text/javascript">
    loadlive2d("live2d", "/assets/live2d/model/tia/model.json");
</script>
'''