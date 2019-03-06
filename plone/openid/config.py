import pkg_resources

try:
    pkg_resources.get_distribution('openid.yadis')
except pkg_resources.DistributionNotFound:
    HAS_OPENID = False
else:
    HAS_OPENID = True

try:
    pkg_resources.get_distribution('oic')
except pkg_resources.DistributionNotFound:
    HAS_OIDC = False
else:
    HAS_OIDC = True

import socket
HAS_SSL = hasattr(socket, "ssl")
del socket
