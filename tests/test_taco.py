#!/usr/bin/env python
import sys
import unittest
from subprocess import Popen, PIPE

def run_tests():
    class __unit_tests__(unittest.TestCase):
        def setUp(self):
            # no setup
            pass 

        def tearDown(self):
            # no tear down
            pass

        def test_taco_ls(self):
            command = ['taco','ls']
            p = Popen(command, stdout=PIPE, stderr=PIPE).communicate()
            
            p_err = p[0].decode('utf-8')
            p_out = p[1].decode('utf-8')

            self.assertFalse(False)

            # other xamples:
            # self.assertEqual(fp.readline(), 'This is a test')
            # self.assertFalse(os.path.exists('a'))
            # self.assertTrue(os.path.exists('a'))
            # self.assertTrue('already a backup server' in c.stderr)
            # self.assertIn('fun', 'disfunctional')
            # self.assertNotIn('crazy', 'disfunctional')
            # with self.assertRaises(Exception):
            #     raise Exception('test')

    suite = unittest.TestLoader().loadTestsFromTestCase(__unit_tests__)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    if 'test' in sys.argv[1:]:
        run_tests()
        sys.exit(0)

