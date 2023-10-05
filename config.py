# 用来存储相关配置文件
import os


class ConfigManager:
    # 目录路径
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    # WEB路径
    WEB_URL = 'http://127.0.0.1'

    # 手机号注册路径
    WEB_URL_REGISTER_TEL = f'{WEB_URL}/Home/user/reg.html'
    # 登录路径
    WEB_URL_LOGIN = f'{WEB_URL}/Home/user/login.html'

    # 报告文件
    REPORT_FILE = os.path.join(BASE_DIR, 'reports\\allure-report\\index.html')

    # 邮件信息
    EMAIL_INFO = {
        'username': 'xiahuakun2021@163.com',  # 切换成你自己的地址
        'password': 'ULOBNBGFKYHNASAD',
        'smtp_host': 'smtp.163.com',
        'smtp_port': 465
    }

    # 收件人
    ADDRESSEE = [
        '577246924@qq.com',
    ]

con = ConfigManager()
