import pytest
from config import con
from time import sleep
from page.page_login import PageLogin
from tools.read_json import get_json


class TestLogin:
    @pytest.fixture(scope='function', autouse=True)
    def open_web(self, drivers):
        self.driver = drivers

        self.login = PageLogin(self.driver)  # 传入driver
        self.login.get_url(con.WEB_URL_LOGIN)  # 传入登录页面
        sleep(0.5)

    @pytest.mark.parametrize('username, password, verify_code, expect, isTrue', get_json())
    def test_002(self, username, password, verify_code, expect, isTrue):
        self.login.page_login(username=username, password=password, verify_code=verify_code)
        sleep(2)
        if isTrue:
            alertText2 = self.login.get_true_submit_context()
            sleep(1)
            assert alertText2 == expect
            sleep(1)
            self.login.click_quit()
            sleep(1)
            self.driver.refresh()
            self.login.click_log()
            sleep(2)

        else:
            alertText = self.login.get_false_submit_context()
            self.driver.refresh()
            sleep(1)
            assert alertText == expect
