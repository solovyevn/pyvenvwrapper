#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#Copyright (c) 2016 Nikita Solovyev
#Part of pyvenvwrapper package
"""pyvenvwrapper installation script"""

from __future__ import unicode_literals
from os import path
import sys
import codecs

bashrc_file = path.join(path.expanduser("~"), ".bashrc")
module_dir = path.dirname(path.realpath(__file__))
wrapper_file = path.join(module_dir, "pyvenvwrapper") 
wrapper_settings_file = path.join(module_dir, "pyvenvwrapper_settings")
source_lines = ["source "+wrapper_settings_file+"\n", "source "+wrapper_file+"\n"]

def pyvenvwrapper_enable():
    bashrc=codecs.open(bashrc_file, 'a+', encoding='utf-8')
    try:
        bashrc.seek(0)
        for line in source_lines:
            if line not in bashrc:
                bashrc.write(line)
    finally:
        bashrc.close()
    return 0

def pyvenvwrapper_disable():
    bashrc=codecs.open(bashrc_file, 'a+', encoding='utf-8')
    bashrc_lines=[]
    try:
        bashrc.seek(0)
        for line in bashrc:
            if line not in source_lines:
                bashrc_lines.append(line)
        bashrc.seek(0)
        bashrc.truncate()
        bashrc.writelines(bashrc_lines)
    finally:
        bashrc.close()
    return 0
