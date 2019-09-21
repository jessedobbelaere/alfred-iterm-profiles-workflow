#!/usr/bin/env bash

# Ensure the script fails when one command fails
set -e

# Build the workflow
zip -r  alfred-iterm-profiles-workflow.alfredworkflow lib/*
zip -r  alfred-iterm-profiles-workflow.alfredworkflow workflow/*
zip -r  alfred-iterm-profiles-workflow.alfredworkflow *.py
zip -r  alfred-iterm-profiles-workflow.alfredworkflow README.md
zip -r  alfred-iterm-profiles-workflow.alfredworkflow icon.png
zip -r  alfred-iterm-profiles-workflow.alfredworkflow info.plist
zip -r  alfred-iterm-profiles-workflow.alfredworkflow package-lock.json
zip -r  alfred-iterm-profiles-workflow.alfredworkflow package.json
