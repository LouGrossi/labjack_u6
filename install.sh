# for MacOS

# get homebrew
sh -c "$(curl -fsSL https://raw.githubusercontent.com/Linuxbrew/install/master/install.sh)"
# install exodriver
  brew updatebrew upgrade \
  && brew install exodriver
pip install -r requirements.txt
