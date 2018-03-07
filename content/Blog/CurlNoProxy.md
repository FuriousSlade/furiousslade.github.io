Title:Curl 不使用代理
Date:2018-03-07
Modified:2018-03-07
Category:笔记
Tags:Curl

被系统全局http代理折腾了一把

```shell
curl -X POST \
  http://ip:port/rpc \
  -d '{
    "hello": "world"
}' --noproxy "*"
```
