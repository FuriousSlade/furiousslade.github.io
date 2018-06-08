---
Title: JaCoCo代码覆盖率实践笔记
Date: 2018-06-05
Modified: 2018-06-05
Category: 笔记
Tags: JaCoCo
Status: draft
---

[TOC]

测试用例(产品需求)的覆盖率，往往很容易达到较高的水准。但这不代表测试覆盖到了代码运行时所有的可能性。为了更好的覆盖到方方面面，引入代码覆盖率来进一步的提升自动化测试的覆盖率。

通过查看各类技术博客，选择使用JaCoCo来获取代码覆盖率。原因的话是JaCoCo对Java8的支持，以及可以在程序运行时获取程序执行信息。

大多数博客介绍的都是本地代码执行来获取覆盖率，我面对的情况是被测服务分布式的部署在测试环境。在实践过程中走了点弯路，记下笔记。


### 主要工具
#### Jenkins
>Jenkins是一个用Java编写的开源的持续集成工具。

>Jenkins提供了软件开发的持续集成服务。可以执行基于Apache Ant和Apache Maven的项目，以及任意的Shell脚本和Windows批处理命令。

>可以通过各种手段触发构建。例如提交给版本控制系统时被触发，也可以通过类似Cron的机制调度，也可以在其他的构建已经完成时，还可以通过一个特定的URL进行请求。

Jenkins是优秀的持续集成工具，在配合丰富的插件。基本上不需要写什么代码，就能满足大多数持续集成的需求。

我主要利用 Jenkins 建立参数化的Job（构建代码覆盖率报告）。

自动或手工触发Job。

持续从内部 gitlab 更新项目源码（用于生成代码覆盖率报告）。

调度 Jaococo ant 工具来生成代码覆盖率，并发送邮件等相关工作。

#### Ant
>Apache Ant，是一个将软件编译、测试、部署等步骤联系在一起加以自动化的一个工具，大多用于Java环境中的软件开发。

使用Ant的原因：

ANT本身就是一个流程脚本引擎，用于自动化调用程序。

有ssh 和 scp 的需求，但因为一些条件限制无法使用密钥对验证的情况下。Ant 可调用库 jsch-0.1.54.jar 提供在shell脚本中使用 ssh 和 scp 且可配置密码的方式访问远端，无需手工输入密码。

jacocoant.jar 生成代码覆盖率报告


#### JaCoCo

Jacocoagent.jar 用于收集代码执行时的信息并在请求时导出数据。[Java Agent 官方文档](https://www.jacoco.org/jacoco/trunk/doc/agent.html){:target="_blank}

Jacocoant.jar 用于Jenkins Job执行中获取远端 agent数据的收集和报表的生成。[Jacoco Ant 官方文档](https://www.jacoco.org/jacoco/trunk/doc/index.html){:target="_blank}

### 代码覆盖率获取过程

#### 背景

1. Java Maven 项目。
2. 公司发布系统，分布式部署，需要对多台服务器收集数据。
3. 自用的Jenkins部署在一台Ubuntu系统的服务器上。
4. 无法使用密钥对验证ssh到测试服务器，只能通过密码验证。

#### 部署Jacocoagent

先从[JaCoCo](https://www.jacoco.org/jacoco/){:target="_blank}官网下载 jacoco-*.zip 包，下载解压后就有我们需要的 jacocoagent.jar 和 jacocoant.jar。

jacocoagent.jar 用于部署在被测服务端，收集覆盖率数据。

将 jacocoagent.jar scp到远端服务器目录下,例如:

    scp jacocoagent.jar username@remoterserver:/data/jacocoagent.jar

修改java项目启动时的 jvm 参数，增加：

    -javaagent:/data/jacocoagent.jar=output=tcpserver,address=*,port=8338,classdumpdir=/data/dump

重启服务

将 jacocoant.jar 放到本地Ubuntu服务器 `/data/jacocoant.jar`


#### Ubuntu上安装ant

    sudo apt-get install ant

    # 创建目录
    mkdir -p ~/.ant/lib


下载JSch至 ~/.ant/lib 目录内，因为原下载地址被墙，[网盘JSch](https://pan.baidu.com/s/1-51QQSorenNs3v8-0CSLRA){:target="_blank}

#### 调试
jacoco 统计覆盖并生成报表需要三部分数据

* 通过jacocoant 获取远端 jacocoagent 的覆盖率统计数据 jacoco.exec
* 远端服务执行中class文件
* 项目源码


**完整的 ant 构建所需 build.xml**

```xml
<?xml version="1.0" ?>
<project name="coverage" xmlns:jacoco="antlib:org.jacoco.ant" >
  <taskdef uri="antlib:org.jacoco.ant" resource="org/jacoco/ant/antlib.xml">
    <!-- 让ant找到jacocoant.jar -->
    <classpath path="/data/jacocoant.jar" />
  </taskdef>

  <!-- 用于重置jacocoagent的数据 -->
  <target name="reset">
    <jacoco:dump address="${remote_host}"
      reset="true" destfile="/dev/null"
      port="8335" append="true"/>
  </target>

  <!-- 用于获取远端覆盖率数据 -->
  <target name="dump">
    <delete file="jacoco.exec"/>
    <jacoco:dump address="${remote_host}"
      reset="false"
      destfile="jacoco.exec"
      port="8335"
      append="true"/>
    <delete dir="dump"/>
    <sshexec host="${remote_host}"
      username="${username}"
      password="${password}"
      trust="true"
      command="cd /data;tar -czf dump.tar.gz dump"/>
    <scp file="${username}:${password}@remote_host:/data/dump.tar.gz" todir="./"/>
    <untar src="dump.tar.gz" compression="gzip" dest="dump"/>
    <delete dir="dump.tar.gz"/>
  </target>

</project>
```