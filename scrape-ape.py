import sys
import tkinter as tk
from tkinter import messagebox
import os
import subprocess
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import webbrowser
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

driver = None
log_text = None
url_entry = None

website_types = {
    'Static HTML/CSS Websites': ['html', 'css'],
    'Dynamic Websites': ['php', 'python', 'ruby', 'node.js'],
    'Content Management Systems (CMS)': ['wordpress', 'joomla', 'drupal'],
    'E-commerce Websites': ['shopify', 'woocommerce', 'magento'],
    'Social Media Websites': ['facebook', 'twitter', 'instagram', 'linkedin'],
    'Blogs': ['blog'],
    'Portfolio Websites': ['portfolio'],
    'Educational Websites': ['coursera', 'udemy', 'khan academy'],
    'Web Applications': ['web application'],
    'Single Page Applications (SPAs)': ['spa'],
    'Government Websites': ['government'],
    'News and Media Websites': ['news', 'media'],
    'Forums and Discussion Boards': ['forum'],
    'Wiki Websites': ['wiki'],
    'Business Websites': ['business'],
    'Personal Websites': ['personal'],
    'Landing Pages': ['landing page']
}

def nggyu():
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

def scrape_custom_page():
    custom_url = url_entry.get()
    if custom_url:
        scrape_url(custom_url)

def scrape_url(url):
    try:
        driver.get(url)
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        website_type = detect_website_type(soup)
        website_path = os.path.join(os.getcwd(), 'websites', website_type)
        os.makedirs(website_path, exist_ok=True)
        generate_files(page_source, website_path)
        add_to_log("Scraping Complete: " + website_type)
        messagebox.showinfo("Scraping Complete", "Scraping process is complete!")
    except WebDriverException:
        add_to_log("Error: Web browser window closed unexpectedly.")
        messagebox.showerror("Error", "Web browser window closed unexpectedly.")

def detect_website_type(soup):
    for website, keywords in website_types.items():
        for keyword in keywords:
            if soup.find_all(string=lambda text: keyword in text.lower()):
                return website
    return 'Unknown'

def generate_files(page_source, website_path):
    html_file_path = os.path.join(website_path, 'index.html')
    with open(html_file_path, 'w', encoding='utf-8') as html_file:
        html_file.write(page_source)

def add_to_log(message):
    log_text.insert(tk.END, message + "\n")
    log_text.see(tk.END)

def fetch_resource(url, session=None):
    session = session or requests.Session()
    try:
        response = session.get(url, timeout=10)
        if response.status_code == 200:
            return response.content
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
    return None

def save_resource(content, resource_path):
    os.makedirs(os.path.dirname(resource_path), exist_ok=True)
    with open(resource_path, 'wb') as file:
        file.write(content)

def extract_and_save_resources(soup, base_url, output_dir):
    session = requests.Session()
    for img_tag in soup.find_all('img'):
        img_url = img_tag.get('src')
        if img_url:
            img_url = urljoin(base_url, img_url)
            img_data = fetch_resource(img_url, session)
            if img_data:
                img_name = os.path.basename(img_url.split('?')[0])
                img_path = os.path.join(output_dir, img_name)
                save_resource(img_data, img_path)
    for resource_tag in soup.find_all(['link', 'script']):
        if resource_tag.name == 'link' and resource_tag.get('rel') == ['stylesheet']:
            resource_url = resource_tag.get('href')
        elif resource_tag.name == 'script' and resource_tag.get('src'):
            resource_url = resource_tag.get('src')
        else:
            continue
        if resource_url:
            resource_url = urljoin(base_url, resource_url)
            resource_data = fetch_resource(resource_url, session)
            if resource_data:
                resource_name = os.path.basename(resource_url.split('?')[0])
                resource_path = os.path.join(output_dir, resource_name)
                save_resource(resource_data, resource_path)

def retrieve_scraped_resources():
    page_source_path = os.path.join(os.getcwd(), 'page-source')
    for root, dirs, files in os.walk(page_source_path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                print(f"Content of {file_path}:\n{content}\n")

def scrape_and_save_page_source():
    try:
        current_url = driver.current_url
        if current_url:
            page_source = driver.page_source
            soup = BeautifulSoup(page_source, 'html.parser')
            page_source_path = os.path.join(os.getcwd(), 'page-source')
            os.makedirs(page_source_path, exist_ok=True)
            css_content = extract_css(soup)
            js_content = extract_js(soup, current_url)
            for script_or_style in soup(['script', 'style']):
                script_or_style.extract()
            main_html_file_path = os.path.join(page_source_path, 'main.html')
            with open(main_html_file_path, 'w', encoding='utf-8') as main_html_file:
                main_html_file.write(page_source)
            index_html_file_path = os.path.join(page_source_path, 'index.html')
            with open(index_html_file_path, 'w', encoding='utf-8') as index_html_file:
                html_only = soup.find('html')
                index_html_file.write(html_only.prettify() if html_only else '')
            css_file_path = os.path.join(page_source_path, 'styles.css')
            with open(css_file_path, 'w', encoding='utf-8') as css_file:
                css_file.write(css_content)
            js_file_path = os.path.join(page_source_path, 'scripts.js')
            with open(js_file_path, 'w', encoding='utf-8') as js_file:
                js_file.write(js_content)
            add_to_log("Page source, CSS, and JS saved successfully to " + page_source_path)
            messagebox.showinfo("Success", "Page source, CSS, and JS have been saved successfully.")
            extract_and_save_resources(soup, current_url, page_source_path)
            retrieve_scraped_resources()  
    except WebDriverException as e:
        add_to_log("Error: " + str(e))
        messagebox.showerror("Error", "An error occurred while trying to save the page source, CSS, and JS.")

def extract_css(soup):
    css_content = ""
    for style in soup.find_all("style"):
        css_content += style.text + "\n"
    for link in soup.find_all("link", rel="stylesheet"):
        href = link.get('href')
        if href:
            css_content += f'@import url("{href}");\n'
    return css_content

def extract_js(soup, base_url):
    js_content = ""
    for script in soup.find_all("script"):
        src = script.get('src')
        if src:
            if src.startswith("http://") or src.startswith("https://"):
                js_url = src
            else:
                js_url = base_url + src
            js_content += f'// External script: {js_url}\n'
            try:
                response = requests.get(js_url)
                if response.status_code == 200:
                    js_content += response.text + "\n"
            except requests.RequestException as e:
                js_content += f'// Failed to fetch the script: {e}\n'
        else:
            js_content += script.text + "\n"
    return js_content

def run_puppeteer_script():
    custom_url = url_entry.get()
    if not custom_url:
        add_to_log("Error: No URL provided.")
        messagebox.showerror("Error", "Please enter a URL to scrape.")
        return
    puppeteer_command = ['node', 'scrape-ape-puppeteer.js', custom_url]
    try:
        completed_process = subprocess.run(puppeteer_command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        add_to_log(completed_process.stdout)
        messagebox.showinfo("Success", "Puppeteer script executed successfully.")
    except subprocess.CalledProcessError as e:
        add_to_log("Error: " + e.stderr)
        messagebox.showerror("Error", e.stderr)

def main():
    global driver, log_text, url_entry
    driver = webdriver.Chrome()
    root = tk.Tk()
    root.title("Scrape - APE")
    window_width = 550
    window_height = 650
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate = (screen_width - window_width) // 2
    y_coordinate = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")
    if getattr(sys, 'frozen', False):
        datadir = os.path.dirname(sys.executable)
    else:
        datadir = os.path.dirname(os.path.realpath(__file__))
    root.iconbitmap(os.path.join(datadir, 'Scrape-APE.ico'))
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)
    current_page_button = tk.Button(button_frame, text="NGGYU", command=nggyu)
    current_page_button.grid(row=0, column=0, padx=20)
    custom_page_button = tk.Button(button_frame, text="Scrape Custom Page", command=scrape_custom_page)
    custom_page_button.grid(row=0, column=1, padx=20)
    page_source_button = tk.Button(button_frame, text="Scrape Page Source", command=scrape_and_save_page_source)
    page_source_button.grid(row=0, column=2, padx=20)
    puppeteer_button = tk.Button(button_frame, text="Run Puppeteer Script", command=run_puppeteer_script)
    puppeteer_button.grid(row=0, column=3, padx=20)
    url_frame = tk.Frame(root)
    url_frame.pack(pady=10)
    url_label = tk.Label(url_frame, text="URL:")
    url_label.grid(row=0, column=0)
    url_entry = tk.Entry(url_frame, width=40)
    url_entry.grid(row=0, column=1)
    log_frame = tk.Frame(root)
    log_frame.pack(pady=10)
    log_text = tk.Text(log_frame, height=30, width=60)
    log_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    log_scroll = tk.Scrollbar(log_frame, orient=tk.VERTICAL, command=log_text.yview)
    log_scroll.pack(side=tk.RIGHT, fill=tk.Y)
    log_text.config(yscrollcommand=log_scroll.set)
    log_frame.place(relx=0.5, rely=1.0, anchor=tk.S, y=-2)
    root.mainloop()

if __name__ == "__main__":
    main()
