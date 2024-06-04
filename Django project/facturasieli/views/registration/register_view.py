# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/views/registration/register_view.py
# Author : Zineb
# ---------------------------------------------------------------------------

from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from facturasieli.forms import ProfileForm

def register(request: HttpRequest):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            form.save_m2m()  # Save the many-to-many data for roles
            return HttpResponseRedirect(reverse('facturasieli:welcome'))
    else:
        form = ProfileForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context)