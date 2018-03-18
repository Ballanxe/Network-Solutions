from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

# Create your models here.


@python_2_unicode_compatible
class Client(models.Model):

	name = models.CharField(_('Name'), max_length=40, null=False, default=None, blank=False)
	email = models.EmailField(_('Email'), null=False, blank=False, default=None)

	message = models.TextField(_('Message'), null=True, blank=True)

	date_created = models.DateField(verbose_name='Creation Date', auto_now_add=True)


	def __str__(self):
		return self.name

