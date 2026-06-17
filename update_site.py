import os
import glob

html_files = glob.glob('d:/rk/*.html')
for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace Title
    content = content.replace('<title>Reincon - Construction HTML5 Template</title>', '<title>RK - Construction HTML5 Template</title>')
    
    # Replace Favicon
    content = content.replace('href="images/favicon.png"', 'href="images/rklatestfooter.png"')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print('Updated title and favicon in all HTML files.')
