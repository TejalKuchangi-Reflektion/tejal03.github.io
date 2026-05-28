#!/usr/bin/env python3
import datetime
import xml.etree.ElementTree as ET
from pathlib import Path
import sys

# Default sitemap path; will be replaced by user input or CLI arg if provided
SITEMAP_PATH = Path("sitemap.xml")

def detect_namespace(root_tag: str) -> str:
    # root_tag example: "{http://www.sitemaps.org/schemas/sitemap/0.9}urlset"
    if root_tag.startswith("{") and "}" in root_tag:
        return root_tag.split("}")[0].strip("{")
    return ""

def main():
    # Allow an optional command-line argument to specify sitemap path.
    # If not provided, use the default 'sitemap.xml' without prompting.
    if len(sys.argv) > 1:
        S_PATH = Path(sys.argv[1])
    else:
        S_PATH = SITEMAP_PATH

    if not S_PATH.exists():
        raise SystemExit(f"ERROR: {S_PATH} not found. Ensure it is at repo root or provide a correct path.")

    today = datetime.date.today().isoformat()  # YYYY-MM-DD

    tree = ET.parse(S_PATH)
    root = tree.getroot()
    ns = detect_namespace(root.tag)

    def q(tag: str) -> str:
        return f"{{{ns}}}{tag}" if ns else tag

    changed = 0

    # Update/create <lastmod> for only the first two <url> entries
    urls = root.findall(q("url"))
    for url in urls[:2]:  # Only update the first two entries
        lastmod = url.find(q("lastmod"))
        if lastmod is None:
            lastmod = ET.SubElement(url, q("lastmod"))
            lastmod.text = today
            changed += 1
        else:
            if (lastmod.text or "").strip() != today:
                lastmod.text = today
                changed += 1

    tree.write(S_PATH, encoding="utf-8", xml_declaration=True)
    print(f"Updated {S_PATH} lastmod to {today}. Entries changed: {changed}")

if __name__ == "__main__":
    main()