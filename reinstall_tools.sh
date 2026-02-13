rm -rf ./tools/__pycache__
rm -rf ./tools/mytools.egg-info

pip uninstall mytools
pip install -e ./tools/