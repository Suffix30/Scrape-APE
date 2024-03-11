const puppeteer = require("puppeteer");
const fs = require("fs").promises;
const path = require("path");

async function scrapeAPE(url) {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();

  const baseDir = path.join(__dirname, "Puppet-pages");
  const htmlDir = path.join(baseDir, "HTML");
  const cssDir = path.join(baseDir, "CSS");
  const jsDir = path.join(baseDir, "JS");

  try {
    await fs.mkdir(baseDir, { recursive: true });
    await fs.mkdir(htmlDir, { recursive: true });
    await fs.mkdir(cssDir, { recursive: true });
    await fs.mkdir(jsDir, { recursive: true });

    await page.goto(url, { waitUntil: "networkidle0" });

    const htmlContent = await page.evaluate(
      () => document.documentElement.outerHTML
    );

    await fs.writeFile(path.join(htmlDir, "page.html"), htmlContent);

    const cssLinks = await page.$$eval('link[rel="stylesheet"]', (links) =>
      links.map((link) => link.href)
    );
    const jsScripts = await page.$$eval("script[src]", (scripts) =>
      scripts.map((script) => script.src)
    );

    for (const [index, cssLink] of cssLinks.entries()) {
      const response = await page.goto(cssLink);
      const cssContent = await response.text();
      await fs.writeFile(path.join(cssDir, `style${index}.css`), cssContent);
    }

    for (const [index, jsLink] of jsScripts.entries()) {
      const response = await page.goto(jsLink);
      const jsContent = await response.text();
      await fs.writeFile(path.join(jsDir, `script${index}.js`), jsContent);
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
