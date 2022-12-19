from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div

from dal import autocomplete
from dal import forward

from demoWeb.extends import formext


class MenuList(formext.BaseEditForm):

    main = forms.ChoiceField(label='Main Dishes',
                                    widget=autocomplete.ListSelect2(url='demoWeb:lookup_mainDishes',
                                                                     attrs={'data-placeholder': 'Select Main...'},
                                                                     forward=[forward.Const(1, 'stat')]))

    dessert = forms.ChoiceField(label='Dessert Dishes',
                                    widget=autocomplete.ListSelect2(url='demoWeb:lookup_dessertDishes',
                                                                     attrs={'data-placeholder': 'Select Dessert ...'},
                                                                     forward=[forward.Field('main', '1')]))

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-sm-2'
    helper.field_class = 'col-sm-6'
    helper.form_tag = False
    helper.layout = Layout(
        Div(
            Div('main'),
            Div('dessert'),
            css_class='form-group'),
    )