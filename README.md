
# Scrape-APE

![Scrape-APE Icon](Scrape-APE.ico)

Scrape-APE is a web scraping toolkit designed to "somewhat" gather data from a wide range of websites, including those that rely on JavaScript for dynamic content rendering. Utilizing Python for back-end processing and Puppeteer with Node.js for handling JavaScript-heavy websites, this application offers a Ghetto approach to web scraping. It comes with a user-friendly graphical interface, making it accessible to both beginners and seasoned professionals. ( I had to build it for class ) But got the grade for making it within the 90min. Contribute to it, make it your own, whatever. Was a fun build.

## Features

- Comprehensive scraping capabilities for static, dynamic, CMS-based, e-commerce websites, and more.
- Integration with Puppeteer for JavaScript execution, enhancing scraping from dynamic web pages.
- A straightforward graphical user interface to simplify the web scraping process.
- Customizable scraping tasks to focus on specific types of websites or data requirements.
- Efficient data storage in structured formats for subsequent analysis or utilization.

## Getting Started

### Prerequisites

Ensure you have Python (version 3.6 or newer) and Node.js installed on your machine to run Scrape-APE and its components.

You will also need the following packages and tools:
- BeautifulSoup4
- Selenium
- Puppeteer

### Installation

#### Step 1: Clone the Repository

Clone Scrape-APE to your local system:

```sh
git clone https://github.com/Suffix30/Scrape-APE.git
cd scrape-ape
```

#### Step 2: Install Required Packages

##### Python Packages

```sh
pip install beautifulsoup4
pip install selenium
```

##### Node.js Packages

```sh
npm install puppeteer
```

#### Step 3: WebDriver Setup

To scrape dynamic websites with Selenium, you'll need a WebDriver:
- **Chrome:** Download [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/).
- **Firefox:** Download [GeckoDriver](https://github.com/mozilla/geckodriver/releases).

Make sure the driver is in your PATH or specified in your script.

### Usage

#### Running Scrape-APE with Python

Execute the Python script to launch the GUI and start scraping:

```sh
python scrape-ape.py
```

#### Using Puppeteer for JavaScript-Heavy Websites

Run the following command to scrape websites with JavaScript:

```sh
node scrape-ape-puppeteer.js <URL>
```
or just add the url in the provided URL entry when running scrape-ape.py from the terminal

Replace `<URL>` with the website you wish to scrape.

## Contributing

Contributions are welcome! Feel free to fork the repo, make improvements, and submit a pull request.

## License

Open for personal and commercial use under the terms in the LICENSE file.

## Acknowledgments

- Thanks to the creators of BeautifulSoup, Selenium, and Puppeteer.
