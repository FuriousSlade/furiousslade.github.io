Title:解决Android复制文件报“Read-only file system”的问题。
Date:2015-05-12
Category:Blog 
Tags:Android
Summary:解决Android复制文件报“Read-only file system”的问题。

问题
=====
当往android的/system目录下拷贝文件时一般是会报“Read-only file system”。因为/system目录默认是只读的。

解决方法
======
首先是获取手机的**root权限**后
	
	adb shell
	su # 切换成ROOT用户
	mount -o rw,remount /system		#将/system目录设置为读写模式
	mount -o ro,remount /system 	#将/system目录设置为只读模式