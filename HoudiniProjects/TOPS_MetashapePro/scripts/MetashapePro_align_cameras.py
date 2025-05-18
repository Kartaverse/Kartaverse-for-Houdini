# 1. For simplicity, install Python 3.11 to a custom location in the root folder like:
# C:\Python\

# 2. Download the Metashape Python Module from:
# https://www.agisoft.com/downloads/installer/

# 3. The Python Module is installed in the command prompt/terminal using:
# pip install Metashape-*.whl

import sys, os
import importlib

# Update the System PATH to include the user installed Python site-package folder
sitePackagesPath = str(work_item.data.stringData("PYTHON_SITE_PACKAGES", 0))
sys.path.insert(0, sitePackagesPath)

# Print the Python version
# Example: 3.11.7 (main, Feb 22 2024, 17:21:30) [MSC v.1935 64 bit (AMD64)]
# print(sys.version)

# Import the metashape Python module
metashape = importlib.import_module('Metashape.Metashape')

# --------------------------------------
# Start writing your code here:

# Metashape Project Filename
psxFile = str(work_item.data.stringData("PSX_PROJECT", 0))

# Open an existing document
doc = metashape.Document()
doc.open(psxFile)

# Get the chunk
chunk = doc.chunk

# Align the views
chunk.matchPhotos()
chunk.alignCameras()

# Save the document
doc.save()

print("[Align Cameras Complete]")
