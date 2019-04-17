i=15
if [ $i -lt 14 ]
then
echo 'it is cold'
fi
if [ $i -gt 14 && $i -lt 35 ]
then 
echo 'normal'
fi
if [ $i -gt 35 ]
then
echo 'its hot'
fi
