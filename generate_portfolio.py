import os

os.makedirs('assets', exist_ok=True)

projects = [
    {
        'id': 'titanax',
        'title': '🤖 TitanAx Labs',
        'subtitle': 'AI-Driven Secure Code Generation',
        'lines': [
            'An AI-powered platform that generates code with a security',
            'linting layer — catching secret exposure and injection patterns',
            'before they ship.'
        ],
        'tags': [('React', '#61DAFB'), ('Node.js', '#5FA04E'), ('AI', '#FFFFFF')]
    },
    {
        'id': 'adoptnest',
        'title': '🐾 AdoptNest',
        'subtitle': 'Secure Pet Adoption Marketplace',
        'lines': [
            'A full-stack adoption platform with identity management built',
            'around JWT refresh-token rotation and role-based access',
            'control.'
        ],
        'tags': [('React', '#61DAFB'), ('Express', '#FFFFFF'), ('MongoDB', '#47A248')]
    },
    {
        'id': 'snipsnap',
        'title': '🔐 SnipSnap',
        'subtitle': 'Encrypted Code Snippet Manager',
        'lines': [
            'A developer tool that protects stored snippets with field-level',
            'AES-256 encryption — combining productivity with security-',
            'first design.'
        ],
        'tags': [('React', '#61DAFB'), ('Node.js', '#5FA04E'), ('AES-256', '#FFD700')]
    },
    {
        'id': 'security',
        'title': '🛡️ Security Philosophy',
        'subtitle': '',
        'lines': [
            'Security should be part of the architecture, not an',
            'afterthought.',
            '',
            'Every project I build has security baked in — from',
            'authentication flows to encrypted data at rest.'
        ],
        'tags': [('→ See my full portfolio', '#58A6FF')]
    }
]

def generate_svg(proj):
    width = 460
    height = 220
    
    # Background and border
    svg = f'''<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <linearGradient id="border_grad_{proj['id']}" x1="0" y1="0" x2="1" y2="1">
            <stop offset="0%" stop-color="#58A6FF" stop-opacity="0.5"/>
            <stop offset="100%" stop-color="#1F6FEB" stop-opacity="0.1"/>
        </linearGradient>
    </defs>
    
    <!-- Background -->
    <rect x="2" y="2" width="{width-4}" height="{height-4}" rx="12" fill="#161B22" />
    <!-- Gradient Border -->
    <rect x="2" y="2" width="{width-4}" height="{height-4}" rx="12" stroke="url(#border_grad_{proj['id']})" stroke-width="1.5" />
    '''
    
    # Title
    svg += f'''
    <text x="24" y="45" fill="#E6EDF3" font-family="system-ui, -apple-system, sans-serif" font-size="22" font-weight="700">{proj['title']}</text>
    '''
    
    # Subtitle
    if proj['subtitle']:
        svg += f'''
        <text x="24" y="70" fill="#8B949E" font-family="system-ui, -apple-system, sans-serif" font-size="14" font-weight="600">{proj['subtitle']}</text>
        '''
        y_offset = 105
    else:
        y_offset = 85
        
    # Lines
    for i, line in enumerate(proj['lines']):
        if line:
            font_style = "font-weight='500'" if proj['id'] == 'security' and i < 2 else "font-weight='400'"
            color = "#C9D1D9" if proj['id'] == 'security' and i < 2 else "#8B949E"
            svg += f'''
            <text x="24" y="{y_offset + i*22}" fill="{color}" font-family="system-ui, -apple-system, sans-serif" font-size="14" {font_style}>{line}</text>
            '''
            
    # Tags
    tag_x = 24
    for tag_name, tag_color in proj['tags']:
        tag_width = len(tag_name) * 8 + 24
        if proj['id'] == 'security':
            tag_width = len(tag_name) * 8 + 30
            # Just render as text link style for security
            svg += f'''
            <text x="24" y="190" fill="{tag_color}" font-family="system-ui, -apple-system, sans-serif" font-size="15" font-weight="600">{tag_name}</text>
            '''
        else:
            svg += f'''
            <rect x="{tag_x}" y="170" width="{tag_width}" height="28" rx="14" fill="#21262D" stroke="#30363D" stroke-width="1" />
            <circle cx="{tag_x + 12}" cy="184" r="4" fill="{tag_color}" />
            <text x="{tag_x + 22}" y="189" fill="#C9D1D9" font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="500">{tag_name}</text>
            '''
            tag_x += tag_width + 12
            
    svg += '</svg>'
    return svg

for proj in projects:
    with open(f"assets/project_{proj['id']}.svg", "w", encoding="utf-8") as f:
        f.write(generate_svg(proj))
    print(f"Generated assets/project_{proj['id']}.svg")
