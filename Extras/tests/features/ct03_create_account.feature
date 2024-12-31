@create_account
Feature: Criar conta no formulário de cadastro

  @successful
  Scenario: Criar uma conta com sucesso
    Given que estou na página de cadastro de conta
    When eu acesso o formulário de criação de conta
    And preencho todos os campos disponíveis
    And eu salvo a conta
    Then a conta deve ser criada com sucesso
    And todos os campos devem estar presentes nos detalhes da conta