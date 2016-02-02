from zope.interface import Interface

class IBoto3Session(Interface):
    """A marker for a boto3.session.Session"""

class IAWSResource(Interface):
    """Marker for an AWS resource"""

class IS3Resource(IAWSResource):
    """Marker for an AWS S3 resource"""

class IS3BucketResource(IAWSResource):
    """Marker for an AWS S3 Bucket resource"""