from utils import utils

def test_reversed():
    assert utils.reversed(4065) == 5604, "Case 1 Fail"
    assert utils.reversed("hello") == None, "Case 2 Fail"
    assert utils.reversed("264") == 462, "Case 3 Fail"
    assert utils.reversed(45.7) == None, "Case 4 Fail"
    assert utils.reversed("25.87") == None, "Case 5 Fail"

def test_formatter():
    assert utils.formatter(170)[0] == 10101010, "Case 1 Fail"
    assert utils.formatter("hello")[0] == None, "Case 2 Fail"
    assert utils.formatter("25")[0] == 462, "Case 3 Fail"
    assert utils.formatter(45.7)[0] == None, "Case 4 Fail"
    assert utils.formatter("25.87")[0] == None, "Case 5 Fail"
    assert utils.formatter(325)[1] == 505, "Case 6 Fail"
    assert utils.formatter("hello")[1] == None, "Case 7 Fail"
    assert utils.formatter("47")[1] == 57, "Case 8 Fail"
    assert utils.formatter(45.7)[1] == None, "Case 9 Fail"
    assert utils.formatter("25.87")[1] == None, "Case 10 Fail"