from django.test import TestCase
from log.models import Plane

class TestPlane(TestCase):
	def test_unicode(self):
		expected = u'%s' % '321BL'
		plane = Plane(call_number=expected)
		self.assertEquals(expected, plane.__unicode__())
