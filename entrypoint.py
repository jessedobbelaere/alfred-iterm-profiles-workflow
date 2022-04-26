#!/usr/bin/env python3
# encoding: utf-8
from __future__ import annotations

import os
import sys

# setup access to the local .site-packages
sys.path.insert(0, os.path.dirname(__file__) + "/.site-packages")  # noqa


from workflow import Workflow3, ICON_WARNING, MATCH_SUBSTRING
from lib import biplist


def main(wf: Workflow3):
    try:
        # Fetch cached profiles
        all_profiles = wf.cached_data('profiles', read_iterm_profiles, max_age=30)

        # Query argument Ensure `query` is initialised
        query = None
        if len(wf.args):
            query = wf.args[0]

        # Filter profiles by query
        profiles = wf.filter(query, all_profiles, filter_key_for_profile, match_on=MATCH_SUBSTRING)

        if not profiles:
            wf.add_item('No profile matches', icon=ICON_WARNING)

        profiles.sort(key=sort_key_for_profile)
        for profile in profiles:
            wf.add_item(title=profile['name'],
                        subtitle=((str(profile['tags']) + ' ') if profile['tags'] else '') + profile['command'],
                        arg=profile['name'],
                        valid=True,
                        icon=profile['icon'])

        wf.send_feedback()
    except Exception as e:
        wf.logger.exception(e)
        raise

def read_iterm_profiles():
    # Read iTerm's preferences file
    iTermPreferencesPath = os.path.join(os.environ["HOME"], "Library", "Preferences", "com.googlecode.iterm2.plist")
    plist = biplist.readPlist(iTermPreferencesPath)
    # Extract profile data from plist
    profiles = []
    for nb in plist['New Bookmarks']:
        profiles.append({
            'name': nb.get('Name'),
            'command': nb.get('Command'),
            'icon': nb.get('Custom Icon Path'),
            'tags': nb.get('Tags')
        })

    return profiles

def filter_key_for_profile(profile):
    return profile['name'] + ' ' + str(profile['tags'])

def sort_key_for_profile(profile):
    return profile['name']

if __name__ == "__main__":
    # Create a global `Workflow3` object
    wf = Workflow3()
    wf.logger.info(__name__)
    # Call your entry function via `Workflow3.run()` to enable its
    # helper functions, like exception catching, ARGV normalization,
    # magic arguments etc.
    wf.run(main)
