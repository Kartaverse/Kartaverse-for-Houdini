# 1. For simplicity, install Python 3.11 to a custom location in the root folder like:
# C:\Python\

# 2. Download the Metashape Python Module from:
# https://www.agisoft.com/downloads/installer/

# 3. The Python Module is installed in the command prompt/terminal using:
# pip install Metashape-*.whl

import sys, os
import importlib

# Update the System PATH to include the Metashape based site-package folder
sys.path.insert(0, "C:\Python\Lib\site-packages")

# Print the Python version
# Example: 3.11.7 (main, Feb 22 2024, 17:21:30) [MSC v.1935 64 bit (AMD64)]
# print(sys.version)

# Import the metashape Python module
metashape = importlib.import_module('Metashape.Metashape')

# --------------------------------------
# Start writing your code here:

# Create a new document
doc = metashape.Document()
# print(dir(doc))

# Add a chunk
chunk = doc.addChunk()

# Access work item filenames
images = work_item.data.allDataMap["files"]
# print(images)

# Add the images
chunk.addPhotos(images)

# Save the document
psxFile = str(work_item.data.stringData("PSX_PROJECT", 0))
doc.save(psxFile)

print("[Import Images Complete]")
