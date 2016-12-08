#!/bin/bash

#also needs java, ewww :'(

mkdir watchers
mkdir jsout
cd watchers; wget https://raw.githubusercontent.com/rpasta42-personal/pywatch/master/pywatch.py; chmod u+x pywatch.py; cd ..
sudo pip install pyinotify
sudo pip3 install transcrypt sh
