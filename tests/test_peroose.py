import os
from contextlib import contextmanager
from subprocess import check_call, check_output
from tempfile import TemporaryDirectory

import uproot


def test_peroose_help():
    check_call(["peroose", "--help"])


def test_peroose_execute_simple_code():
    message = "Hello World"
    output = check_output(
        ["peroose", "-c", f'print("{message}")'], universal_newlines=True
    )
    assert message in output


@contextmanager
def temprootfile():
    with TemporaryDirectory() as d:
        fname = f"{d}{os.sep}test.root"
        rootfile = uproot.recreate(fname)
        rootfile["tree"] = uproot.newtree({"x": "int32"})
        rootfile["tree"].extend({"x": [1, 2, 3]})
        rootfile.close()
        yield fname


def test_read_root_file():
    with temprootfile() as fname:
        output = check_output(
            ["peroose", "--io", "uproot", "-c", 'print(list(tree["x"]))', fname],
            universal_newlines=True,
        )
        assert "1, 2, 3" in output
