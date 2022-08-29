#!/usr/bin/env python

import json
import pytest
from unittest.mock import Mock, patch

from gc2 import gc2

from mock.gc2_mock import GC2_BASEURL


class TestGc2Auth(object):
    # @classmethod
    # def setup_class(cls):
    #     cls.mock_get_patcher = patch("gc2.gc2.Gc2.requests.get")
    #     cls.mock_get = cls.mock_get_patcher.start()
    #
    # @classmethod
    # def teardown_class(cls):
    #     cls.mock_get_patcher.stop()

    def test_gc2_base(self):
        testgc2 = gc2.Gc2(GC2_BASEURL)
        assert isinstance(testgc2, gc2.Gc2)

    def test_auth(self):
        """Test the authentication setting."""
        # self.mock_get.return_value = Mock()
        # self.mock_get.return_value.status_code = 401
        # self.mock_get.return_value.text = json.dumps(version_resp_text)

        testgc2= gc2.Gc2(GC2_BASEURL)
        assert isinstance(testgc2, gc2.Gc2)

        try:
            testgc2.set_authentication("myd", "hawk2000")
        except Exception as e:
            raise pytest.fail(f"Authentication raises: {e}")

    # def test_wrong_auth(self):
    #     """Test the behavior when a wrong authentication is set."""
    #     # Configure the mock
    #     self.mock_get.return_value = Mock()
    #     self.mock_get.return_value.status_code = 200
    #     # self.mock_get.return_value.text = json.dumps(version_resp_text)
    #
    #     testactinia = gc2.Gc2(GC2_BASEURL)
    #     assert isinstance(testactinia, gc2.Gc2)
    #
    #     # check wrong auth behavior
    #     self.mock_get.return_value = Mock()
    #     self.mock_get.return_value.status_code = 401
    #
    #     with pytest.raises(Exception) as e:
    #         testactinia.set_authentication("user", "pw")
    #
    #     assert e.type == Exception
    #     assert (
    #         str(e.value) == "Wrong user or password. Please check your inputs."
    #     )
