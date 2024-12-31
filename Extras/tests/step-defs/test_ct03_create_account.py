import pytest
from pytest_bdd import given, scenario, then, when

from pages.account_page import AccountPage
from pages.login_page import LoginPage


@pytest.fixture
def ap(driver):
    return AccountPage(driver, screenshot=True)


@pytest.mark.account
@scenario(
    "../features/ct03_create_account.feature", "Criar uma conta com sucesso"
)
def test_ct03_create_account():
    pass


@given("que estou na página de cadastro de conta")
def acessar_pagina_cadastro(driver, ap):
    login_page = LoginPage(driver)
    login_page.login_com_sucesso()
    ap.verificar_pagina_cadastro()


@when("eu acesso o formulário de criação de conta")
def acessar_formulario_criacao_conta(ap):
    ap.abrir_formulario_criacao_conta()


@when("preencho todos os campos disponíveis")
def preencher_campos_disponiveis(ap, load_account_data):
    ap.preencher_formulario_conta(load_account_data)


@when("eu salvo a conta")
def clicar_criar_conta(ap):
    ap.salvar_conta()


@then("a conta deve ser criada com sucesso")
def verificar_edicao_conta(ap, load_new_account_data):
    ap.verificar_sucesso(
        n_campos=len(load_new_account_data),
        campos_adicionais=1,
        campos_agrupados=0,
    )


@then("todos os campos devem estar presentes nos detalhes da conta")
def verificar_campos_detalhes(ap, load_account_data):
    ap.verificar_campos_detalhes(load_account_data)
