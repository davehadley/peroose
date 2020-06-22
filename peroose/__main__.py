import contextlib
import argparse
import glob
import os
import sys
from typing import List, Iterable

from IPython import start_ipython
from traitlets.config import get_config

import peroose
from peroose.fileio import IOMode, loadtree, loadfile

# Import modules the user is very likely to want to use
np = None
plt = None
uproot = None
ROOT = None
with contextlib.suppress(ImportError):
    import numpy as np
with contextlib.suppress(ImportError):
    import matplotlib.pyplot as plt
with contextlib.suppress(ImportError):
    import uproot


def _matchfilepattern(pattern: str) -> List[str]:
    return glob.glob(os.path.abspath(os.path.expandvars(os.path.expanduser(pattern))))


def _findfiles(patterns: Iterable[str]) -> List[str]:
    return list(sorted(m for p in patterns for m in _matchfilepattern(p)))


def _parsecml() -> argparse.Namespace:
    parser = argparse.ArgumentParser("peroose")
    parser.add_argument("input_files",
                        nargs="+",
                        type=str,
                        help="Input ROOT files. Unix shell-style glob patterns are allowed (eg \"*.root\").")
    parser.add_argument("--tree", type=str, default=None,
                        help="Name of tree to load. If not, specified, a tree will automatically selected."
                        )
    parser.add_argument("--io", type=IOMode, choices=list(IOMode), default=IOMode.ROOT,
                        help="IO method to use."
                        )
    return parser.parse_args()


if __name__ == "__main__":
    args = _parsecml()
    filelist = _findfiles(args.input_files)
    header = f"{__package__} ({peroose.__version__}) [{peroose.url}]"
    config = get_config()
    config.InteractiveShellApp.display_banner = False
    config.InteractiveShellApp.exec_lines = [
        # ROOT needed to be imported inside the ipython shell, otherwise GUI won't work.
        'print(header)',
        '''with contextlib.suppress(ImportError):
            import ROOT
        ''',
        'filelist = _findfiles(args.input_files)',
        'tree = loadtree(filelist, args.tree, args.io)',
        'print(f"{len(filelist)} files found.")',
        'print(f"tree = {tree}")'
    ]
    sys.exit(start_ipython([], config=config, user_ns={**locals(), **globals()}))
