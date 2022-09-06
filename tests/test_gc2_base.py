#!/usr/bin/env python

import json
import pytest
from unittest.mock import Mock, patch

from gc2 import Gc2

from .mock.gc2_mock import GC2_BASEURL, GC2_USER, GC2_DB, GC2_PWD


class TestGc2Auth(object):
    def test_gc2_base(self):
        testgc2 = Gc2(GC2_BASEURL)
        assert isinstance(testgc2, Gc2)

    def test_auth(self):
        testgc2 = Gc2(GC2_BASEURL)
        assert isinstance(testgc2, Gc2)

        try:
            testgc2.set_authentication(GC2_USER, GC2_PWD, GC2_DB)
        except Exception as e:
            raise pytest.fail(f"Authentication raises: {e}")

