import re

with open('index.css', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('--primary: #000000;            /* Ray-Ban black */', '--primary: #000000;            /* E&M Black */')
content = content.replace('--accent: #E60000;             /* Ray-Ban iconic red */', '--accent: #222222;             /* E&M Accent */')
content = content.replace('--accent-dark: #B30000;', '--accent-dark: #000000;')
content = content.replace('--rayban-red-gradient: linear-gradient(135deg, #E60000 0%, #B30000 100%);', '--brand-gradient: linear-gradient(135deg, #333333 0%, #000000 100%);')
content = content.replace('var(--rayban-red-gradient)', 'var(--brand-gradient)')

# Remove top-promo and reseller-bar CSS since they are gone
content = re.sub(r'/\* Header & Promo \*/.*?/\* Navigation \*/', '/* Header & Navigation */\n', content, flags=re.DOTALL)

with open('index.css', 'w', encoding='utf-8') as f:
    f.write(content)

