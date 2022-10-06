from calculator import *

def test_multiply():
    assert calculate("15*10")==150
    assert calculate("1*1")==1
    assert calculate("67*0")==0
    assert calculate("1*2*3*4*5")==120
    assert calculate("-1*20")==-20
    assert calculate("-5*-5")==25
    assert calculate("7*-6")==-42
    assert calculate("120*-82")==-9840

def test_addition():
    assert calculate("1+2")==3
    assert calculate("43+377")==420
    assert calculate("0+0")==0
    assert calculate("1+2+3+4+5")==15

# Confirms that the multiply string function works correctly internally
def test_multiply_string():
    assert multiply_string("1+2*3")=="1+6"
    assert multiply_string("1+2*-3")=="1+-6"
    assert multiply_string("-2*3")=="-6"
    assert multiply_string("1-2*-3")=="1--6"
    assert multiply_string("136+120*-82")=="136+-9840"
