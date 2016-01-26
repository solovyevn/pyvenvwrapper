========
Settings
========

The following settings are defined in *pyvenvwrapper_settings* file in *pyvenvwrapper* package directory, which is sourced in user's *.bashrc*. The settings have sane defaults, but can be redefined directly in *pyvenvwrapper_settings* or in the end of user's *.bashrc* file. For changes to take effect the shell has to be rebooted or user's *.bachrc* has to be sourced by running '*source ~/.bashrc*'.

**PYVENVWRAPPER_ENV_DIR** (*=~/.virtualenvs*)    Directory to keep virtual environments. No symlinks allowed. **The only setting that must be defined in order to make pyvenvwrapper work.**

**PYVENVWRAPPER_PROJ_DIR** (*=~/projects*)    Directory to keep project folders. No symlinks allowed. If this setting is undefined, then pyvenvwrapper will silently not perform any actions, that assume existence of project folders related to virtual environments. Therefore not defining this option makes pyvenvwrapper work only with virtual environments. However if any command is called with explicit option related to project folder when this option is undefined, the command will be aborted with error.

**PYVENVWRAPPER_CD_ON_WORKON** (*=true*)    Enables/Disables directory change to corresponding project directory after virtual environment activation with workon command. Possible values: true/false. Requires *PYVENVWRAPPER_PROJ_DIR* to be set in order to work.

**PYVENVWRAPPER_CD_ON_DEACT** (*=true*)    Enables/Disables directory change to the one used at the time of workon execution after virtual environment deactivation with deact call. Possible values: true/false.

**PYVENVWRAPPER_ACTIVATE_ON_CD** (*=true*)    Enables/Disables redefinition of *cd*, *popd*, *pushd* commands in oreder to activate virtual environment if directory changed to one of virtual environments' or corresponding projects' directory, otherwise do nothing or deactivate active virtual environment. Possible values: true/false. Requires shell reboot after changing or sourcing user's *.bashrc*.

Note on *PYVENVWRAPPER_ACTIVATE_ON_CD*: redefinition of commands is intended to be transparent, so argumetns of original built-in functions are not affected in any way, return value are always that of wrapped built-in and no additional output related to added behavior is introduced.
