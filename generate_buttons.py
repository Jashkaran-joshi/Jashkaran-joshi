import urllib.request
import re
import os

os.makedirs('assets', exist_ok=True)

buttons = {
    'linkedin': {
        'label': 'LINKEDIN',
        'icon': 'linkedin',
        'color1': '#0A66C2',
        'color2': '#004182',
        'width': 125
    },
    'letsconnect': {
        'label': "LET'S CONNECT",
        'icon': 'linkedin',
        'color1': '#0A66C2',
        'color2': '#004182',
        'width': 155
    }
}

for name, data in buttons.items():
    try:
        url = f"https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/{data['icon']}.svg"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla'})
        svg_content = urllib.request.urlopen(req).read().decode('utf-8')
        path_match = re.search(r'<path[^>]+d="([^"]+)"', svg_content)
        path_d = path_match.group(1) if path_match else ""
        
        svg = f'''<svg width="{data['width']}" height="40" viewBox="0 0 {data['width']} 40" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad_{name}" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{data['color1']}" />
      <stop offset="100%" stop-color="{data['color2']}" />
    </linearGradient>
    
  </defs>
  <rect width="{data['width']}" height="40" rx="8" fill="url(#grad_{name})" />
  
  <g transform="translate(12, 10)">
    <path d="{path_d}" fill="#ffffff" transform="scale(0.833)" />
  </g>
  
  <text x="40" y="25" fill="#ffffff" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="800" letter-spacing="1.2">{data['label']}</text>
</svg>'''
        
        with open(f'assets/{name}.svg', 'w', encoding='utf-8') as f:
            f.write(svg)
        print(f'Generated {name}.svg')
    except Exception as e:
        print(f"Error generating {name}: {e}")
