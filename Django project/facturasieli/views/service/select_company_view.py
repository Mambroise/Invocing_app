# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/views/service/select_company_view.py
# Author : Morice
# ---------------------------------------------------------------------------
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from facturasieli.forms.searchForm import SearchForm
from facturasieli.models import Company

def search_company(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('facturasieli:custom_log_in'))
    
    companies = []

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data['search']
            try:
                companies = Company.objects.filter(name__icontains=search)
            except Company.DoesNotExist:
                companies = None

            if not companies :
                try:
                    companies = Company.objects.filter(siret__icontains=search)
                except Company.DoesNotExist:
                    companies = None
    else:
        form = SearchForm()

    context = {"form": form, "companies": companies}
    return render(request, "facturasieli/service/select_company.html", context)