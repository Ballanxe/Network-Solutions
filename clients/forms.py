from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from crispy_forms.helper import FormHelper
from crispy_forms import layout, bootstrap

from .models import Client 


class ClientForm(ModelForm):

	class Meta: 

		model=Client
		fields=[
			'name',
			'email',
			'message',
		]


	def __init__(self, *args, **kwargs):
		super(ClientForm, self).__init__(*args, **kwargs)

		self.helper = FormHelper()
		self.helper.form_action = ""
		self.helper.form_method = "POST"
		self.helper.layout = layout.Layout(

			layout.Fieldset(
				_("Formulario de Contacto"),
				layout.Field("name",
					css_class="form-control",
					placeholder="Inserte su nombre"
				),
				layout.Field("email",
					css_class="form-control",
					placeholder="Inserte su correo"
				),
				layout.Field("message",
					css_class="form-control",
					placeholder="Díganos qué necesita"
				),
				bootstrap.FormActions(
					layout.Submit("submit", _("Save")),
				)
			)

		)

















			# 		layout.Field("name",
			# 			css_class="form-control",

			# 		),
			# 		layout.Field("email",
			# 			css_class="form-control"),

			# 		layout.Field("message",
			# 			css_class="form-control",
			# 			rows="2"),
			# 		),
			# ),
			# bootstrap.FormActions(
			# 	layout.Submit("submit", _("Save")),
			# )



