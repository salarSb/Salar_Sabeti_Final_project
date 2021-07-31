from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from sale.forms import QuoteItemForm
from sale.models import QuoteItem, Quote


class QuotesList(LoginRequiredMixin, ListView):
    model = Quote
    extra_context = {
        'page_title': 'Quotes'
    }

    def get_queryset(self):
        qs = super(QuotesList, self).get_queryset()
        qs = qs.filter(owner=self.request.user)
        return qs


class CreateQuote(PermissionRequiredMixin, CreateView):
    model = QuoteItem
    form_class = QuoteItemForm
    success_url = reverse_lazy('organizations:list-organizations')
    extra_context = {
        'page_title': 'Submit Quote'
    }
    permission_required = ['sale.add_quote', 'sale.add_quoteitem']

    def get_form_kwargs(self):
        kwargs = super(CreateQuote, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        quote_instance = Quote.objects.create(owner=self.request.user)
        form.instance.quote = quote_instance
        return super(CreateQuote, self).form_valid(form)
