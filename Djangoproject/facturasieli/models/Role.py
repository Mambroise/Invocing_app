# ---------------------------------------------------------------------------
#                    F a c t u r a S i e l i   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : facturasieli/models/Role.py
# Author : Arnaud, Zineb
# ---------------------------------------------------------------------------

from django.db import models


class Role(models.Model):
    role = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.role
