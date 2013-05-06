from Products.CMFCore.utils import getToolByName
from ll.policy.tests.base import IntegrationTestCase


class TestCase(IntegrationTestCase):
    """TestCase for Plone setup."""

    def setUp(self):
        self.portal = self.layer['portal']

    def test_package_installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('ll.policy'))

    def test_metadata__dependency__Products_PFGExtendedMailAdapter(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('PFGExtendedMailAdapter'))

    def test_metadata__dependency__Products_PFGSelectionStringField(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('PFGSelectionStringField'))

    def test_metadata__dependency__abita_development(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('abita.development'))

    def test_metadata__dependency__collective_folderlogo(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('collective.folderlogo'))

    def test_metadata__dependency__collective_microsite(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('collective.microsite'))

    def test_metadata__dependency__collective_pfg_payment(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('collective.pfg.payment'))

    def test_metadata__dependency__collective_pfg_showrequest(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('collective.pfg.showrequest'))

    def test_metadata__dependency__collective_prettyphoto(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('collective.prettyphoto'))

    def test_metadata__dependency__sll_basepolicy(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('sll.basepolicy'))

    def test_metadata__dependency__ll_theme(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('ll.theme'))

    def test_metadata__version(self):
        setup = getToolByName(self.portal, 'portal_setup')
        self.assertEqual(setup.getVersionForProfile('profile-ll.policy:default'), u'1')

    def test_uninstall__package(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['ll.policy'])
        self.failIf(installer.isProductInstalled('ll.policy'))
