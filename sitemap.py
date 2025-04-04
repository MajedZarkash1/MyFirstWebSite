import os
from datetime import datetime

BASE_URL="http://localhost"

# Function to generate sitemap XML content
def generate_sitemap(directory):
    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>']
    sitemap.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

    # search for for .html files
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                # Create the URL and lastmod entries
                file_path = os.path.relpath(os.path.join(root, file), directory)
                url = f"{BASE_URL}/{file_path.replace(os.sep, '/')}"
                lastmod = datetime.now().strftime("%Y-%m-%d")
                
                sitemap.append("  <url>")
                sitemap.append(f"    <loc>{url}</loc>")
                sitemap.append(f"    <lastmod>{lastmod}</lastmod>")
                sitemap.append("    <priority>0.5</priority>")
                sitemap.append("  </url>")
    
    sitemap.append("</urlset>")
    return "\n".join(sitemap)

# Find current location 
local_directory = os.getcwd()



# call generate_sitemap function 
sitemap_content = generate_sitemap(local_directory)

# Save the sitemap to a file in the current directory
sitemap_file = os.path.join(local_directory, "sitemap.xml")
with open(sitemap_file, "w", encoding="utf-8") as f:
    f.write(sitemap_content)

print(f"Sitemap generated and saved to {sitemap_file}")