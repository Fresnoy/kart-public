# -*- encoding: utf-8 -*-
from django.core.management import call_command
from io import StringIO
from django.test import TestCase


class CommandsTestCase(TestCase):
    """
    Tests School Commands
    """

    def setUp(self):
        self.out = StringIO()

    def tearDown(self):
        pass
