import os
import re

dir_path = r'd:\rk'
for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file.endswith('.html'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Replace logo-white.svg with rklogo.png
            content = content.replace('images/logo-white.svg', 'images/rklogo.png')
            
            # Replace themeht.com references
            # E.g. <title>Page not found - themeht.com</title> -> <title>RK Constructions</title>
            content = re.sub(r'<title>.*?- themeht\.com.*?</title>', '<title>RK Constructions</title>', content, flags=re.IGNORECASE)
            
            # Remove themeht.com from <meta name='author'>
            content = re.sub(r'<meta name=\'author\' content=\'www\.themeht\.com\' />', '<meta name=" author\ content=\RK Constructions\ />', content, flags=re.IGNORECASE)
 content = re.sub(r'<meta name=\author\ content=\www\.themeht\.com\ />', '<meta name=\author\ content=\RK Constructions\ />', content, flags=re.IGNORECASE)
 
 with open(file_path, 'w', encoding='utf-8') as f:
 f.write(content)
print('Done!')
