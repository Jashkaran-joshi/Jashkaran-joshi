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

# 5. Profile Views
try:
    url = 'https://komarev.com/ghpvc/?username=Jashkaran-joshi'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla'})
    komarev_svg = urllib.request.urlopen(req).read().decode('utf-8')
    
    # Extract the view count
    match = re.search(r'<text[^>]*y="14">(\d+)</text>', komarev_svg)
    if match:
        views = match.group(1)
        # Generate custom premium SVG for views
        width = 160
        custom_svg = f'''<svg width="{width}" height="40" viewBox="0 0 {width} 40" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad_views" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0F766E" />
      <stop offset="100%" stop-color="#042F2E" />
    </linearGradient>
    
  </defs>
  <rect width="{width}" height="40" rx="8" fill="url(#grad_views)" />
  
  <g transform="translate(12, 10)">
    <path d="M12 4.5C7 4.5 2.73 7.61 1 12c1.73 4.39 6 7.5 11 7.5s9.27-3.11 11-7.5c-1.73-4.39-6-7.5-11-7.5zM12 17c-2.76 0-5-2.24-5-5s2.24-5 5-5 5 2.24 5 5-2.24 5-5 5zm0-8c-1.66 0-3 1.34-3 3s1.34 3 3 3 3-1.34 3-3-1.34-3-3-3z" fill="#ffffff" transform="scale(0.833)" />
  </g>
  
  <text x="40" y="25" fill="#ffffff" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="800" letter-spacing="1.2">VIEWS: {views}</text>
</svg>'''
        with open('assets/views.svg', 'w', encoding='utf-8') as f:
            f.write(custom_svg)
        print(f'Generated assets/views.svg with {views} views')
    else:
        print('Error extracting views from komarev SVG')
except Exception as e:
    print('Error views:', e)
