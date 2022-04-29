import os,glob
import json
folder_path = 'siteConfig'
for filename in glob.glob(os.path.join(folder_path, '*.config')):
  with open(filename, 'r') as f:
    text = f.read()
    print(filename)
    print(json.loads(text))