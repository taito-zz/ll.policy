from sll.basepolicy.upgrades import install_packages


PROFILE_ID = 'profile-ll.policy:default'


def upgrade_0_to_1(context):
    """Install collective.folderlogo"""
    install_packages(context, 'collective.folderlogo')
