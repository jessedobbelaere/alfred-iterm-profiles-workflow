#!/usr/local/bin/python

from lib import biplist
import os
import json
import sys

# Query argument
q = sys.argv[1]

# Read iTerm's preferences file
iTermPreferencesPath = os.path.join(os.environ["HOME"], "Library", "Preferences", "com.googlecode.iterm2.plist")
plist = biplist.readPlist(iTermPreferencesPath)

# Extract profile data from plist
profiles = {}
for nb in plist['New Bookmarks']:
    profileName = nb.get('Name')
    profiles[nb.get('Name')] = {
        'name': nb.get('Name'),
        'command': nb.get('Command'),
        'tags': nb.get('Tags')
    }

# Check if query matches any of the profile names
if len(q) > 1:
    profiles = [profile for key, profile in profiles.items() if q.lower() in key.lower()]
else:
    profiles = [profile for key, profile in profiles.items()]

# Generate json output for Alfred
data = {'items': []}
for profile in profiles:
    data['items'].append({
        'uuid': profile['name'],
        'title': profile['name'],
        'subtitle': profile['command'],
        'arg': profile['name'],
    })

print json.dumps(data).encode('utf-8-sig')
