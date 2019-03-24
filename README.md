# SimpleRelay
Simple Discord Relay Bot

## Installation instructions
rename config.py.example to config.py and fill out as required.
install discord.py from the rewrite branch using the following
  `pip3 install -U git+https://github.com/Rapptz/discord.py@rewrite#egg=discord.py`
install the rest of the deps using the requirements file
run the file using python3 in the same directory (needs to be same working directory to pick up config)
to run as a service I reccomend supervisor but use whatever you are comfortable with.
