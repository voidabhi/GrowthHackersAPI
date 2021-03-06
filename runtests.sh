# shell script for running tests

# activate virtualenv
source venv/bin/activate

python setup.py develop

# install coveralls
pip install coveralls
echo "======================================================================"
echo
if [ "$1" == "remote" ] ; then
    REMOTE=true python -m unittest discover tests -v
else 
    python -m unittest discover tests -v
fi
echo "======================================================================"
echo
coverage report -m
echo "======================================================================"
coveralls
echo "======================================================================"
yes | pip uninstall GrowthHackers
yes | pip uninstall coveralls
