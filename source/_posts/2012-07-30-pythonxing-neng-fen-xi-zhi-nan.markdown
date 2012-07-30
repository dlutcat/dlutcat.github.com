---
layout: post
title: "Python性能分析指南"
date: 2012-07-30 16:53
comments: true
categories: [Python]
---

## 主题

介绍几种用于Python程序性能分析的工具和方法。

## 思路

一般情况下，要分析一段代码的性能，可以从下面几个问题入手：  

1. **目前执行效率如何？**  
2. **效率瓶颈在哪里？**  
3. **占用了多少内存？**  
4. **内存消耗在哪里？**  

下面我们用几个工具来一一解答这些疑问。  

## Unix命令行工具: `time`

`time`是几乎所有\*nix系统自带的一个工具，我们可以用它来对程序进行初步的分析：   

```
$ time python yourprogram.py

real    0m1.028s
user    0m0.001s
sys     0m0.003s
```

输出的三条数据的具体含义可以参考这里：[What do 'real', 'user' and 'sys' mean in the output of time(1)?](http://stackoverflow.com/questions/556405/what-do-real-user-and-sys-mean-in-the-output-of-time1)。这里给出简单的说明：  

* `real` - 时钟时间。从程序开始到结束流逝的时间(actual elapsed time)，包括其他进程占用的时间，比如IO等待时间。
* `user` - 内核之外（用户空间）该进程占用时间(cpu time)。
* `sys` - 该进程的内核执行时间(cpu time)

如果发现`sys`和`user`的时间之和远小于`real`就说明我们的程序很有可能在IO等待上花费了大量时间。

## 自定义Timer类

{% gist 3205931 %}

可以把时间输出到一个性能日志文件，比如profile.log，方便以后分析我们程序的性能瓶颈。

## 行执行时间分析：[`line_profiler`](http://packages.python.org/line_profiler/)
