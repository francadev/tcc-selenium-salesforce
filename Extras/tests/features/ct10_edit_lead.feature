@edit_lead
Feature: Edição de lead

  @successful
  Scenario: Editar um lead existente com sucesso
    Given que estou na página de lista de leads
    And eu acesso um lead existente
    When eu clico no botão de editar
    And eu preencho os campos do formulário de edição de lead com as novas informações
    And eu salvo as alterações no lead
    Then o lead deve ser atualizado com sucesso
    And todos os campos devem refletir as novas informações nos detalhes do lead
