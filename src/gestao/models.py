from django.utils.translation import gettext as _
from django.db.models import CharField, DateField, Model, BooleanField


class Cliente(Model):
    nome = CharField(_("nome do cliente"), max_length=256)
    dominio = CharField(_("domínio"), max_length=512, unique=True)
    is_active = BooleanField(_("ativo?"), default=True)
    created_on = DateField(_("criado em"), auto_now_add=True)

    class Meta:
        verbose_name = _("cliente")
        verbose_name_plural = _("clientes")
        ordering = ["nome"]
