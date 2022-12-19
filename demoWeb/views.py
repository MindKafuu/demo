from demoWeb.extends.viewext import BigFormView

from . import forms

# Create your views here.
class Start(BigFormView):
    template_name = 'index.html'
    form_class = forms.MenuList
    prefix = "main"




