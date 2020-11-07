from subprocess import check_call


def test_peroose_help():
    check_call(["peroose", "--help"])
