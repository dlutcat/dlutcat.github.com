---
layout: post
title: "重新设置Mysql的root密码"
date: 2013-05-02 20:07
comments: true
categories: Mysql, Linux
---

昨天帮朋友安装部署Mysql的时候，用`mysqladmin`给root用户设置了一个16位的随机密码，还没来得及记下来就被突然插进来的事儿打断了，等我回来的时候已经找不到这个密码了。像这样的事情在我身上已经发生过了2次，每次Google『Mysql忘记root密码』都没有找到可行的方案（可能是因为Mysql版本和网上这些提到的不一样导致重置失败），所以这次我要记下来一个自己确认可行的方案以供今后参考。  

我的环境版本
------------
* CentOS release 6.3 (Final)
* mysql Ver 14.14 Distrib 5.1.69, for redhat-linux-gnu (x86\_64) using readline 5.1

问题描述
--------
```bash
mysqladmin -u root -p randompassword
```

之后，忘记了`randompassword`，无法登陆`mysql`，需要找回root密码。

解决方案
--------
1. 修改`mysqld`的配置文件`/etc/my.cnf'，在每个section里追加一条设置：「skip-grant-tables 」，比如：
```
[mysqld] 
datadir=/var/lib/mysql 
socket=/var/lib/mysql/mysql.sock 
skip-grant-tables 
```
2. 重启`mysqld`。
3. 登陆`mysql`，修改root密码。
```
> mysql -u root
mysql> USE mysql;
mysql> UPDATE user SET Password=password ('new-password') WHERE User = 'root';
mysql> FLUSH PRIVILEGES;
```
4. 将`/etc/my.cnf`更改回来。
5. 重启`mysqld`。

<span style="color: red;">注意: </span>「skip-grant-tables」模式是忽略权限认证的意思，所以在上述`步骤1`开始前先保证外人无法连接你的`mysqld`。
