# peroose

A python-based command line tool to peruse ROOT (https://root.cern.ch/) files.

## Installation

```bash
pip install peroose
```

## Usage

To inspect a ROOT file:
```bash
python -m peroose path/to/root/files/*.py
```

This will load the TTree (if the file contains one) and start an IPython
REPL. The following variables will be defined:
* `filelist : List[str]` list of files found.
* `tree : Optional[TTree]` the ROOT TTree found.  

```python
print(filelist) # see the files that were found.
tree.Draw("branch_name") # make a plot!
``` 

For more options see:
```bash
python -m peroose --help
```