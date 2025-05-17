# Using PyAutoGUI to automate "unscriptable workflows" via GUI automation
# 1. For simplicity, install Python 3.11 to a custom location in the root folder like:
# C:\Python\

# 2. The PyAutoGUI Python Module is installed in the command prompt/terminal using:
# pip install pyautogui

# 3. Customize the attribtuecreate node's "PYTHON_SITE_PACKAGES" variable to point at your local
# Python site-packages folder. This will point Hython (Houdini Python) at the site-packages 
# location where the Python module is installed. The default 3rd party site-packages location 
# used by the included .hip example is:
# C:\Python\Lib\site-packages

# 4. You can validate where PyAutoGUI was installed from the command prompt/terminal using:
# pip list
# pip show PyAutoGUI

import sys, os
import importlib

# Update the System PATH to include the user installed Python site-package folder
sitePackagesPath = str(work_item.data.stringData("PYTHON_SITE_PACKAGES", 0))
sys.path.insert(0, sitePackagesPath)

# Print the Python version
# Example: 3.11.7 (main, Feb 22 2024, 17:21:30) [MSC v.1935 64 bit (AMD64)]
# print(sys.version)

# Import the PyAutoGUI Python module
ui = importlib.import_module('pyautogui')

# --------------------------------------
# Start writing your code here:

# List all PyAutoGUI methods
print(dir(ui))