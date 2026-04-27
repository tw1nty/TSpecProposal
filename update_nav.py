import os
import glob

html_files = glob.glob('*.html')
html_files.remove('growth.html')

for filename in html_files:
    with open(filename, 'r') as f:
        content = f.read()

    # The link to portfolio might have class="active" or not
    # So we replace portfolio.html">Portfolio</a>
    # and portfolio.html" class="active">Portfolio</a>
    
    # We will do a regex or string replacement
    # We just need to find the block:
    # <a href="portfolio.html">Portfolio</a>
    # or <a href="portfolio.html" class="active">Portfolio</a>
    # and append <a href="growth.html">Growth</a>
    
    import re
    # We want to replace `<a href="portfolio.html"[^>]*>Portfolio</a>` 
    # with `\g<0>\n        <a href="growth.html">Growth</a>` 
    # ONLY inside the `<div class="links">` block.
    # Actually, across all files, it's safe to just replace the portfolio link in the top nav
    # The top nav link has no <br> or anything, it's just the <a> tag.
    # Let's be specific and look for spaces/newlines if needed, or just use re.sub
    
    def replacer(match):
        return match.group(0) + '\n        <a href="growth.html">Growth</a>'
    
    # Let's match `<div class="links">...</div>` and replace inside it
    def div_replacer(match):
        div_content = match.group(0)
        # add growth link if not present
        if 'href="growth.html"' not in div_content:
            div_content = re.sub(r'(<a href="portfolio\.html"[^>]*>Portfolio</a>)', replacer, div_content)
        return div_content

    new_content = re.sub(r'<div class="links">.*?</div>', div_replacer, content, flags=re.DOTALL)
    
    if new_content != content:
        with open(filename, 'w') as f:
            f.write(new_content)
        print(f'Updated {filename}')
