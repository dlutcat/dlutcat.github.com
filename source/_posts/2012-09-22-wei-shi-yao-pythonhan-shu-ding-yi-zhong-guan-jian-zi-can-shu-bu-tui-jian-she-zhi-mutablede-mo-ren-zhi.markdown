---
layout: post
title: "为什么Python函数定义中关键字参数不推荐设置mutable的默认值？"
date: 2012-09-22 15:55
comments: true
categories: Python
---

很多关于Python的[Best Practice](http://www.google.com.hk/search?q=python+best+practices&aq=0&oq=python+best+prac&sugexp=chrome,mod=10&sourceid=chrome&ie=UTF-8)中都会提到，在函数定义的时候，关键词参数的默认值不要设置成mutable的类型，比如list, dict。那么具体原因是什么呢？之前一直没有去思考，直到膝盖中了一箭。
先看下面的例子：

``` python
    def example(items=[]):
        items.append("test")
        return items
```

调用`example()`会返回什么呢？第二次，第三次调用又会返回什么呢？

``` bash
    >>> example()
    ['test']

    >>> example()
    ['test', 'test']

    >>> example()
    ['test', 'test', 'test']
```

是不是觉得结果有些意外？是的，这就是Python函数的定义机制：  
> 在生命周期中，函数的声明语句只会执行一次，就是在源码被解释器解释的时候，而不是在被调用的时候。
