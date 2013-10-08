import unittest
from . import basics


if __name__ == "__main__":
    tests = unittest.TestLoader().loadTestsFromTestCase(
        basics.TestGnomeGoogleCalendar)
    unittest.TextTestRunner(verbosity=2).run(tests)
