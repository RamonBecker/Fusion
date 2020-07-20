from django.contrib import admin
from .models import Cargo, Funcionario, Servico, Feature


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'modificado')


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'ativo', 'modificado', 'bio', 'facebook', 'instagram', 'twitter', 'imagem')


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'icone', 'ativo', 'modificado')


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('servico', 'icone', 'descricao', 'criado', 'ativo', 'modificado')
