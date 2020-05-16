# Homebrew Dependency Viewer

This is a utility to view Homebrew packages that no other packages depend on. This is helpful for removing old packages that were once requirements but are no longer used.

## Usage

Run `./main.py` to print all packages that aren't depenencies for another package (automatically calls `brew deps --installed`)

Run `./main.py -f <file>` to check dependencies based on a specific file instead of automatically calling `brew deps --installed`. To save a file in the right format, try `brew deps --installed > <file>`.

Run `./main.py -e <file>` to exclude packages that are in the file. This is helpful if you have a set of packages that you use regularly and don't want to show up in the output. See an [example file](exclude.txt). To save a file in the right format, try `./main.py > <file>`.

You can chain `-f` and `-e` together if desired (`./main.py -f <deps-file> -e <exclude-file>`)

## Tips

It may be helpful to define some aliases to make removing and viewing the packages earlier.

These are the ones I use:

```sh
alias bi='brew info'
alias bu='brew uninstall --force'
alias bd='brew deps --installed > <BREW_DEPS_LOCATION>/deps.txt
```
