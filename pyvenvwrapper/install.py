#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#Copyright (c) 2016 Nikita Solovyev
#Part of pyvenvwrapper package
"""pyvenvwrapper installation script"""

from __future__ import unicode_literals
from __future__ import print_function
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

def show_info():
    info = """
==================================
       pyvenvwrapper 0.1.0
==================================
Copyright (c) 2016 Nikita Solovyev

See full documentation at http://pyvenvwrapper.readthedocs.org/en/latest/.

To enable pyvenvwrapper for current user run 'pyvenvwrapper_enable' command,
and restart your shell or run 'source ~/.bashrc'.

You can redefine default setting in the end of your '.bashrc' file, see 
README.RST or the docs for settings' description.

pyvenvwrapper includes the following commands:

 mkvenv - creates virtual environment and optionally related project folder;

 workon - activates existing virtual environment and optionally changes current
          working directory to related project folder;

 deact - deactivates currently active virtual environment and optionally changes
         current working directory back to the one used before this virtual
         environment activation;

 lsvenv - prints existing virtual environments' names, or if used with virtual
          environment name as argument prints packages installed in it;

 cdvenv - changes current working directory to specified virtual environments
          directory, or related project directory depending on provided options;

 cpvenv - copies existing virtual environment with new name and optionally
          related project folder;

 rmvenv - deletes existing virtual environment and optionally related project
          folder.

Use '[command] -h' or '[command] --help' to see usage and possible options
for each command (after enabling pyvenvwrapper for current user).
"""
    print(info)
    return 0
