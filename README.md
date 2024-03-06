# Scrape-APE

Scrape-APE is an innovative web scraping application designed to efficiently extract information from various types of websites and save the data for further analysis or use. Built using Python, this tool leverages the powerful libraries BeautifulSoup and Selenium to navigate and parse web pages, making it capable of handling both static and dynamic content. The application features a user-friendly graphical interface, making web scraping accessible to users with varying levels of technical expertise.

## Features

- Support for a wide range of website types including static, dynamic, CMS-based, e-commerce, and more.
- User-friendly graphical interface for easy operation.
- Customizable scraping tasks to target specific website types or content.
- Ability to save scraped content in a structured format for easy access and analysis.

## Getting Started

### Prerequisites

Before you can run Scrape-APE, you'll need to have Python installed on your system (Python 3.6 or later is recommended). Additionally, you'll need the following Python packages:

- BeautifulSoup4
- Selenium

### Installation

#### Step 1: Clone the Repository

First, clone the Scrape-APE repository to your local machine using the following command in your terminal:

```sh
git clone https://github.com/Suffix30/Scrape-APE.git
cd scrape-ape
```

#### Step 2: Install Required Python Packages

Install BeautifulSoup4 and Selenium directly using pip. Open the terminal in VS Code (`Ctrl+``) and enter the following commands:

```sh
pip install beautifulsoup4
pip install selenium
```

These commands install the necessary Python libraries to run Scrape-APE.

#### Step 3: Set Up WebDriver

For web scraping dynamic websites that require JavaScript execution, Selenium needs a WebDriver. Depending on your preferred web browser, download and set up the appropriate WebDriver:

- **Chrome:** Download ChromeDriver from [ChromeDriver - WebDriver for Chrome](https://sites.google.com/a/chromium.org/chromedriver/). Ensure it's placed in a directory included in your system's PATH, or specify its location directly in your script.
  
- **Firefox:** Download GeckoDriver from [GitHub - mozilla/geckodriver](https://github.com/mozilla/geckodriver/releases). Similar to ChromeDriver, make sure it's accessible via your system's PATH or referenced directly in your code.

- **Others:** For other browsers like Edge or Safari, please refer to their respective documentation for WebDriver installation instructions.

### Running Scrape-APE in VS Code

After installing the required packages and setting up WebDriver, you're ready to run Scrape-APE. Open the project folder in VS Code, then use the terminal (`Ctrl+``) to execute the script:

```sh
python scrape-ape.py
```

This command launches the Scrape-APE application, providing you with a GUI to start your web scraping tasks.

## Contributing

Contributions to Scrape-APE are welcome! Feel free to fork the repository, improve the existing codebase or add new features, and submit a pull request. Whether it's fixing bugs, adding documentation, or suggesting new functionality, your contributions are greatly appreciated.

## License

This project is open to the public for personal and commercial use. You can clone, modify, and distribute the software in accordance with the terms specified in the LICENSE file.

## Acknowledgments

- Special thanks to the developers of BeautifulSoup and Selenium for providing the essential tools for web scraping.
