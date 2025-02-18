import sys
import os

# Get the absolute path of the project root directory
project_root = os.path.abspath(os.path.dirname(__file__))

# Add the 'src' directory to the Python path
sys.path.insert(0, os.path.join(project_root, "src"))
