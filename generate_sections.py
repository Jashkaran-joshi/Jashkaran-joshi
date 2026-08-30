import os
import urllib.request
import re

os.makedirs('assets', exist_ok=True)

def fetch_icon_path(icon_name):
    try:
        url = f"https://cdn.jsdelivr.net/npm/simple-icons@v11/icons/{icon_name}.svg"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla'})
        svg_content = urllib.request.urlopen(req).read().decode('utf-8')
        match = re.search(r'<path[^>]+d="([^"]+)"', svg_content)
        return match.group(1) if match else ""
    except:
        return ""

# Common template
def get_base_svg(width, height, shadow_id, border_color="#30363D"):
    return f'''
    <defs>
        <filter id="{shadow_id}" x="-5%" y="-5%" width="110%" height="110%">
            <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.3"/>
        </filter>
    </defs>
    <rect x="2" y="2" width="{width-4}" height="{height-4}" rx="12" fill="#161B22" filter="url(#{shadow_id})" />
    <rect x="2" y="2" width="{width-4}" height="{height-4}" rx="12" stroke="{border_color}" stroke-width="1" />
    '''

def create_about():
    width = 960
    height = 200
    svg = f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none" xmlns="http://www.w3.org/2000/svg">'
    svg += get_base_svg(width, height, "shadow_about")
    
    # Content
    svg += '''
    <text x="30" y="45" fill="#E6EDF3" font-family="system-ui, sans-serif" font-size="22" font-weight="700">⚡ About</text>
    
    <text x="30" y="85" fill="#C9D1D9" font-family="system-ui, sans-serif" font-size="16" font-weight="400">I build applications that are <tspan font-weight="600" fill="#58A6FF">functional by design</tspan> and <tspan font-weight="600" fill="#58A6FF">secure by default</tspan>.</text>
    
    <text x="30" y="115" fill="#C9D1D9" font-family="system-ui, sans-serif" font-size="16" font-weight="400">My work sits at the intersection of full-stack engineering and offensive security — I think beyond</text>
    <text x="30" y="140" fill="#C9D1D9" font-family="system-ui, sans-serif" font-size="16" font-weight="400">implementation to consider how systems can fail, where they can be attacked, and how to reduce risk.</text>
    
    <text x="30" y="175" fill="#8B949E" font-family="system-ui, sans-serif" font-size="15" font-weight="500">Focusing on <tspan fill="#E6EDF3">DevSecOps</tspan>, <tspan fill="#E6EDF3">application security</tspan>, and <tspan fill="#E6EDF3">data-driven automation</tspan>.</text>
    '''
    svg += '</svg>'
    with open('assets/about.svg', 'w', encoding='utf-8') as f:
        f.write(svg)

def create_tech_stack():
    width = 960
    height = 240
    svg = f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none" xmlns="http://www.w3.org/2000/svg">'
    svg += get_base_svg(width, height, "shadow_tech")
    
    svg += '<text x="30" y="45" fill="#E6EDF3" font-family="system-ui, sans-serif" font-size="22" font-weight="700">🛠 Tech Stack</text>'
    
    columns = [
        {"title": "Frontend", "x": 30, "icons": [("react", "#61DAFB"), ("nextdotjs", "#FFFFFF"), ("javascript", "#F7DF1E"), ("tailwindcss", "#06B6D4"), ("html5", "#E34F26"), ("css3", "#1572B6")]},
        {"title": "Backend", "x": 270, "icons": [("nodedotjs", "#339933"), ("express", "#FFFFFF"), ("python", "#3776AB"), ("django", "#092E20"), ("flask", "#FFFFFF"), ("cplusplus", "#00599C")]},
        {"title": "Data &amp; Infra", "x": 510, "icons": [("mongodb", "#47A248"), ("postgresql", "#4169E1"), ("docker", "#2496ED"), ("linux", "#FCC624"), ("git", "#F05032"), ("postman", "#FF6C37")]},
        {"title": "Security", "x": 750, "icons": [("kalilinux", "#557C94"), ("wireshark", "#1679A7"), ("metasploit", "#2596CD")]}
    ]
    
    for col in columns:
        svg += f'<text x="{col["x"]}" y="90" fill="#8B949E" font-family="system-ui, sans-serif" font-size="16" font-weight="600">{col["title"]}</text>'
        
        icon_x = col["x"]
        icon_y = 120
        for i, (icon_name, color) in enumerate(col["icons"]):
            path = fetch_icon_path(icon_name)
            if i == 3: # new row
                icon_x = col["x"]
                icon_y += 50
            if path:
                # scale to 32x32 from 24x24 simpleicons viewBox
                svg += f'''
                <g transform="translate({icon_x}, {icon_y}) scale(1.33)">
                    <rect width="24" height="24" rx="4" fill="#242938" />
                    <path d="{path}" fill="{color}" transform="scale(0.7) translate(5, 5)" />
                </g>
                '''
            icon_x += 50
            
    svg += '</svg>'
    with open('assets/tech_stack.svg', 'w', encoding='utf-8') as f:
        f.write(svg)

def create_certs():
    width = 960
    height = 200
    svg = f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none" xmlns="http://www.w3.org/2000/svg">'
    svg += get_base_svg(width, height, "shadow_certs")
    
    svg += '<text x="30" y="45" fill="#E6EDF3" font-family="system-ui, sans-serif" font-size="22" font-weight="700">🏆 Certifications</text>'
    
    # Headers
    svg += '''
    <text x="30" y="85" fill="#8B949E" font-family="system-ui, sans-serif" font-size="14" font-weight="600">CERTIFICATION</text>
    <text x="500" y="85" fill="#8B949E" font-family="system-ui, sans-serif" font-size="14" font-weight="600">ISSUER</text>
    <text x="800" y="85" fill="#8B949E" font-family="system-ui, sans-serif" font-size="14" font-weight="600">CREDENTIAL</text>
    <line x1="30" y1="100" x2="930" y2="100" stroke="#30363D" stroke-width="1" />
    '''
    
    rows = [
        ("CEH Master — Certified Ethical Hacker", "EC-Council", "Credly"),
        ("CND — Certified Network Defender", "EC-Council", "Credly"),
        ("Cybersecurity &amp; Threat Intelligence", "Deloitte", "—")
    ]
    
    y = 130
    for title, issuer, cred in rows:
        svg += f'''
        <text x="30" y="{y}" fill="#E6EDF3" font-family="system-ui, sans-serif" font-size="16" font-weight="500">{title}</text>
        <text x="500" y="{y}" fill="#C9D1D9" font-family="system-ui, sans-serif" font-size="15" font-weight="400">{issuer}</text>
        <text x="800" y="{y}" fill="#58A6FF" font-family="system-ui, sans-serif" font-size="15" font-weight="500">{cred}</text>
        '''
        y += 35
        
    svg += '</svg>'
    with open('assets/certifications.svg', 'w', encoding='utf-8') as f:
        f.write(svg)

def create_exploring():
    width = 960
    height = 200
    svg = f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none" xmlns="http://www.w3.org/2000/svg">'
    svg += get_base_svg(width, height, "shadow_exploring")
    
    svg += '<text x="30" y="45" fill="#E6EDF3" font-family="system-ui, sans-serif" font-size="22" font-weight="700">🔭 Currently Exploring</text>'
    
    items = [
        ("🔧", "DevSecOps pipelines &amp; CI/CD security gates"),
        ("🛡️", "OWASP Top 10 — deep dives and mitigations"),
        ("📊", "Data analytics &amp; business intelligence automation"),
        ("🚩", "CTF challenges on TryHackMe")
    ]
    
    y = 85
    for emoji, text in items:
        svg += f'''
        <text x="30" y="{y}" font-family="system-ui, sans-serif" font-size="18">{emoji}</text>
        <text x="70" y="{y}" fill="#C9D1D9" font-family="system-ui, sans-serif" font-size="16" font-weight="500">{text}</text>
        '''
        y += 30
        
    svg += '</svg>'
    with open('assets/exploring.svg', 'w', encoding='utf-8') as f:
        f.write(svg)

create_about()
print("Generated about.svg")
create_tech_stack()
print("Generated tech_stack.svg")
create_certs()
print("Generated certifications.svg")
create_exploring()
print("Generated exploring.svg")
