@edit_account
Feature: Edição de conta

  @successful
  Scenario: Editar uma conta existente com sucesso
    Given que estou na página de lista de contas
    And eu acesso uma conta existente
    When eu clico no botão de editar
    And eu preencho os campos do formulário de edição de conta com as novas informações
    And eu salvo as alterações na conta
    Then a conta deve ser atualizado com sucesso
    And todos os campos devem refletir as novas informações nos detalhes da conta
