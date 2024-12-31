import pytest
from pytest_bdd import given, scenario, then, when

from pages.login_page import LoginPage
from pages.opportunity_page import OpportunityPage


@pytest.fixture
def op(driver):
    return OpportunityPage(driver, screenshot=True)


@scenario(
    "../features/ct09_edit_opportunity.feature",
    "Editar uma oportunidade existente com sucesso",
)
def test_ct09_edit_account():
    pass


@given("que estou na página de lista de oportunidades")
def acessar_pagina_cadastro(driver, op):
    login_page = LoginPage(driver)
    login_page.login_com_sucesso()
    op.verificar_pagina_cadastro_oportunidade()


@given("eu acesso uma oportunidade existente")
def acessar_oportunidade_existente(op):
    op.acessar_oportunidade_existente()


@when("eu clico no botão de editar")
def clicar_em_editar(op):
    op.clicar_em_editar()


@when(
    "eu preencho os campos do formulário de edição de oportunidade com as "
    "novas informações"
)
def preencher_formulario_criacao_oportunidade(op, load_new_opportunity_data):
    op.preencher_formulario_oportunidade(load_new_opportunity_data, edit=True)


@when("eu salvo as alterações na oportunidade")
def salvar_oportunidade(op):
    op.salvar_oportunidade()


@then("a oportunidade deve ser atualizado com sucesso")
def verificar_edicao_oportunidade(op, load_new_opportunity_data):
    op.verificar_sucesso(
        n_campos=len(load_new_opportunity_data), campos_adicionais=3
    )


@then(
    "todos os campos devem refletir as novas informações nos detalhes da "
    "oportunidade"
)
def verificar_campos_detalhes(op, load_new_opportunity_data):
    op.verificar_campos_detalhes_oportunidade(
        load_new_opportunity_data, edit=True
    )
