# Homebrew Dependency Viewer

This is a utility to view Homebrew packages that no other packages depend on. This is helpful for removing old packages that were once requirements but are no longer used.

## Usage

Run `./main.py`

## Tips

It may be helpful to define some aliases to make removing and viewing the packages earlier.

These are the ones I use:

```sh
alias bi='brew info'
alias bu='brew uninstall --force'
alias bd='brew deps --installed > <BREW_DEPS_LOCATION>/deps.txt
```
