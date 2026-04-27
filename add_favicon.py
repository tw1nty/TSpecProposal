import glob

html_files = glob.glob('*.html')
favicon_tag = '  <link rel="icon" type="image/png" href="assets/img/favicon.png">\n'

for filename in html_files:
    with open(filename, 'r') as f:
        content = f.read()
    
    if 'favicon.png' not in content:
        # Insert before </head>
        content = content.replace('</head>', f'{favicon_tag}</head>')
        
        with open(filename, 'w') as f:
            f.write(content)
        print(f"Added favicon to {filename}")

