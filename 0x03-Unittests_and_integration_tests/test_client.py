#!/usr/bin/env python3
"""test module testing client.py"""
import json
import unittest
from client import GithubOrgClient
from unittest.mock import patch, PropertyMock, Mock
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class


class TestGithubOrgClient(unittest.TestCase):
    """tests github org client """
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """test organization if returned correctly by URL"""
        github_org_client = GithubOrgClient(org_name)

        result = github_org_client.org()

        expected_url = GithubOrgClient.ORG_URL.format(org=org_name)
        mock_get_json.assert_called_once_with(expected_url)

    """Test public repos url if they return the expected
    amount in payload"""

    def test_public_repos_url(self):
        """Test public repos url if they return the expected
        amount in payload"""
        m_payload = {"repos_url": "https://api.github.com/orgs/testorg/repos"}

        with patch.object(GithubOrgClient, 'org', new_callable=PropertyMock,
                          return_value=m_payload):
            github_org_client = GithubOrgClient("testorg")

            result = github_org_client._public_repos_url

            expected_url = "https://api.github.com/orgs/testorg/repos"
            self.assertEqual(result, expected_url)

    @patch('client.get_json')
    @patch('client.GithubOrgClient._public_repos_url',
           new_callable=PropertyMock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """Test public repos url if they return the expected
        amount in payload on the specified payload"""
        mock_payload = [{"name": "repo1"}, {"name": "repo2"}]
        mock_get_json.return_value = mock_payload

        github_org_client = GithubOrgClient("testorg")
        result = github_org_client.public_repos()

        expected_repos = ["repo1", "repo2"]
        self.assertEqual(result, expected_repos)

        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """tests if the repo has a license or not and is it getting an
        expected result"""
        github_org_client = GithubOrgClient("testorg")

        result = github_org_client.has_license(repo, license_key)

        self.assertEqual(result, expected_result)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD,
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Tests for GithubOrgClient using actual data from GitHub API."""
    @classmethod
    def setUpClass(cls):
        """Hook method for setting up class fixtures before
        tests in this class are run."""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        cls.mock_get.side_effect = [
            unittest.mock.Mock(json=lambda: cls.org_payload),
            unittest.mock.Mock(json=lambda: cls.repos_payload),
        ]

    @classmethod
    def tearDownClass(cls):
        """Tear down any resources,
        like, connections to databases.
        in this case it tears down the class used for testing"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Check that public repos can be retrieved correctly"""
        github_org_client = GithubOrgClient("testorg")

        result = github_org_client.public_repos()

        self.assertEqual(result, self.expected_repos)
