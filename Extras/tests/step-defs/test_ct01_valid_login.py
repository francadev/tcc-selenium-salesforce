import pytest
from pytest_bdd import given, scenario, then, when

from pages.login_page import LoginPage


@pytest.fixture
def lp(driver):
    return LoginPage(driver, screenshot=True)


@scenario("../features/ct01_login.feature", "Logar com sucesso")
def test_ct01_valid_login():
    pass


@given("que eu estou na página de login da minha org no Salesforce")
def acessar_pagina_login(lp):
    lp.verifica_pagina_login()


@when("preencho o campo de email e senha com dados válidos")
def preencher_credenciais(lp):
    lp.preencher_credenciais()


@when("clico em fazer login")
def clicar_login(lp):
    lp.clicar_login()


@then("o login deve ser realizado com sucesso")
def verificar_acesso_aplicativo(lp):
    lp.verificar_acesso_aplicativo()
