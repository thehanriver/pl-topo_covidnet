
from unittest import TestCase
from unittest import mock
from topo_covidnet.topo_covidnet import Topo_covidnet


class Topo_covidnetTests(TestCase):
    """
    Test Topo_covidnet.
    """
    def setUp(self):
        self.app = Topo_covidnet()

    def test_run(self):
        """
        Test the run code.
        """
        args = []
        if self.app.TYPE == 'ds':
            args.append('inputdir') # you may want to change this inputdir mock
        args.append('outputdir')  # you may want to change this outputdir mock

        # you may want to add more of your custom defined optional arguments to test
        # your app with
        # eg.
        # args.append('--custom-int')
        # args.append(10)

        options = self.app.parse_args(args)
        self.app.run(options)

        # write your own assertions
        self.assertEqual(options.outputdir, 'outputdir')
