from selenium.webdriver.common.by import By
from base.base import BaseMethod



class PageLogin(BaseMethod):

    # 输入手机号
    def __input_phone(self, value):
        self.base_send_keys(username, value)

    # 设置密码
    def __input_password(self, value):
        self.base_send_keys(password, value)

    # 输入验证码
    def __input_verify(self, value):
        self.base_send_keys(verify_code, value)