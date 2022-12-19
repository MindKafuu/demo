from django.views.generic import ListView,TemplateView,FormView,UpdateView
from django.views.generic.edit import FormMixin
from django.http import Http404
from django.core.paginator import InvalidPage
from django.utils.translation import gettext as _
from django.contrib import messages
from django.http import JsonResponse

from collections import OrderedDict
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSetFactory, NamedFormsetsMixin

class BigBaseView:
    bottons = []

    def get_bottons(self):
        """
        Floating Action Button
        """
        bottons = self.bottons
        return bottons

    def get_columns(self):
        columns = OrderedDict()
        try:
            for f in getattr(self.model, '_meta').get_fields():
                if hasattr(f, 'verbose_name'):
                    columns.update({f.name: f.verbose_name})
        except:
            pass
        return columns

class TitleFormsetsMixin(NamedFormsetsMixin):
    inlines_titles = []

    def get_inlines_titles(self):
        return self.inlines_titles

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        inlines = kwargs.get('inlines', [])
        inlines_titles = self.get_inlines_titles()

        if inlines and inlines_titles:
            for index, inline in enumerate(inlines):
                if inlines_titles[index]:
                    setattr(inline, "title", inlines_titles[index])

        return context

class BigInlineFormSetFactory(InlineFormSetFactory):
    can_add = True

class BigCreateWithInlinesView(TitleFormsetsMixin, CreateWithInlinesView):
    """
    Custom Create Inline Form.
    """
    bottons = []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['botton'] = self.get_bottons()
        return context

    def get_bottons(self):
        """
        Floating Action Button
        """
        bottons = self.bottons
        return bottons

    def get_success_url(self):
        success_url = super().get_success_url()
        storage = messages.get_messages(self.request)
        storage.used = True
        messages.add_message(self.request, messages.SUCCESS, 'บันทึกสำเร็จ')
        return success_url

    def construct_inlines(self):
        construct_inlines = super().construct_inlines()
        inlines = super().get_inlines()
        for idx, inline in enumerate(construct_inlines):
            klass = inlines[idx]
            if hasattr(klass, 'can_add'):
                setattr(inline, 'can_add', getattr(klass, 'can_add'))
        return construct_inlines

class BigUpdateWithInlinesView(TitleFormsetsMixin, UpdateWithInlinesView):
    """
    Custom Create Inline Form.
    """
    bottons = []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['botton'] = self.get_bottons()
        return context

    def get_bottons(self):
        """
        Floating Action Button
        """
        bottons = self.bottons
        return bottons

    def get_success_url(self):
        success_url = super().get_success_url()
        storage = messages.get_messages(self.request)
        storage.used = True
        messages.add_message(self.request, messages.SUCCESS, 'บันทึกสำเร็จ')
        return success_url

    def construct_inlines(self):
        construct_inlines = super().construct_inlines()
        inlines = super().get_inlines()
        for idx, inline in enumerate(construct_inlines):
            klass = inlines[idx]
            if hasattr(klass, 'can_add'):
                setattr(inline, 'can_add', getattr(klass, 'can_add'))
        return construct_inlines

class BigListView(FormMixin, ListView):
    paginate_by = 25
    allow_empty = True
    bottons = []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['columns'] = self.get_columns()
        context['botton'] = self.get_bottons()
        return context

    def get_columns(self):
        columns = OrderedDict()
        for f in getattr(self.model, '_meta').get_fields():
            if hasattr(f, 'verbose_name'):
                columns.update({f.name: f.verbose_name})
        return columns

    def get_form_kwargs(self):
        return {
            'initial': self.get_initial(),
            'prefix': self.get_prefix(),
            'data': self.request.GET or None
        }

    def get_bottons(self):
        """
        Floating Action Button
        """
        bottons = self.bottons
        return bottons

    def get_queryset(self):
        queryset = super().get_queryset()
        form = self.get_form(self.get_form_class())
        if form.is_valid():
            queryset = form.filter_queryset(self.request, queryset)
        return queryset

    def paginate_queryset(self, queryset, page_size):
        paginator = self.get_paginator(
            queryset, page_size, orphans=self.get_paginate_orphans(),
            allow_empty_first_page=self.get_allow_empty())
        page_kwarg = self.page_kwarg
        page = self.kwargs.get(page_kwarg) or self.request.GET.get(page_kwarg) or 1

        # Fixed error if form values and page number changed without submit button
        page = page if int(page) <= paginator.num_pages else 1

        try:
            page_number = int(page)
        except ValueError:
            if page == 'last':
                page_number = paginator.num_pages
            else:
                raise Http404(_("Page is not 'last', nor can it be converted to an int."))
        try:
            page = paginator.page(page_number)
            return (paginator, page, page.object_list, page.has_other_pages())
        except InvalidPage as e:
            raise Http404(_('Invalid page (%(page_number)s): %(message)s') % {
                'page_number': page_number,
                'message': str(e)
            })

class BigFormView(FormView,BigBaseView):
    # bottons = []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['columns'] = self.get_columns()
        context['botton'] = self.get_bottons()
        return context

    # def get_columns(self):
    #     columns = OrderedDict()
    #     for f in getattr(self.model, '_meta').get_fields():
    #         if hasattr(f, 'verbose_name'):
    #             columns.update({f.name: f.verbose_name})
    #     return columns

    def get_form_kwargs(self):
        return {
            'initial': self.get_initial(),
            'prefix': self.get_prefix(),
            'data': self.request.GET or None
        }

    # def get_bottons(self):
    #     """
    #     Floating Action Button
    #     """
    #     bottons = self.bottons
    #     return bottons

class BigUpdateView(UpdateView,BigBaseView):
    # bottons = []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['columns'] = self.get_columns()
        context['botton'] = self.get_bottons()
        return context

    # def get_columns(self):
    #     columns = OrderedDict()
    #     for f in getattr(self.model, '_meta').get_fields():
    #         if hasattr(f, 'verbose_name'):
    #             columns.update({f.name: f.verbose_name})
    #     return columns
    #
    # def get_bottons(self):
    #     """
    #     Floating Action Button
    #     """
    #     bottons = self.bottons
    #     return bottons

class JSONResponseMixin:
    """
    A mixin that can be used to render a JSON response.
    """
    def render_to_json_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        return JsonResponse(
            self.get_data(context),
            **response_kwargs
        )

    def get_data(self, context):
        """
        Returns an object that will be serialized as JSON by json.dumps().
        """
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return context

class JSONView(JSONResponseMixin, TemplateView):
    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(context, **response_kwargs)