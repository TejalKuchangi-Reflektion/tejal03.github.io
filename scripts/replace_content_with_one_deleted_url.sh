#!/bin/bash

# Exit immediately if any command fails
set -e

ORIGINAL="../orignal_sitemap.xml"
DELETED="../deleted_one_url_sitemap.xml"
TEMP="../sitemap.xml"

echo ""
echo "=== Copying contents of '$DELETED' to '$TEMP' ==="
cp "$DELETED" "$TEMP"
echo "=== Task completed successfully ==="