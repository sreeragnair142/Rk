import os
import glob

html_files = glob.glob('d:/rk/*.html')
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update description meta tag
    content = content.replace('<meta name="description" content="HTML5 Template" />', '<meta name="description" content="RK - Premium Construction & Building Services" />')
    
    # 2. Add Open Graph tags right below description if they don't exist
    if '<meta property="og:title"' not in content:
        og_tags = """
<meta property="og:title" content="RK - Construction & Building Services" />
<meta property="og:description" content="Premium Construction & Building Services" />
<meta property="og:type" content="website" />
<meta property="og:image" content="images/rklatestfooter.png" />
"""
        content = content.replace('<meta name="author" content="www.themeht.com" />', '<meta name="author" content="RK Constructions" />\n' + og_tags)
    
    # 3. Replace all remaining occurrences of Reincon in text
    content = content.replace('Reincon With Awesome Colors', 'RK With Awesome Colors')
    content = content.replace('Reincon company', 'RK company')
    content = content.replace('Reincon', 'RK')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print('Updated meta tags and all text references from Reincon to RK.')
