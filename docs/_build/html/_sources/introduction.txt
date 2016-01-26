============
Introduction
============
pyvenvwrapper_ is a small and lightweight set of Bash script functions, that enhance the use of Python pyvenv_ tool.
This functions allow to create and manipulate virtual environments and corresponding projet folders in convenient way using only their names. Additional feature is automatic activation/deactivation of virtual environment when changing current working directory in the shell. Since pyvenv_ and virtualenv_ use similar technics for virtual environments, pyvenvwrapper can be used for both, though main aim is pyvenv.

**pyvenvwrapper** can be used to manage virtual environments and corresponding project folders or only virtual environments. In former case it assumes that the same name is used for virtual environment folder and the project folder which uses this virtual environment. The directories containing this folders are configured using special variables.

The idea to create pyvenvwrapper is inspired by using virtualenvwrapper_, which at that moment didn't have support for pyvenv virtual environment management. *pyvenvwrapper code is in no way related to virtualenvwrapper code.* 

------------------------------------------------------------

Compatibility
-------------
pyvenvwrapper functions are written and tested for Bash shell, however they might work with other Bash-like shells.
pyvenvwrapper is pure shell script with calls to common system tools, so it doesn't care much on what Python version is used, therefore it should work with any Python 2 or Python 3 version. Some features will require '*pip*'.
pyvenvwrapper originally was intended to be used with '*pyvenv*' tool, but it supports '*virtualenv*' tool too.

Support
-------
Any questions or issues can be reported via `GitHub Issues`_.

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
.. _pyvenvwrapper: https://github.com/solovyevn/pyvenvwrapper
.. _`GitHub Issues`: https://github.com/solovyevn/pyvenvwrapper/issues
