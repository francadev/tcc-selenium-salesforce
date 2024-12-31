import os

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPageLocators:
    logo_alt = (By.ID, "logo")
    username_field = (By.ID, "username")
    password_field = (By.ID, "password")
    login_button = (By.ID, "Login")


class HomePageLocators:
    title = (By.XPATH, "//span[@title='Vendas']")


class LoginPage(BasePage):
    def __init__(self, driver, screenshot=False):
        super().__init__(driver)
        self.screenshot = screenshot

    def verifica_pagina_login(self):
        self.exists_on_screen(LoginPageLocators.logo_alt)

    def preencher_credenciais(self):
        email = os.getenv("EMAIL")
        password = os.getenv("PASSWORD")
        self.write(LoginPageLocators.username_field, email)
        self.write(LoginPageLocators.password_field, password)
        self.take_ss(self.screenshot, "01_valid_login.png")

    def clicar_login(self):
        self.click(LoginPageLocators.login_button)

    def verificar_acesso_aplicativo(self):
        home = os.getenv("HOME_PAGE_URL")
        self.access_link(home)
        self.exists_on_screen(HomePageLocators.title, "Vendas", timeout=20)
        self.take_ss(self.screenshot, "02_valid_login.png")

    def login_com_sucesso(self):
        self.verifica_pagina_login()
        self.preencher_credenciais()
        self.clicar_login()
        self.verificar_acesso_aplicativo()

    def take_ss(self, screenshot, filename):
        ss_dir = "test_ct01_valid_login"
        self.ss(screenshot, filename, ss_dir)
