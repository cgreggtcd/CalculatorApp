from calculator import *

def test_multiply():
    assert calculate("15*10")==150
    assert calculate("1*1")==1
    assert calculate("67*0")==0
    assert calculate("1*2*3*4*5")==120

def test_addition():
    assert calculate("7+21")==28
    assert calculate("65+371")==436
    assert calculate("0+0")==0
    assert calculate("6+7+8+9+10")==40

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
    assert calculate("-1*20")==-20
    assert calculate("-5*-5")==25
    assert calculate("7*-6")==-42
    assert calculate("120*-82")==-9840

# Confirms that the multiply string function works correctly internally
def test_multiply_string():
    assert multiply_string("1+2*3")=="1+6"
    assert multiply_string("1+2*-3")=="1+-6"
    assert multiply_string("-2*3")=="-6"
    assert multiply_string("1-2*-3")=="1--6"
    assert multiply_string("136+120*-82")=="136+-9840"
    
# Confirms that the subtract string function works correctly internally
def test_subtract_string():
    assert subtract_string("24-35")=="-11"
    assert subtract_string("54-11")=="43"
    assert subtract_string("10-9-8-7-6")=="-20"

# Confirms that the subtract string function works correctly internally
def test_add_string():
    assert add_string("1+2")=='3'
    assert add_string("43+377")=="420"
    assert add_string("0+0")=='0'
    assert add_string("1+2+3+4+5")=="15"

def test_resolve_signs():
    assert resolve_signs("1+-2")=="1-2"
    assert resolve_signs("1-+2")=="1-2"
    assert resolve_signs("11--22")=="11+22"
    assert resolve_signs("11+22")=="11+22"
