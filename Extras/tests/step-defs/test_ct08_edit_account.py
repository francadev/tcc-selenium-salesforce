import pytest
from pytest_bdd import given, scenario, then, when

from pages.account_page import AccountPage
from pages.login_page import LoginPage


@pytest.fixture
def ap(driver):
    return AccountPage(driver, screenshot=True)


@scenario(
    "../features/ct08_edit_account.feature",
    "Editar uma conta existente com sucesso",
)
def test_ct08_edit_account():
    pass


@given("que estou na página de lista de contas")
def acessar_pagina_cadastro(driver, ap):
    login_page = LoginPage(driver)
    login_page.login_com_sucesso()
    ap.verificar_pagina_cadastro()


@given("eu acesso uma conta existente")
def acessar_conta_existente(ap):
    ap.acessar_conta_existente()


@when("eu clico no botão de editar")
def clicar_em_editar(ap):
    ap.clicar_em_editar()


@when(
    "eu preencho os campos do formulário de edição de conta com as novas "
    "informações"
)
def preencher_formulario_criacao_conta(ap, load_new_account_data):
    ap.preencher_formulario_conta(load_new_account_data, edit=True)


@when("eu salvo as alterações na conta")
def salvar_conta(ap):
    ap.salvar_conta()


@then("a conta deve ser atualizado com sucesso")
def verificar_edicao_conta(ap, load_new_account_data):
    ap.verificar_sucesso(
        n_campos=len(load_new_account_data),
        campos_adicionais=1,
        campos_agrupados=0,
    )


@then(
    "todos os campos devem refletir as novas informações nos detalhes da "
    "conta"
)
def verificar_campos_detalhes(ap, load_new_account_data):
    ap.verificar_campos_detalhes(load_new_account_data, edit=True)
