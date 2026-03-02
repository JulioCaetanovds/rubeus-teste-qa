import pytest
from playwright.sync_api import Page, expect, Playwright

@pytest.mark.xfail(reason="UX Bug: Field accepts letters")
@pytest.mark.parametrize("url", ["https://qualidade.apprbs.com.br/site", "https://qualidade.apprbs.com.br/certificacao"])
def test_phone_field_should_not_accept_letters(page: Page, url):
    page.goto(url)
    phone_field = page.get_by_placeholder("(11) 96123-")
    phone_field.fill("INVALID_TEXT")
    
    actual_value = phone_field.input_value()
    assert not any(c.isalpha() for c in actual_value)

@pytest.mark.xfail(reason="Responsiveness Bug: Hamburger menu missing")
def test_mobile_responsive_menu_absence(playwright: Playwright, browser):
    iphone = playwright.devices['iPhone 13 Pro Max']
    context = browser.new_context(**iphone)
    page = context.new_page()
    page.goto("https://qualidade.apprbs.com.br/site")
    
    # ACTION: toggle locator
    mobile_menu = page.locator(".navbar-toggler, .menu-mobile, #hamburger")
    expect(mobile_menu).to_be_visible()
    
    context.close()