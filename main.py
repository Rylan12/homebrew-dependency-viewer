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


def num_times_depended(module, deps):
    count = 0
    for dep in deps:
        if module in deps[dep]:
            count += 1
    return count


def print_output(mods):
    for mod in mods:
        print(mod)


if __name__ == '__main__':
    deps = get_deps_from_file('deps.txt')

    mods = []
    for mod in deps:
        if num_times_depended(mod, deps) == 0:
            mods.append(mod)
    print_output(mods)
