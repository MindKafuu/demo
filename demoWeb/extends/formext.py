from django import forms
from ..contrib.sysdate import dateFromLocal

class DateBigInput(forms.DateInput):
    def value_from_datadict(self, data, files, name):
        valData = super().value_from_datadict(data, files, name)
        return dateFromLocal(valData)

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['attrs']['data-provide'] = 'datepicker'
        context['widget']['attrs']['data-date-language'] = 'th-th'
        # context['widget']['attrs']['data-date-startdate'] = '-10d'
        # context['widget']['attrs']['data-date-enddate'] = '+10d'
        context['widget']['attrs']['class'] = 'form-control'
        return context

class NumberBigInput(forms.TextInput):
    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['attrs']['data-inputmask-alias'] = 'currency'
        context['widget']['attrs']['class'] = 'form-control'
        return context

class TextBigInput(forms.TextInput):
    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['attrs']['class'] = 'form-control'
        return context

class DecimalBigInput(forms.TextInput):
    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['attrs']['data-inputmask-alias'] = 'currency'
        context['widget']['attrs']['class'] = 'form-control'
        return context

class IntegerBigInput(forms.TextInput):
    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['attrs']['data-inputmask-alias'] = 'integer'
        context['widget']['attrs']['class'] = 'form-control'
        return context

# class ChoiceBigSelect(forms.Select):
#     def get_context(self, name, value, attrs):
#         context = super().get_context(name, value, attrs)
#         context['widget']['attrs']['class'] = 'form-control'
#         return context

class FormMixinBig:
    use_required_attribute = False
    readonly = []
    field_require = []
    currency = []
    # selectChoice = []

    def form_init(self):
        self.__WidgetBase()
        self.__FieldBase()

    def __FieldBase(self):
        for field in iter(self.fields):
            self.fields[field].required = False
            fieldType = self.fields[field].widget.__class__.__name__
            if fieldType not in ['Select', 'Select2','HiddenInput']:
                clsAttr = self.fields[field].widget.attrs.get('class','')
                if clsAttr.find('form-control') < 0 :
                    self.fields[field].widget.attrs['class'] = '{} form-control'.format(clsAttr)

            if fieldType in ['DateInput', 'DateTimeInput']:
                self.fields[field].widget = DateBigInput()
            if field in self.currency:
                self.fields[field].widget = NumberBigInput()

            if field in self.readonly or self.readonly == 'all':
                self.fields[field].widget.attrs['readonly'] = True
                if fieldType in ['DateInput', 'DateTimeInput']:
                    self.fields[field].widget.attrs['disabled'] = True

            if field in self.field_require or self.field_require == 'all':
                self.fields[field].required = True
                # if self.fields[field].label and not self.fields[field].label[0:1] == '*':
                #     self.fields[field].label = '*{}'.format(self.fields[field].lable)

    def __WidgetBase(self):
        if not hasattr(self,'Meta') : return
        if not hasattr(self.Meta, 'widgets'): return
        for widget in self.Meta.widgets:
            fieldType = self.Meta.widgets[widget].__class__.__name__
            if fieldType not in ['Select', 'Select2','HiddenInput']:
                clsAttr = self.Meta.widgets[widget].attrs.get('class', '')
                if clsAttr.find('form-control') < 0:
                    self.Meta.widgets[widget].attrs['class'] = '{} form-control'.format(clsAttr)


class BaseEditModelForm(forms.ModelForm,FormMixinBig):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.form_init()

    def clean(self):
        super().clean()
        for f in self.cleaned_data:
            if not self.cleaned_data[f] and not self.cleaned_data[f] == 0:
                self.cleaned_data[f] = None

class BaseEditForm(forms.Form,FormMixinBig):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.form_init()
