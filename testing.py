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
    assert calculate("1+2+3+4+5")==15

def test_subtraction():
    assert calculate("2-1")==1
    assert calculate("1-2")==-1
    assert calculate("1-2-3-4-5")==-13

def test_multi_op():
    assert calculate("1+2*3")==7
    assert calculate("1+2-3")==0
    assert calculate("3*4-1")==11
    assert calculate("8+6-7*4+3-2*6")==-23

def test_neg_values():
    assert calculate("-1+2")==1
    assert calculate("1+-2")==-1
    assert calculate("-4*5")==-20
    assert calculate("5*-4")==-20
    assert calculate("1--2")==3
    assert calculate("-1--2")==1
