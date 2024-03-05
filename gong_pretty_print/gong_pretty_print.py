from playwright.sync_api import sync_playwright
import csv
import os

def auto_print_to_pdf(playwright, csv_path, url_base):
    browser_type = playwright.chromium
    browser = browser_type.launch(headless=False)  # Consider setting headless to True for automation without GUI
    context = browser.new_context()

    # 1. Launcher or Navigation
    page = context.new_page()

    # 2. Primary Landing: Login
    login_url = 'https://app.gong.io/welcome/sign-in'
    page.goto(login_url)
    
    print("Login manually using your account. After logging in, press Enter here to continue.")
    input("After you've logged in and are ready to proceed, press Enter...")


    with open(csv_path, newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            call_id = row[0]
            target_url = f"{url_base}{call_id}"
            print(f"Processing: {target_url}")
            page.goto(target_url)

            # Optional: Adjust for the page load or wait for a specific element that confirms the page has loaded
            page.wait_for_timeout(1000)  # Milliseconds; adjust as necessary

            # Save the page as a PDF
            pdf_filename = f"PDFs/call_transcript_{call_id}.pdf"
            print(f"Saving PDF as: {pdf_filename}")
            page.pdf(path=pdf_filename)

    # Clean up
    context.close()
    browser.close()

csv_path = input("Please enter the CSV path: ")
url_base = input("Please enter the target URL base: ")

with sync_playwright() as playwright:
    auto_print_to_pdf(playwright, csv_path, url_base)


