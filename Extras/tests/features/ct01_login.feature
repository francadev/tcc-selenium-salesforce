@login
Feature: Login no Salesforce

  @successful
  Scenario: Logar com sucesso
    Given que eu estou na página de login da minha org no Salesforce
    When preencho o campo de email e senha com dados válidos
    And clico em fazer login
    Then o login deve ser realizado com sucesso