import page
from time import sleep
from base.base import BaseMethod


class PageShopping(BaseMethod):

    # ���������������������
    def __input_search_value(self, value):
        self.base_send_keys(page.home_search, value)

    # ���������ť
    def __click_search_btn(self):
        self.base_click_element(page.search_btn)

    # ����������
    def __slide_scrollbar(self, x, y):
        self.base_slide_scrollbar(x, y)
        sleep(1)

    # ������빺�ﳵ
    def __click_add_shoppingcart(self):
        self.base_click_element(page.shoppingcart_btn1)
        sleep(2)
        self.base_click_element(page.shoppingcart_btn2)

    # ���ȥ���ﳵ����
    def __click_shopping_settlement(self):
        self.base_switch_frame(page.frame_id)
        sleep(1)
        self.base_click_element(page.shopping_settlement_btn)
        sleep(1)
        self.base_switch_default_frame()

    # ���ȥ����
    def __click_settlement(self):
        self.base_click_element(page.shoppingcart_settlement)

    # ����ύ����
    def __click_submit_order(self):
        self.base_click_element(page.indent_btn)

    # ��ȡ�ύ��������ı�����
    def page_get_submit_context(self):
        return self.base_get_text(page.submit_text)

    # �����Ʒ�����ﳵ���ύ�������
    def page_shopping_cart(self, value):
        self.__input_search_value(value)
        self.__click_search_btn()
        self.__click_add_shoppingcart()
        self.__click_shopping_settlement()
        self.__slide_scrollbar(0, 300)
        self.__click_settlement()
        self.__slide_scrollbar(0, 1000)
        self.__click_submit_order()
