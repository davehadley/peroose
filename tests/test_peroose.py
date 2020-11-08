from subprocess import check_call, check_output


def test_peroose_help():
    check_call(["peroose", "--help"])


def test_peroose_execute_simple_code():
    message = "Hello World"
    output = check_output(
        ["peroose", "-c", f'print("{message}")'], universal_newlines=True
    )
    assert message in output
