# pages/add_account_page.py
class AddAccountPage:
    def __init__(self, driver):
        self.driver = driver

    def click_add_account(self):
        """点击'添加账号'按钮"""
        try:
            elem = self.driver.find_element("xpath", '//android.widget.TextView[@resource-id="android:id/title"]')
            elem.click()
            return True
        except:
            return False

    def get_page_title(self):
        """获取页面标题"""
        try:
            title = self.driver.find_element("xpath", "//*[@class='android.widget.TextView']")
            return title.text
        except Exception:
            return ""