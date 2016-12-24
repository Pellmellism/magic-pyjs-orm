#!/bin/bash

#also needs java, ewww :'(

mkdir watchers
mkdir jsout

cd watchers; wget https://raw.githubusercontent.com/rpasta42-personal/myutils/master/pywatch/pywatch.py; sudo chmod u+x pywatch.py; cd ..
sudo pip3 install pyinotify sh
pip3 install transcrypt
