# PyClock
This is a very simple Python3.8-based terminal clock.   
It syncronizes with the internal system clock every 10 seconds.   
Note: that just corrects the numbers, not the waiting times themselves, so the clock may be up to one second off real-time!   

# install-pyclock.sh
This script copies `pyclock.py` to `/usr/bin/pyclock/pyclock.py` and installs that as a command by creating a script in `/bin/pyclock` that just starts python3 with `/usr/bin/pyclock/pyclock.py`. It does also install it as `clock` by creating a symbolic link `/bin/clock` that links to `/bin/pyclock`.   
After that it starts `pyclock` to see if it works.   
Note: somehow python3 says that `/usr/bin/pyclock/pyclock.py` is not there even though it surely is. 

# uninstall-pyclock.sh
This script will be created by `./install-pyclock.sh` and can be run with or without the argument `--rm-clk`.   
* If you run it without `--rm-clk` it won't do anything with `/bin/clock`.   
* If you run it with `--rm-clk` it will delete `/bin/clock`.   
   
After that it deletes itself but lets all of the other files in the downloaded folder unchanged. 
