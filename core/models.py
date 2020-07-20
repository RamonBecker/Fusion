from django.db import models
from stdimage.models import StdImageField
import uuid  # G era valores hexadecimais diferentes, aleatórios


# Função para evitar duplicação de nomes de imagens, e renomear o nome da imagem com hash
def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    criado = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now_add=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

    def __str__(self):
        return "'{}' '{}' '{}'".format(self.criado, self.modificado, self.ativo)


class Servico(Base):
    ICONE_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    )

    servico = models.CharField('Serviço', max_length=100)
    descricao = models.TextField('Descricao', max_length=200)
    icone = models.CharField('Icone', max_length=20, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return "'{}' '{}' '{}'".format(self.servico, self.descricao, self.icone)


class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return "'{}'".format(self.cargo)


class Funcionario(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    imagem = StdImageField('Imagem', upload_to=get_file_path,
                           variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return "'{}' '{}' '{}' '{}' '{}' '{}'".format(self.nome, self.cargo, self.bio, self.facebook, self.twitter,
                                                      self.instagram)


class Feature(Base):

    ICONE_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-rocket', 'Foguete'),
        ('lni-laptop-phone', 'Computador'),
        ('lni-leaf', 'Folha_Arvores'),
        ('lni-layers', 'Multiplos_Templates'),
        ('lni-leaf', 'Contato_Trabaho'),

    )
    servico = models.CharField('Serviço', max_length=100)
    descricao = models.TextField('Descricao', max_length=200)
    icone = models.CharField('Icone', max_length=20, choices=ICONE_CHOICES)

    def __str__(self):
        return "'{}' '{}' '{}'".format(self.servico, self.descricao, self.icone)
