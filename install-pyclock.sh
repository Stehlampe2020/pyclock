#!/bin/bash

echo "Installing as \"pyclock\"..."
sudo mkdir /usr/share/pyclock 2> /dev/null
cat << '**ENDOFFILE**' > pyclock.tmp
#!/bin/sh
python3 /usr/share/pyclock/pyclock.py $@
**ENDOFFILE**
sudo mv $HOME/pyclock/pyclock.tmp /bin/pyclock
sudo cp $HOME/pyclock/pyclock.py /usr/share/pyclock/pylock.py
echo "Making \"pyclock\" executable..."
sudo chmod +x /bin/pyclock
echo "Installing as \"clock\" by creating a soft link to \"pyclock\", if that doesn't already exist..."
if [ -f "/bin/clock" ] || [ -d "/bin/clock" ]
then
	echo "\"/bin/clock\" does already exist, not overwriting it!"
else
	echo "\"/bin/clock\" did not already exist, creating symbolic link to \"pyclock\"."
	sudo ln -s /bin/pyclock /bin/clock
fi

echo "Creating uninstall script..."
cat << '**ENDOFFILE**' > uninstall-pyclock.sh
#!/bin/bash

sudo rm -vr /usr/share/pyclock
sudo rm -v /bin/pyclock
if [ "$1" == "--rm-clk" ]
then
sudo rm -v /bin/clock
fi
rm uninstall-pyclock.sh
**ENDOFFILE**
chmod +x uninstall-pyclock.sh

echo "Showig info about pyclock:"
pyclock -i
echo "Starting pyclock:"
pyclock
