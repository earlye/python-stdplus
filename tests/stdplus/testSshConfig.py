from __future__ import print_function

from stdplus._sshConfig import parseSshConfig
from stdplus import readSshConfig

def test_parseSshConfig():
    result = parseSshConfig("Host 192.168.*\n"
                            + "     User ec2-user\n"
                            + "     IdentityFile /Users/earlye/.ssh/identity.pem\n"
                            + "     ProxyCommand ssh -q -i /Users/earlye/.ssh/id_rsa.pub -W %h:%p earlye@some-bastion.somewhere.com\n")
    assert( '192.168.*' in result.hosts )
    assert( 'ProxyCommand' in result.hosts['192.168.*'].settings)
    assert( 1 == len(result.hosts['192.168.*'].settings['ProxyCommand']) )
    assert( result.hosts['192.168.*'].settings['ProxyCommand'][0].value == 'ssh -q -i /Users/earlye/.ssh/id_rsa.pub -W %h:%p earlye@some-bastion.somewhere.com' )

def test_readSshConfig():
    result = readSshConfig()

