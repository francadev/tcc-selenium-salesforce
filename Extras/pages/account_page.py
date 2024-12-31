import os

from dotenv import load_dotenv
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils import functions as uf

load_dotenv()


class AccountLocators:
    account_page = (By.XPATH, '//span[@class="slds-var-p-right_x-small"]')
    form_input_labels = (By.XPATH, "//flexipage-field//label")
    criar_button = (By.XPATH, '//div[@title="Criar"]')
    salvar_button = (By.XPATH, '//button[text()="Salvar"]')
    h2_criar_conta = (By.XPATH, '//h2[text()="Criar Conta"]')
    input_fields = (
        By.XPATH,
        '//flexipage-field//label[text()="{0}"]'
        "/following-sibling::div//input |"
        ' //flexipage-field//label[text()="{0}"]'
        "/following-sibling::div/textarea",
    )
    dropdown_fields = (
        By.XPATH,
        '//flexipage-field//label[text()="{}"]'
        "/following-sibling::div"
        "//lightning-base-combobox-item"
        '[@data-value="{}"]',
    )
    dropdown_options = (
        By.XPATH,
        '//flexipage-field//label[text()="{}"]'
        "/following-sibling::div"
        "//lightning-base-combobox-item"
        '//span[@class="slds-truncate"]',
    )
    dropdown = (
        By.XPATH,
        '//flexipage-field//label[text()="{}"]'
        "/following-sibling::div//lightning-base-combobox"
        "//button",
    )
    lookup = (
        By.XPATH,
        '//flexipage-field//label[text()="{}"]'
        "//following-sibling::*//lightning-base-combobox-forma"
        'tted-text[@title="{}"]',
    )
    all_detail_field = (
        By.XPATH,
        "//dt//span/ancestor::dt"
        "//following-sibling::dd"
        '//slot[@name="output" '
        "and normalize-space()]",
    )
    detail_fields = (
        By.XPATH,
        '//dt//span[text()="{0}"]/ancestor::dt'
        "//following-sibling::dd"
        '//lightning-formatted-text[text()="{1}"] | '
        '//dt//span[text()="{0}"]/ancestor::dt'
        "//following-sibling::dd"
        '//a[normalize-space() = "{1}"]',
    )
    receita_anual = (
        By.XPATH,
        '//dt//span[text()="Receita anual"]'
        "/ancestor::dt//following-sibling::dd"
        "//lightning-formatted-text",
    )
    endereco_cobranca = (
        By.XPATH,
        '//dt//span[text()="Endereço de cobrança"]'
        "/ancestor::dt//following-sibling::dd"
        '//div[@class="slds-truncate"]',
    )
    field_out = (By.XPATH, '//input[@name="CNPJ__c"]')
    editar_button = (By.XPATH, '//button[@name="Edit"]')
    ultima_conta = (By.XPATH, "(//th//span//a)[1]")
    apagar_lookup_conta_pai = (
        By.XPATH,
        '(//button[@title="Limpar seleção"])[1]',
    )


class AccountPage(BasePage):
    def __init__(self, driver, screenshot=False):
        super().__init__(driver)  # Passa o driver para o BasePage
        self.screenshot = screenshot  # Define se vai tirar screenshot ou não
        self.dir_test02 = "test_ct02_labels_create_account"
        self.dir_test03 = "test_ct03_create_account"
        self.dir_test08 = "test_ct08_edit_account"

    def verificar_pagina_cadastro(self):
        url = os.getenv("ACCOUNT_PAGE_URL")
        self.access_link(url)
        self.text_exists_on_screen(AccountLocators.account_page, "Contas")

    def abrir_formulario_criacao_conta(self):
        self.click_script(AccountLocators.criar_button)

    def verificar_labels_layout(self, labels_json):
        labels_layout = self.get_all_elements(
            AccountLocators.form_input_labels
        )

        # Check if there are any missing labels in visible labels
        for label, keys in labels_json.items():
            if label not in labels_layout:
                assert False, (
                    f"Valor '{label}' não encontrado no "
                    f"layout (labels_layout)"
                )

        # Check if there are any extra labels in visible labels
        for label in labels_layout:
            if label not in dict(labels_json).keys():
                assert False, (
                    f"Valor '{label}' não encontrado na lista de "
                    f"labels esperadas (labels_json)"
                )

        self.take_ss(
            self.screenshot, "01_labels_create_account.png", self.dir_test02
        )

    def verificar_picklists(self, labels_json):
        i = 2
        for key, values in labels_json.items():
            if "options" in values:
                dropdown_expected = [option for option in values["options"]]
                dropdown = (
                    AccountLocators.dropdown[0],
                    AccountLocators.dropdown[1].format(key),
                )
                self.click_script(dropdown)
                self.take_ss(
                    self.screenshot,
                    f"{i:02}_labels_create_account.png",
                    self.dir_test02,
                )
                i += 1

                dropdown_options = (
                    AccountLocators.dropdown_options[0],
                    AccountLocators.dropdown_options[1].format(key),
                )

                dropdown_layout = self.all_dropdown_options(dropdown_options)

                assert len(dropdown_layout) == len(dropdown_expected), (
                    f"Quantidade esperada {len(dropdown_expected)}, "
                    f"quantidade encontrada {len(dropdown_layout)}"
                )

                for expected, layout in zip(
                    dropdown_expected, dropdown_layout
                ):
                    assert expected == layout, (
                        f"Esperado '{expected}', " f"encontrado '{layout}'"
                    )

    def preencher_formulario_conta(self, carregar_labels, edit=False):
        for key, value in carregar_labels.items():
            key = key.replace("*", "")
            if "options" in value:
                option = value["value"]
                dropdown_field = (
                    AccountLocators.dropdown_fields[0],
                    AccountLocators.dropdown_fields[1].format(key, option),
                )
                dropdown = (
                    AccountLocators.dropdown[0],
                    AccountLocators.dropdown[1].format(key),
                )
                self.click_script(dropdown)
                self.click_script(dropdown_field)
            else:
                input_field = (
                    AccountLocators.input_fields[0],
                    AccountLocators.input_fields[1].format(key),
                )
                if edit:
                    if key == "Conta pai":
                        self.click_script(
                            AccountLocators.apagar_lookup_conta_pai
                        )
                    self.overwrite(input_field, value["value"])
                else:
                    self.write(input_field, value["value"])

                if key == "Conta pai":
                    dropdown_field = (
                        AccountLocators.lookup[0],
                        AccountLocators.lookup[1].format(key, value["value"]),
                    )
                    self.click_script(dropdown_field)

        ss_name = "02_edit_account.png" if edit else "01_create_account.png"
        ss_dir = self.dir_test08 if edit else self.dir_test03
        self.take_ss(self.screenshot, ss_name, ss_dir)

    def salvar_conta(self):
        self.send_key()
        self.click_script(AccountLocators.salvar_button)

    def verificar_sucesso(self, n_campos, campos_adicionais, campos_agrupados):
        # self.access_link("https://playful-hawk-7aqdza-dev-ed.trailblaze.light
        # ning.force.com/lightning/r/Account/001ak00000ezjKcAAI/view")
        elements = self.find_elements(AccountLocators.all_detail_field)
        total_campos = n_campos + campos_adicionais - campos_agrupados
        assert len(elements) == total_campos, (
            f"Esperado {total_campos} "
            f"elementos, mas foram "
            f"encontrados {len(elements)}'"
        )

    def verificar_campos_detalhes(self, carregar_labels, edit=False):
        for key, value in carregar_labels.items():
            key = key.replace("*", "")
            if "options" in value:
                option = value["value"]
                detail_field = (
                    AccountLocators.detail_fields[0],
                    AccountLocators.detail_fields[1].format(key, option),
                )
                assert self.exists_on_screen(
                    detail_field
                ), f"Opção '{option}' em '{key}' não encontrada"
            elif key == "Receita anual":
                element = self.find_element(AccountLocators.receita_anual)
                value = value["value"]
                converted_value = uf.format_currency(value)
                assert (
                    element.text == converted_value
                ), f"Valor '{element.text}' em '{key}' não encontrado"
            else:
                detail_field = (
                    AccountLocators.detail_fields[0],
                    AccountLocators.detail_fields[1].format(
                        key, value["value"]
                    ),
                )

                assert self.exists_on_screen(
                    detail_field
                ), f"Valor '{value['value']}' em '{key}' não encontrado"

        ss_name = "03_edit_account.png" if edit else "02_create_account.png"
        ss_dir = self.dir_test08 if edit else self.dir_test03
        self.take_ss(self.screenshot, ss_name, ss_dir)

    def acessar_conta_existente(self):
        self.click_script(AccountLocators.ultima_conta)

    def clicar_em_editar(self):
        self.click_script(AccountLocators.editar_button)
        self.take_ss(self.screenshot, "01_edit_account.png", self.dir_test08)

    def take_ss(self, screenshot, filename, ss_dir):
        self.ss(screenshot, filename, ss_dir)
