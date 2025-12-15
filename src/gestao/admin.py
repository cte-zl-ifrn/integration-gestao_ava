from django.utils.translation import gettext as _
from django.utils.html import format_html
from django.db.models import Model
from django.contrib.admin import register, display, TabularInline
from base.admin import BaseModelAdmin
from gestao.models import Cliente


@register(Cliente)
class ClienteAdmin(BaseModelAdmin):
    list_display = ("nome", "dominio", "is_active", "created_on")
    search_fields = ("nome", "dominio")
    readonly_fields = ("created_on", )
    list_filter = ("is_active", )