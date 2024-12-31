@edit_opportunity
Feature: Edição de oportunidade

  @successful
  Scenario: Editar uma oportunidade existente com sucesso
    Given que estou na página de lista de oportunidades
    And eu acesso uma oportunidade existente
    When eu clico no botão de editar
    And eu preencho os campos do formulário de edição de oportunidade com as novas informações
    And eu salvo as alterações na oportunidade
    Then a oportunidade deve ser atualizado com sucesso
    And todos os campos devem refletir as novas informações nos detalhes da oportunidade
