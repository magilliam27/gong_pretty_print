from playwright.sync_api import sync_playwright
import csv
from bs4 import BeautifulSoup
import os

def remove_service_trade_participants(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    service_trade_h3 = soup.find('h3', string='ServiceTrade')
    service_trade_participants = []
    if service_trade_h3 is not None:
        for sibling in service_trade_h3.find_next_siblings():
            if sibling.name == 'h3':
                break
            if sibling.get('class') == ['participant']:
                participant_name = sibling.find('div', class_='participantName').get_text(strip=True).split()[0]  # First name only
                service_trade_participants.append(participant_name)

    for monologue in soup.find_all('div', class_='monologue'):
        speaker_name = monologue.find('p', class_='speaker').get_text(strip=True).split()[0]
        if speaker_name in service_trade_participants:
            monologue.decompose()

    return str(soup)

def auto_print_to_pdfs(playwright):
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

    # 3. Fetch Call IDs from CSV
    with open('internalcallids - Sheet1 (3).csv', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            call_id = row[0]
            target_url = f"https://us-21176.app.gong.io/call/pretty-transcript?call-id={call_id}"
            print(f"Processing: {target_url}")
            page.goto(target_url)

            # Optional: Adjust for the page load or wait for a specific element that confirms the page has loaded
            page.wait_for_timeout(5000)  # Milliseconds; adjust as necessary

            # Define the HTML file name including the call ID
            html_filename = f"HTMLs/call_transcript_{call_id}.html"
            print(f"Saving HTML as: {html_filename}")
            
            # Check if the directory exists, if not, create it
            directory = os.path.dirname(html_filename)
            if not os.path.exists(directory):
                os.makedirs(directory)
            # Capture the page as HTML
            html_content = page.content()
            # Remove ServiceTrade participants from HTML content
            modified_html_content = remove_service_trade_participants(html_content)
            with open(html_filename, 'w') as f:
                f.write(modified_html_content)

    # Clean up
    context.close()
    browser.close()

with sync_playwright() as playwright:
    auto_print_to_pdfs(playwright)
