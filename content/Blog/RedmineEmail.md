Title:Redmine异步发送邮件。
Date:2015-05-12
Category:Blog
Tags:Redmine
Summary:Redmine异步发送邮件。

当Redmine配置邮件后，会发现提交Bug等操作响应缓慢。是因为Redmine在确定邮件发送完成后才会返回提交成功的页面。设置成异步发送邮件，操作流程就流畅了。

    vim /var/www/redmine/config/configuration.yml
    delivery_method：async_smtp
or

    delivery_method: async_sendmail
