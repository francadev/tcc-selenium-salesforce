import pytest
from pytest_bdd import given, scenario, then, when

from pages.lead_page import LeadPage
from pages.login_page import LoginPage


@pytest.fixture
def lp(driver):
    return LeadPage(driver, screenshot=True)


@pytest.mark.edit_lead
@scenario(
    "../features/ct10_edit_lead.feature",
    "Editar um lead existente com sucesso",
)
def test_ct10_edit_lead():
    pass


@given("que estou na página de lista de leads")
def acessar_pagina_cadastro_lead(driver, lp):
    login_page = LoginPage(driver)  # Instancia a página de login
    login_page.login_com_sucesso()  # Chama o método de login
    lp.verificar_pagina_cadastro_lead()


@given("eu acesso um lead existente")
def acessar_lead_existente(lp):
    lp.acessar_lead_existente()


@when("eu clico no botão de editar")
def clicar_em_editar(lp):
    lp.clicar_em_editar()


@when(
    "eu preencho os campos do formulário de edição de lead com as novas "
    "informações"
)
def preencher_formulario_criacao_lead(lp, load_new_lead_data):
    lp.preencher_formulario_lead(load_new_lead_data, edit=True)


@when("eu salvo as alterações no lead")
def salvar_lead(lp):
    lp.salvar_lead()


@then("o lead deve ser atualizado com sucesso")
def verificar_criacao_lead(lp, load_new_lead_data):
    lp.verificar_sucesso(
        n_campos=len(load_new_lead_data),
        campos_adicionais=3,
        campos_agrupados=2,
    )


@then(
    "todos os campos devem refletir as novas informações nos detalhes do "
    "lead"
)
def verificar_novo_campos_detalhes(lp, load_new_lead_data):
    lp.verificar_campos_detalhes_lead(load_new_lead_data, edit=True)
