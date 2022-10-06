from calculator import *

def test_multiply():
    assert multiply_string("22*3")=="66"
    assert multiply_string("7*7")=="49"
    assert multiply_string("4*17")=="68"
    assert calculate("15*10")==150
    assert calculate("1*1")==1
    assert calculate("67*0")==0
    assert calculate("1*2*3*4*5")==120

def test_addition():
    assert add_string("1+2")=='3'
    assert add_string("43+377")=="420"
    assert add_string("0+0")=='0'
    assert add_string("1+2+3+4+5")=="15"
    assert calculate("7+21")==28
    assert calculate("65+371")==436
    assert calculate("0+0")==0
    assert calculate("6+7+8+9+10")==40

def test_subtraction():
    assert subtract_string("24-35")=="-11"
    assert subtract_string("54-11")=="43"
    assert subtract_string("10-9-8-7-6")=="-20"
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
