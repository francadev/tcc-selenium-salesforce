import pytest
from pytest_bdd import given, scenario, then, when

from pages.lead_page import LeadPage
from pages.login_page import LoginPage


@pytest.fixture
def lp(driver):
    return LeadPage(driver, screenshot=True)


@pytest.mark.lead
@scenario("../features/ct07_create_lead.feature", "Criar um lead com sucesso")
def test_ct07_create_lead():
    pass


@given("que estou na página de cadastro de lead")
def acessar_pagina_cadastro_lead(driver, lp):
    login_page = LoginPage(driver)  # Instancia a página de login
    login_page.login_com_sucesso()  # Chama o método de login
    lp.verificar_pagina_cadastro_lead()


@when("eu acesso o formulário de criação de lead")
def acessar_formulario_criacao_lead(lp):
    lp.abrir_formulario_criacao_lead()


@when("preencho todos os campos disponíveis")
def preencher_formulario_criacao_lead(lp, load_lead_data):
    lp.preencher_formulario_lead(load_lead_data)


@when("eu salvo o lead")
def salvar_nova_lead(lp):
    lp.salvar_lead()


@then("o lead deve ser criado com sucesso")
def verificar_criacao_lead(lp, load_lead_data):
    lp.verificar_sucesso(
        n_campos=len(load_lead_data), campos_adicionais=3, campos_agrupados=2
    )


@then("todos os campos devem estar presentes nos detalhes da lead")
def verificar_campos_detalhes(lp, load_lead_data):
    lp.verificar_campos_detalhes_lead(load_lead_data)
