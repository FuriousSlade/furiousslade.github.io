Title:RabbitMQ基础概念
Date:2017-02-07
Category:笔记
Tags:RabbitMQ

[TOC]

## RabbitMQ简介
RabbitMQ是一个开源的AMQP实现，服务器端用Erlang语言编写，支持多种客户端，如：Python、Ruby、.NET、Java、PHP等，支持AJAX。用于在分布式系统中存储转发消息。
>AMQP，即Advanced Message Queuing Protocol，高级消息队列协议，是应用层协议的一个开放标准，为面向消息的中间件设计。


## 关键字
### Producer
Producer(生产者),投递消息的程序。

### Consumer
Consumer(消费者),接受消息的程序。

### Exchange
Exchange(交换机)，它指定消息按什么规则，路由到哪个队列

### Queue
Queue(队列)是RabbitMQ的内部对象，用于存储消息.

### Durable
Durable(持久化)，队列消息的持久化。

### Binding
Binding(绑定)，它的作用就是把exchange和queue按照路由规则绑定起来。

### Routing Key
Routing Key(路由关键字)，exchange根据这个关键字进行消息投递。

### Vhost
Vhost(虚拟主机),一个服务实例里可以开设多个vhost，用作不同用户的权限分离。

### Exchange Types
#### Fanout
Fanout类型的Exchange路由规则非常简单，它会把所有发送到该Exchange的消息路由到所有与它绑定的Queue中。

![](https://www.rabbitmq.com/img/tutorials/python-three.png)

#### Direct
Direct类型的Exchange路由规则也很简单，它会把消息路由到那些binding key与routing key完全匹配的Queue中。

![](https://www.rabbitmq.com/img/tutorials/direct-exchange.png)

#### Topic
Topic类型的Exchange路由规则也很简单，它会把消息路由到那些binding key与routing key进行模糊匹配，然后发送到相应的Queue中。

![](https://www.rabbitmq.com/img/tutorials/python-five.png)

