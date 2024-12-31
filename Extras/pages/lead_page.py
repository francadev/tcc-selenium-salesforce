import os

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils import functions as uf


class LeadLocators:
    lead_page = (By.XPATH, '//span[@class="slds-var-p-right_x-small"]')
    criar_button = (By.XPATH, '//div[@title="Criar"]')
    editar_button = (By.XPATH, '//button[@name="Edit"]')
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
        '//a[normalize-space() = "{1}"] | '
        '//dt//span[text()="{0}"]/ancestor::dt'
        "//following-sibling::dd"
        '//lightning-formatted-number[text()="{1}"]',
    )
    receita_anual = (
        By.XPATH,
        '//dt//span[text()="Receita anual"]'
        "/ancestor::dt//following-sibling::dd"
        "//lightning-formatted-text",
    )
    nome_completo = (
        By.XPATH,
        '//dt//span[text()="Nome completo"]'
        "/ancestor::dt//following-sibling::dd"
        "//lightning-formatted-name",
    )
    ultimo_lead = (By.XPATH, "(//th//span//a)[1]")


class LeadPage(BasePage):
    def __init__(self, driver, screenshot=False):
        super().__init__(driver)
        self.screenshot = screenshot
        self.dir_test06 = "test_ct06_labels_create_lead"
        self.dir_test07 = "test_ct07_create_lead"
        self.dir_test10 = "test_ct10_edit_lead"

    def verificar_pagina_cadastro_lead(self):
        url = os.getenv("LEAD_PAGE_URL")
        self.access_link(url)
        self.text_exists_on_screen(LeadLocators.lead_page, "Leads")

    def abrir_formulario_criacao_lead(self):
        self.click_script(LeadLocators.criar_button)

    def verificar_labels_layout_lead(self, labels_json):
        labels_layout = self.get_all_elements(LeadLocators.form_input_labels)

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
            self.screenshot, "01_labels_create_lead.png", self.dir_test06
        )

    def verificar_picklists_lead(self, labels_json):
        i = 2
        for key, values in labels_json.items():
            key = key.replace("*", "")
            if "options" in values:
                dropdown_expected = [option for option in values["options"]]
                dropdown = (
                    LeadLocators.dropdown[0],
                    LeadLocators.dropdown[1].format(key),
                )
                self.click_script(dropdown)
                self.take_ss(
                    self.screenshot,
                    f"{i:02}_labels_create_lead.png",
                    self.dir_test06,
                )
                i += 1

                dropdown_options = (
                    LeadLocators.dropdown_options[0],
                    LeadLocators.dropdown_options[1].format(key),
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

    def preencher_formulario_lead(self, carregar_labels, edit=False):
        for key, value in carregar_labels.items():
            key = key.replace("*", "")
            if "options" in value:
                option = value["value"]
                dropdown_field = (
                    LeadLocators.dropdown_fields[0],
                    LeadLocators.dropdown_fields[1].format(key, option),
                )
                dropdown = (
                    LeadLocators.dropdown[0],
                    LeadLocators.dropdown[1].format(key),
                )
                self.click_script(dropdown)
                self.click_script(dropdown_field)
            else:
                input_field = (
                    LeadLocators.input_fields[0],
                    LeadLocators.input_fields[1].format(key),
                )
                if edit:
                    self.overwrite(input_field, value["value"])

                else:
                    self.write(input_field, value["value"])

                ss_name = "01_edit_lead.png" if edit else "01_create_lead.png"
                ss_dir = self.dir_test10 if edit else self.dir_test07
                self.take_ss(self.screenshot, ss_name, ss_dir)

    def salvar_lead(self):
        self.send_key()
        self.click_script(LeadLocators.salvar_button)

    def verificar_sucesso(self, n_campos, campos_adicionais, campos_agrupados):
        elements = self.find_elements(LeadLocators.all_detail_field)
        total_campos = n_campos + campos_adicionais - campos_agrupados
        assert len(elements) == total_campos, (
            f"Esperado {total_campos} "
            f"elementos, mas foram "
            f"encontrados {len(elements)}'"
        )

    def verificar_campos_detalhes_lead(self, carregar_labels, edit=False):
        # self.access_link("https://playful-hawk-7aqdza-dev-ed.trailblaze.light"
        #                  "ning.force.com/lightning/r/Lead/00Qak00000AX6VWEA1/view")
        nome_completo = []

        for key, value in carregar_labels.items():
            key = key.replace("*", "")
            if "options" in value and key != "Tratamento":
                option = value["value"]
                detail_field = (
                    LeadLocators.detail_fields[0],
                    LeadLocators.detail_fields[1].format(key, option),
                )
                assert self.exists_on_screen(
                    detail_field
                ), f"Opção '{option}' em '{key}' não encontrada"
            elif key in ["Tratamento", "Primeiro Nome", "Sobrenome"]:
                nome_completo.append(value["value"])
            elif key == "Receita anual":
                element = self.find_element(LeadLocators.receita_anual)
                value = value["value"]
                converted_value = uf.format_currency(value)
                assert (
                    element.text == converted_value
                ), f"Valor '{element.text}' em '{key}' não encontrado"
            else:
                detail_field = (
                    LeadLocators.detail_fields[0],
                    LeadLocators.detail_fields[1].format(key, value["value"]),
                )

                assert self.exists_on_screen(
                    detail_field
                ), f"Valor '{value['value']}' em '{key}' não encontrado"

        element = self.find_element(LeadLocators.nome_completo)
        assert element.text == " ".join(
            nome_completo
        ), f"Valor '{element.text}' em 'Nome completo' não encontrado"

        ss_name = "02_edit_lead.png" if edit else "02_create_lead.png"
        ss_dir = self.dir_test10 if edit else self.dir_test07
        self.take_ss(self.screenshot, ss_name, ss_dir)

    def acessar_lead_existente(self):
        self.click_script(LeadLocators.ultimo_lead)

    def clicar_em_editar(self):
        self.click_script(LeadLocators.editar_button)
        self.take_ss(self.screenshot, "01_edit_lead.png", self.dir_test10)

    def take_ss(self, screenshot, filename, ss_dir):
        self.ss(screenshot, filename, ss_dir)
