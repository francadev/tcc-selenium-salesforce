import pytest
from pytest_bdd import given, scenario, then, when

from pages.login_page import LoginPage
from pages.opportunity_page import OpportunityPage


@pytest.fixture
def op(driver):
    return OpportunityPage(driver, screenshot=True)


@pytest.mark.opportunity
@scenario(
    "../features/ct05_create_opportunity.feature",
    "Criar uma oportunidade com sucesso",
)
def test_ct05_create_opportunity():
    pass


@given("que estou na página de cadastro de oportunidade")
def acessar_pagina_cadastro_oportunidade(driver, op):
    login_page = LoginPage(driver)  # Instancia a página de login
    login_page.login_com_sucesso()  # Chama o método de login
    op.verificar_pagina_cadastro_oportunidade()


@when("eu acesso o formulário de criação de oportunidade")
def acessar_formulario_criacao_oportunidade(op):
    op.abrir_formulario_criacao_oportunidade()


@when("preencho todos os campos disponíveis")
def preencher_formulario_criacao_oportunidade(op, load_opportunity_data):
    op.preencher_formulario_oportunidade(load_opportunity_data)


@when("eu salvo a oportunidade")
def salvar_nova_oportunidade(op):
    op.salvar_oportunidade()


@then("a oportunidade deve ser criada com sucesso")
def verificar_criacao_oportunidade(op, load_opportunity_data):
    op.verificar_sucesso(
        n_campos=len(load_opportunity_data), campos_adicionais=3
    )


@then("todos os campos devem estar presentes nos detalhes da oportunidade")
def verificar_campos_detalhes(op, load_opportunity_data):
    op.verificar_campos_detalhes_oportunidade(load_opportunity_data)
