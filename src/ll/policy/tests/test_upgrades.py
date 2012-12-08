from ll.policy.tests.base import IntegrationTestCase

import mock


class TestCase(IntegrationTestCase):
    """TestCase for Plone setup."""

    def setUp(self):
        self.portal = self.layer['portal']

    @mock.patch('ll.policy.upgrades.install_packages')
    def test_upgrade_0_to_1(self, install_packages):
        from ll.policy.upgrades import upgrade_0_to_1
        upgrade_0_to_1(self.portal)

        install_packages.assert_called_with(self.portal, 'collective.folderlogo')
