Title:Python3学习笔记
Date:2018-02-25
Modified:2018-02-27
Category:笔记
Tags:Python

[TOC]

## 简述
Life is short, you need Python.

Shut up and show me the code.

## 基础语法
### 编码
Python 3 源码文件默认以 UTF-8 编码。也可以自行指定。

	# -*- coding: <encoding_name> -*-
	
encoding\_name 为 pyhton 支持的有效[编码](https://docs.python.org/3.7/library/codecs.html#standard-encodings){:target="_blank}

例如：

	# -*- coding: gb2312 -*-
 
或

	# -*- coding: cp-1252 -*-
	

### 关键字

```python
import keyword

keyword.kwlist
```




    ['False',
     'None',
     'True',
     'and',
     'as',
     'assert',
     'break',
     'class',
     'continue',
     'def',
     'del',
     'elif',
     'else',
     'except',
     'finally',
     'for',
     'from',
     'global',
     'if',
     'import',
     'in',
     'is',
     'lambda',
     'nonlocal',
     'not',
     'or',
     'pass',
     'raise',
     'return',
     'try',
     'while',
     'with',
     'yield']


### 注释
```python
# 单行注释

'''
多行
注释
'''

"""
还是
多行
注释
"""
```

### 行与缩进

Python最具特色的就是使用缩进来表示代码块。

行缩进使用4个空格，或将tab调整为4个空格。

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Year(object):

    def __init__(self):
        self.do_better()

    def do_better(self, day=1):
        if day < 365:
            day += 1
            self.do_better(day)

if __name__ == '__main__':
    new_year = Year()
```

### 多行语句
```python
game_machines = 'PS4,' + \
				'Xbox,' + \
				'Nintendo Switch'
					
print(game_machines)
```
	PS4,Xbox,Nintendo Switch


```python
game_machines = ['PS4',
				 'Xbox',
				 'Nintendo Switch']
					
print(game_machines)
```

	['PS4', 'Xbox', 'Nintendo Switch']
	

## 数据类型
### 内置对象
1. 数字
2. 字符串
3. 列表
4. 字典
5. 元组
6. 集合
7. 文件
8. None
9. 布尔型
10. ...

### 数字
```python
# int 整数型
1 + 2
```

	3
	
```python
# float 浮点型
1.5 * 3
```
	4.5
	
```python
# float 浮点型
3.14159 * 3
```
	# 浮点计算会存在精度问题需要特别处理
	9.424769999999999
	
### 字符串
#### 字符串格式化
*version >= 3.6*

```python
msg = 'world!'
print(f'hello {msg}')
```

	hello world!

```python
d = {'a':1, 'b':3.1415927}
print(f'a = {d["a"]}')
print(f'b = {d["b"]}')
print(f'b = {d["b"]:.2f}')
print(f'a + b = {d["a"] + d["b"]:.2f}')
```
	a = 1
	b = 3.1415927
	b = 3.14
	a + b = 4.14
```python
f'mapping is { {a:b for (a, b) in ((1, 2), (3, 4))} }'
```
	'mapping is {1: 2, 3: 4}'


## 赋值、浅拷贝、深拷贝

坑过

```python
import copy

a = ["空银子", {"age": 15}]
# 赋值
b = a
# 浅拷贝
c = a.copy()
# 深拷贝
d = copy.deepcopy(a)

print(f'a is {a}, id is {id(a)}')
print('-' * 35)
print(f'b is {b}, id is {id(b)}')
print(f'c is {c}, id is {id(c)}')
print(f'd is {d}, id is {id(d)}\r\n')
print(f'a[1] is {a[1]}, id is {id(a[1])}')
print('-' * 35)
print(f'b[1] is {b[1]}, id is {id(b[1])}')
print(f'c[1] is {c[1]}, id is {id(c[1])}')
print(f'd[1] is {d[1]}, id is {id(d[1])}\r\n')
print('Changed a: a[0] = "雏鹤爱", a[1]["age"] = 9\r\n')
a[0] = "雏鹤爱"
a[1]["age"] = 9
print(f'a is {a}, id is {id(a)}')
print('-' * 35)
print(f'b is {b}, id is {id(b)}')
print(f'c is {c}, id is {id(c)}')
print(f'd is {d}, id is {id(d)}\r\n')
print(f'a[1] is {a[1]}, id is {id(a[1])}')
print('-' * 35)
print(f'b[1] is {b[1]}, id is {id(b[1])}')
print(f'c[1] is {c[1]}, id is {id(c[1])}')
print(f'd[1] is {d[1]}, id is {id(d[1])}')

```

```
a is ['空银子', {'age': 15}], id is 4415182472
-----------------------------------
b is ['空银子', {'age': 15}], id is 4415182472
c is ['空银子', {'age': 15}], id is 4415182408
d is ['空银子', {'age': 15}], id is 4415184200

a[1] is {'age': 15}, id is 4413290608
-----------------------------------
b[1] is {'age': 15}, id is 4413290608
c[1] is {'age': 15}, id is 4413290608
d[1] is {'age': 15}, id is 4414213144

Changed a: a[0] = "雏鹤爱", a[1]["age"] = 9

a is ['雏鹤爱', {'age': 9}], id is 4415182472
-----------------------------------
b is ['雏鹤爱', {'age': 9}], id is 4415182472
c is ['空银子', {'age': 9}], id is 4415182408
d is ['空银子', {'age': 15}], id is 4415184200

a[1] is {'age': 9}, id is 4413290608
-----------------------------------
b[1] is {'age': 9}, id is 4413290608
c[1] is {'age': 9}, id is 4413290608
d[1] is {'age': 15}, id is 4414213144
```



## To be continued ...