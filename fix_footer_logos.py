files = [
    'service-home-construction.html',
    'service-property-maintenance.html',
    'service-innovation-planning.html',
    'service-design-build.html',
    'service-pre-construction.html',
]

old = '<img class="img-fluid" src="images/logo-white.svg" alt="Logo Img">'
new = '<img class="img-fluid" src="images/rklatestfooter.png" alt="Logo Img" style="width:150px;height:auto">'

for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        content = fh.read()
    if old in content:
        content = content.replace(old, new)
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(content)
        print(f'Updated: {f}')
    else:
        print(f'Already updated or not found: {f}')
