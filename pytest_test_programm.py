import math as m
import pytest as pt
import pytest_programm as pt_p

def test_pos_int_diff():
    assert pt_p.equalize(1, 2) == 5.1962

def test_negative_numbers():
    assert pt_p.equalize(2, -1) == 0.3333

def test_zero():
    with pt.raises(ZeroDivisionError) as er:
        assert pt_p.equalize(2, 2) in str(er.value)

def test_positive_numbers():
    assert pt_p.equalize(0.2, 0.1) == 1.6432

def test_negative_root():
    assert pt_p.equalize(1, -2) == "Can't sqrt negative"

def test_error_input():
    assert pt_p.equalize("werwerer", 0) == "This is not number"
    assert pt_p.equalize("", 0) == "This is not number"
    assert pt_p.equalize("10**-9", 0) == "This is not number"