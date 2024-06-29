#!/usr/bin/env python3
""" GithubOrgClient """
from client import GithubOrgClient
from utils import get_json
from parameterized import parameterized, parameterized_class
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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json) -> None:
        """ test_public_repos """
        payload = {
            'username': 'donatello',
            'quote': 'we die with dying, we born with the dead'
        }
        mock_get_json.return_value = payload
        with patch(
             'client.GithubOrgClient._public_repos_url',
             new_callable=PropertyMock,
             return_value=payload
             ) as mock_public_repos:
            self.assertEqual(
                GithubOrgClient('google').org,
                GithubOrgClient('google')._public_repos_url
            )
            mock_get_json.assert_called_once()
            mock_public_repos.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, 'my_license'),
        ({"license": {"key": "other_license"}}, 'my_license')
    ])
    def test_has_license(self, repo: Dict, license_key: str) -> None:
        """ test has license """
        GithubOrgClient.has_license(repo, license_key)


def requests_get(*args, **kwargs):
    """
    Function that mocks requests.get function
    Returns the correct json data based on the given input url
    """
    class MockResponse:
        """
        Mock response
        """
        def __init__(self, json_data):
            self.json_data = json_data

        def json(self):
            return self.json_data

    if args[0] == "https://api.github.com/orgs/google":
        return MockResponse(TEST_PAYLOAD[0][0])
    if args[0] == TEST_PAYLOAD[0][0]["repos_url"]:
        return MockResponse(TEST_PAYLOAD[0][1])


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    [(TEST_PAYLOAD[0][0], TEST_PAYLOAD[0][1],
      TEST_PAYLOAD[0][2], TEST_PAYLOAD[0][3])]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ TestIntegrationGithubOrgClient """
    @classmethod
    def setUpClass(cls) -> None:
        """
        Set up function for TestIntegrationGithubOrgClient class
        Sets up a patcher to be used in the class methods
        """
        cls.get_patcher = patch('utils.requests.get', side_effect=requests_get)
        cls.get_patcher.start()
        cls.client = GithubOrgClient('google')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.get_patcher.stop()

    def test_public_repos(self) -> None:
        """ test_pubilc_repos """
        self.assertEqual(
            GithubOrgClient('google').public_repos(),
            self.expected_repos
        )
