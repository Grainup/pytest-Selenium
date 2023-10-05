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

    # 获取弹窗的文本内容
    def get_true_submit_context(self):
        return self.base_get_text(page.alert_true)

    def get_false_submit_context(self):
        return self.base_get_text(page.login_alert_false)

    # 登录成功后，点击安全退出
    def click_quit(self):
        self.base_click_element(page.alert_true)

    # 退出登录后，点击登录
    def click_log(self):
        self.base_click_element(page.click_log)

    # 组合方法
    def page_login(self, username, password, verify_code):
        self.__input_phone(username)
        self.__input_password(password)
        self.__input_verify(verify_code)
        self.__click_login()
