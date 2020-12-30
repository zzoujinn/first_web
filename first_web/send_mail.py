import os
from django.core.mail import EmailMultiAlternatives

os.environ['DJANGO_SETTINGS_MODULE'] = 'first_web.settings'

if __name__ == '__main__':

    subject, from_email, to = '来自zouj的测试邮件', 'zzoujinn520@163.com', '501845230@qq.com'
    text_content = '欢迎访问www.liujiangblog.com，这里是刘江的博客和教程站点，专注于Python和Django技术的分享！'
    html_content = '<p>欢迎访问<a href="http://www.liujiangblog.com" target=blank>www.liujiangblog.com</a>，这里是刘江的博客和教程站点，本站专注于Python、Django和机器学习技术的分享！</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()