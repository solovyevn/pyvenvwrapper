=============
pyvenvwrapper
=============

pyvenvwrapper_ is a small and lightweight set of Bash script functions, that enhance the use of Python pyvenv_ tool.
This functions allow to create and manipulate virtual environments and corresponding projet folders in convenient way using only their names. Additional feature is automatic activation/deactivation of virtual environment when changing current working directory in the shell. Since pyvenv_ and virtualenv_ use similar technics for virtual environments, pyvenvwrapper can be used for both, though main aim is pyvenv.

**pyvenvwrapper** can be used to manage virtual environments and corresponding project folders or only virtual environments. In former case it assumes that the same name is used for virtual environment folder and the project folder which uses this virtual environment. The directories containing this folders are configured using special variables.

The idea to create pyvenvwrapper is inspired by using virtualenvwrapper_, which at that moment didn't have support for pyvenv virtual environment management. *pyvenvwrapper code is in no way related to virtualenvwrapper code.*

`Full pyvenvwrapper documentation`_ is available online at readthedocs.org.

------------------------------------------------------------

-------------
Compatibility
-------------
pyvenvwrapper functions are written and tested for Bash shell, however they might work with other Bash-like shells.
pyvenvwrapper is pure shell script with calls to common system tools, so it doesn't care much on what Python version is used, therefore it should work with any Python 2 or Python 3 version. Some features will require '*pip*'.
pyvenvwrapper originally was intended to be used with '*pyvenv*' tool, but it supports '*virtualenv*' tool too.

------------
Installation
------------
To install **pyvenvwrapper**:

1. Run '*pip install pyvenvwrapper*', this will download and install required files on your machine.

2. Run '*pyvenvwrapper_enable*', this will enable pyvenvwrapper for current user by adding the following lines to user's *.bashrc* file::

         source [path_to_pyvenvwrapper]/pyvenvwrapper_settings
         source [path_to_pyvenvwrapper]/pyvenvwrapper

   There's also '*pyvenvwrapper_disable*' command, which disables pyvenvwrapper for current user by removing those lines.

3. Reboot your shell or run '*source ~/.bashrc*'.

4. Run '*pyvenvwrapper*' to see available commands and start using **pyvenvwrapper** or see `Settings`_ to customize its behavior first.

See additional details on installation in the `documentation`_.

--------
Commands
--------
pyvenvwrapper includes the following functions, that are used as common commands in Bash:

        **mkvenv** - creates virtual environment and optionally related project folder;

        **workon** - activates existing virtual environment and optionally changes current working directory to related project folder;

        **deact** - deactivates currently active virtual environment and optionally changes current working directory back to the one used before this virtual environment activation;

        **lsvenv** - prints existing virtual environments' names, or if used with virtual environment name as argument prints packages installed in it;

        **cdvenv** - changes current working directory to specified virtual environments directory, or related project directory depending on provided options;

        **cpvenv** - copies existing virtual environment with new name and optionally related project folder;

        **rmvenv** - deletes existing virtual environment and optionally related project folder.

All commands support auto-completion with existing virtual environment names, and display usage and possible options when called with **-h** or **--help** options.

All commands can have added behavior before and/or after execution via custom scripts that can be assigned to special hook variables. See "Hooks" section in docs for details.

--------
Settings
--------
pyvenvwrapper uses the following variables for settings (provided with defaults), which you can redefine in *pyvenvwrapper_settings* file in *pyvenvwrapper* package or in the end of user's *.bashrc* file:

        **PYVENVWRAPPER_ENV_DIR=~/.virtualenvs** - directory to keep virtula environment folders, the only mandatory setting. 

        **PYVENVWRAPPER_PROJ_DIR=~/projects** - directory to keep project folders;

        **PYVENVWRAPPER_CD_ON_WORKON=true** - enables/disables automatic current working directory change to related project folder after virtual environment activation using workon command;

        **PYVENVWRAPPER_CD_ON_DEACT=true** - enables/disables automatic current working directory change after deact command execution back to the one used before virtual environment activation;

        **PYVENVWRAPPER_ACTIVATE_ON_CD=true** - enables/disables automatic activation of virtual environment when changing current working directory using cd/popd/pushd command to any directory related to existing virtual environment or its corresponding project, and virtual environment deactivation when exiting it. This is made possible via redefining Bash's cd, popd, pushd built-ins, thought it's done in a transparent fashion and shouldn't affect their use in other contexts.

-------
Support
-------
Any questions or issues can be reported via `GitHub Issues`_.

-------
License
-------
*The MIT License (MIT)*

**Copyright (c) 2016 Nikita Solovyev**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

**THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.**

.. _pyvenv: https://docs.python.org/3/library/venv.html
.. _virtualenv: https://pypi.python.org/pypi/virtualenv
.. _virtualenvwrapper: https://pypi.python.org/pypi/virtualenvwrapper/
.. _`GitHub Issues`: https://github.com/solovyevn/pyvenvwrapper/issues
.. _pyvenvwrapper: https://github.com/solovyevn/pyvenvwrapper
.. _`Full pyvenvwrapper documentation`: http://pyvenvwrapper.readthedocs.org/en/latest/
.. _`documentation`: http://pyvenvwrapper.readthedocs.org/en/latest/
