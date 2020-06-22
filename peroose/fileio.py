from enum import Enum
from typing import Union, List, Optional, Any


class IOMode(Enum):
    ROOT = "ROOT"
    uproot = "uproot"


def loadtree(filelist: List[str], tree: Optional[str], mode: IOMode = IOMode.ROOT) -> Union[Any, None]:
    if (mode == IOMode.ROOT):
        return _loadtree_root(filelist, tree)
    elif (mode == IOMode.uproot):
        return _loadtree_uproot(filelist, tree)


def loadfile(filename: str, mode: IOMode = IOMode.ROOT) -> Union[Any, dict, None]:
    if (mode == IOMode.ROOT):
        import ROOT
        return ROOT.TFile(filename)
    elif (mode == IOMode.uproot):
        import uproot
        return uproot.open(filename)


def _loadtree_root(filelist: List[str], tree: Optional[str]) -> Optional[Any]:
    import ROOT
    chain = None
    for fname in filelist:
        tfile = ROOT.TFile(fname)
        if tree is None:
            trees = [(key.GetName(), key.ReadObj().GetEntriesFast()) for key in tfile.GetListOfKeys() if
                     key.GetClassName() == "TTree"]
            tree = None if len(trees) == 0 else max(trees, key=lambda p: p[1])[0]
        if tree is not None:
            t = tfile.Get(tree)
            if t and t.IsA().InheritsFrom("TTree"):
                if chain is None:
                    chain = ROOT.TChain(tree, tree)
                chain.Add(fname)
    return chain


def _loadtree_uproot(filelist: List[str], tree: str) -> Optional[dict]:
    import uproot
    chain = []
    for fname in filelist:
        tfile = uproot.open(fname)
        if tree is None:
            items = tfile.allitems(filterclass=lambda cls: issubclass(cls, uproot.tree.TTreeMethods))
            tree = max(items, key=lambda i: len(i[1]))[0]
        if tree is not None:
            if tree in tfile:
                chain.append(fname)
    return None if len(chain) == 0 else uproot.lazyarrays(chain, tree)
