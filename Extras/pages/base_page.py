import os
from time import sleep

import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def ss(
        self,
        screenshot=False,
        filename="screenshot.png",
        ss_dir="D:/Code/Windows/Aqua/tcc-selenium-pytest/utils/screenshots"
        "/default",
    ):
        if screenshot:
            sleep(0.5)
            path_dir = (
                "D:/Code/Windows/Aqua/tcc-selenium-pytest/utils"
                "/screenshots/"
            ) + ss_dir
            if not os.path.exists(path_dir):
                os.makedirs(path_dir)

            filepath = os.path.join(path_dir, filename)
            self.driver.save_screenshot(filepath)

    def roll_page(self, n_vezes=1, keys="PAGE_DOWN"):
        ac = ActionChains(self.driver)
        for _ in range(n_vezes):
            if keys == "PAGE_DOWN":
                ac.send_keys(Keys.PAGE_DOWN).perform()
            elif keys == "PAGE_UP":
                ac.send_keys(Keys.PAGE_UP).perform()
            sleep(0.5)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def presence_wait(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def refresh(self):
        self.driver.refresh()

    def access_link(self, tab_link):
        self.driver.get(tab_link)

    def exists_on_screen(self, locator, text=None, timeout=10):
        if text:
            locator = (locator[0], locator[1].format(text))
        try:
            self.presence_wait(locator, timeout)
            assert self.find_element(
                locator
            ).is_displayed(), f"O texto {text} não foi encontrado na tela!"
            return True
        except TimeoutException:
            pytest.fail(
                f"O seletor {locator} não foi encontrado na tela!",
                pytrace=True,
            )

    def text_exists_on_screen(self, locator, text, timeout=10):
        try:
            self.presence_wait(locator, timeout)
            element = self.find_element(locator)
            assert text in element.text, (
                f"O texto '{text}' não foi encontrado "
                f"no elemento com o seletor {locator}!"
            )

        except TimeoutException:
            pytest.fail(
                f"O seletor {locator} não foi encontrado na tela!",
                pytrace=True,
            )

    def click(self, locator):
        self.presence_wait(locator, 20)
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)
        sleep(3)

    def write(self, locator, text, timeout=10):
        if self.find_element(locator).get_attribute(
            "disabled"
        ) or self.find_element(locator).get_attribute("value"):
            pass
        else:
            self.presence_wait(locator, timeout)
            self.find_element(locator).send_keys(text)

    def overwrite(self, locator, text, timeout=10):
        self.presence_wait(locator, timeout)
        self.find_element(locator).clear()
        self.find_element(locator).send_keys(text)

    def undo(self, undo):
        self.click_script(undo)

    def click_script(self, locator):
        self.presence_wait(locator, 20)
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)
        sleep(3)

    def get_attr(self, locator, label, attr):
        if label:
            locator = (locator[0], locator[1].format(label))
        elemento = self.find_element(locator)
        attr = elemento.get_attribute(attr)
        return attr

    def get_all_elements(self, locator):
        elements = self.find_elements(locator)
        labels_visiveis = [element for element in elements]
        return [label.text for label in labels_visiveis]

    def send_key(self):
        ac = ActionChains(self.driver)
        ac.send_keys(Keys.TAB * 3).perform()
        sleep(0.5)

    def all_dropdown_options(self, locator):
        elements = self.find_elements(locator)
        return [element.text for element in elements]
