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
        'icon': nb.get('Custom Icon Path'),
        'tags': nb.get('Tags')
    }

# Check if query matches any of the profile names
if len(q) > 1:
    profiles = {name: data for name, data in profiles.iteritems() if q.lower() in name.lower()}

# Generate json output for Alfred
data = {'items': []}
for profileName, profileData in sorted(profiles.iteritems()):
    data['items'].append({
        'uuid': profileName,
        'title': profileName,
        'subtitle': (str(profileData['tags']) if profileData['tags'] else '') + profileData['command'],
        'icon': {'path': profileData['icon']} if profileData['icon'] else 'icon.png',
        'arg': profileName,
    })

print json.dumps(data).encode('utf-8-sig')
