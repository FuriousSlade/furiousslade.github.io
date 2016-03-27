Title:Redmine使用Mongrel服务器。
Date:2015-05-13
Category:Blog
Tags:Redmine
Summary:Redmine使用Mongrel服务器。

由于Redmine自带的Webrick Web服务器发布的问题，需要使用Mongrel组件来替换Webrick。Mongrel是一种快速的针对Ruby的Http服务器，专门为部署发布ROR应用而产生的。Mongrel相比Rails自带的纯Ruby服务器Webrick速度快很多并支持并发访问，有望成为Ruby的Tomcat.


1.	替换其自带的服务器webrick为mongrel，方法：
	
	`gem install mongrel`

	rails 3.1以上执行:

    `gem install mongrel –pre`
 
 
2.	修改redmine下gemfile，在gemfile中加入：

	` gem 'mongrel'`

     如果安装的mongrel pre， 则gemfile中加:

	`gem 'mongrel','~> 1.2.0.pre2'`
 
 
 
3.	删除gemfile.lock文件，重新执行: 

	`bundle install`
 
 
 
4.    执行
 
	`ruby script/rails server mongrel -e production`