import os
import smtplib
import email
# 负责构造文本
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
# 负责构造图片
from email.mime.image import MIMEImage
# 负责将多个对象集合起来
from email.mime.multipart import MIMEMultipart
from email.header import Header


# 格式化邮件收件人
from email.utils import parseaddr, formataddr


def _format_addr(s):
    name,addr=parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))




def send_email(to_user,mail_subject,mail_content,mail_pics=None,mail_files=None):

    """
    :param to_user: 收件人列表，传入字典值，格式为{"张三":"zhangsan@163.com","李四":"lisi@163.com","王五","wangwu@163.com"}
    :param mail_subject:邮件主题
    :param mail_content:邮件内容
    :param mail_pics:邮件中包含的图片,格式为列表
    :param mail_files:邮件中包含的附件,格式为列表
    :return:
    """

    # --------------设置邮箱域名----------------------
    #
    # SMTP服务器,这里使用163邮箱
    mail_host = "smtp.163.com"
    mail_port=25
    # 发件人邮箱
    mail_sender = "happyboy_99n1e@163.com"
    # 邮箱授权码,注意这里不是邮箱密码,如何获取邮箱授权码,请看本文最后教程
    mail_license = "RRDBZOXUEVNIROAT"
    # 收件人邮箱，可以为多个收件人
    # mail_receivers = ["330445748@qq.com", "happyboy_99n1e@163.com"]
    mail_receivers=list(to_user.keys())
    # -----------------------------------
    # 构建MIMEMultipart对象代表邮件本身，可以往里面添加文本、图片、附件等
    mm = MIMEMultipart('related')

    # ---------------设置邮件头部内容--------------------
    #
    # 邮件主题
    subject_content = mail_subject
    # 设置发送者,注意严格遵守格式,里面邮箱为发件人邮箱
    mm["From"] = mail_sender
    # 设置接受者,注意严格遵守格式,里面邮箱为接受者邮箱
    # mm["To"] = "陈强<330445748@qq.com>,陈强<happyboy_99n1e@163.com>"
    # mm["To"] = _format_addr("陈强<330445748@qq.com>")+","+_format_addr("陈强<happyboy_99n1e@163.com>")
    mm["To"] = ",".join(list(map(lambda x:_format_addr("{}<{}>".format(x[1],x[0])),to_user.items())))
    # 设置邮件主题
    mm["Subject"] = Header(subject_content, 'utf-8')

    # ---------------添加正文文本-----------------------
    #
    # 邮件正文内容
    body_content = mail_content
    # 构造文本,参数1：正文内容，参数2：文本格式，参数3：编码方式
    message_text = MIMEText(body_content, "plain", "utf-8")
    # 向MIMEMultipart对象中添加文本对象
    mm.attach(message_text)

    # ----------------添加图片----------------------
    #
    # 二进制读取图片
    if mail_pics:
        for img in mail_pics:
            image_data = open(img, 'rb')
            # 设置读取获取的二进制数据
            message_image = MIMEImage(image_data.read())
            image_name=os.path.basename(img)
            message_image['Content-Disposition']='attachment;filename=%s'%image_name.encode('utf-8')
            # 关闭刚才打开的文件
            image_data.close()
            # 添加图片文件到邮件信息当中去
            mm.attach(message_image)

    # # ----------------添加附件----------------------
    # #
    if mail_files:
        for f in mail_files:
            f_name = os.path.basename(f)
            # 构造附件
            atta=MIMEBase('application', 'octet-stream')
            atta.set_payload(open(f, 'rb').read())
            # atta = MIMEText(open(f, 'rb').read(), 'base64', 'utf-8')
            # 设置附件信息
            atta.add_header("Content-Disposition","attachment",filename=('gbk','',f_name))
            email.encoders.encode_base64(atta)
            # atta["Content-Disposition"] = 'attachment; filename="sample.xlsx"'
            # 添加附件到邮件信息当中去
            mm.attach(atta)

    # -----------------发送邮件----------------------
    #
    # 创建SMTP对象
    stp = smtplib.SMTP()
    # 设置发件人邮箱的域名和端口，端口地址为25
    stp.connect(mail_host, mail_port)
    # set_debuglevel(1)可以打印出和SMTP服务器交互的所有信息
    stp.set_debuglevel(1)
    # 登录邮箱，传递参数1：邮箱地址，参数2：邮箱授权码
    stp.login(mail_sender, mail_license)
    # 发送邮件，传递参数1：发件人邮箱地址，参数2：收件人邮箱地址，参数3：把邮件内容格式改为str
    stp.sendmail(mail_sender, mail_receivers, mm.as_string())
    print("邮件发送成功")
    # 关闭SMTP对象
    stp.quit()



if __name__ == '__main__':
    print(_format_addr("陈强<happyboy_99n1e@163.com>"))
    # ail_receivers = ["330445748@qq.com", "happyboy_99n1e@163.com"]
    # send_email()
    #to_user={"happyboy_99n1e@163.com":"陈强","330445748@qq.com":"陈强"}
    #pics=[r"F:\temp\2008-11-06-015.bmp484878892.jpg",r"F:\temp\191703990雅晶.JPG",r"F:\temp\195301666图片_001.jpg"]
    #files=[r"E:\category.json",r"F:\学到老爱到老.mp3"]
    #send_email(to_user, "测试主题3", "添加图片", mail_pics=None, mail_files=files)

