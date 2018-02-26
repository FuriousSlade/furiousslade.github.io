Title:Python3学习笔记
Date:2018-02-25
Modified:2018-02-26
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


## To be continued ...