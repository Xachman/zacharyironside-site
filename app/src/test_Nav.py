import unittest
from src import Nav

class TestNav(unittest.TestCase):

    def test_makelink(self):
        nav = Nav.Nav("")

        self.assertEqual(nav.makeLink("/", "Home"), '<li class="active"><a href="/">Home</a></li>')

