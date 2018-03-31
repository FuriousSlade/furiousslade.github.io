Title: Docker学习笔记
Date: 2018-3-31 10:36
Modified: 2018-3-31 10:36
Category: 笔记
Tags: Docker

[TOC]

### Docker 是什么
>Docker 是使用 Google 公司推出的 Go 语言进行开发实现，基于 Linux 内核的 cgroup，namespace，以及 AUFS 类的 Union FS 等技术，对进程进行封装隔离，属于操作系统层面的虚拟化技术。由于隔离的进程独立于宿主和其它的隔离的进程，因此也称其为容器。最初实现是基于 LXC，从 0.7 版本以后开始去除 LXC，转而使用自行开发的 libcontainer，从 1.11 开始，则进一步演进为使用 runC 和 containerd。
Docker 在容器的基础上，进行了进一步的封装，从文件系统、网络互联到进程隔离等等，极大的简化了容器的创建和维护。使得 Docker 技术比虚拟机技术更为轻便、快捷。


### Docker 的优势

1. 更高效的利用系统资源
2. 更快的启动时间
3. 一致的运行环境
4. 易部署
5. 易扩展
6. 镜像构建过程透明

### Docker 的用途
#### 个人
1. 提供一次性，一致性的环境，用于测试或是构建
2. 代替虚拟机在一台机器上搭建多个微服务

### Docker 基本概念
#### 镜像
>Docker 镜像是一个特殊的文件系统，除了提供容器运行时所需的程序、库、资源、配置等文件外，还包含了一些为运行时准备的一些配置参数（如匿名卷、环境变量、用户等）。镜像不包含任何动态数据，其内容在构建之后也不会被改变。

#### 容器
>镜像（Image）和容器（Container）的关系，就像是面向对象程序设计中的 类 和 实例 一样，镜像是静态的定义，容器是镜像运行时的实体。容器可以被创建、启动、停止、删除、暂停等。

#### 仓库
>镜像构建完成后，可以很容易的在当前宿主机上运行，但是，如果需要在其它服务器上使用这个镜像，我们就需要一个集中的存储、分发镜像的服务，Docker Registry 就是这样的服务。

### macOS 安装 Docker

<a href="https://docs.docker.com/docker-for-mac/install/" target="_blank">https://docs.docker.com/docker-for-mac/install/</a>

### 常用命令

```shell
# 拉取镜像
docker pull
# 查看本地镜像
docker images
# 查看容器
docker ps
# 删除本地镜像
docker image rm
# 启动容器
docker run
# 清理所有处于终止状态的容器
docker container prune
```



### Demo

#### 拉取ubuntu镜像

寻找 docker images 上 <a href="https://hub.docker.com" target="&quot;_blank">docker hub</a>
```shell
docker pull ubuntu:14.04
```

```
14.04: Pulling from library/ubuntu
99ad4e3ced4d: Pull complete
ec5a723f4e2a: Pull complete
2a175e11567c: Pull complete
8d26426e95e0: Pull complete
46e451596b7c: Pull complete
Digest: sha256:ed49036f63459d6e5ed6c0f238f5e94c3a0c70d24727c793c48fded60f70aa96
Status: Downloaded newer image for ubuntu:14.04
```


#### 查看本地镜像


```shell
docker images
```

```
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
ubuntu              14.04               a35e70164dfb        12 days ago         222MB
```


#### 构建镜像


##### Docker commit

黑箱镜像，不常用，不推荐。


##### Docker file

```shell
touch Dockerfile
```

```
FROM ubuntu:14.04

RUN apt-get update \
    && apt-get install -y python \
    && apt-get install -y python-pip \
    && pip install flask

COPY ./hello.py /app/
CMD  ["python", "/app/hello.py"]
```

```python

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello docker!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
```

```shell

docker build -t demo:v1 ./
```

##### 启动容器

```
docker run -p 5000:5000 demo:v1
```

### 参考文献
<a href="https://yeasy.gitbooks.io/docker_practice/content/" target="_blank">Docker — 从入门到实践</a>
