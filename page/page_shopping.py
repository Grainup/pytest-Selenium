import page
from time import sleep
from base.base import BaseMethod


class PageShopping(BaseMethod):

    # 点击搜索框并输入搜索内容
    def __input_search_value(self, value):
        self.base_send_keys(page.home_search, value)

    # 点击搜索按钮
    def __click_search_btn(self):
        self.base_click_element(page.search_btn)

    # 滑动滚动条
    def __slide_scrollbar(self, x, y):
        self.base_slide_scrollbar(x, y)
        sleep(1)

    # 点击加入购物车
    def __click_add_shoppingcart(self):
        self.base_click_element(page.shoppingcart_btn1)
        sleep(2)
        self.base_click_element(page.shoppingcart_btn2)

    # 点击去购物车结算
    def __click_shopping_settlement(self):
        self.base_switch_frame(page.frame_id)
        sleep(1)
        self.base_click_element(page.shopping_settlement_btn)
        sleep(1)
        self.base_switch_default_frame()

    # 点击去结算
    def __click_settlement(self):
        self.base_click_element(page.shoppingcart_settlement)

    # 点击提交订单
    def __click_submit_order(self):
        self.base_click_element(page.indent_btn)

    # 获取提交订单后的文本内容
    def page_get_submit_context(self):
        return self.base_get_text(page.submit_text)

    # 添加商品到购物车并提交订单组合
    def page_shopping_cart(self, value):
        self.__input_search_value(value)
        self.__click_search_btn()
        self.__click_add_shoppingcart()
        self.__click_shopping_settlement()
        self.__slide_scrollbar(0, 300)
        self.__click_settlement()
        self.__slide_scrollbar(0, 1000)
        self.__click_submit_order()
