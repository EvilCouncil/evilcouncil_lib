""" Unit tests for HttpYamlConfigLoader."""

import unittest
from http import HTTPStatus
from unittest import mock
import requests
from eclib.config import http_yaml_config_loader


class HttpYamlConfigLoaderTest(unittest.TestCase):
    """The unit tests."""

    @mock.patch.object(requests, "get")
    def test_create_config_loader(self, mock_request):
        """Verify that constructor works."""
        mock_response = mock.MagicMock()
        mock_response.status_code = HTTPStatus.OK
        mock_response.text = """---
        top_key:
            sub_key1: value_1
            sub_key2: value_2
        """
        mock_request.return_value = mock_response

        loader = http_yaml_config_loader.HttpYamlConfigLoader(
            "http://192.0.2.1/config.yaml"
        )
        self.assertIsNotNone(loader)

    @mock.patch.object(requests, "get")
    def test_config_loader_key(self, mock_request):
        """Test that config loading works."""
        mock_response = mock.MagicMock()
        mock_response.status_code = HTTPStatus.OK
        mock_response.text = """---
        top_key:
            sub_key1: value_1
            sub_key2: value_2
        """
        mock_request.return_value = mock_response

        loader = http_yaml_config_loader.HttpYamlConfigLoader(
            "http://192.0.2.1/config.yaml"
        )
        actual_key = loader.get_config("top_key.sub_key1")
        self.assertEqual(actual_key, "value_1")
