Title:在Android shell下无法使用cp命令的解决方案。
Date:2015-05-12
Category:Blog
Tags:Android
Summary:在Android shell下无法使用cp命令的解决方案。

在Android shell 下可能并没有安装cp命令，一般都不会安装。需要的可以自己安装busybox工具。在紧急的情况下可以使用cat命令来代替cp。
	
	adb shell
	cd /mnt/sdcard	
	cat xxx.apk >> yyy.apk		# 将/mnt/sdcard目录下的xxx.apk复制为yyy.apk

<a herf="http://www.busybox.net/downloads/binaries/" target="_black">Busybox</a>是一个集成了一百多个最常用linux命令和工具的软件。需要选择适合你手机cpu的版本来安装。查看手机CPU信息，根据Processor来选择安装版本。
	
	cat /proc/cpuinfo
	Processor       : ARMv7 Processor rev 2 (v7l)
	...

将busybox复制到 /system/xbin 目录下，并修改文件权限，使其可执行。

	cat busybox-armv7l >> /system/xbin/busybox
	chmod 775 busybox
	busybox --install

大功告成，现在就可以在Android shell下使用常用的linux命令了。

