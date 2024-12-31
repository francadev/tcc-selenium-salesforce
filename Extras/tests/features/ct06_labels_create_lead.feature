@labels_create_lead
Feature: Verificar labels de criação de lead no formulário de cadastro

  @successful
  Scenario: Todas as labels de criação de lead estão visíveis no formulário
    Given que estou na página de cadastro de lead
    When eu acesso o formulário de criação de lead
    Then eu devo ver as labels visíveis
    And todas as picklists devem conter as opções corretas