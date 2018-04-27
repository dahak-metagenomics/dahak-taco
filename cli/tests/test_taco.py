from unittest import TestCase
from .test_utility import captured_output
from .test_utility2 import hello
from cli.command import main

class TestTaco(TestCase):

    def test_tests(self):
        """
        Sanity check
        """
        def hello():
            print('hello world')
        with captured_output() as (out, err):
            hello()
        output = out.getvalue().strip()
        self.assertEqual(output, 'hello world')

    def test_ls(self):
        """
        Assert that calling taco ls 
        without arguments or rules
        will result in an exit code -1
        """
        with self.assertRaises(SystemExit) as cm:
            with captured_output() as (out, err):
                main(["ls"])
            output = out.getvalue().strip()
            #self.assertIn('ERROR',output)

        # Exception objects have .error_code attribute
        # SystemExit objects have .code
        # https://stackoverflow.com/a/15672165
        the_exception = cm.exception
        self.assertEqual(the_exception.code, -1)

