---
layout: post
title: "Mac英文系统下iTunes导入中文歌曲乱码的解决方法"
date: 2013-03-08 20:09
comments: true
categories: [Mac, iTunes, MP3, Python] 
---

为了命令行的方便，我的Mac一直用的都是英文的系统。今天我往iTunes里导入中文歌曲的时候发现歌曲名，专辑名，作者名全是乱码，网上搜到的解决方案没有几个靠谱的。于是，还是自己用Python写了个脚本来搞定吧。

我的MP3文件的ID3信息编码都是GBK的，把它转成UTF8就OK了。读写ID3信息的库我用的是[Mutagen](https://code.google.com/p/mutagen/)，接口简单，示例文档小巧。我在转编码的时候遇到一个难点，就是怎么把下面unicode中的编码decode?

```python
s = u"COMM=='chi'=www.lizhizhuangbi.com\nTALB=\xb1\xbb\xbd\xfb\xbc\xc9\xb5\xc4\xd3\xce\xcf\xb7\nTDRC=2004\nTIT2=\xbf\xa8\xb7\xf2\xbf\xa8\nTPE1=\xc0\xee\xd6\xbe\nTPE2=\xc0\xee\xd6\xbe"
```

看上去原信息是GBK编码，可是怎么decode呢?Mutagen返回的直接就是unicode，没法decode 。最后只能尝试直接读取字符流，然后按照GBK来decode才成功。下面的`decode_gbk_from_unicode(s)`就是实现逻辑。


{% gist 5115640 %}
