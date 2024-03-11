const puppeteer = require("puppeteer");
const fs = require("fs").promises;
const path = require("path");

async function scrapeAPE(url) {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();

  const baseDir = path.join(__dirname, "Puppet-pages");

  try {
    await fs.mkdir(baseDir, { recursive: true });

    await page.goto(url, { waitUntil: "networkidle0" });

    const htmlContent = await page.evaluate(
      () => document.documentElement.outerHTML
    );

    await fs.writeFile(path.join(baseDir, "page.html"), htmlContent);

    const cssLinks = await page.$$eval('link[rel="stylesheet"]', (links) =>
      links.map((link) => link.href)
    );
    const jsScripts = await page.$$eval("script[src]", (scripts) =>
      scripts.map((script) => script.src)
    );

    for (const [index, cssLink] of cssLinks.entries()) {
      const response = await page.goto(cssLink);
      const cssContent = await response.text();
      await fs.writeFile(path.join(baseDir, `style${index}.css`), cssContent);
      await page.goBack();
    }

    for (const [index, jsLink] of jsScripts.entries()) {
      const response = await page.goto(jsLink);
      const jsContent = await response.text();
      await fs.writeFile(path.join(baseDir, `script${index}.js`), jsContent);
      await page.goBack();
    }
  } catch (error) {
    console.error("Error occurred during scraping:", error);
  } finally {
    await browser.close();
  }
}

const targetUrl = process.argv[2];

if (targetUrl) {
  scrapeAPE(targetUrl);
} else {
  console.error("No URL provided");
  process.exit(1);
}
