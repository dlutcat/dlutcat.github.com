---
layout: post
title: "多服务器管理之Fabric"
date: 2012-11-25 15:38
comments: true
categories: [Fabric, Python]
---

### 背景
最近公司服务器从单机扩展到三机，新环境的搭建和部署也采用了新的自动化方式：[Fabric](http://docs.fabfile.org/en/1.5/)。   

### 什么是Fabric
用[Fabric](http://docs.fabfile.org/en/1.5/)其实就是一套用Python封装了基于SSH的常见操作的库。因此，它的优势显而易见：

1. 你可以用Python代理Shell来做运维工作。
1. 方便集中式管理多台服务器。

### 怎样使用Fabric
有Python基础的程序员对Fabric一点都不会陌生，因为它就是Python。  
我们先从一个简单的例子开始：  

```python fabfile.py
from fabric.api import local

def host_type():
    local('uname -s')
```
```bash
    fab host_type
```

上面例子的便是实用fabric在local环境下执行命令`uname`，就是这么简单。下面在看一个在remote环境下的操作：  

```python fabfile.py
from fabric.api import run

env.user = 'pat'
env.key_filename = '~/.ssh/id_rsa'
env.password = 'patpassword'

def host_type():
    run('uname -s')
```
```bash
    fab host_type
```

注意，这次我们用`run`代替了`local`，它的意思是在remote机器上执行某命令。当然，能够从local连接到remote，并且有执行权限才可以执行，这些都是可以在`env`中指定的。`env`结论是整个fabric脚本执行中的一个全局变量，`env.user`，`env.key_filename`和`env.password`都是`env`的保留关键字，分别指明登陆remote的user，密钥以及密码。密钥和密码可以是二选一。密码在使用`sudo`命令的时候是必须的。  
如果我们想要管理多台remote服务器的时候该怎么做呢？好，我现在开始介绍。  
首先，我需要引入Fabric中的一个概念：**role**。你可以把**role**理解成remote的标识，它可以是一个remote，也可以是一组remotes，通常我们在fabfile中是用`env.roledefs`来定义的，然后通过指定`env.roles`来决定使用那一个/组roles。  

```python fabfile.py
env.roledefs ={
    'local': ['localhost'],
    'prd_1': ['192.168.0.100'],
    'prd_2': ['192.168.0.101'],
    'prd_3': ['192.168.0.102'],
    'product': ['192.168.0.100', 
            '192.168.0.101', 
            '192.168.0.102',
            ]
}

def prd_1():
    env.user = 'pat'
    env.key_filename = 'xxxx'
    env.password = 'patpassword'
    env.roles = ['prd1']

def prd_2():
    env.user = 'pat'
    env.key_filename = 'xxxx'
    env.password = 'patpassword'
    env.roles = ['prd2']

def prd_3():
    env.user = 'pat'
    env.key_filename = 'xxxxx'
    env.password = 'patpassword'
    env.roles = ['prd3']

def product():
    env.user = 'pat'
    env.key_filename = 'xxxx'
    env.password = 'patpassword'
    env.roles = ['product']

def host_type():
    run('uname -s')

```
```bash 调用
# 只在prd_1上执行
fab prd_1 host_type

# 只在prd_2上执行
fab prd_2 host_type

# 同时在三台remote上执行
fab product host_type
```

看到这里，你是否发现其实`fab`就是在依次执行后面的方法。嗯，其实道理就是这么简单。  

现在，你就可以用Fabric进行自己的集群运维管理了。提示一下，下面两个API不多，先好好了解下Fabric都可以做些什么吧：

1. [Core API](http://docs.fabfile.org/en/1.5/#core-api)
1. [Contrib API](http://docs.fabfile.org/en/1.5/#contrib-api)
1. 提供一个完整的Fabfile做参考：[fabfile.py](https://github.com/samuelclay/NewsBlur/blob/master/fabfile.py)
