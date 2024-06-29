#!/usr/bin/env python3
""" GithubOrgClient """
from client import GithubOrgClient
from utils import get_json
from parameterized import parameterized
import unittest
from unittest.mock import patch, MagicMock, PropertyMock
from fixtures import TEST_PAYLOAD
from typing import Dict


class TestGithubOrgClient(unittest.TestCase):
    """Tests the `GithubOrgClient` class."""
    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch(
        "client.get_json",
    )
    def test_org(self, org: str, resp: Dict, mocked_fxn: MagicMock) -> None:
        """Tests the `org` method."""
        mocked_fxn.return_value = MagicMock(return_value=resp)
        gh_org_client = GithubOrgClient(org)
        self.assertEqual(gh_org_client.org(), resp)
        mocked_fxn.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org)
        )

    def test_public_repos_url(self) -> None:
        """ test_public_repos_url """
        with patch(
              'client.GithubOrgClient.org',
              new_callable=PropertyMock
              ) as mock_org:
            mock_org.return_value = {
                'repos_url': 'https://api.github.com/orgs/google/repos'
            }
            self.assertEqual(
                GithubOrgClient('google')._public_repos_url,
                'https://api.github.com/orgs/google/repos'
            )
