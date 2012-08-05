---
layout: post
title: "Python线程和gevent简易服务器实现对比"
date: 2012-08-05 23:12
comments: true
categories: [Python,gevent,thread]
---

### 记前
最近项目上线，终于迎来了一个双休日，宅在家里眼瞅着肚子上的赘肉一圈一圈，实在不敢相信当年我是那个“怎么吃都不长肉”的瘦身少年。瘦子没法理解胖子的痛，瘦子终于有了同感。于是乎，待到晚上9点半开始了跑步，拉力器，仰卧起坐等一系列瘦身塑形锻炼。大汗淋漓地冲了一个澡，爽！

### 正文
用Python也有两年了，很少在生产中用到线程来设计程序，最近看到两篇不错的文章，准备自己记录一下。原文在这里：  

* [Introduction to Gevent](http://blog.pythonisito.com/2012/07/introduction-to-gevent.html)  
* [Gevent, Threads, and Benchmarks](http://blog.pythonisito.com/2012/07/gevent-threads-and-benchmarks.html)  

### 插曲
MD，写到这里接到老大地bug报告，修完了一个SB地Bug回来继续。  

### 单进程单线程服务器(无实用价值)
{% include_code webserver_single_thread.py %}  
批注：没有人会用单线程做服务器，除非你是像我现在一样用来练习。

### 单进程多线程服务器(无实用价值)
{% include_code webserver_multi_threads.py %}
批注：多线程之间的切换也是很耗资源的事情，所以就有了下面的线程池。

### 单进程线程池服务器(无实用价值)
{% include_code webserver_thread_pool.py %}
批注：受到Python的GIL的制约。

### 单进程gevent服务器(无实用价值)
{% include_code webserver_gevent.py %}
批注：研究中。

### gevent协程池服务器(无实用价值)
{% include_code webserver_gevent_pool.py %}
批注：研究中。
