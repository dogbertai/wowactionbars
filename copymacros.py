#!/usr/bin/env python

import json
import os
import shutil


masterfolder = 'macros'


def copy_to_wtf(basefolder, classdict):
    src = os.path.join(masterfolder, 'macros-cache.txt')
    dst = os.path.join(basefolder)
    shutil.copy(src, dst)
    src = os.path.join(masterfolder, 'bindings-cache.wtf')
    shutil.copy(src, dst)
    for clas,chars in classdict.items():
        src = os.path.join(masterfolder, clas, 'macros-cache.txt')
        for char in chars:
            dst = os.path.join(basefolder, char)
            shutil.copy(src, dst)


def copy_to_master(basefolder, classdict):
    src = os.path.join(basefolder, 'macros-cache.txt')
    dst = os.path.join(masterfolder)
    shutil.copy(src, dst)
    src = os.path.join(basefolder, 'bindings-cache.wtf')
    shutil.copy(src, dst)
    for clas,chars in classdict.items():
        dst = os.path.join(masterfolder, clas)
        os.makedirs(dst, exist_ok=True)
        for char in chars:
            src = os.path.join(basefolder, char, 'macros-cache.txt')
            shutil.copy(src, dst)
            # only first char is treated as master
            break


def load_json(path):
    with open(path, encoding='utf-8') as f:
        result = json.load(f)
    return (result['path'], result['chars'])


def main():
    retaildictpath = 'retaildict.json'
    retaildata = load_json(retaildictpath)
    ptrdictpath = 'ptrdict.json'
    ptrdata = load_json(ptrdictpath)
    #copy_to_master(*retaildata)
    copy_to_master(*ptrdata)
    #copy_to_wtf(*ptrdata)
    #copy_to_wtf(*retaildata)


if __name__ == "__main__":
    main()