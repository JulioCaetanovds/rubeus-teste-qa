from playwright.sync_api import Page, expect
from faker import Faker

fake = Faker('pt_BR')

def test_site_carousel_button_does_not_redirect(page: Page):
    page.goto("https://qualidade.apprbs.com.br/site")
    
    # SETUP: url
    initial_url = page.url
    
    # ACTION
    carousel_btn = page.locator("text=INSCREVA-SE").first
    carousel_btn.click()
    
    # ASSERT
    expect(page).to_have_url(initial_url)

def test_site_newsletter_shows_base_local_error(page: Page):
    page.goto("https://qualidade.apprbs.com.br/site")
    
    # SETUP: faker data
    fake_name = fake.name()
    fake_email = fake.email()
    fake_phone = fake.msisdn()[:11]
    
    # ACTION: fill
    page.locator('input[name="pessoa.nome"]').fill(fake_name)
    page.get_by_placeholder("email@exemplo.com").fill(fake_email)
    page.get_by_placeholder("(11) 96123-").fill(fake_phone)
    
    # ACTION: submit
    page.get_by_role("button", name="CONCLUIR").click()
    
    # ASSERT: error
    error_toast = page.locator("#toast-container div").filter(has_text="É necessário informar a base")
    expect(error_toast).to_be_visible()