import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
QSS_DIR = os.path.join(BASE_DIR, 'iQSS')

for i in os.listdir(BASE_DIR):
    sys.path.insert(os.listdir(BASE_DIR).index(i), os.path.join(BASE_DIR, i))
