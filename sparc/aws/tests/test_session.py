import unittest
from doctest import DocTestSuite
from doctest import DocFileSuite

import sparc.aws

def test_suite():
    return unittest.TestSuite((
        DocFileSuite('session.txt',
                     package=sparc.aws),))

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')