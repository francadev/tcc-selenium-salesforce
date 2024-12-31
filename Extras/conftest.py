import json
import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    opt = Options()
    opt.add_experimental_option(
        "prefs", {"profile.default_content_setting_values.notifications": 2}
    )
    driver = webdriver.Chrome(options=opt)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://login.salesforce.com")

    yield driver

    driver.quit()


@pytest.fixture
def load_account_data():
    caminho_json = os.path.join(
        os.path.dirname(__file__), "tests/data/account.json"
    )
    with open(caminho_json, "r", encoding="utf-8") as f:
        data = json.load(f)
        return data["labels"]


@pytest.fixture
def load_opportunity_data():
    caminho_json = os.path.join(
        os.path.dirname(__file__), "tests/data/opportunity.json"
    )
    with open(caminho_json, "r", encoding="utf-8") as f:
        data = json.load(f)
        return data["labels"]


@pytest.fixture
def load_lead_data():
    caminho_json = os.path.join(
        os.path.dirname(__file__), "tests/data/lead.json"
    )
    with open(caminho_json, "r", encoding="utf-8") as f:
        data = json.load(f)
        return data["labels"]


@pytest.fixture
def load_contact_data():
    caminho_json = os.path.join(
        os.path.dirname(__file__), "tests/data/contact.json"
    )
    with open(caminho_json, "r", encoding="utf-8") as f:
        data = json.load(f)
        return data["labels"]


@pytest.fixture
def load_new_lead_data():
    caminho_json = os.path.join(
        os.path.dirname(__file__), "tests/data/new_lead.json"
    )
    with open(caminho_json, "r", encoding="utf-8") as f:
        data = json.load(f)
        return data["labels"]


@pytest.fixture
def load_new_account_data():
    caminho_json = os.path.join(
        os.path.dirname(__file__), "tests/data/new_account.json"
    )
    with open(caminho_json, "r", encoding="utf-8") as f:
        data = json.load(f)
        return data["labels"]


@pytest.fixture
def load_new_opportunity_data():
    caminho_json = os.path.join(
        os.path.dirname(__file__), "tests/data/new_opportunity.json"
    )
    with open(caminho_json, "r", encoding="utf-8") as f:
        data = json.load(f)
        return data["labels"]


# @pytest.hookimpl(tryfirst=True)
# def pytest_runtest_teardown(item):
#     # Comando a ser executado após cada teste
#     print(f"\nComando executado após o teste: {item.name}")
#     print(f"ID completo do teste: {item.nodeid}")
