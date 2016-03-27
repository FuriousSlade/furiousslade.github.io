Title:Python调用Java的代码片段。
Date:2015-05-15 15:09
Category:Blog
Tags:Python
Summary:Python使用jpype库创建jvm，从而使用java类。

	# coding:utf-8
	# 使用jpype第三方库创建jvm使用java类
	import jpype
	
	class MyDes:
	
	    @staticmethod  # 建立静态方法
	    def encode(data):
	        # 读取系统jvm环境变量
	        jvmPath = jpype.getDefaultJVMPath()
	        # 设置javaClass文件路径,可以是一个jar包
	        classpath = "D:\\git\\VeryTeleTest\\JavaServer"
	        jvmArg = "-Djava.class.path=" + classpath
	        # 尝试开启jvm
	        if not jpype.isJVMStarted():
	            jpype.startJVM(jvmPath, jvmArg)
				# 开启多线程支持
                jpype.attachThreadToJVM()
	        # 导入MyDes.class(DES加密模块)
	        javaClass = jpype.JClass("MyDes")
	        key1 = "xxxxxxxxxxxxxxxxx"  # 秘钥1
	        key2 = "xxxxxxxxxxxxxxxxx"  # 秘钥2
	        return javaClass.encode(data, key1, key2)  # 使用MyDes.encode方法进行加密
	
	    @staticmethod  # 建立静态方法
	    def decode(data):
	        # 读取系统jvm环境变量
	        jvmPath = jpype.getDefaultJVMPath()
	        # 设置javaClass文件路径,可以是一个jar包
	        classpath = "D:\\git\\VeryTeleTest\\JavaServer"
	        jvmArg = "-Djava.class.path=" + classpath
	        # 尝试开启jvm
	        if not jpype.isJVMStarted():
	            jpype.startJVM(jvmPath, jvmArg)
				# 开启多线程支持
                jpype.attachThreadToJVM()
	        # 导入MyDes.class(DES加密模块)
	        javaClass = jpype.JClass("MyDes")
	        key1 = "xxxxxxxxxxxxxxxxx"  # 秘钥1
	        key2 = "xxxxxxxxxxxxxxxxx"  # 秘钥2
	        return javaClass.decode(data, key1, key2)  # 使用MyDes.decode方法进行加密

