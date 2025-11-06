import pytest
from selene import browser, be, have


@pytest.fixture
def setup_browser():
    browser.open('https://duckduckgo.com/')


@pytest.fixture
def input_text_search(setup_browser):
    browser.element('[name="q"]').should(be.blank).type('qa.guru').press_enter()


@pytest.fixture
def input_invalid_text_search(setup_browser):
    browser.element('[name="q"]').should(be.blank).type('cvzvzvzvzxvzxvzxvzx').press_enter()



def test_find_text_to_search(input_text_search):
    browser.element('#react-layout').should(have.text('QA.GURU'))
    browser.element('[data-result="snippet"]').should(have.text(
        'Освойте тестирование ПО с нуля: курсы QA на Java, Python, JS. Практика от экспертов, портфолио на GitHub, помощь в трудоустройстве.'))

def test_invalid_text_to_search(input_invalid_text_search):
    browser.element('#react-layout').should(have.text('По запросу «cvzvzvzvzxvzxvzxvzx» ничего не найдено.'))
