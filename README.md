# PyClock
This is a very simple Python3.8-based terminal clock.   
It syncronizes with the internal system clock every second.   
I will re-write the program even further than in release 1.2, to make it syncronize with the system clock ten times a second or more.   
Note: that just corrects the numbers, not the waiting times themselves, so the clock may be up to one second off real-time!   

# install-pyclock.sh
This script installs the latest version of `__pycache__/pyclock-cpython38.pyc`, renamed to `pyclock` and installs that as a command by moving it to `/bin/pyclock`. It does also install it as `clock` by creating a symbolic link `/bin/clock` that links to `/bin/pyclock`.   
After that it starts `pyclock` to see if it works. 
