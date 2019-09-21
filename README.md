# iTerm Profiles Workflow for [Alfred 3](http://www.alfredapp.com)

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](http://makeapullrequest.com)

> Search through your iTerm profiles using Alfred and easily open one. Extremely useful if you have a lot of profiles, e.g. with an SSH command for each server.

## 🔧 Installation

**[Download workflow here](https://github.com/jessedobbelaere/alfred-iterm-profiles-workflow/releases)**

## ⚙️ Usage

1. Enter keyword `profile` in Alfred, followed by a searchquery to find the profile you need.
2. Hit <enter> and iTerm will open your profile

![Preview](https://i.imgur.com/TKlKLct.png)

## 🔨 Development

When developing an Alfred workflow, you can call `alfred-link` directly from your cli. Use `npx` to call the local installation of `alfred-link` and `alfred-unlink`.

```
$ npx alfred-link
```

This will create a symlink in the Alfred workflows directory pointing to your development location without transforming `info.plist`.

To remove the symlink afterwards, you can call `alfred-unlink`.

```
$ npx alfred-unlink
```
