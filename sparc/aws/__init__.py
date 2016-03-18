from sparc.i18n import SparcMessageFactory
MessageFactory = SparcMessageFactory('sparc.aws')


#Interface imports start here
from interfaces import IAWSResource
from interfaces import IBoto3Session
from interfaces import IS3BucketResource
from interfaces import IS3Resource