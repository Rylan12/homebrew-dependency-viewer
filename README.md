# Homebrew Dependency Viewer

This is a utility to view Homebrew packages that no other packages depend on. This is helpful for removing old packages that were once requirements but are no longer used.

## Usage

Run `./brew-deps` to print all packages that aren't depenencies for another package (automatically calls `brew deps --installed`)

Run `./brew-deps -f <file>` to check dependencies based on a specific file instead of automatically calling `brew deps --installed`. To save a file in the right format, try `brew deps --installed > <file>`.

Run `./brew-deps -e <file>` to exclude packages that are in the file. This is helpful if you have a set of packages that you use regularly and don't want to show up in the output. See an example file [here](exclude.txt). To save a file in the right format, try `./brew-deps > <file>`.

You can chain `-f` and `-e` together if desired (`./brew-deps -f <deps-file> -e <exclude-file>`)

## Tips

It may be helpful to define some aliases to make removing and viewing the packages earlier.

These are the ones I use:

```sh
alias bi='brew info'
alias bu='brew uninstall --force'
alias bd='brew deps --installed > <BREW_DEPS_LOCATION>/deps.txt
```
