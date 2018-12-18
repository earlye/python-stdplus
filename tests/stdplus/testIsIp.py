from __future__ import print_function
import sys

from nose.core import run
from nose.core import unittest

from pprint import pprint

from stdplus._sshConfig import parseSshConfig
from stdplus import *

def test_isIp_InvalidSamples():
    assert(not isIp( "Obviously not an ip" )) # obvious
    assert(not isIp( "16" )) # obvious
    assert(not isIp( "1234.123.123.123" )) # first octet is too long
    assert(not isIp( "123.1234.123.123" )) # second octet is too long
    assert(not isIp( "123.123.1234.123" )) # third octet is too long
    assert(not isIp( "123.123.123.1234" )) # fourth octet is too long
    assert(not isIp( "12a.123.123.123" )) # first octet contains alpha
    assert(not isIp( "123.12a.123.123" )) # second octet contains alpha
    assert(not isIp( "123.123.12a.123" )) # third octet contains alpha
    assert(not isIp( "123.123.123.12a" )) # fourth octet contains alpha
    assert(not isIp( "192.168.1.1.32" )) # too many octets
    assert(not isIp( "foo.192.168.1.1" )) # too many octets, leading octet not even a number

def test_isIp_validSamples():
    assert(isIp( "8.8.8.8" )) # all octets single digits
    assert(isIp( "18.18.18.18" )) # all octets two digits
    assert(isIp( "192.168.100.200" )) # all octets 3 digits
