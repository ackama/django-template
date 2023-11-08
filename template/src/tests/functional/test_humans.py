from playwright.sync_api import Page


def test_can_get_humans_txt(live_server, page: Page):
    url = f"{live_server.url}/humans.txt"
    page.goto(url)
    assert "/* TEAM */" in page.content()
