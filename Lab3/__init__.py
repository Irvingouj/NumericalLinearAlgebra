import os
import sys


current_path = os.path.abspath(os.path.dirname(__file__))
parent_path = os.path.abspath(os.path.join(current_path, os.pardir))
sys.path.append(os.path.abspath(os.path.join(parent_path, os.pardir)))

