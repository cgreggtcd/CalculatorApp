from calculator import *

def test_multiply():
    assert calculate("15*10")==150
    assert calculate("1*1")==1
    assert calculate("67*0")==0
    assert calculate("1*2*3*4*5")==120

def test_addition():
    assert calculate("1+2")==3
    assert calculate("43+377")==420
    assert calculate("0+0")==0
    assert calculate("1+2+3+4+5")==6
