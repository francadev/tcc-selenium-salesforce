import pytest
from pytest_bdd import given, scenario, then, when

from pages.lead_page import LeadPage
from pages.login_page import LoginPage


@pytest.fixture
def lp(driver):
    return LeadPage(driver, screenshot=True)


@pytest.mark.lead
@scenario(
    "../features/ct06_labels_create_lead.feature",
    "Todas as labels de criação de lead estão " "visíveis no formulário",
)
def test_ct06_labels_create_lead():
    pass


@given("que estou na página de cadastro de lead")
def acessar_pagina_cadastro_lead(driver, lp):
    login_page = LoginPage(driver)  # Instancia a página de login
    login_page.login_com_sucesso()  # Chama o método de login
    lp.verificar_pagina_cadastro_lead()


@when("eu acesso o formulário de criação de lead")
def acessar_formulario_criacao_lead(lp):
    lp.abrir_formulario_criacao_lead()


@then("eu devo ver as labels visíveis")
def verificar_labels_layout(lp, load_lead_data):
    lp.verificar_labels_layout_lead(load_lead_data)


@then("todas as picklists devem conter as opções corretas")
def verificar_picklists(lp, load_lead_data):
    lp.verificar_picklists_lead(load_lead_data)
