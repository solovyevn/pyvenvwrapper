=================
Command reference
=================
Usage and possible options for each command can be displayed in the shell by calling a command with *-h* or *--help* option.

All commands support auto-completion of virtual environment names.

All commands return:

- '*0*' exit code on successful execution;
- '*1*' exit code when an error occurres;
- '*2*' exit code on invocation syntax errors.

------
mkvenv
------
*mkvenv command is a wrapper for pyvenv/virtualenv and pip install*

Usage: mkvevn [OPTIONS] VENV_NAME

mkvenv command creates new virtual environment with the name of VENV_NAME in directory specified by PYVENVWRAPPER_ENV_DIR and new project directory with the same name in directoy specified by PYVENVWRAPPER_PROJ_DIR, if this variable is set. Additional options, that modify this command's behavior are described below.

Mandatory arguments to long options are mandatory for short options too.
Combined options are not supported, i.e. instead of '-aj' use '-a -j'.

  -o, --options <options>               Options to provide to underlying tool
                                        for virtual environment creation.
				        See additional information below. 

  -i, --install <requirements>          Install packages listed in requirements
                                        using pip after virtual environment is
					created. <requirements> should be quoted
					string in "pip install" requirement
					specifier format. mkvenv will
					automatically try to install pip if it
					isn't already available.

  -r, --requirements <file>             Install packages listed in requirements
                                        file using pip after virtual environment
					is created. <file> should be path
					pointing to a file containing
					requirement specifications in "pip
					install -r" requirements file format.
					mkvenv will automatically try to install 
					pip if it isn't already available.

  -u, --util <util name>                Specify the name of utility to use for
                                        virtual environment creation. By defaul t
					mkvenv tries to use "pyvenv" first, if
					it's not available mkvenv tries to use
					"virtualenv".

  -p, --pip                             Install pip after virtual environment is
                                        created. 

  -t, --template <template dir path>    Copy files and directories from template
                                        directory to newly created project
					directory. Precludes use of -n option.

  -n, --no-project                      Don't create project directory.
                                        Precludes use of -t, -j options.

  -a, --activate                        Activate virtual environment after it is
                                        created.

  -e, --env                             Change current directory to virtual
                                        environment directory after it is
					created. Precludes use of -j option.

  -j, --project                         Change current directory to project
                                        directory after it is created.
					Precludes use of -n, -e options.

------
workon
------
Usage: workon [-n] VENV_NAME

*workon command is a wrapper for VIRTUAL_ENV/bin/activate*

workon command activates existing virtual environment with the name of VENV_NAME from directory specified by PYVENVWRAPPER_ENV_DIR, and changes current working directory to corresponding project directory if PYVENVWRAPPER_PROJ_DIR is specified and PYVENVWRAPPER_CD_ON_WORKON is set to "true".

  -n, --no-cd    Don't change current working directory to corresponding project
                 directory after virtual environment activation.

-----
deact
-----
Usage: deact

*deact command is a wrapper for deactivate*

deact command deactivates active virtual environment, and changes current working directory back to its value at the time of virtual environment activation if PYVENVWRAPPER_CD_ON_DEACT is set to "true".

------
lsvenv
------

Usage: lsvevn [OPTIONS] [VENV_NAME]

lsvenv command list existing virtual environments in the directory specified by PYVENVWRAPPER_ENV_DIR. If used with existing virtual environment name as optional argument VENV_NAME, then lsvenv lists packages installed in this virtual environment in requirements format (alias to "pip freeze"). Additional options, that modify this command's behavior are described below.

Combined options are not supported, i.e. instead of '-se' use '-s -e'.

  -l, --local       If virtual environment has global access, do not list
                    globally-installed packages. Has no meaning if VENV_NAME
		    is not provided.
  -s, --simple      Use simple output format instead of requirements format
                    (alias to "pip list"). Has no meaning if VENV_NAME
		    is not provided.
  -e, --extended    Show additional information.

------
cdvenv
------

Usage: cdvenv [OPTIONS] VENV_NAME 

cdvenv command changes current working directory to directory of virtual environment specified by VENV_NAME argument. Additional options, that modify this command's behavior are described below.

  -s, --site       Change current working directory to virtual environment's
                   site-packages directory instead.
		   Precludes use of -p option.
  -p, --project    Change current working directory to virtual environment's
                   related project directory instead.
		   Precludes use of -s option.

------
cpvenv
------

Usage: cpvenv [OPTIONS] SRC_VENV_NAME DST_VENV_NAME

cpvenv command creates a copy of virtual environment. It copies all contents of SRC_VENV_NAME virtual environment directory to a new directory for virtual environment with the name specified by DST_VENV_NAME. If PYVENVWRAPPER_PROJ_DIR is set, cpvenv also creates a new project directory related to new virtual environment with DST_VENV_NAME. cpvenv will not overwrite any existing data in DST_VENV_NAME virtual environment directory (and related project directory) if it already exists and is not empty, unless -f option is provided. Additional options, that modify this command's behavior are described below.

**Note**: Depending on the name of source virtual environment destination virtual environment might be broken after copy. This is due to renaming in destination virtual environment which has to take place because of how virtual environments work. Source virtual environment will not be affected in any way. This should normally not happen if the name is unique and not anything more generic like simple "if", "var", etc..

Combined options are not supported, i.e. instead of '-fp' use '-f -p'.

  -f, --force         Overwrite data in DST_VENV_NAME virtual environment
                      directory (and related project directory) if it already
		      exists and is not empty.
  -p, --project       Copy contents of project directory related to
                      SRC_VENV_NAME virtual environment to new project directory
                      related to DST_VENV_NAME virtual environment.
		      Precludes use of -n option.
  -n, --no-project    Don't create project directory.
                      Precludes use of -p option.

------
rmvenv
------

Usage: rmvenv [OPTIONS] VENV_NAME

rmvenv command removes virtual environment directory with the name specified by VENV_NAME. Additional options, that modify this command's behavior are described below.

Combined options are not supported, i.e. instead of '-fp' use '-f -p'.

  **Be cautious when using options!**
  
  -f, --force      Don't prompt for any confirmations. 
  -p, --project    Also remove related project directory with all contents.
