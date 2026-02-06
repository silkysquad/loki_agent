#!/usr/bin/env node

/**
 * Simple browser automation using Puppeteer
 * Usage: node browser.js <command> <url> [options]
 * 
 * Commands:
 *   goto <url>           Navigate to URL
 *   screenshot <url>     Take screenshot
 *   text <url>          Get page text content
 *   html <url>          Get page HTML
 */

const puppeteer = require('puppeteer');

async function run() {
  const args = process.argv.slice(2);
  const command = args[0] || 'goto';
  const url = args[1] || 'https://www.clickclickclaw.com/';
  
  console.log(`🚀 Launching browser...`);
  console.log(`   Command: ${command}`);
  console.log(`   URL: ${url}\n`);
  
  const browser = await puppeteer.launch({
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  
  const page = await browser.newPage();
  
  try {
    await page.goto(url, { waitUntil: 'networkidle2', timeout: 30000 });
    
    switch (command) {
      case 'screenshot':
        await page.screenshot({ path: '/tmp/screenshot.png', fullPage: true });
        console.log('📸 Screenshot saved to /tmp/screenshot.png');
        break;
        
      case 'text':
        const text = await page.evaluate(() => document.body.innerText);
        console.log('📄 Page text:\n');
        console.log(text);
        break;
        
      case 'html':
        const html = await page.evaluate(() => document.documentElement.outerHTML);
        console.log('🔍 Page HTML:\n');
        console.log(html.substring(0, 5000));
        break;
        
      case 'goto':
      default:
        const title = await page.title();
        console.log(`✅ Loaded: ${title}`);
        console.log(`   URL: ${page.url()}`);
        break;
    }
  } catch (error) {
    console.log(`❌ Error: ${error.message}`);
  }
  
  await browser.close();
}

run().catch(console.error);
