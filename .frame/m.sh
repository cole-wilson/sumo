rm -rf sumo
git clone http://github.com/cole-wilson/sumo
ssh robot@ev3dev.local prep
sftp robot@ev3dev.local:/home/robot <<< $'put -rf sumo'
echo 'PUSHED'
echo 'PUSHED'