---
layout: post
title: "Mac下的网络IP自动切换"
date: 2012-09-18 20:45
comments: true
categories: [Mac, Network]
---

用惯了自己的电脑，我喜欢在公司也自带电脑，由于家里和公司的网络环境不同，而且因为某些原因都需要手动设置IP, Subnet, Router和DNS，这样每天晚上回家和早上上班手动设置会很麻烦，就研究了一下Mac下自动设置。在Mac下面有一个命令`networksetup`，用man查看，它有很多参数，我们这里要用到以下这些参数：

#### 查看本机地网络设备

```bash
$ networksetup -listallnetworkservices

An asterisk (*) denotes that a network service is disabled.
Bluetooth DUN
Ethernet
PPPoE Service
FireWire
Wi-Fi
```

#### 查看指定网络设备地状态
例如，查看Wi-Fi的详细状态：

```bash
$ networksetup -getinfo Wi-Fi

Manual Configuration
IP address: 192.168.0.129
Subnet mask: 255.255.255.0
Router: 192.168.0.1
IPv6: Automatic
IPv6 IP address: none
IPv6 Router: none
Wi-Fi ID: e6:ce:8e:10:a6:af
```


#### 设置手动IP, Subnet, Router
例如，把IP设置成`192.168.2.129`, Router设置为`192.168.2.1`:

```bash

$ networksetup -setmanual Wi-Fi 192.168.2.129 255.255.255.0 192.168.2.1

$ networksetup -getinfo Wi-Fi

Manual Configuration
IP address: 192.168.2.129
Subnet mask: 255.255.255.0
Router: 192.168.2.1
IPv6: Automatic
IPv6 IP address: none
IPv6 Router: none
Wi-Fi ID: e6:ce:8e:10:a6:af
```

#### 查看和设置DNS
例如，把DNS从`192.169.0.1`设置为`192.168.2.1`:
```bash
$ networksetup -getdnsservers Wi-Fi

192.168.0.1

$ networksetup -setdnsservers wi-fi 192.168.2.1

$ networksetup -getdnsservers Wi-Fi

192.168.2.1
```

#### 实现家里和办公室网络自动切换
有了以上的命令我们可以在CLI环境下切换了，甚至可以写成切换脚本，比GUI中设置要方便多了。如果想要更懒一点，需要自动切换网络怎么做呢？没问题，我们也可以搞定。思路就是检查当前的wifi热点，如果是家里的就自动设置成家里的配置，反之，设置成办公室地。  
自动检查wifi热点，我们放在开机启动项来做。 从网上找来这么一个方法，可以在CLI环境下调用`airport`来扫描wifi热点:
```bash
$ sudo ln -s /System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport /usr/bin/airport

$ airport -s

SSID BSSID             RSSI CHANNEL HT CC SECURITY (auth/unicast/group)
CMCC 30:49:3b:07:15:66 -76  1       N  US NONE
Tenda c8:3a:35:f4:ad:28 -48  6,+1    Y  CN WPA2(PSK/AES/AES)
```

这样，我们就可以写一个小脚本，自动检查网络环境并且自动切换了，我的脚本如下：  

{% gist 3743043 %}

#### 把脚本加入自动启动
Mac的自动启动脚本plist需要存放在：`/Library/LaunchDaemons`

``` xml pat.netswitch.plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>Label</key>
	<string>pat.netswitch.plist</string>
	<key>ProgramArguments</key>
	<array>
		<string>/Users/patto/bin/netswitch</string>
	</array>
	<key>KeepAlive</key>
	<false/>
	<key>RunAtLoad</key>
	<true/>
</dict>
</plist>
```

这样就大功告成了！
