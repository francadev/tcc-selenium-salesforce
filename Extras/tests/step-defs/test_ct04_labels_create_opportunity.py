import pytest
from pytest_bdd import given, scenario, then, when

from pages.login_page import LoginPage
from pages.opportunity_page import OpportunityPage


@pytest.fixture
def op(driver):
    return OpportunityPage(driver, screenshot=True)


@pytest.mark.opportunity
@scenario(
    "../features/ct04_labels_create_opportunity.feature",
    "Todas as labels de criação de oportunidade estão "
    "visíveis no formulário",
)
def test_ct04_labels_create_opportunity():
    pass


@given("que estou na página de cadastro de oportunidade")
def acessar_pagina_cadastro_oportunidade(driver, op):
    login_page = LoginPage(driver)  # Instancia a página de login
    login_page.login_com_sucesso()  # Chama o método de login
    op.verificar_pagina_cadastro_oportunidade()


@when("eu acesso o formulário de criação de oportunidade")
def acessar_formulario_criacao_oportunidade(op):
    op.abrir_formulario_criacao_oportunidade()


@then("eu devo ver as labels visíveis")
def verificar_labels_layout(op, load_opportunity_data):
    op.verificar_labels_layout_oportunidade(load_opportunity_data)


@then("todas as picklists devem conter as opções corretas")
def verificar_picklists(op, load_opportunity_data):
    op.verificar_picklists_oportunidade(load_opportunity_data)
