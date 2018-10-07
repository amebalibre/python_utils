# Configparser Module

This module is easy way to use configparser in your project. If you not specify
path and filename for your config file, then use default configuration (`$HOME/conf.ini`).

You can too specify with any values from your path and your config filename. If you
like store config file into dir of project then specify `path=''`.


### Quick start

1.  Import module over your python file `import alu_configparser as alu_cp`.

2.  Initialize a config object `myconf = alu_cp.Configparser().get()`.

3.  Done! You can read your properties from `$HOME/config.ini`.


### Advices

*   By default works with `$HOME/conf.ini` file config.
*   This class are prepared to work with system variables.
*   You can set path and filename on class constructor: `alu_cp.Configparser('arg0', 'arg1')`.
*   A empty path represents path of summoner terminal.
*   You can check if config file have any configuration with: `alu_cp.Configparser().is_loaded()`
*   You can know where is your file config using: `alu_cp.Configparser().where_is()`
*   It's cool specify `/opt/appname/conf.ini` how path for your config file.


### IMPORTANT

**Script was checked on GNU/Linux. Can be used on all platforms but isn't yet tested on Windows and MacOS systems.**
