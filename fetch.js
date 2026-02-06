#!/usr/bin/env node

/**
 * Web fetcher using curl - simulates browser behavior
 * Usage: node fetch.js <command> <url> [options]
 * 
 * Commands:
 *   fetch <url>          Get page content
 *   text <url>          Get plain text
 *   json <url>          Parse as JSON if possible
 *   post <url> <data>   POST request
 */

const { execSync } = require('child_process');

function curl(url, options = {}) {
  // Build command as array to avoid shell escaping issues
  const args = ['curl', '-s', '-L'];
  
  // User agent without special chars that might cause issues
  args.push('-A', 'Mozilla/5.0');
  
  args.push('--connect-timeout', '10');
  args.push('--max-time', '30');
  
  if (options.post) {
    args.push('-X', 'POST');
    args.push('-d', options.post);
  }
  
  if (options.headers) {
    Object.entries(options.headers).forEach(([k, v]) => {
      args.push('-H', `${k}: ${v}`);
    });
  }
  
  args.push(url);
  
  try {
    return execSync(args.join(' '), { encoding: 'utf8', maxBuffer: 10 * 1024 * 1024 });
  } catch (e) {
    return `Error: ${e.message}`;
  }
}

function extractFormFields(html) {
  const forms = [];
  const formMatch = html.match(/<form[^>]*>/gi) || [];
  
  formMatch.forEach((form, i) => {
    const action = form.match(/action=["']([^"']+)["']/i);
    const method = form.match(/method=["']([^"']+)["']/i);
    const inputs = [];
    
    const inputMatches = html.match(/<input[^>]*>/gi) || [];
    inputMatches.forEach(input => {
      const name = input.match(/name=["']([^"']+)["']/i);
      const type = input.match(/type=["']([^"']+)["']/i);
      const placeholder = input.match(/placeholder=["']([^"']+)["']/i);
      if (name) {
        inputs.push({
          name: name[1],
          type: type ? type[1] : 'text',
          placeholder: placeholder ? placeholder[1] : ''
        });
      }
    });
    
    forms.push({
      index: i,
      action: action ? action[1] : '',
      method: method ? method[1] : 'GET',
      inputs
    });
  });
  
  return forms;
}

async function run() {
  const args = process.argv.slice(2);
  const command = args[0] || 'fetch';
  let url = args[1] || 'https://www.clickclickclaw.com/';
  
  // Fix URL if just domain
  if (!url.startsWith('http') && !url.startsWith('//')) {
    url = 'https://' + url;
  }
  
  console.log(`🌐 Fetching: ${url}`);
  console.log(`   Command: ${command}\n`);
  
  try {
    const content = curl(url);
    
    switch (command) {
      case 'text':
        // Strip HTML tags for text
        const text = content
          .replace(/<script[^>]*>[\s\S]*?<\/script>/gi, '')
          .replace(/<style[^>]*>[\s\S]*?<\/style>/gi, '')
          .replace(/<[^>]+>/g, ' ')
          .replace(/\s+/g, ' ')
          .trim();
        console.log('📄 Page text:\n');
        console.log(text.substring(0, 3000));
        break;
        
      case 'json':
        try {
          const json = JSON.parse(content);
          console.log('📊 JSON response:\n');
          console.log(JSON.stringify(json, null, 2));
        } catch {
          console.log('⚠️ Not valid JSON, showing first 2000 chars:');
          console.log(content.substring(0, 2000));
        }
        break;
        
      case 'forms':
        const forms = extractFormFields(content);
        console.log('📋 Found forms:\n');
        forms.forEach(f => {
          console.log(`Form ${f.index}: ${f.method} ${f.action || '(current page)'}`);
          console.log(`  Inputs: ${f.inputs.map(i => `[${i.type}] ${i.name}`).join(', ')}`);
          console.log();
        });
        break;
        
      case 'fetch':
      default:
        // Show title and meta info
        const titleMatch = content.match(/<title[^>]*>([^<]+)<\/title>/i);
        const descMatch = content.match(/<meta[^>]*description[^>]*content=["']([^"']+)["']/i);
        
        console.log(`✅ Page loaded`);
        console.log(`   Title: ${titleMatch ? titleMatch[1] : 'N/A'}`);
        if (descMatch) {
          console.log(`   Description: ${descMatch[1]}`);
        }
        console.log(`   Size: ${content.length} bytes`);
        console.log(`\n📄 Content preview (first 2000 chars):\n`);
        console.log(content.substring(0, 2000).replace(/</g, '&lt;').replace(/>/g, '&gt;'));
        break;
    }
  } catch (error) {
    console.log(`❌ Error: ${error.message}`);
  }
}

run();
