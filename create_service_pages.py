import re

files_to_create = [
    ('service-building-construction.html', 'Building Construction'),
    ('service-home-construction.html', 'Home Construction'),
    ('service-property-maintenance.html', 'Property Maintenance'),
    ('service-innovation-planning.html', 'Innovation Planning'),
    ('service-design-build.html', 'Design Build'),
    ('service-pre-construction.html', 'Pre-Construction'),
]

with open('service-single.html', 'r', encoding='utf-8') as f:
    content = f.read()

# First update all sidebar links in the template
# Building Construction -> service-building-construction.html etc
link_map = {
    'Building Construction': 'service-building-construction.html',
    'Home Construction': 'service-home-construction.html',
    'Property Maintenance': 'service-property-maintenance.html',
    'Innovation Planning': 'service-innovation-planning.html',
    'Design Build': 'service-design-build.html',
    'Pre-Construction': 'service-pre-construction.html',
}

# Service descriptions/images for each service
service_data = {
    'Building Construction': {
        'icon': 'flaticon-building-1',
        'image': 'images/services/large/01.jpg',
        'heading': 'Quality Construction Management',
        'desc1': 'RK Constructions delivers world-class building construction services backed by four generations of expertise. We understand that each project is unique and requires a tailored approach with precision and dedication.',
        'desc2': 'Our team of architects, engineers, and designers are committed to excellence. We specialize in residential, commercial, and industrial construction projects, providing full-service solutions from groundbreaking to handover.',
    },
    'Home Construction': {
        'icon': 'flaticon-roof',
        'image': 'images/services/large/02.jpg',
        'heading': 'Custom Home Construction',
        'desc1': 'We build homes that are tailored to your vision and lifestyle. From bungalows to multi-story residences, our home construction service ensures superior craftsmanship and timely delivery at every stage.',
        'desc2': 'Our experienced team manages everything from architectural design to finishing touches, ensuring your dream home is delivered with quality materials, skilled labor, and transparent communication throughout.',
    },
    'Property Maintenance': {
        'icon': 'flaticon-plan',
        'image': 'images/services/large/03.jpg',
        'heading': 'Comprehensive Property Maintenance',
        'desc1': 'Keeping your property in peak condition is essential. RK Constructions offers comprehensive property maintenance services for residential and commercial properties, ensuring longevity and value preservation.',
        'desc2': 'From routine inspections to emergency repairs, our certified maintenance professionals are available to handle all your property needs efficiently and with minimal disruption to your daily operations.',
    },
    'Innovation Planning': {
        'icon': 'flaticon-plan',
        'image': 'images/services/large/04.jpg',
        'heading': 'Strategic Innovation Planning',
        'desc1': 'Innovation is at the core of what we do at RK Constructions. Our innovation planning service integrates the latest construction technologies and methodologies to deliver projects that are ahead of their time.',
        'desc2': 'We evaluate new materials, smart construction techniques, and sustainable solutions to optimize your project outcomes. Our planning experts ensure that innovation translates into measurable value and performance.',
    },
    'Design Build': {
        'icon': 'flaticon-roof',
        'image': 'images/services/large/05.jpg',
        'heading': 'Integrated Design Build Services',
        'desc1': 'Our Design-Build approach streamlines the entire project lifecycle by integrating design and construction under one roof. This reduces risk, saves time, and provides a single point of accountability for clients.',
        'desc2': 'From concept to completion, our design-build teams collaborate closely to deliver projects that match your vision while staying within budget and schedule, ensuring a seamless and stress-free experience.',
    },
    'Pre-Construction': {
        'icon': 'flaticon-building-1',
        'image': 'images/services/large/06.jpg',
        'heading': 'Expert Pre-Construction Services',
        'desc1': 'Successful projects start with thorough pre-construction planning. Our pre-construction services include feasibility studies, budgeting, scheduling, and permit management to set your project up for success.',
        'desc2': 'We identify potential challenges before they become costly problems. Our proactive pre-construction process ensures that all stakeholders are aligned, risks are mitigated, and the project is ready to proceed efficiently.',
    },
}

for filename, title in files_to_create:
    page_content = content

    # Update sidebar links
    for svc_name, svc_file in link_map.items():
        page_content = page_content.replace(
            f'<a href="service-single.html">{svc_name}</a>',
            f'<a href="{svc_file}">{svc_name}</a>'
        )

    # Remove active from all sidebar li's
    page_content = page_content.replace('<li class="active">', '<li>')

    # Make current service active
    current_file = link_map[title]
    page_content = page_content.replace(
        f'<li>\n                <a href="{current_file}">{title}</a>',
        f'<li class="active">\n                <a href="{current_file}">{title}</a>'
    )

    # Update page title H1
    page_content = page_content.replace(
        '<h1>Building Construction</h1>',
        f'<h1>{title}</h1>'
    )

    # Update breadcrumb
    page_content = page_content.replace(
        '<li class="breadcrumb-item active" aria-current="page">Building Construction</li>',
        f'<li class="breadcrumb-item active" aria-current="page">{title}</li>'
    )

    # Update main heading
    sdata = service_data[title]
    page_content = page_content.replace(
        '<h3>Quality Construction Management</h3>',
        f'<h3>{sdata["heading"]}</h3>'
    )

    # Update descriptions
    page_content = page_content.replace(
        'While there are some tourists who venture to Centralia out of curiosity, they don\'t stay long. And why would they? The town is unlivable and it\'s devoid of any meaningful experiences. If I had arrived hoping to find a local video store to rent a movie from, I\'d be confused by this pop-up We understand that each project is unique and requires a specific approach.',
        sdata['desc1']
    )
    page_content = page_content.replace(
        'Our team of architects, engineers, and designers are committed to excellence. We specialize in residential, commercial, and industrial construction projects, providing full-service solutions for our clients what\'s lurking around the corner.',
        sdata['desc2']
    )

    # Update service image
    page_content = page_content.replace(
        '<img class="img-fluid" src="images/services/large/01.jpg" alt="...">',
        f'<img class="img-fluid" src="{sdata["image"]}" alt="{title}">'
    )

    # Also update navbar active state - remove active from Home, add to Services  
    page_content = page_content.replace(
        '<a class="nav-link active" href="index.html">Home</a>',
        '<a class="nav-link" href="index.html">Home</a>'
    )
    page_content = page_content.replace(
        '<a class="nav-link" href="service-single.html">Services</a>',
        '<a class="nav-link active" href="service-single.html">Services</a>'
    )

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(page_content)
    print(f'Created: {filename}')

# Also update service-single.html sidebar links and navbar
content2 = content
for svc_name, svc_file in link_map.items():
    content2 = content2.replace(
        f'<a href="service-single.html">{svc_name}</a>',
        f'<a href="{svc_file}">{svc_name}</a>'
    )
# Update sidebar: Building Construction link goes to its own page
# (already done above)

# Now update the index.html services section links
print('Service pages created. Now updating service-single.html sidebar links...')
with open('service-single.html', 'w', encoding='utf-8') as f:
    f.write(content2)
print('Done.')
