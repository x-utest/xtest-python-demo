echo 'start remove old build'
rm -rf build/
echo 'end remove build'
python setup.py install

echo 'start remove new build'
rm -rf build/
