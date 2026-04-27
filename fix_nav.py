import os
import glob
import re

html_files = glob.glob('*.html')

for filename in html_files:
    with open(filename, 'r') as f:
        content = f.read()

    # Step 1: Replace <span>TSPEC</span> with <span><img src="assets/img/tspec-logo.png" alt="TSPEC"></span>
    # if it's not already an image.
    def brand_replacer(match):
        brand_html = match.group(0)
        if '<img src="assets/img/tspec-logo.png"' not in brand_html:
            brand_html = re.sub(r'<span>TSPEC</span>', r'<span><img src="assets/img/tspec-logo.png" alt="TSPEC"></span>', brand_html)
        return brand_html

    content = re.sub(r'<div class="brand">.*?</div>', brand_replacer, content, flags=re.DOTALL)

    # Step 2: Strip numbers from the links in growth.html or any other file
    # Example: <a href="index.html">00. Cover</a> -> <a href="index.html">Cover</a>
    def links_replacer(match):
        links_html = match.group(0)
        # Remove "00. ", "01. ", etc. inside the <a> tags
        links_html = re.sub(r'>\d{2}\.\s+', '>', links_html)
        # Also remove inline style="color: var(--accent);"
        links_html = re.sub(r'\s*style="color:\s*var\(--accent\);"', '', links_html)
        return links_html

    content = re.sub(r'<div class="links">.*?</div>', links_replacer, content, flags=re.DOTALL)
    
    with open(filename, 'w') as f:
        f.write(content)
    print(f'Processed {filename}')

