Title:解决百度爬虫无法爬取Github Pages上的个人博客
Date:2018-02-24
Category:Blog
Tags:Blog,Pelican

某天突然发现无法百度到自己的博客内容了，于是乎开始一段曲折的排障过程。

我的blog是放在GitHub pages，并通过cloudflare搞了一个伪https，并且使用了cloudflare的cdn服务。

通过各种搜百度，搜谷歌，站长工具debug。确认了是GitHub屏蔽了百度的爬虫。GG

参考了[知乎](http://t.cn/RzEyiSv)上的几个解决方案：

1. 使用CDN
2. Dnspod 双路解析
3. 更换pages服务商


我原本就使用了cdn服务依然出现爬虫失败的问题，分析下来一个是流量本身太小（是根本没有好吗），造成请求很容易回源，然后403。

Dnspod 双路解析的话就无法使用cloudflare提供的伪https了，瞬间逼格就下来了。

最终我选择了更换pages服务提供者。

Coding的pages服务，5秒广告，谢谢不送。

GitCafe被Coding收购了 GG。

又看了下Gitee（码云）的pages服务，不支持自定义域名，不符合需求。

GitLab的pages服务完全符合需求 nice，开搞。

原本blog使用的python的pelican框架代码在GitHub上并通过Travis-ci进行构建的，并不是本地构建后推送到远端的，主要是因为懒，这样只需要写Markdown文件，提交，持续集成，持续发布。所以又想了一个懒办法。在Travis-ci进行构建GitHub pages的同时把代码提交到GitLab仓库，再由GitLab的CI/CD进行持续集成构建。

GitLab提供的pages服务使用姿势和GitHub还是有很大不同的。

[GitLab pages搭建官方说明](https://gitlab.com/help/user/project/pages/index.md)

简单来说就是需要见一个项目，且项目名必须是 {username}.gitlab.io

并在项目下建立GitLab Ci所用配置文件 .gitlab-ci.yml

以我使用的python pelican blog生成器举例 .gitlab-ci.yml：

	image: python:2.7-alpine
	
	before_script:
	  - apk update && apk upgrade && apk add git
	
	pages:
	  script:
	  - pip install -r requirements.txt
	  - git clone --depth 1 https://github.com/FuriousSlade/pelican-swain.git
	  - git clone --depth 1 https://github.com/FuriousSlade/pelican-plugins.git
	  - pelican -s publishconf.py
	  - mv output public
	  artifacts:
	    paths:
	    - public/

详解：
	
	# 构建使用的docker镜像
	image: python:2.7-alpine 
	
	# 构建前执行脚本
	# 因为需要git clone 依赖的模版和插件，构建前先安装git（基础镜像无git命令）
	before_script:
	  - apk update && apk upgrade && apk add git
	
	# 构建pages
	pages:
	  script:
	  # pip安装依赖库
	  - pip install -r requirements.txt
	  # git clone 依赖模版
	  - git clone --depth 1 https://github.com/FuriousSlade/pelican-swain.git
	  # git clone 依赖插件
	  - git clone --depth 1 https://github.com/FuriousSlade/pelican-plugins.git
	  # 构建静态blog
	  - pelican -s publishconf.py
	  # 将构建结果目录output重命名为public，注意静态资源的输出目录必须是public
	  - mv output public
	  artifacts:
	    paths:
	    # 最终将会发布到pages的目录
	    # 本来我改了目录为output最终导致pages 404
	    # 只有使用public时pages服务正常可用，不知道是不是潜规则
	    - public/



确定GitLab能正确触发构建，生成pages页面。

变更域名解析至GitLab pages。

最终代码依然提交GitHub，利用GitLab提供pages服务。
