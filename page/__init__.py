# 需要操作哪个页面就创建哪个页面的page文件
from selenium.webdriver.common.by import By
from page import page_register

# =============== 注册界面 =============== #
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
