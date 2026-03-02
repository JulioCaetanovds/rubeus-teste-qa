from playwright.sync_api import Page, expect
from faker import Faker

fake = Faker('pt_BR')

def test_certification_saiba_mais_button_does_not_redirect(page: Page):
    page.goto("https://qualidade.apprbs.com.br/certificacao")
    
    # SETUP: url
    initial_url = page.url
    
    # ACTION
    saiba_mais_btn = page.locator("text=Saiba mais").first
    saiba_mais_btn.click()
    
    # ASSERT
    expect(page).to_have_url(initial_url)

def test_certification_form_shows_base_local_error(page: Page):
    page.goto("https://qualidade.apprbs.com.br/certificacao")
    
    # SETUP: faker data
    fake_name = fake.name()
    fake_email = fake.email()
    fake_phone = fake.msisdn()[:11] 
    
    # ACTION: fill
    page.locator('input[name="pessoa.nome"]').fill(fake_name)
    page.get_by_placeholder("email@exemplo.com").fill(fake_email)
    page.get_by_placeholder("(11) 96123-").fill(fake_phone)
    
    # ACTION: submit
    page.get_by_role("button", name="Avançar").click()
    
    # ASSERT: error
    error_toast = page.locator("#toast-container div").filter(has_text="É necessário informar a base")
    expect(error_toast).to_be_visible()