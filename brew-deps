#!/usr/bin/env python3

import argparse
import os


BREW_DEPS_COMMAND = '/usr/bin/env brew deps --installed'


def parser():
    parser = argparse.ArgumentParser(
            description="Show top-level Homebrew packages.")
    parser.add_argument(
            '-f', dest='file', metavar='FILE',
            help='use Homebrew dependency file')
    parser.add_argument(
            '-e', dest='exclude', metavar='FILE',
            help="don't list certain packages")
    return parser


def get_file(file, parser, arg):
    file_lines = []
    if file is not None:
        try:
            with open(file) as f:
                file_lines = f.read().strip().split('\n')
        except FileNotFoundError:
            parser.error("argument -{}: file not found: '{}'"
                         .format(arg, file))
    return file_lines


def convert_to_dict(lines):
    deps = {}
    for line in lines:
        colon_index = line.index(':')
        reqs = line[colon_index + 2:]
        deps[line[:colon_index]] = reqs.split(' ') if reqs != '' else []
    return deps


def parse_args(parser):
    args = parser.parse_args()
    deps = get_file(args.file, parser, 'f')
    exclusions = get_file(args.exclude, parser, 'e')

    if len(deps) == 0:
        deps = os.popen(BREW_DEPS_COMMAND).read().strip().split('\n')
    deps = convert_to_dict(deps)

    return deps, exclusions


def num_times_required(module, deps):
    count = 0
    for dep in deps:
        if module in deps[dep]:
            count += 1
    return count


def print_output(mods):
    for mod in mods:
        print(mod)


if __name__ == '__main__':
    parser = parser()
    deps, exclusions = parse_args(parser)

    mods = []
    for mod in deps:
        if num_times_required(mod, deps) == 0 and mod not in exclusions:
            mods.append(mod)
    print_output(mods)
