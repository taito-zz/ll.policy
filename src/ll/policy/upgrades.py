from Products.CMFCore.utils import getToolByName

import logging


PROFILE_ID = 'profile-ll.policy:default'


def install_packages(context, names, logger=None):
    """Installs package."""
    if logger is None:
        logger = logging.getLogger(__name__)

    installer = getToolByName(context, 'portal_quickinstaller')
    if not isinstance(names, list):
        names = [names]
    for name in names:
        logger.info('Installing {}.'.format(name))
        installer.installProduct(name)


def upgrade_0_to_1(context, logger=None):
    """Install collective.folderlogo"""
    if logger is None:
        logger = logging.getLogger(__name__)

    install_packages(context, 'collective.folderlogo', logger)
