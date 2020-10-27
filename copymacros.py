#!/usr/bin/env python

import os
import shutil

masterfolder = 'macros'
basefolder = r'C:\Program Files (x86)\World of Warcraft\_retail_\WTF\Account\DOGBERTAI'

classdict = {
    'deathknight' : ['Mannoroth/Chaundrea'],
    'demonhunter' : ['Wyrmrest Accord/Mykessa'],
    'druid' : ['Mannoroth/Tifaña'],
    'hunter' : ['Mannoroth/Tessica'],
    'mage' : ['Mannoroth/Kerilynn'],
    'monk' : ['Mannoroth/Meilani'],
    'paladin' : ['Mannoroth/Kydesha'],
    'priest' : ['Mannoroth/Tyra'],
    'rogue' : ['Mannoroth/Serelena'],
    'shaman' : ['Mannoroth/Gothan'],
    'warlock' : ['Mannoroth/Kalana'],
    'warrior' : ['Mannoroth/Keyra'],
}

def copy_to_wtf():
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


def copy_to_master():
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


if __name__ == "__main__":
    copy_to_master()