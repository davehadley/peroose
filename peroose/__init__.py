"""A python-based command line tool to peruse ROOT (https://root.cern.ch/) files.

Examples
--------

python -m peroose /path/to/root/files/*.root

python -m peroose --help

"""

from peroose import _version

__version__ = _version.__version__
__license__ = "MIT"
__author__ = "David Hadley"

url = "https://github.com/davehadley/peroose"
