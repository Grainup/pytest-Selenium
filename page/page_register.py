import page
from base.base import BaseMethod


class PageRegister(BaseMethod):

    # 输入手机号
    def __input_phone(self, value):
        self.base_send_keys(page.username, value)

    # 输入验证码
    def __input_verify(self, value):
        self.base_send_keys(page.verify_code, value)

    # 设置密码
    def __input_password(self, value):
        self.base_send_keys(page.password, value)

    # 确认密码
    def __input_password2(self, value):
        self.base_send_keys(page.password2, value)

    # 推荐人手机号
    def __input_refer(self, value):
        self.base_send_keys(page.referrer, value)

    # 点击我已阅读并同意
    def __click_agree(self):
        self.base_click_element(page.agree_btn)

    # 点击同意并注册
    def __click_register(self):
        self.base_click_element(page.register)

    # 获取弹窗的文本内容
    def get_true_submit_context(self):
        return self.base_get_text(page.alert_true)

    def get_false_submit_context(self):
        return self.base_get_text(page.alert_false)

    # 登录成功后，点击安全退出
    def click_quit(self):
        self.base_click_element(page.alert_true)

    # 退出登录后，点击注册
    def click_reg(self):
        self.base_click_element(page.click_reg)

    # 组合方法
    def page_register(self, username, verify_code, password, password2, referrer=None):
        self.__input_phone(username)
        self.__input_verify(verify_code)
        self.__input_password(password)
        self.__input_password2(password2)
        self.__input_refer(referrer)
        self.__click_register()
