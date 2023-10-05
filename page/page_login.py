import page
from base.base import BaseMethod

# 登录界面
class PageLogin(BaseMethod):

    # 输入手机号
    def __input_phone(self, value):
        self.base_send_keys(page.login_user, value)

    # 设置密码
    def __input_password(self, value):
        self.base_send_keys(page.login_pass, value)

    # 输入验证码
    def __input_verify(self, value):
        self.base_send_keys(page.login_code, value)

    # 点击登录
    def __click_login(self):
        self.base_click_element(page.login_btn)

    # 组合方法
    def page_register(self, username, password, verify_code):
        self.__input_phone(username)
        self.__input_password(password)
        self.__input_verify(verify_code)
        self.__click_login()
