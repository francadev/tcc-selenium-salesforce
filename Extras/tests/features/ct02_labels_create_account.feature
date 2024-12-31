@labels_create_account
Feature: Verificar labels de criação de conta no formulário de cadastro

  @successful
  Scenario: Todas as labels de criação de conta estão visíveis no formulário
    Given que estou na página de cadastro de conta
    When eu acesso o formulário de criação de conta
    Then eu devo ver as labels visíveis
    And todas as picklists devem conter as opções corretas