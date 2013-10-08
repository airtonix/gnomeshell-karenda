#!/usr/bin/env python
#
#  Unit tests for karenda

import unittest
import datetime
from karenda import backend


class TestGnomeGoogleCalendar(unittest.TestCase):

    def test_GetMonthKey(self):
        from time import strftime, localtime

        def tostr(timestamps):
            return [strftime('%Y%m%d %H%M%S', localtime(stamp)) for stamp in timestamps]

        self.assertEqual(
            tostr(backend.get_month_key(
                datetime.datetime(2011, 12, 12))),
            ['20111127 000000', '20111231 235959'])
        self.assertEqual(tostr(
            backend.get_month_key(
                datetime.datetime(2011, 11, 1))),
            ['20111030 000000', '20111203 235959'])
        self.assertEqual(tostr(
            backend.get_month_key(
                datetime.datetime(2011, 1, 31))),
            ['20101226 000000', '20110205 235959'])
        self.assertEqual(tostr(
            backend.get_month_key(
                datetime.datetime(2012, 1, 31))),
            ['20120101 000000', '20120204 235959'])
