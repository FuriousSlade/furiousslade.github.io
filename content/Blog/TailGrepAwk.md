---
Title: 命令行统计log中关键字出现的次数
Date: 2018-06-08
Modified: 2018-06-08
Category: 笔记
Tags: Linux
---

通过 tail, grep, awk 命令组合使用用来统计log中关键字出现的次数

```shell
tail -f info.log | awk '/关键字/ {++i;printf "\r%d",i}'
```
