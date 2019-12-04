#!/bin/sh

echo "Removing old repo..."
rm -r /home/robot/sumo
cd /home/robot
echo "Cloning..."
git clone https://github.com/cole-wilson/sumo.git
cd sumo
echo "Updated 'sumo'"
