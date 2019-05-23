# RaspiKeeper

背景：
1. 使用ADSL或者其他拨号连接互联网的时候获取的是动态的IP地址。在外网需要连接raspi的时候需要获取外网地址。
2. 不使用DDNS。 可以使用花生壳在路由器上进行登录得外网地址的解析。但是，从6月份开始，需要实名制。不爽，遂废弃。
3. 国外DDNS。不稳定+路由不支持，暂时放弃。  
添加了对DDNS NO-ip的更新支持。

解决办法：
python获取外网IP后发送到126邮箱。

执行方法：
1. 添加126邮箱的用户名和密码到py文件中，手动执行.<br/>
\#you need to update the following value.  
mail_user=""  
mail_passwd=""  
2. 添加到corn job中
如：root用户下
crontab -u root -e
如：每小时的25分执行  
25 * * * * {path}/raspikeeper.py