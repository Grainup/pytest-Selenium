from selenium.webdriver.common.by import By
from base.base import BaseMethod

username = By.CSS_SELECTOR, '#username'
verify_code = By.CSS_SELECTOR, '.J_imgcode'
password = By.CSS_SELECTOR, '#password'
password2 = By.CSS_SELECTOR, '#password2'
referrer = By.CSS_SELECTOR, '.fnlogin :nth-child(5) .J_cellphone'
agree_btn = By.CSS_SELECTOR, '.fnlogin .J_protocal'
register = By.CSS_SELECTOR, '.fnlogin .J_btn_agree'
alert_true = By.CSS_SELECTOR, '.islogin :nth-child(2)'
alert_false = By.CSS_SELECTOR, '.layui-layer-padding'
click_reg = By.CSS_SELECTOR, '.nologin :nth-child(2)'


class PageRegister(BaseMethod):

    # 输入手机号
    def __input_phone(self, value):
        self.base_send_keys(username, value)

    # 输入验证码
    def __input_verify(self, value):
        self.base_send_keys(verify_code, value)

    # 设置密码
    def __input_password(self, value):
        self.base_send_keys(password, value)

    # 确认密码
    def __input_password2(self, value):
        self.base_send_keys(password2, value)

    # 推荐人手机号
    def __input_refer(self, value):
        self.base_send_keys(referrer, value)

    # 点击我已阅读并同意
    def __click_agree(self):
        self.base_click_element(agree_btn)

    # 点击同意并注册
    def __click_register(self):
        self.base_click_element(register)

    # 获取弹窗的文本内容
    def get_true_submit_context(self):
        return self.base_get_text(alert_true)

    def get_false_submit_context(self):
        return self.base_get_text(alert_false)

    # 登录成功后，点击安全退出
    def click_quit(self):
        self.base_click_element(alert_true)

    # 退出登录后，点击注册
    def click_reg(self):
        self.base_click_element(click_reg)

    # 组合方法
    def page_register(self, username, verify_code, password, password2, referrer=None):
        self.__input_phone(username)
        self.__input_verify(verify_code)
        self.__input_password(password)
        self.__input_password2(password2)
        self.__input_refer(referrer)
        self.__click_register()
