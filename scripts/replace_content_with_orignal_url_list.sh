#!/bin/bash

# Exit immediately if any command fails
set -e

ORIGINAL="../orignal_sitemap.xml"
DELETED="../deleted_one_url_sitemap.xml"
TEMP="../sitemap.xml"

echo "=== Copying contents of '$ORIGINAL' to '$TEMP' ==="
cp "$ORIGINAL" "$TEMP"
echo "=== Task completed successfully ==="