from Products.CMFCore.utils import getToolByName
from ll.policy.tests.base import IntegrationTestCase


class TestCase(IntegrationTestCase):
    """TestCase for Plone setup."""

    def setUp(self):
        self.portal = self.layer['portal']

    def test_install_package(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['collective.folderlogo'])
        self.assertFalse(installer.isProductInstalled('collective.folderlogo'))

        from ll.policy.upgrades import install_packages
        install_packages(self.portal, 'collective.folderlogo')

        self.assertTrue(installer.isProductInstalled('collective.folderlogo'))
