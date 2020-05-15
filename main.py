#!/usr/bin/env python3


def get_deps_from_file(file):
    lines = []
    with open(file, 'r') as f:
        lines = f.read().strip().split('\n')
    return convert_to_dict(lines)


def convert_to_dict(lines):
    deps = {}
    for line in lines:
        colon_index = line.index(':')
        reqs = line[colon_index + 2:]
        deps[line[:colon_index]] = reqs.split(' ') if reqs != '' else []
    return deps


def num_times_required(module, deps):
    count = 0
    for dep in deps:
        if module in deps[dep]:
            count += 1
    return count


def load_exclusions(file):
    try:
        with open(file, 'r') as f:
            exclusions = f.read().strip().split('\n')
    except FileNotFoundError:
        exclusions = []
    return exclusions


def print_output(mods):
    for mod in mods:
        print(mod)


if __name__ == '__main__':
    deps = get_deps_from_file('deps.txt')
    exclusions = load_exclusions('exclude.txt')

    mods = []
    for mod in deps:
        if num_times_required(mod, deps) == 0 and mod not in exclusions:
            mods.append(mod)
    print_output(mods)
