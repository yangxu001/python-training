import os
import glob

print __file__

path = os.path.abspath(__file__)
print path

directory = os.path.dirname(path)
print directory

print os.path.dirname(directory)

print os.path.join(directory, "README.md")

directory, file_name = os.path.split(path)
print directory, file_name

print os.path.splitext(file_name)
print os.path.splitext(path)

try:
    print os.listdir(path)
except Exception as e:
    print e

print path, os.path.isdir(path)
print directory, os.path.isdir(directory)
print os.listdir(directory)

print [py for py in os.listdir(directory) if os.path.splitext(py)[1][1:] == 'py']
print [os.path.join(directory, py) for py in os.listdir(directory) if os.path.splitext(py)[1][1:] == 'py']

print glob.glob(path)
print glob.glob(os.path.join(directory, '*.py'))
