Title:Adb常用命令。
Date:2015-05-12
Category:Blog
Tags:Android
Summary:记录下一些常用的ADB命令。

# 常用命令

	adb devices 	# 查看已连接PC的终端
	adb shell 		# 连接终端
	adb -s [devicesId] shell	# 多台设备根据设备号连接终端
	adb push xxx.apk /mnt/sdcard/xxx.apk		# 将本地文件传送至手机	
	adb pull /mnt/sdcard/xxx.apk xxx.apk		# 将手机中的文件传送至本地