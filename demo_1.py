import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.wait_for_load_state('networkidle')
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.get_by_text("Home Practice Courses Blog Contact open menu Test login This is a simple Login").click()
    page.get_by_label("Username").click()
    page.get_by_label("Username").fill("student")
    page.get_by_label("Username").press("Tab")
    page.get_by_label("Password").fill("Password123")
    page.get_by_role("button", name="Submit").click()

    # ---------------------
    context.close()
    browser.close()

    print("Demo website login completed !!")


with sync_playwright() as playwright:
    run(playwright)
