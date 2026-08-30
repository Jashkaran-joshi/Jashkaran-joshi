import urllib.request
import re
import os
import hashlib

os.makedirs('assets', exist_ok=True)

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

# Find all img tags with http src
img_src_pattern = re.compile(r'src="(https?://[^"]+)"')
urls = img_src_pattern.findall(readme)

for url in urls:
    # Skip if it's already an asset (it shouldn't be matched by http anyway)
    # Give a meaningful name based on the URL
    if 'skillicons.dev' in url:
        match = re.search(r'i=([a-zA-Z0-9_,]+)', url)
        if match:
            slug = f"skillicon_{match.group(1).replace(',', '_')}"
        else:
            slug = "skillicon_" + hashlib.md5(url.encode()).hexdigest()[:6]
    elif 'shields.io' in url:
        match = re.search(r'badge/([a-zA-Z0-9_\.\-]+)', url)
        if match:
            slug = f"shield_{match.group(1).replace('-', '_')}"
        else:
            slug = "shield_" + hashlib.md5(url.encode()).hexdigest()[:6]
    elif 'capsule-render' in url:
        slug = "capsule_footer"
    else:
        slug = "img_" + hashlib.md5(url.encode()).hexdigest()[:6]
        
    filename = f"assets/{slug}.svg"
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla'})
        svg = urllib.request.urlopen(req).read().decode('utf-8')
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(svg)
            
        print(f"Downloaded {filename}")
        readme = readme.replace(url, filename)
    except Exception as e:
        print(f"Failed to download {url}: {e}")

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme)

print("README.md updated with local assets.")
