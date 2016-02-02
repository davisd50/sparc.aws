from sparc.i18n import SparcMessageFactory
MessageFactory = SparcMessageFactory('sparc.aws')


# Configuration (this package only)
from importlib import import_module
from sparc.configuration.zcml import Configure as SparcConfigure
def Configure():
    SparcConfigure([import_module(__name__)])

#Interface imports start here
from interfaces import IAWSResource
from interfaces import IBoto3Session
from interfaces import IS3BucketResource
from interfaces import IS3Resource