# 存放公共页面操作方法
import time
from tools.getlogger import GetLogger
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = GetLogger.get_logger()


class BaseMethod:

    # 初始化，获取driver
    def __init__(self, driver):
        self.driver = driver
        logger.info("正在获取浏览器驱动对象：{}".format(driver))
    # 获取url
    def get_url(self, url):
        """打开网址并验证"""
        self.driver.maximize_window()  # 页面最大化窗口
        self.driver.set_page_load_timeout(30)  # 设置页面超时时间30秒
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(10)  # 隐式等待10秒，10秒内找元素
            logger.info("打开网页：%s" % url)
        except TimeoutException:
            raise TimeoutException("打开%s超时请检查网络或网址服务器" % url)

    # 查找元素
    def base_find_element(self, loc, timeout=30, poll=0.5):
        """
        :param loc: 定位的元素，如：（By.CSS_SELECTOR, '#username'）
        :param timeout: 查找元素的超时时间
        :param poll:    调用方法之间的睡眠时间
        :return:
        """
        logger.info("正在查找元素： {} ".format(loc))
        return WebDriverWait(self.driver, timeout=timeout,
                             poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 点击元素
    def base_click_element(self, loc):
        self.base_find_element(loc).click()
        logger.info("正在点击元素：{}".format(loc))

    # 输入元素内容
    def base_send_keys(self, loc, value):
        time.sleep(0.5)
        el = self.base_find_element(loc)
        logger.info("正在给元素： {} 输入内容：{}".format(loc, value))
        # 清空内容
        el.clear()
        logger.info("正在给元素：{} 清空".format(loc))
        # 输入内容
        el.send_keys(value)
        logger.info("正在给元素： {} 输入内容".format(loc))

    # 获取元素文本
    def base_get_text(self, loc):
        logger.info("正在获取元素：{} 的文本内容".format(loc))
        return self.base_find_element(loc).text

    # 截图
    def base_screenshot(self):
        self.driver.get_screenshot_as_file("../images/{}.png".format(time.strftime("%Y_%m_%d %H_%M_%S")))
        logger.info("正在截图")

    # 判断元素是否存在
    def base_if_exists_element(self, loc):
        logger.info("正在检查元素：{} 是否存在".format(loc))
        try:
            self.base_find_element(loc, timeout=2)
            return True  # 代表元素存在
        except:
            return False  # 代表元素不存在

    # 滑动滚动条     x=横坐标，y纵坐标
    def base_slide_scrollbar(self, x=0, y=0):
        js = "window.scrollTo({x},{y})".format(x=x, y=y)
        self.driver.execute_script(js)
        logger.info("正在滑动滚动条")

    # 切换iframe框架    参数：iframe id 或 iframe name
    def base_switch_frame(self, name):
        self.driver.switch_to.frame(name)
        logger.info("正在切换iframe框架")

    # 切换默认iframe框架
    def base_switch_default_frame(self):
        self.driver.switch_to.default_content()
        logger.info("正在切换为默认的iframe框架")

    # 获取弹窗内容
    # def base_get_alert(self):
    #     wait = WebDriverWait(self.driver, 10)
    #     wait.until(EC.alert_is_present())
    #     self.driver.switch_to.alert.accept()  # 注意之前的两步
        # self.driver.switch_to.alert()
