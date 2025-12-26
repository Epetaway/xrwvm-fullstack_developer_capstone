const { chromium, firefox, webkit } = require('playwright');
const path = require('path');

(async () => {
  const base = 'http://127.0.0.1:8000';
  const outDir = path.join(__dirname, '../server/artifacts');

  const browserName = process.env.BROWSER || 'webkit';
  const browserType = { chromium, firefox, webkit }[browserName] || webkit;
  const headless = process.env.HEADLESS === 'false' ? false : true;

  // Prefer WebKit on macOS to avoid Chromium crashes on some machines.
  const browser = await browserType.launch({ headless });
  const page = await browser.newPage({ viewport: { width: 1366, height: 768 } });

  // Q16: dealers before login
  await page.goto(`${base}/dealers/`, { waitUntil: 'networkidle' });
  await page.waitForTimeout(1500);
  await page.screenshot({ path: path.join(outDir, 'get_dealers.png'), fullPage: true });

  // Q18: dealers by state (Kansas)
  await page.goto(`${base}/dealers/`, { waitUntil: 'networkidle' });
  // Try selecting Kansas in a <select>. Fallback: click option by text.
  const select = await page.$('select');
  if (select) {
    await select.selectOption({ label: 'Kansas' }).catch(() => {});
    await page.waitForTimeout(1200);
  }
  await page.screenshot({ path: path.join(outDir, 'dealersbystate.png'), fullPage: true });

  // Q25/Q27 (logged-in views). Login first.
  await page.goto(`${base}/login/`, { waitUntil: 'networkidle' });
  await page.waitForSelector('input[name="username"]');
  await page.fill('input[name="username"]', 'admin');
  await page.fill('input[name="psw"]', 'admin123');
  await page.click('input[type="submit"]').catch(() => {});
  await page.waitForTimeout(1500);

  // Logged-in dealers page
  await page.goto(`${base}/dealers/`, { waitUntil: 'networkidle' });
  await page.waitForTimeout(1200);
  await page.screenshot({ path: path.join(outDir, 'deployed_loggedin.png'), fullPage: true });

  // Dealer detail with reviews (id 29)
  await page.goto(`${base}/dealer/29`, { waitUntil: 'networkidle' });
  await page.waitForTimeout(1200);
  await page.screenshot({ path: path.join(outDir, 'deployed_dealer_detail.png'), fullPage: true });

  // Added review view (same page)
  await page.screenshot({ path: path.join(outDir, 'deployed_add_review.png'), fullPage: true });

  await browser.close();
})();
