from unittest import TestCase
from .test_utility import captured_output
from cli.command import main
from subprocess import call, Popen, PIPE
import os
import shutil, tempfile


"""
Tests for the Taco Command Line Utility



Two kinds of tests:
    - tests where we expect success (e.g., using a real taco workflow)
    - tests where we expect failure (e.g., checking exit code is -1 for invalid input options)

We create a unittest TestCase for each kind of test.
Nose will automatically find these tests and run them
when we run python setup.py test.
"""


class TestTacoSuccess(TestCase):
    """
    Class of test cases intended to test
    that taco works.

    This uses the subprocess PIPE var
    to capture system input and output,
    since we are running taco from the 
    command line directly using subprocess.
    """
    @classmethod
    def setUpClass(self):
        """
        Set up a genuine taco workflow test.
        Create a temporary directory, and clone the 
        taco-simple workflow repo there.
        """
        # make temp dir
        #self.tmp = tempfile.mkdtemp()
        self.tmp = '/tmp/likewhateverman'
        call(['mkdir',self.tmp])

        # clone git dir
        clonecmd = ['git','clone','https://github.com/dahak-metagenomics/taco-simple', self.tmp]
        call(clonecmd)

        # now we're ready to run taco commands
        # make sure to set cwd=tmp


    def test_git_clone_worked(self):
        """
        Make sure the setup went smoothly
        """
        b = os.path.isdir( os.path.join(self.tmp,'rules') )
        self.assertTrue(b)


    def test_taco_ls(self):
        """
        In the temporary directory containing the taco-simple 
        workflow, run taco ls. We should see a few workflows
        """
        command = ['taco','ls']
        p = Popen(command, cwd=self.tmp, stdout=PIPE, stderr=PIPE).communicate()

        p_err = p[0].decode('utf-8').strip()
        p_out = p[1].decode('utf-8').strip()

        self.assertIn('workflow1',p_err)
        self.assertIn('workflow2',p_err)
        self.assertIn('workflow3',p_err)


    def test_taco_ls_workflow1(self):
        """
        In the temporary directory containing the taco-simple 
        workflow, run taco ls workflow1.

        Note that this will link taco-simple to taco, 
        so we should "freeze" taco-simple (use a tag)
        to keep taco tests from failing.
        """
        cmd = ['taco','ls','workflow1']
        p = Popen(cmd, cwd=self.tmp, stdout=PIPE, stderr=PIPE).communicate()

        p_err = p[0].decode('utf-8').strip()
        p_out = p[1].decode('utf-8').strip()

        self.assertIn('hello_target',   p_err)
        self.assertIn('goodbye_target', p_err)
        self.assertIn('master',         p_err)



    def test_taco_workflow1(self):
        """
        In the temporary directory containing the taco-simple 
        workflow, run taco workflow1 and specify config/params files.
        
        We also pass workflow config and params files.

        Note that this will link taco-simple to taco, 
        so we should "freeze" taco-simple (use a tag)
        to keep taco tests from failing.
        """
        config_flagname = 'config-yaml'
        config_dirname  = 'workflow-config'
        config_filename = 'workflow1_config_simple.yaml'

        params_flagname = 'params-yaml'
        params_dirname  = 'workflow-params'
        params_filename = 'workflow1_params_simple.yaml'

        cmd = ['taco','workflow1']
        cmd += ['--{}={}/{}'.format(config_flagname,config_dirname,config_filename)]
        cmd += ['--{}={}/{}'.format(params_flagname,params_dirname,params_filename)]

        p = Popen(cmd, cwd=self.tmp, stdout=PIPE, stderr=PIPE).communicate()

        p_err = p[0].decode('utf-8').strip()
        p_out = p[1].decode('utf-8').strip()

        self.assertIn('Finished job', p_out)



    def test_taco_workflow1_fail(self):
        """
        In the temporary directory containing the taco-simple 
        workflow, run taco workflow1 without arguments.
        This should fail.
        """
        config_flagname = 'config-yaml'
        config_dirname  = 'workflow-config'
        config_filename = 'workflow1_config_simple.yaml'

        params_flagname = 'params-yaml'
        params_dirname  = 'workflow-params'
        params_filename = 'workflow1_params_simple.yaml'

        cmd = ['taco','workflow1']

        p = Popen(cmd, cwd=self.tmp, stdout=PIPE, stderr=PIPE).communicate()

        p_err = p[0].decode('utf-8').strip()
        p_out = p[1].decode('utf-8').strip()

        # don't know why, but errors are printed to p_out...???
        # and help is printed to p_err
        self.assertIn('ERROR', p_out)



    @classmethod
    def tearDownClass(self):
        """
        Clean up after the genuine taco workflow test.
        """
        # remove temp dir
        shutil.rmtree(self.tmp)




class TestTacoFail(TestCase):
    """
    Class of test cases intended to test that 
    taco will fail as expected.

    This uses the captured_output() function
    to catpure system input and output, 
    because we are calling the command line utility
    from Python and not the command line itself.
    """

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

    def test_ls_exit_code(self):
        """
        Assert that calling taco ls without arguments or rules
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


