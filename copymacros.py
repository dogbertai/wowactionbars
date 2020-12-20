#!/usr/bin/env python

import json
import os
import shutil


masterfolder = 'macros'


def copy_all_char_to_wtf(basefolder, classdict, file):
    """Copy specified file from master to all chars."""
    src = os.path.join(masterfolder, file)
    for chars in classdict.values():
        for char in chars:
            dst = os.path.join(basefolder, char)
            shutil.copy(src, dst)


def copy_all_char_to_wtf2(basefolder, classdict):
    """Copy files from master to all chars."""
    copy_all_char_to_wtf(basefolder, classdict, 'AddOns.txt')
    copy_all_char_to_wtf(basefolder, classdict, 'layout-local.txt')


def copy_per_account_to_wtf(basefolder):
    """Copy files from master to account."""
    src = os.path.join(masterfolder, 'macros-cache.txt')
    dst = os.path.join(basefolder)
    shutil.copy(src, dst)
    src = os.path.join(masterfolder, 'bindings-cache.wtf')
    shutil.copy(src, dst)


def copy_per_class_to_wtf(basefolder, classdict):
    """Copy files from master to each class."""
    for clas, chars in classdict.items():
        src = os.path.join(masterfolder, clas, 'macros-cache.txt')
        for char in chars:
            dst = os.path.join(basefolder, char)
            shutil.copy(src, dst)


def copy_to_wtf(basefolder, classdict):
    copy_per_account_to_wtf(basefolder)
    copy_per_class_to_wtf(basefolder, classdict)
    copy_all_char_to_wtf2(basefolder, classdict)


def copy_tyra_to_master(basefolder, file):
    """Copy specified file from Tyra to master."""
    src = os.path.join(basefolder, 'Mannoroth/Tyra', file)
    dst = os.path.join(masterfolder)
    shutil.copy(src, dst)


def copy_tyra_to_master2(basefolder):
    """Copy files from Tyra to master."""
    copy_tyra_to_master(basefolder, 'AddOns.txt')
    copy_tyra_to_master(basefolder, 'layout-local.txt')


def copy_per_account_to_master(basefolder, classdict):
    """Copy files from account to master."""
    src = os.path.join(basefolder, 'macros-cache.txt')
    dst = os.path.join(masterfolder)
    shutil.copy(src, dst)
    src = os.path.join(basefolder, 'bindings-cache.wtf')
    shutil.copy(src, dst)


def copy_per_class_to_master(basefolder, classdict):
    """Copy files from first char per class to master."""
    for clas, chars in classdict.items():
        dst = os.path.join(masterfolder, clas)
        os.makedirs(dst, exist_ok=True)
        for char in chars:
            src = os.path.join(basefolder, char, 'macros-cache.txt')
            shutil.copy(src, dst)
            # only first char is treated as master
            break


def copy_to_master(basefolder, classdict):
    copy_per_account_to_master(basefolder, classdict)
    copy_per_class_to_master(basefolder, classdict)
    copy_tyra_to_master2(basefolder)


def load_json(path):
    with open(path, encoding='utf-8') as f:
        result = json.load(f)
    return (result['path'], result['chars'])


def main():
    retaildictpath = 'retaildict.json'
    retaildata = load_json(retaildictpath)
    ptrdictpath = 'ptrdict.json'
    ptrdata = load_json(ptrdictpath)
    copy_to_master(*retaildata)
    # copy_to_master(*ptrdata)
    # copy_to_wtf(*ptrdata)
    copy_to_wtf(*retaildata)


if __name__ == "__main__":
    main()
