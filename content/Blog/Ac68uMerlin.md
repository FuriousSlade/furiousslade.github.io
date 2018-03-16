Title:AC68U折腾笔记
Date:2018-03-07
Modified:2018-03-16
Category:笔记
Tags:merlin

[TOC]

## 自动挂载U盘至/opt
```
cat << EOF > /tmp/script_usbmount.tmp
if [ \$1 = "/tmp/mnt/sda" ]
then
ln -sf \$1 /tmp/opt
/opt/etc/init.d/rc.unslung start
fi
EOF
nvram set script_usbmount="`cat /tmp/script_usbmount.tmp`"
cat << EOF > /tmp/script_usbumount.tmp
if [ \$1 = "/tmp/mnt/sda" ]
then
/opt/etc/init.d/rc.unslung stop
fi
EOF
```
```
nvram set script_usbumount="`cat /tmp/script_usbumount.tmp`"
nvram commit 
```
```
reboot
```
## 安装 Entware
较新版本的merlin系统已自带entware安装脚本

```
entware-setup.sh
```
```
# 更新仓库索引
opkg update
# 安装软件
opkg install {package}
```
