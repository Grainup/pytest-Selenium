import zmail
from config import con


def send_report():
    """发送报告"""
    with open(con.REPORT_FILE, encoding='utf-8') as f:
        content_html = f.read()
    try:
        mail = {
            'from': 'xiahuakun2021@163.com',
            'subject': '最新的测试报告邮件',
            'content_html': content_html,
            'attachments': [con.REPORT_FILE, ]
        }
        server = zmail.server(*con.EMAIL_INFO.values())
        server.send_mail(con.ADDRESSEE, mail)
        print("测试邮件发送成功！")
    except Exception as e:
        print("Error: 无法发送邮件，{}！", format(e))


if __name__ == "__main__":
    '''请先在config/conf.py文件设置QQ邮箱的账号和密码'''
    send_report()
