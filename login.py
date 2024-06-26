import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500, args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    page.wait_for_load_state('networkidle')
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.get_by_text("Home Practice Courses Blog Contact open menu Test login This is a simple Login").click()
    page.get_by_label("Username").click()
    page.get_by_label("Username").fill("student")
    page.get_by_label("Username").press("Tab")
    page.get_by_label("Password").fill("Password123")
    try:
        page.get_by_role("button", name="Submit").click(timeout=3000)
        print("User logged in successfully!")
    except playwright._impl._errors.TimeoutError:
        print("Timeout occurred while clicking the submit button.")

    # page.pause()

    try:
        expect(page.get_by_role("link", name="Log out")).to_be_visible()
        print("Logout button is visible!")
    except playwright._impl._errors.TimeoutError:
        print("Logout button is not visible within the timeout.")
    # ---------------------
    context.close()
    browser.close()

    print("Demo website login completed !!")


with sync_playwright() as playwright:
    run(playwright)
