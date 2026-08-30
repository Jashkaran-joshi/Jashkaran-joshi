import urllib.request
import json
import os
import re

os.makedirs('assets', exist_ok=True)

icons = {
    'burpsuite': 'FF6633',
    'metasploit': '2596CD',
    'wireshark': '1679A7',
    'gnometerminal': '0E83CD'
}

for icon, color in icons.items():
    try:
        url = f'https://cdn.simpleicons.org/{icon}/{color}'
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla'})
        svg_content = urllib.request.urlopen(req).read().decode('utf-8')
        
        path_match = re.search(r'<path[^>]+d="([^"]+)"', svg_content)
        if path_match:
            path_d = path_match.group(1)
            
            custom_svg = f'''<svg width="256" height="256" viewBox="0 0 256 256" fill="none" xmlns="http://www.w3.org/2000/svg">
<rect width="256" height="256" rx="60" fill="#242938"/>
<g transform="scale(7.5) translate(5.06, 5.06)">
  <path d="{path_d}" fill="#{color}"/>
</g>
</svg>'''
            
            with open(f'assets/{icon}.svg', 'w', encoding='utf-8') as f:
                f.write(custom_svg)
            print(f'Generated assets/{icon}.svg')
        else:
            print(f'No path found for {icon}')
    except Exception as e:
        print(f'Error for {icon}: {e}')
