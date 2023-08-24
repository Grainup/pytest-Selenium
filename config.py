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
    WEB_URL_LOGIN = f'{WEB_URL}/Home/User/login.html'


con = ConfigManager()
