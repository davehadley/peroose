# peroose

[![Github Build Status](https://img.shields.io/github/workflow/status/davehadley/peroose/ci?label=Github%20Build)](https://github.com/davehadley/peroose/actions?query=workflow%3Aci)
[![PyPI](https://img.shields.io/pypi/v/peroose)](https://pypi.org/project/peroose/)
[![License: MIT](https://img.shields.io/pypi/l/peroose)](https://github.com/davehadley/peroose/blob/master/LICENSE.txt)
[![Last Commit](https://img.shields.io/github/last-commit/davehadley/peroose/dev)](https://github.com/davehadley/peroose)

A python-based command line tool to peruse ROOT (https://root.cern.ch/) files.

## Installation

```bash
pip install peroose
```

## Usage

To inspect a ROOT file:
```bash
python -m peroose path/to/root/files/*.root
```

This will load the TTree (if the file contains one) and start an IPython
REPL. The following variables will be defined:
* `filelist : List[str]` list of files found.
* `tree : Optional[TTree]` the ROOT TTree found.
* `tfile : Optional[TFile]` the first ROOT TFile found.

Usage examples:
```python
print(filelist) # see the files that were found.
tree.Draw("branch_name") # make a plot!
tfile.ls() # use the TFile
br = TBrowser() # inspect files in the TBrowser
``` 

For convenience, the following are imported into the REPL local scope:
```python
import numpy as np
import matplotlib.pyplot as plt
import ROOT.TFile as TFile # only if pyROOT is installed
import ROOT.TBrowser as TBrowser # only if pyROOT is installed
```

For more options see:
```bash
python -m peroose --help
```