# 需要操作哪个页面就创建哪个页面的page文件
from selenium.webdriver.common.by import By
from page import page_register
from page import page_login

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

# =============== 登录界面 =============== #
login_user = By.CSS_SELECTOR, '.text_uspa #username'
login_pass = By.CSS_SELECTOR, '.text_uspa #password'
login_code = By.CSS_SELECTOR, '.text_uspa #verify_code'
login_btn = By.CSS_SELECTOR, '.J-login-submit'
login_alert_false = By.CSS_SELECTOR, ".layui-layer-content"
click_log = By.CSS_SELECTOR, '.nologin :nth-child(1)'

# =============== 购物车界面 =============== #
home_search = By.CSS_SELECTOR, '.ecsc-search #q'  # 首页-搜索框
search_btn = By.CSS_SELECTOR, ".ecsc-search-button"  # 首页-搜索按钮
# 搜索商品页-加入购物车按钮
shoppingcart_btn1 = By.CSS_SELECTOR, ".shop-list-splb :nth-child(1) > .s_xsall .p-btn"
shoppingcart_btn2 = By.CSS_SELECTOR, ".standard #join_cart"

