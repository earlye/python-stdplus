from __future__ import print_function

from stdplus import removeRoot

def test_removeRoot():
    assert("data0" == removeRoot("/data0"))
    assert("data0/a" == removeRoot("/data0/a"))
    assert("data0" == removeRoot("data0"))
    assert("data0/b" == removeRoot("data0/b"))
    
    
