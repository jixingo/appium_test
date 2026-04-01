import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SettingsPage:
    def __init__(self, driver):
        self.driver = driver

    def click_add_account(self):
        """点击'账号'或'添加账号'"""
        try:
            # 滑动一下，露出更多选项（如果需要）
            size = self.driver.get_window_size()
            self.driver.swipe(
                start_x=size['width'] * 0.5,
                start_y=size['height'] * 0.9,
                end_x=size['width'] * 0.5,
                end_y=size['height'] * 0.4,
                duration=500
            )
            time.sleep(1)

            # 可能叫“账号”或“账户”
            elem = self.driver.find_element("xpath", '//android.widget.TextView[@resource-id="android:id/title" and @text="帐号"]')
            elem.click()
            
            return True
        except Exception:
            return False

    def is_account_page(self):
        """等待最多5秒，直到页面标题“帐号”出现"""
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(("xpath", "//android.widget.TextView[@text='帐号']"))
            )
            return True
        except:
            return False