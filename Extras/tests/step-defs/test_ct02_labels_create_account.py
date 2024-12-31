import pytest
from pytest_bdd import given, scenario, then, when

from pages.account_page import AccountPage
from pages.login_page import LoginPage


@pytest.fixture
def ap(driver):
    return AccountPage(driver, screenshot=True)


@pytest.mark.account
@scenario(
    "../features/ct02_labels_create_account.feature",
    "Todas as labels de criação de conta estão visíveis no formulário",
)
def test_ct02_labels_create_account():
    pass


@given("que estou na página de cadastro de conta")
def acessar_pagina_cadastro(driver, ap):
    login_page = LoginPage(driver)  # Instancia a página de login
    login_page.login_com_sucesso()  # Chama o metodo de login
    ap.verificar_pagina_cadastro()


# Passo para acessar o formulário de criação de conta
@when("eu acesso o formulário de criação de conta")
def acessar_formulario_criacao_conta(ap):
    ap.abrir_formulario_criacao_conta()


@then("eu devo ver as labels visíveis")
def verificar_labels_layout(ap, load_account_data):
    ap.verificar_labels_layout(load_account_data)


@then("todas as picklists devem conter as opções corretas")
def verificar_picklists(ap, load_account_data):
    ap.verificar_picklists(load_account_data)
