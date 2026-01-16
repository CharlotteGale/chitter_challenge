from playwright.sync_api import Page, expect

def test_get_peeps(page, test_web_address, db_connection):
    db_connection.seed("seeds/peeps_test.sql")
    page.goto(f"http://{test_web_address}/home")
    # page.click("text=write a peep!")
    h2_tag = page.locator("h2")
    expect(h2_tag).to_have_text("Chitter Feed")

    peep_author_element = page.locator(".peep-author")
    expect(peep_author_element).to_have_text("Test Author 1")

    peep_content_element = page.locator(".peep-content")
    expect(peep_content_element).to_have_text("This is a peep")

    peep_timestamp_element = page.locator(".timestamp")
    expect(peep_timestamp_element).to_have_text("13:13")
