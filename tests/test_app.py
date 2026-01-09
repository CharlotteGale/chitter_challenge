from playwright.sync_api import Page, expect

def test_get_peeps(page, test_web_address, db_connection):
    db_connection.seed("seeds/peeps.sql")
    page.goto(f"http://{test_web_address}/home")
    # page.click("text=write a peep!")
    h2_tag = page.locator("h2")
    expect(h2_tag).to_have_text("Chitter Feed")

    peep_author_element = page.locator(".peep-author")
    expect(peep_author_element).to_have_text("Test Author 1")
