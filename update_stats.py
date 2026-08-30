import urllib.request
import re
import os

os.makedirs('assets', exist_ok=True)

svgs = {}

# 1. Profile Details
try:
    url = 'https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=Jashkaran-joshi&theme=tokyonight'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla'})
    svg = urllib.request.urlopen(req).read().decode('utf-8')
    svg = svg.replace('#1a1b27', '#0D1117')
    svg = re.sub(r'<rect[^>]*class="header"[^>]*fill="[^"]*"', r'<rect class="header" fill="transparent"', svg)
    svg = re.sub(r'<rect[^>]*rx="4.5"[^>]*fill="[^"]*"', r'<rect rx="4.5" fill="#0D1117"', svg)
    svg = re.sub(r'<g transform="translate\([^)]+\)">\s*<svg[^>]*class="icon"[^>]*>.*?</svg>\s*<text[^>]*>.*?@.*?</text>\s*</g>', '', svg, flags=re.DOTALL)
    svg = re.sub(r'<filter.*?</filter>', '', svg, flags=re.DOTALL)
    svg = re.sub(r' filter=.url\(\#shadow[^)]*\).', '', svg)
    svgs['profile'] = re.sub(r'<\?xml[^>]+\?>', '', svg)
except Exception as e: print('Error profile-details:', e)

# 2. Repos Per Language
try:
    url = 'https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=Jashkaran-joshi&theme=tokyonight'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla'})
    svg = urllib.request.urlopen(req).read().decode('utf-8')
    svg = svg.replace('#1a1b27', '#0D1117')
    svg = re.sub(r'<rect[^>]*class="header"[^>]*fill="[^"]*"', r'<rect class="header" fill="transparent"', svg)
    svg = re.sub(r'<rect[^>]*rx="4.5"[^>]*fill="[^"]*"', r'<rect rx="4.5" fill="#0D1117"', svg)
    svg = re.sub(r'<filter.*?</filter>', '', svg, flags=re.DOTALL)
    svg = re.sub(r' filter=.url\(\#shadow[^)]*\).', '', svg)
    svgs['repos'] = re.sub(r'<\?xml[^>]+\?>', '', svg)
except Exception as e: print('Error repos-per-language:', e)

# 3. Most Commit Language
try:
    url = 'https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=Jashkaran-joshi&theme=tokyonight'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla'})
    svg = urllib.request.urlopen(req).read().decode('utf-8')
    svg = svg.replace('#1a1b27', '#0D1117')
    svg = re.sub(r'<rect[^>]*class="header"[^>]*fill="[^"]*"', r'<rect class="header" fill="transparent"', svg)
    svg = re.sub(r'<rect[^>]*rx="4.5"[^>]*fill="[^"]*"', r'<rect rx="4.5" fill="#0D1117"', svg)
    svg = re.sub(r'<filter.*?</filter>', '', svg, flags=re.DOTALL)
    svg = re.sub(r' filter=.url\(\#shadow[^)]*\).', '', svg)
    svgs['commits'] = re.sub(r'<\?xml[^>]+\?>', '', svg)
except Exception as e: print('Error most-commit-language:', e)

# 4. Streak Stats
try:
    url = 'https://github-readme-streak-stats.herokuapp.com/?user=Jashkaran-joshi&theme=tokyonight&hide_border=true&background=0D1117'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla'})
    svg = urllib.request.urlopen(req).read().decode('utf-8')
    svg = re.sub(r'<filter.*?</filter>', '', svg, flags=re.DOTALL)
    svg = re.sub(r' filter=.url\(\#shadow[^)]*\).', '', svg)
    svgs['streak'] = re.sub(r'<\?xml[^>]+\?>', '', svg)
except Exception as e: print('Error streak:', e)

# 5. Profile Views (Still save standalone SVG as it's separate)
try:
    url = 'https://komarev.com/ghpvc/?username=Jashkaran-joshi'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla'})
    komarev_svg = urllib.request.urlopen(req).read().decode('utf-8')
    match = re.search(r'<text[^>]*y="14">(\d+)</text>', komarev_svg)
    if match:
        views = match.group(1)
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
except Exception as e: print('Error views:', e)

# 6. Combine all into one Master SVG
try:
    master_svg = f'''<svg width="960" height="740" viewBox="0 0 960 740" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect x="2" y="2" width="956" height="736" rx="12" fill="#161B22" />
  <rect x="2" y="2" width="956" height="736" rx="12" stroke="#30363D" stroke-width="1" />
  <text x="30" y="45" fill="#E6EDF3" font-family="system-ui, sans-serif" font-size="22" font-weight="700">📊 GitHub Activity</text>
  <line x1="30" y1="65" x2="930" y2="65" stroke="#30363D" stroke-width="1" />
  <g transform="translate(232, 70)">
{svgs.get('streak', '')}
  </g>
  <g transform="translate(130, 285)">
{svgs.get('profile', '')}
  </g>
  <g transform="translate(130, 505)">
{svgs.get('repos', '')}
  </g>
  <g transform="translate(490, 505)">
{svgs.get('commits', '')}
  </g>
</svg>'''
    with open('assets/github_activity.svg', 'w', encoding='utf-8') as f:
        f.write(master_svg)
    print('Generated assets/github_activity.svg')
except Exception as e:
    print('Error generating master SVG:', e)
