@labels_create_opportunity
Feature: Verificar labels de criação de oportunidade no formulário de cadastro

  @successful
  Scenario: Todas as labels de criação de oportunidade estão visíveis no formulário
    Given que estou na página de cadastro de oportunidade
    When eu acesso o formulário de criação de oportunidade
    Then eu devo ver as labels visíveis
    And todas as picklists devem conter as opções corretas