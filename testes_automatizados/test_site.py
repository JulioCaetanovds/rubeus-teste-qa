from playwright.sync_api import Page, expect
from faker import Faker

fake = Faker('pt_BR')

def test_site_carousel_button_does_not_redirect(page: Page):
    page.goto("https://qualidade.apprbs.com.br/site")
    initial_url = page.url
    # Usando o seletor exato que você mapeou
    page.locator("#izselm").get_by_role("link", name="INSCREVA-SE AGORA!").click()
    expect(page).to_have_url(initial_url)

def test_site_newsletter_shows_base_local_error(page: Page):
    page.goto("https://qualidade.apprbs.com.br/site")
    
    page.locator('input[name="pessoa.nome"]').fill(fake.name())
    page.get_by_placeholder("email@exemplo.com").fill(fake.email())
    page.get_by_placeholder("(11) 96123-").fill("54828828220")
    
    page.get_by_role("button", name="Concluir").click()
    
    error_toast = page.locator("#toast-container div").filter(has_text="É necessário informar a base")
    expect(error_toast).to_be_visible()