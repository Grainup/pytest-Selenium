# 测试用例
import pytest
from config import con
from time import sleep
from page.page_register import PageRegister
from tools.read_json import get_json


class TestRegister:
    @pytest.fixture(scope='function', autouse=True)
    def open_web(self, drivers):
        self.driver = drivers
        """打开注册页面"""
        self.register = PageRegister(self.driver)  # 传入driver
        self.register.get_url(con.WEB_URL_REGISTER_TEL)  # 传入注册页面
        sleep(0.5)

    # @pytest.mark.parametrize('username, verify_code, password, password2, referrer, expect', [
    #     ('', '8888', '123123', '123123', '', '请用手机号或邮箱注册'),
    #     ('17805591583', '8888', '123123', '123321', '', '两次输入密码不一致'),
    # ])
    @pytest.mark.parametrize('username, verify_code, password, password2, referrer, expect, isTrue', get_json())
    def test_001(self, username, verify_code, password, password2, referrer, expect, isTrue):
        self.register.page_register(username=username, verify_code=verify_code, password=password,
                                    password2=password2, referrer=referrer)
        sleep(1)
        # # 验证注册  isTrue---true表示正向用例，false--表示反向用例
        if isTrue:
            alertText2 = self.register.get_true_submit_context()
            sleep(1)
            self.register.click_quit()
            self.register.click_reg()
            assert alertText2 == expect
        else:
            alertText = self.register.get_false_submit_context()
            self.driver.refresh()
            assert alertText == expect
