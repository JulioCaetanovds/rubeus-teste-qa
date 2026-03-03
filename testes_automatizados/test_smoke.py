import re
from playwright.sync_api import Page, expect

def test_pages_are_reachable(page: Page):
    for url in ["https://qualidade.apprbs.com.br/site", "https://qualidade.apprbs.com.br/certificacao"]:
        response = page.goto(url)
        assert response.status == 200

def test_navigation_to_events(page: Page):
    page.goto("https://qualidade.apprbs.com.br/site")
    with page.expect_popup() as popup_info:
        page.get_by_role("link", name="EVENTOS").click()
    
    popup = popup_info.value
    assert "analista-rubeus" in popup.url.lower()