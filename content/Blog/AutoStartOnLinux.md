Title:让Redmine随Linux系统自动启动。
Date:2015-05-15
Category:Blog
Tags:Redmine,Linux
Summary:让Redmine随Linux系统自动启动。

# 起因

最近因为机房经常停电，导致服务器频繁重启。每次都要手动去启动Redmine，我懒。所以把启动redmine的过程加入到了Linux系统启动过程中。

# 我使用的是CentOS 6.5

## 方法 1：


可能因发行版本不同rc.local的位置可能有不同 

		vim /etc/rc.local



在用户登录前执行，权限大。但无法使用“~”作为路劲，因为用户尚未登录，没有用户主目录。可以在/var/log/boot.log看到日志

## 方法 2：

		sudo vi /etc/profile

权限等同当前登录用户，有可能会有权限不足的问题。可以用'~'指定主目录。

## 实现Redmine随Linux系统自启动	

编辑 /etc/rc.local 文件

	vim /etc/rc.local

添加如下字段，因为启用Redmine必须先启动Mysql，所以把Mysql的启动也加了进去。

	service mysqld start
	cd /var/www/redmine/
	rails server Mongrel -d -e production -b 0.0.0.0 -p 3000


之后再断电就不用手工启动服务了。机房断电太坑了。
