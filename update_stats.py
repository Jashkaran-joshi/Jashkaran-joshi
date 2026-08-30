import urllib.request
import re
import os

os.makedirs('assets', exist_ok=True)

# 1. Profile Details
try:
    url = 'https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=Jashkaran-joshi&theme=tokyonight'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla'})
    svg = urllib.request.urlopen(req).read().decode('utf-8')
    
    # Change background to 0D1117 (GitHub Dark theme background)
    svg = svg.replace('#1a1b27', '#0D1117')
    # Make background rect transparent to match exactly
    svg = re.sub(r'<rect[^>]*class="header"[^>]*fill="[^"]*"', r'<rect class="header" fill="transparent"', svg)
    svg = re.sub(r'<rect[^>]*rx="4.5"[^>]*fill="[^"]*"', r'<rect rx="4.5" fill="#0D1117"', svg)
    
    # Remove email for privacy
    svg = re.sub(r'<g transform="translate\([^)]+\)">\s*<svg[^>]*class="icon"[^>]*>.*?</svg>\s*<text[^>]*>.*?@.*?</text>\s*</g>', '', svg, flags=re.DOTALL)
    
    with open('assets/profile-details.svg', 'w', encoding='utf-8') as f:
        f.write(svg)
    print('Generated assets/profile-details.svg')
except Exception as e:
    print('Error profile-details:', e)

# 2. Repos Per Language
try:
    url = 'https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=Jashkaran-joshi&theme=tokyonight'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla'})
    svg = urllib.request.urlopen(req).read().decode('utf-8')
    svg = svg.replace('#1a1b27', '#0D1117')
    svg = re.sub(r'<rect[^>]*class="header"[^>]*fill="[^"]*"', r'<rect class="header" fill="transparent"', svg)
    svg = re.sub(r'<rect[^>]*rx="4.5"[^>]*fill="[^"]*"', r'<rect rx="4.5" fill="#0D1117"', svg)
    with open('assets/repos-per-language.svg', 'w', encoding='utf-8') as f:
        f.write(svg)
    print('Generated assets/repos-per-language.svg')
except Exception as e:
    print('Error repos-per-language:', e)

# 3. Most Commit Language
try:
    url = 'https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=Jashkaran-joshi&theme=tokyonight'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla'})
    svg = urllib.request.urlopen(req).read().decode('utf-8')
    svg = svg.replace('#1a1b27', '#0D1117')
    svg = re.sub(r'<rect[^>]*class="header"[^>]*fill="[^"]*"', r'<rect class="header" fill="transparent"', svg)
    svg = re.sub(r'<rect[^>]*rx="4.5"[^>]*fill="[^"]*"', r'<rect rx="4.5" fill="#0D1117"', svg)
    with open('assets/most-commit-language.svg', 'w', encoding='utf-8') as f:
        f.write(svg)
    print('Generated assets/most-commit-language.svg')
except Exception as e:
    print('Error most-commit-language:', e)

# 4. Streak Stats
try:
    url = 'https://github-readme-streak-stats.herokuapp.com/?user=Jashkaran-joshi&theme=tokyonight&hide_border=true&background=0D1117'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla'})
    svg = urllib.request.urlopen(req).read().decode('utf-8')
    with open('assets/streak.svg', 'w', encoding='utf-8') as f:
        f.write(svg)
    print('Generated assets/streak.svg')
except Exception as e:
    print('Error streak:', e)
