import seldom
from seldom import data
from selenium.webdriver.common.by import By
from pageobject import Page, PageElement


class BaiduPage(Page):
    """Baidu serach test case"""

    search_input = PageElement(id_="kw")
    search_button = PageElement(xpath='//*[@id="su"]')

class BaiduTest(seldom.case.TestCase):
    """

    """

    @data([
        (1, 'seldom'),
        (2, 'selenium'),
        (3, 'unittest'),
    ])
    def test_baidu(self, testcase, search_key):
        """
         used parameterized test
        :param name: case name
        :param search_key: search keyword
        :return:
        """

        self.implicitly_wait = 1
        page = BaiduPage(self.driver)
        page.get('http://www.baidu.com')
        # test = page.search_input
        page.search_input = search_key
        page.search_button.click()


if __name__ == '__main__':
    seldom.main(debug=True)

