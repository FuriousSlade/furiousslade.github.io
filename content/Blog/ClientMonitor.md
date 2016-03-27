Title:移动客户端的性能监控。
Date:2015-05-18
Category:Blog
Tags:Android,iOS
Summary:简述移动客户端的性能监控。

起因
======
在测试一款通话类APP时，需要精确的统计客户端的流量消耗，电量消耗，CPU，内存等指标。磕磕碰碰的最终还是顺利的完成。在测试Android客户端的程中我一开始使用了Android SDK中的DDMS工具。

## DDMS
ddms位于"D:\adt-bundle-windows-x86\sdk\tools"相似的目录下。运行ddms.bat

![](http://ww1.sinaimg.cn/bmiddle/0067jSM2jw1es8e5cej4wj311y0kgn6v.jpg)

选择相应的应用进程例如：com.paobao.verytele 选择Network标签。可以看到该进程网络统计模块。

![](http://ww3.sinaimg.cn/bmiddle/0067jSM2jw1es8e8si1m1j30wq0i779j.jpg)

**RX**为下行数据，**TX**为上行数据。可选择统计数据的时间间隔（250ms），点击Start，就会开始采集数据。

![](http://ww3.sinaimg.cn/bmiddle/0067jSM2jw1es8ea2im2wj30wq0i7gr7.jpg)


因为DDMS使用起来并不是最符合我的需求，所以在这里只做简单的介绍，具体功能可以自己挖掘。

## Emmagee

最终Android端我选择了网易开源项目<a href="https://github.com/NetEase/Emmagee" target="_blank">Emmagee</a>。支持中文，简单直观的选择应用开启统计，可设置采集间隔，并可以设置将报告发送至指定邮箱。报告为Excel格式，统计了APP的CPU、内存、流量、电量以及整体性能状态。

<img src="http://ww1.sinaimg.cn/bmiddle/0067jSM2jw1esozs65rfwj30dc0m8ad8.jpg" width="180px" />
<img src="http://ww1.sinaimg.cn/bmiddle/0067jSM2jw1esozs5stmnj30dc0m8jsb.jpg" width="180px" />
<img src="http://ww3.sinaimg.cn/bmiddle/0067jSM2jw1esozs5vxrdj30dc0m83zr.jpg" width="180px" />
<img src="http://ww2.sinaimg.cn/bmiddle/0067jSM2jw1esozs5qvt2j30dc0m8gnm.jpg" width="180px" />


## GT
iOS端的性能监测工具找到了腾讯的项目<a href="http://gt.tencent.com/index.html" target="_blank">GT</a>。GT本身支持Android和iOS双平台，不过Android没有Emmagee更易用而已。iOS端是一个Framework包，必须嵌入APP工程。我让开发帮我集成进了APP中，同样可以统计APP的CPU、内存、流量、电量以及整体性能状态。