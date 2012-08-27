---
layout: post
title: "跟踪Python嵌套函数调用"
date: 2012-08-27 20:05
comments: true
categories: [Python]
---

今天在浏览Google Reader的时候发现一个好用的工具函数，用来跟踪嵌套调用函数方便debug。  
原文：[Easy tracing of nested function calls in Python](http://eli.thegreenplace.net/2012/08/22/easy-tracing-of-nested-function-calls-in-python/)  

其实是一个装饰器类：  
{% gist 3487991 %}
