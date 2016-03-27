Title:Adb error: unknown host service 的解决方法
Date:2015-06-01
Category:Blog
Tags:Android
Summary:解决在使用adb shell 命令时提示 Adb error: unknown host service 的问题。

#在命令行输入adb shell后输出如下错误：

    adb server is out of date.  killing... 
    ADB server didn't ACK 
    * failed to start daemon * 
    error: unknown host service  


使用`netstat -ano`查看哪个程序占用了**5037**端口
	
	活动连接

  	协议      本地地址               外部地址                 状态           PID
	TCP    0.0.0.0:49154          0.0.0.0:0              LISTENING       1080
  	TCP    0.0.0.0:49163          0.0.0.0:0              LISTENING       588
  	TCP    0.0.0.0:49167          0.0.0.0:0              LISTENING       604
  	TCP    127.0.0.1:5037         0.0.0.0:0              LISTENING       972
  	TCP    127.0.0.1:5037         127.0.0.1:49382        TIME_WAIT       0
  	TCP    127.0.0.1:5354         0.0.0.0:0              LISTENING       1868
  	TCP    127.0.0.1:5354         127.0.0.1:49155        ESTABLISHED     1868
  	TCP    127.0.0.1:5354         127.0.0.1:49156        ESTABLISHED     1868

记录下**PID**：`TCP    127.0.0.1:5037         0.0.0.0:0              LISTENING       972`

使用`taskkill /F /PID 972`杀死占用进程 **/F** 为强制进行
	
	C:\Users\Slade>taskkill /F /PID 972
	成功: 已终止 PID 为 972 的进程。


