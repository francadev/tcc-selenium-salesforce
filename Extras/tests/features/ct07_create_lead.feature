@create_lead
Feature: Criar lead no formulário de cadastro

  @successful
  Scenario: Criar um lead com sucesso
    Given que estou na página de cadastro de lead
    When eu acesso o formulário de criação de lead
    And preencho todos os campos disponíveis
    And eu salvo o lead
    Then o lead deve ser criado com sucesso
    And todos os campos devem estar presentes nos detalhes da lead