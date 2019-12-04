#!/bin/sh

echo "Removing old repo..."
rm -r /home/robot/sumo
cd /home/robot
echo "Cloning..."
git clone https://github.com/cole-wilson/sumo.git
cd sumo
echo "Marking as executable..."
chmod +x *.py
echo "Updated 'sumo'"
echo
$run = "run() {echo 'running'$1; python3 '$1'}"

$run >> ~/.bashrc

echo "To run type `run *.py`"
