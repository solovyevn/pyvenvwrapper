============
Installation
============

By defautl the following instructions show how to enable pyvenvwrapper for particular user, if you wish to enable it system wide, see `Manual installation`_.

----------------------
Automated installation
----------------------
To install **pyvenvwrapper**:

1. Run '*pip install pyvenvwrapper*', this will download and install required files on your machine.

2. Run '*pyvenvwrapper_enable*', this will enable pyvenvwrapper for current user by adding the following lines to user's *.bashrc* file::

        source [path_to_pyvenvwrapper]/pyvenvwrapper_settings
        source [path_to_pyvenvwrapper]/pyvenvwrapper

   There's also '*pyvenvwrapper_disable*' command, which disables pyvenvwrapper for current user by removing those lines.

3. Reboot your shell or run '*source ~/.bashrc*'.

4. Run '*pyvenvwrapper*' to see available commands and start using **pyvenvwrapper** or see :doc:`settings` to customize its behavior first.

-------------------
Manual installation
-------------------
To install **pyvenvwrapper** manually:

1. Run '*pip install pyvenvwrapper*', this will download and install required files on your machine.

2. Find where *pyvenvwrapper* package is installed. Usually somewhere in *site-packages* or *dist-packages*, i.e. */usr/lib/python3/site-packages/*, */usr/local/lib/python2.7/site-packages/*.

3. Open current user's *.bashrc* file in text editor, i.e. '*vim ~/.bashrc*', and add the following lines to the end of the file, substituting *[path_to_pyvenvwrapper_package]* with actual path from step 2::
   
        source [path_to_pyvenvwrapper_package]/pyvenvwrapper_settings
        source [path_to_pyvenvwrapper_package]/pyvenvwrapper

   If you wish to enable pyvenvwrapper system wide, then consider adding the lines above to the end of  */etc/bash.bashrc* file, or adding symlinks for specified files to */etc/profile.d/* directory.

4. Reboot your shell or run '*source ~/.bashrc*'.

5. Run '*pyvenvwrapper*' to see available commands and start using **pyvenvwrapper** or see :doc:`settings` to customize its behavior first.
