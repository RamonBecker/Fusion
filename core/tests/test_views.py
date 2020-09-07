from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy

class IndexViewTestCase(TestCase):

    def setUp(self):
        self.dados = {
            'nome': 'Felicity Jones',
            'email': 'felicity@gmail.com',
            'assunto': 'Meu assunto',
            'mensagem': 'Minha mensagem'
        }
        self.cliente = Client()

    def test_form_valid(self):
        request = self.cliente.post(reverse_lazy('index'), data=self.dados)
        self.assertEquals(request.status_code, 302) # Houve sucesso no redirecionamento
        # 302 é o código ou status que informa sobre o redirecionamento de uma página ou documento web.

    def test_form_invalid(self):
        dados = {
            'nome': 'Felicity jones',
            'assunto': 'Meu assunto'
        }
        request = self.cliente.post(reverse_lazy('index'), data=dados)
        self.assertEquals(request.status_code, 200) #Verificando se o formulário é válido ou não
        #O código HTTP 200 é a resposta de status de sucesso que indica que a requisição foi bem sucedida