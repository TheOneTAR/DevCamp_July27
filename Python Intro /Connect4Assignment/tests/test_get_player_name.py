__author__ = 'TheOneTAR'

import unittest
from connect4_view import View
from unittest.mock import patch
from io import StringIO

long_name = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."\
            "Pellentesque mi nibh, iaculis molestie neque eget, faucibus "\
            "interdum leo. Sed viverra ipsum urna, eget placerat tellus "\
            "hendrerit a. Fusce et ligula vitae ligula facilisis tempus sit"\
            "amet ut lacus. Nulla non tellus id arcu pharetra euismod."\
            "Praesent congue urna ac ornare porttitor."


class Connect4GetPlayerNameTest(unittest.TestCase):
    """Test the Get Player Name prompt from the View"""

    def setUp(self):
        self.view = View()

    def tearDown(self):
        del self.view

    @patch('builtins.input', return_value='Rob-E')
    def test_normal_name(self, input):
        """Ensure that the view will return a string that is input."""
        name = self.view.get_player_name()
        self.assertEqual(name, 'Rob-E')

    @patch('builtins.input', return_value='')
    @patch('sys.stdout', new_callable=StringIO)
    def test_no_name(self, output, inputted_value):
        """

        :param output:
        :param inputted_value:
        :return:
        """
        with open('bin/names.txt') as f:
            names = [line.rstrip() for line in f]
        name = self.view.get_player_name()
        self.assertIn(name, names, "Random name generation failed")

    @patch('builtins.input', return_value=long_name)
    @patch('sys.stdout', new_callable=StringIO)
    def test_long_name(self, output, inputted_value):
        """Ensure that the view will return a more reasonably sized name."""
        name = self.view.get_player_name()

        long_name_error = "Wow, that's an impressive name.\n" \
                          "How about we call you Lorem? Hi, Lorem!\n"

        self.assertEqual(output.getvalue(), long_name_error,
                         "The long name was not shortened")
        if len(name) > 20:
            self.assertTrue(False, "The name is still too long.")
            return

        self.assertIn(name, long_name)


if __name__ == '__main__':
    unittest.main()
