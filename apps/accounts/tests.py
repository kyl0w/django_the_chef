from django.test import TestCase
from django.urls import reverse
from accounts.models import CustomUser
from django.contrib.auth.forms import AuthenticationForm

class ViewsTest(TestCase):
    def test_home_view(self):
        response = self.client.get(reverse('home'))  # Usando o nome da URL
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

class UserTest(TestCase):

    def test_login_page_renders(self):
        response = self.client.get(reverse('login_view'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')  # Verifique a URL da sua template

    def test_login_success(self):
        # Cria o usuário diretamente no teste (não via POST)
        user = CustomUser.objects.create_user(
            email='testuser@example.com',
            password='securepassword123'
        )
        
        # Testa o login com email e senha corretos
        response = self.client.post(reverse('login'), {
            'username': 'testuser@example.com',
            'password': 'securepassword123'
        })
        
        # Verifica se o usuário existe
        self.assertTrue(CustomUser.objects.filter(email='testuser@example.com').exists())
        
        # Verifica o código de status, deve ser 302 para redirecionamento após login
        self.assertEqual(response.status_code, 302)  # O redirecionamento deve acontecer
        
        # Verifica o redirecionamento para a página inicial
        self.assertRedirects(response, reverse('home'))  # Substitua por sua URL desejada após login

    def test_login_failure(self):
        # Testa o login com credenciais incorretas
        response = self.client.post(reverse('login'), {
            'email': 'wronguser@example.com',
            'password': 'wrongpassword'
        })

        # Verifica que o login falhou e a página de login foi renderizada novamente
        self.assertEqual(response.status_code, 400)
        self.assertTemplateUsed(response, 'accounts/login.html')  # Página de login
