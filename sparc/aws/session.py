from boto3.session import Session
from zope.component.factory import Factory
from zope.interface import alsoProvides
from zope.interface import implements
from sparc.aws import IBoto3Session

class Boto3Session(object):
    """Generate a boto3.session.Session marked with IBoto3Session"""
    implements(IBoto3Session)
    
    def __new__(self, *args, **kwargs):
        session = Session(*args, **kwargs)
        alsoProvides(session, IBoto3Session)
        return session

boto3SessionFactory = Factory(Boto3Session)