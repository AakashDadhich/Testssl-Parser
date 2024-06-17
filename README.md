# Testssl CSV Parser - Python3
Python3 script to parse CSV output files from [testssl.sh](https://github.com/drwetter/testssl.sh). 
## Setup 
1. Download `testssl-parser.py` and place it wherever you keep your scripts.
2. **OPTIONAL:** add an alias into your `~/.zshrc` or `~/.bashrc` file:

`alias parse-testssl=python3 {path-to-file}/testssl-parser.py`

## Usage
After downloading the script, it can be ran using `python3` via the command line and providing the `.csv` file as an argument:

`python3 testssl-parser.py {path-to-file}.csv`

If you completed the optional setup step of adding it as an alias, then you can simply run the following from any directory:

`parse-testssl {path-to-file}.csv`

Once ran, an output file named `parsed-testssl.txt` will be created in the current working directory. It can be opened in your favourite text editor, or viewed on the command line by running:

`cat parsed-testssl.txt`
