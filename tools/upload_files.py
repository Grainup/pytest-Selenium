from time import sleep

import pyautogui

from seleniumbase import Driver
from selenium.webdriver.common.by import By


class UploadFile:

    def __init__(self):
        """
        上传文件
        """
        self.driver = Driver(browser="chrome", headless=False)
        self.driver.get('https://www.wenshushu.cn/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def upload(self, filenamePath):
        """
        input标签才能这样：send_keys上传文件
        :return:
        """
        upload = self.driver.find_element_by_css_selector(
            'div.chooice-btn button')
        sleep(3)
        # loadfile.send_keys(filenamePath)
        upload.send_keys('filenamePath')
        self.driver.find_element_by_id('onBtn')

    def autoguiUpload(self, filenamePath):
        """
        pyautogui上传文件
        :param filenamePath:
        :return:
        """
        self.driver.find_element(
            By.CSS_SELECTOR, 'div.chooice-btn button').click()
        # pyautogui.write(filenamePath)
        # sleep(3)
        # # pyautogui.keyDown('enter')
        # # pyautogui.keyUp('enter')
        # pyautogui.press('enter', presses=2)
        try:
            pyautogui.write(filenamePath)  # 输入文件绝对路径
            sleep(2)
            pyautogui.press('enter', 2)  # 按2次回车键（按2次是为了防止出错）
            print('上传成功')
        except Exception as e:

            print('上传文件操作异常',)
            raise e
        else:
            return filenamePath


if __name__ == '__main__':
    a = UploadFile()
    f_path = r'C:\Users\grain\Desktop\1.jpg'
    a.autoguiUpload(f_path)
