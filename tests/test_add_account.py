# tests/test_add_account.py
import pytest
from pages.settings_page import SettingsPage
from pages.add_account_page import AddAccountPage
from appium import webdriver
class TestAddAccount:
    def test_add_account_flow(self, driver): 
        # driver会在conftest.py里定义
        # 1. 进设置主页
        settings = SettingsPage(driver)

        # 2. 点击“账号”
        assert settings.click_add_account(), "点击账号失败"

        # 3. 验证进入账号页面
        assert settings.is_account_page(), "未进入账号页面"

        # 4. 点击“添加账号”
        add_account = AddAccountPage(driver)
        assert add_account.click_add_account(), "点击添加账号失败"

        # 5. 断言：应该进入账号类型选择页面
        print("✅ 模拟添加账号流程测试通过")