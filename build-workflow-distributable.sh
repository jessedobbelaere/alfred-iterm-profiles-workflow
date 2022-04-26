#!/usr/bin/env bash
set -e

# Build the workflow
zip -r alfred-iterm-profiles-workflow.alfredworkflow .site-packages/*
zip -r alfred-iterm-profiles-workflow.alfredworkflow lib/*
zip -r alfred-iterm-profiles-workflow.alfredworkflow *.py
zip -r alfred-iterm-profiles-workflow.alfredworkflow *.png
zip -r alfred-iterm-profiles-workflow.alfredworkflow README.md
zip -r alfred-iterm-profiles-workflow.alfredworkflow icon.png
zip -r alfred-iterm-profiles-workflow.alfredworkflow info.plist
