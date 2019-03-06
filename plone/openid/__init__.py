from AccessControl.Permissions import manage_users as ManageUsers
from Products.PluggableAuthService.PluggableAuthService import registerMultiPlugin

from plone.openid import config

if not config.HAS_OPENID and not config.HAS_OIDC:
    import logging
    logger=logging.getLogger("Plone")
    logger.info("Neither OpenID nor OpeinID Connect system packages installed,"
                " OpenID support not available")
elif not config.HAS_SSL:
    import logging
    logger=logging.getLogger("Plone")
    logger.info("Python does not have SSL support. OpenID support not available")
    config.HAS_OPENID=False
    config.HAS_OIDC = False
elif config.HAS_OIDC:
    config.HAS_OPENID = False
    from plugins import oidc
    registerMultiPlugin(oidc.OpenIdPlugin.meta_type)
else:
    from plugins import oid
    registerMultiPlugin(oid.OpenIdPlugin.meta_type)



def initialize(context):
    if config.HAS_OPENIDC:
        context.registerClass(oidc.OpenIdPlugin,
                                permission=ManageUsers,
                                constructors=
                                        (oidc.manage_addOpenIdPlugin,
                                        oidc.addOpenIdPlugin),
                                visibility=None,
                                icon="www/openid.png")

    elif config.HAS_OPENID:
        context.registerClass(oid.OpenIdPlugin,
                                permission=ManageUsers,
                                constructors=
                                        (oid.manage_addOpenIdPlugin,
                                        oid.addOpenIdPlugin),
                                visibility=None,
                                icon="www/openid.png")

