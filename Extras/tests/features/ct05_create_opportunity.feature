@create_opportunity
Feature: Criar oportunidade no formulário de cadastro

  @successful
  Scenario: Criar uma oportunidade com sucesso
    Given que estou na página de cadastro de oportunidade
    When eu acesso o formulário de criação de oportunidade
    And preencho todos os campos disponíveis
    And eu salvo a oportunidade
    Then a oportunidade deve ser criada com sucesso
    And todos os campos devem estar presentes nos detalhes da oportunidade