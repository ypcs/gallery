import boto

from django.conf import settings

def create_signed_url(url, **kwargs):
    """Create new signed CloudFront URL for
    given URL

    See <http://boto.cloudhackers.com/en/latest/ref/cloudfront.html>
    """
    conn = boto.connect_cloudfront(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY)
    dist = conn.get_distribution_info(settings.AWS_CF_ID)

    signed = dist.create_signed_url(url, settings.AWS_KEYPAIR_ID, private_key_string=settings.AWS_KEYPAIR_PRIVATE_KEY, **kwargs)
    return signed
