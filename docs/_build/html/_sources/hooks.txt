=====
Hooks
=====

If there's a need for added behavior on any command execution, it can be provided via custom scripts, that can be assigned to the hook variables. The script provided will be sourced, which means that its commands will be called in the same process and any changes, ie. directory changes, global variables, will be kept in current shell session after sourcing. There're hooks that will be sourced before and after each command.

Custom hook script will be sourced:

 - for **PRE** command - before any actions are taken, but after command line options and arguments are parsed and verified;
 - for **POST** command - after all actions are taken, as last instructions, but only if no errors occured.

For convenience every script defined for hook variables will get "*venv=VENV_NAME*" as first argument and all the arguments from command line as subsequent arguments.
Special cases are:

 - **LSVENV** might be called without *VENV_NAME*, in this case "*venv=*" will be provided;
 - **CPVENV** will get "*venv=SRC_VENV*" and "*dst=DST_VENV*" as first and second arguments and all the arguments from command line as subsequent arguments;
 - **DEACT** will not get any arguments, as it doesn't use any. (Active virtual evironment path is kept in *VIRTUAL_ENV* environment variable, so it can be used.)

*VENV_NAME*, *SRC_VENV*, *DST_VENV* will be the actual virtual environments names provided as argument to corresponding command.

Custom script should return '*0*' in the end if no errors occured. If the sourced script will return any return code other than '*0*', then the command will be aborted with error.

Provide a path to a custom script file as a value for the following variables directly in *pyvenvwrapper_settings* in *pyvenvwrapper* package or in the end of user's *.bashrc* file to define hooks (i.e. *PYVENVWRAPPER_POST_MKVENV=~/custom_sript*). Fot changes to take effect you'll have to reboot the shell or run '*source ~/.bashrc*'.

 - Sourced before and after *mkvenv*:
        **PYVENVWRAPPER_PRE_MKVENV**
        **PYVENVWRAPPER_POST_MKVENV**

 - Sourced before and after *lsvenv*:
        **PYVENVWRAPPER_PRE_LSVENV**
        **PYVENVWRAPPER_POST_LSVENV**

 - Sourced before and after *cdvenv*:
        **PYVENVWRAPPER_PRE_CDVENV**
        **PYVENVWRAPPER_POST_CDVENV**

 - Sourced before and after *rmvenv*: 
        **PYVENVWRAPPER_PRE_RMVENV**
        **PYVENVWRAPPER_POST_RMVENV**

 - Sourced before and after *cpvenv*:
        **PYVENVWRAPPER_PRE_CPVENV**
        **PYVENVWRAPPER_POST_CPVENV**

 - Sourced before and after *workon*:
        **PYVENVWRAPPER_PRE_WORKON**
        **PYVENVWRAPPER_POST_WORKON**

 - Sourced before and after *deact*:
        **PYVENVWRAPPER_PRE_DEACT**
        **PYVENVWRAPPER_POST_DEACT**

 - Sourced before and after virtual environment activation on directory change if *PYVENVWRAPPER_ACT_ON_CD* setting is enabled:
        **PYVENVWRAPPER_PRE_ACT_ON_CD**
        **PYVENVWRAPPER_POST_ACT_ON_CD**

Note for *PYVENVWRAPPER_PRE_ACT_ON_CD* and *PYVENVWRAPPER_POST_ACT_ON_CD*:
        If *cd* to directory not related in any way to any virtual environment, hooks are not called. If *cd* to directory related to virtual environment, even if there's any already active virtual environment, the *PRE* hook will be source before currently active environment deactivation. For these hook scripts any output to console will be suppresed.
