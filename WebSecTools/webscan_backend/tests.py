from django.test import TestCase

from webscan_backend.plugins.check.common import check_ip


# Create your tests here.
def haha():
    check_ip("128.0.0.1")

haha()
