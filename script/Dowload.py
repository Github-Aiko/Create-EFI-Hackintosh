import requests
import zipfile
import os
import shutil

# Set the repository owner, repository name, and file path
owner = 'acidanthera'
repo = 'OpenCorePkg'
path = 'path/to/file.txt'

# check latest release
r = requests.get('https://api.github.com/repos/{}/{}/releases/latest'.format(owner, repo))
latest_release = r.json()['tag_name']

# dowload file from latest release
r = requests.get('https://github.com/acidanthera/OpenCorePkg/releases/download/{}/OpenCore-{}-RELEASE.zip'.format(latest_release, latest_release))
with open('OpenCore-{}-RELEASE.zip'.format(latest_release), 'wb') as f:
	f.write(r.content)

# Unzip the file
with zipfile.ZipFile('OpenCore-{}-RELEASE.zip'.format(latest_release), 'r') as zip_ref:
	zip_ref.extractall('./FILE-OC/')

# info download file
print('Downloaded file: OpenCore-{}-RELEASE.zip'.format(latest_release))

# Delete the zip file
os.remove('OpenCore-{}-RELEASE.zip'.format(latest_release))

# Set the source and destination directories
src = './FILE-OC/X64/EFI/'
dst = './EFI/'

# Use shutil.copytree() to copy the directory tree
shutil.copytree(src, dst, dirs_exist_ok=True)

# Coppy File config.plist
shutil.copyfile('./FILE-OC/Docs/Sample.plist', './EFI/OC/config.plist')

# Delete the directory tree
shutil.rmtree('./FILE-OC/')
