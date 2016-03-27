Title:在Mac下使用抓包工具Charles抓取APP的Https请求。
Date:2016-01-05
Category:Blog
Tags:Charles
Summary:在Mac下使用抓包工具Charles抓取APP的Https请求（基于中间人攻击）。部分App的可请求可被解析，也能被有效的防御。



APP在实际生产环境的部分追求安全性的接口都是https的。抓包工具一般情况下是无法抓取显示https接口调用内容的。这对一些线上问题的追踪产生了一定的障碍。

我一直在mac下使用Charles这个软件来进行抓包分析。Charles本身就是支持抓取https请求的。在一番折腾后成功抓取了https请求。

在此记录下过程：

首先你需要安装Charles，可以从它的官网下载[Charles](http://www.charlesproxy.com/download/){:target="_blank}。

下载所需要使用到的[证书](http://www.charlesproxy.com/documentation/additional/legacy-ssl-proxying/){:target="_blank}.

>Version of Charles prior to v3.10 used a single SSL Root Certificate. You can still download the legacy certificate bundle **here** or the certificate itself **here** (for installing on mobile devices). Note that these certificates will not work on Charles v3.10.

在两个**here**处可以分别下载证书的压缩版本和可直接安装版本。

建议下载直接安装的证书到手机后，我使用的Android手机，进入“设置“-->“安全”-->“从SD卡安装证书”，找到下载好的证书并导入。

然后打开Charles进入Proxy-->SSL Proxying Settings中勾选Enable SSL Proxying,并添加需要抓取的的域名和端口（443）。

然后手机设置代理指向Mac，就可以开始抓取https请求了。


## 然而 \(╯‵ □′ )╯︵┻━┻  
我高兴的太早了。。。并不是所有的APP发出的HTTPS请求都能被正确的抓取到。Charles抓取HTTPS使用的是[代理中间人攻击](http://baike.baidu.com/view/1531871.htm "百度百科"){:target="_blank}方法，是可以有效的被防御的。
>中间人攻击（Man-in-the-MiddleAttack，简称“MITM攻击”）是一种“间接”的入侵攻击，这种攻击模式是通过各种技术手段将受入侵者控制的一台计算机虚拟放置在网络连接中的两台通信计算机之间，这台计算机就称为“中间人”。

只要客户端在SSL协议握手时对服务器返回的证书做校验，伪造的证书就会被识别出来就GG了。

能抓到https请求的，说明APP就是

有BUG\_(:з」∠)_ 

有BUG\_(:з」∠)_ 

有BUG\_(:з」∠)_ 


Charles抓取HTTPS请求的结果最终并不理想，但至少HTTPS请求是否会被中间人攻击也能作为一个测试点去关注。

