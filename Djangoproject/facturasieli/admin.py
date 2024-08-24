# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/admin.py
# Author : Team
# ---------------------------------------------------------------------------

from django.contrib import admin

from facturasieli.models import Invoice, Profile, Role, Service


admin.site.register(Profile)
admin.site.register(Invoice)
admin.site.register(Role)
admin.site.register(Service)
