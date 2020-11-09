from django.db import models
from stdimage.models import StdImageField
import uuid  # G era valores hexadecimais diferentes, aleatórios
from django.utils.translation import gettext_lazy as _

# Função para evitar duplicação de nomes de imagens, e renomear o nome da imagem com hash
def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    criado = models.DateField(_('Criação'), auto_now_add=True)
    modificado = models.DateField(_('Atualização'), auto_now_add=True)
    ativo = models.BooleanField(_('Ativo?'), default=True)

    class Meta:
        abstract = True



class Servico(Base):
    ICONE_CHOICES = (
        ('lni-cog', _('Engrenagem')),
        ('lni-stats-up', _('Gráfico')),
        ('lni-users', _('Usuários')),
        ('lni-layers', _('Design')),
        ('lni-mobile', _('Mobile')),
        ('lni-rocket', _('Foguete')),
    )

    servico = models.CharField(_('Serviço'), max_length=100)
    descricao = models.TextField(_('Descricao'), max_length=200)
    icone = models.CharField(_('Icone'), max_length=20, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = _('Serviço')
        verbose_name_plural = _('Serviços')

    def __str__(self):
        return self.servico


class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = _('Cargo')
        verbose_name_plural = _('Cargos')

    def __str__(self):
        return self.cargo


class Funcionario(Base):
    nome = models.CharField(_('Nome'), max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name=_('Cargo'), on_delete=models.CASCADE)
    bio = models.TextField(_('Bio'), max_length=200)
    imagem = StdImageField(_('Imagem'), upload_to=get_file_path,
                           variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField(_('Facebook'), max_length=100, default='#')
    twitter = models.CharField(_('Twitter'), max_length=100, default='#')
    instagram = models.CharField(_('Instagram'), max_length=100, default='#')

    class Meta:
        verbose_name = _('Funcionário')
        verbose_name_plural = _('Funcionários')

    def __str__(self):
        return self.nome


class Feature(Base):
    ICONE_CHOICES = (
        ('lni-cog', _('Engrenagem')),
        ('lni-rocket', _('Foguete')),
        ('lni-laptop-phone', _('Computador')),
        ('lni-leaf', _('Folha_Arvores')),
        ('lni-layers', _('Multiplos_Templates')),
        ('lni-leaf', _('Contato_Trabaho')),

    )
    servico = models.CharField(_('Serviço'), max_length=100)
    descricao = models.TextField(_('Descricao'), max_length=200)
    icone = models.CharField(_('Icone'), max_length=20, choices=ICONE_CHOICES)

    def __str__(self):
        return self.servico
