import os

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils import functions as uf


class OpportunityLocators:
    opportunity_page = (By.XPATH, '//span[@class="slds-var-p-right_x-small"]')
    criar_button = (By.XPATH, '//div[@title="Criar"]')
    form_input_labels = (By.XPATH, "//flexipage-field//label")
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
    salvar_button = (By.XPATH, '//button[text()="Salvar"]')
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
    valor = (
        By.XPATH,
        '//dt//span[text()="Valor"]'
        "/ancestor::dt//following-sibling::dd"
        "//lightning-formatted-text",
    )
    probabilidade = (
        By.XPATH,
        '//dt//span[text()="Probabilidade (%)"]'
        "/ancestor::dt//following-sibling::dd"
        "//lightning-formatted-number",
    )
    ultima_oportunidade = (By.XPATH, "(//th//span//a)[1]")
    editar_button = (By.XPATH, '//button[@name="Edit"]')
    apagar_lookup_nome_da_conta = (
        By.XPATH,
        '(//button[@title="Limpar seleção"])[1]',
    )


class OpportunityPage(BasePage):
    def __init__(self, driver, screenshot=False):
        super().__init__(driver)
        self.screenshot = screenshot
        self.dir_test04 = "test_ct04_labels_create_opportunity"
        self.dir_test05 = "test_ct05_create_opportunity"
        self.dir_test09 = "test_ct09_edit_opportunity"

    def verificar_pagina_cadastro_oportunidade(self):
        url = os.getenv("OPPORTUNITY_PAGE_URL")
        self.access_link(url)
        self.text_exists_on_screen(
            OpportunityLocators.opportunity_page, "Oportunidades"
        )

    def abrir_formulario_criacao_oportunidade(self):
        self.click_script(OpportunityLocators.criar_button)

    def verificar_labels_layout_oportunidade(self, labels_json):
        labels_layout = self.get_all_elements(
            OpportunityLocators.form_input_labels
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
            self.screenshot,
            "01_labels_create_opportunity.png",
            self.dir_test04,
        )

    def verificar_picklists_oportunidade(self, labels_json):
        i = 2
        for key, values in labels_json.items():
            key = key.replace("*", "")
            if "options" in values:
                dropdown_expected = [option for option in values["options"]]
                dropdown = (
                    OpportunityLocators.dropdown[0],
                    OpportunityLocators.dropdown[1].format(key),
                )
                self.click_script(dropdown)
                self.take_ss(
                    self.screenshot,
                    f"{i:02}_labels_create_opportunity.png",
                    self.dir_test04,
                )
                i += 1

                dropdown_options = (
                    OpportunityLocators.dropdown_options[0],
                    OpportunityLocators.dropdown_options[1].format(key),
                )

                dropdown_layout = self.all_dropdown_options(dropdown_options)

                assert len(dropdown_layout) == len(dropdown_expected), (
                    f"Picklist: {key}, "
                    f"Quantidade esperada {len(dropdown_expected)}, "
                    f"quantidade encontrada {len(dropdown_layout)}"
                )

                for expected, layout in zip(
                    dropdown_expected, dropdown_layout
                ):
                    assert expected == layout, (
                        f"Esperado '{expected}', " f"encontrado '{layout}'"
                    )

    def preencher_formulario_oportunidade(self, carregar_labels, edit=False):
        for key, value in carregar_labels.items():
            key = key.replace("*", "")
            if "options" in value:
                option = value["value"]
                dropdown_field = (
                    OpportunityLocators.dropdown_fields[0],
                    OpportunityLocators.dropdown_fields[1].format(key, option),
                )
                dropdown = (
                    OpportunityLocators.dropdown[0],
                    OpportunityLocators.dropdown[1].format(key),
                )
                self.click_script(dropdown)
                self.click_script(dropdown_field)
            else:
                input_field = (
                    OpportunityLocators.input_fields[0],
                    OpportunityLocators.input_fields[1].format(key),
                )
                if edit:
                    if key == "Nome da conta":
                        self.click_script(
                            OpportunityLocators.apagar_lookup_nome_da_conta
                        )
                    self.overwrite(input_field, value["value"])
                else:
                    self.write(input_field, value["value"])

                if key == "Nome da conta":
                    dropdown_field = (
                        OpportunityLocators.lookup[0],
                        OpportunityLocators.lookup[1].format(
                            key, value["value"]
                        ),
                    )
                    self.click_script(dropdown_field)

        ss_name = (
            "02_edit_opportunity.png" if edit else "01_create_opportunity.png"
        )
        ss_dir = self.dir_test09 if edit else self.dir_test05
        self.take_ss(self.screenshot, ss_name, ss_dir)

    def salvar_oportunidade(self):
        self.send_key()
        self.click_script(OpportunityLocators.salvar_button)

    def verificar_sucesso(
        self,
        n_campos,
        campos_adicionais,
    ):
        elements = self.find_elements(OpportunityLocators.all_detail_field)
        total_campos = n_campos + campos_adicionais
        assert len(elements) == total_campos, (
            f"Esperado {total_campos} "
            f"elementos, mas foram "
            f"encontrados {len(elements)}'"
        )

    def verificar_campos_detalhes_oportunidade(
        self, carregar_labels, edit=False
    ):
        for key, value in carregar_labels.items():
            key = key.replace("*", "")
            if "options" in value:
                option = value["value"]
                detail_field = (
                    OpportunityLocators.detail_fields[0],
                    OpportunityLocators.detail_fields[1].format(key, option),
                )
                assert self.exists_on_screen(
                    detail_field
                ), f"Opção '{option}' em '{key}' não encontrada"
            elif key == "Valor":
                element = self.find_element(OpportunityLocators.valor)
                value = value["value"]
                converted_value = uf.format_currency(value, add_decimal=True)
                assert (
                    element.text == converted_value
                ), f"Valor '{element.text}' em '{key}' não encontrado"
            elif key == "Probabilidade (%)":
                element = self.find_element(OpportunityLocators.probabilidade)
                converted_value = value["value"] + "%"
                assert (
                    element.text == converted_value
                ), f"Valor '{element.text}' em '{key}' não encontrado"
            else:
                detail_field = (
                    OpportunityLocators.detail_fields[0],
                    OpportunityLocators.detail_fields[1].format(
                        key, value["value"]
                    ),
                )

                assert self.exists_on_screen(
                    detail_field
                ), f"Valor '{value['value']}' em '{key}' não encontrado"

        ss_name = (
            "03_edit_oppotunity.png" if edit else "02_create_opportunity.png"
        )
        ss_dir = self.dir_test09 if edit else self.dir_test05
        self.take_ss(self.screenshot, ss_name, ss_dir)

    def acessar_oportunidade_existente(self):
        self.click_script(OpportunityLocators.ultima_oportunidade)

    def clicar_em_editar(self):
        self.click_script(OpportunityLocators.editar_button)
        self.take_ss(
            self.screenshot, "01_edit_opportunity.png", self.dir_test09
        )

    def take_ss(self, screenshot, filename, ss_dir):
        self.ss(screenshot, filename, ss_dir)
