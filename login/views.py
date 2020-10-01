from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from Home.models import fichas
def cadastro(request):
    if request.method == 'POST':
        username = request.POST['username']
        nome = request.POST['nome']
        sobrenome = request.POST['sobrenome']
        email = request.POST['email']
        senha = request.POST['senha']
        senha2 = request.POST['senha2']
        sexo = request.POST['sexo']
        if not username.strip():
            print('O campo Username não pode ficar em branco')
            return redirect('cadastro')
        if not nome.strip():
            print('O campo nome não pode ficar em branco')
            return redirect('cadastro')
        if not sobrenome.strip():
            print('O campo sobrenome não pode ficar em branco')
            return redirect('cadastro')
        if not email.strip():
            print('O campo email não pode ficar em branco')
            return redirect('cadastro')
        if senha != senha2:
            print('As senhas não são iguais')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            print('Usuário já cadastrado')
            return redirect('cadastro')
        if User.objects.filter(username=username).exists():
            print('Usuário já cadastrado')
            return redirect('cadastro')
        user = User.objects.create_user(username=username, email=email, password=senha,first_name=nome, last_name =sobrenome)
        user.save()
        print('Usuário cadastrado com sucesso')
        return redirect('login')
    else:
        return render(request,'registrar.html')
    return render(request,'registrar.html')

def login(request):
    if request.method == 'POST':
        usuario =  request.POST['usuario']
        senha = request.POST["senha"]
        if usuario == "" or senha == "":
            print('Os campos email e senha não podem ficar em branco')
            print(usuario, senha)
            return render(request,'login.html')
        if User.objects.filter(email=usuario).exists():
            nome = User.objects.filter(email=usuario).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                print('Login realizado com sucesso')
                return redirect('dashboard')
            print(nome)
        user = auth.authenticate(request, username=usuario, password=senha)
        if user is not None:
            auth.login(request, user)
            print('Login realizado com sucesso')
            return redirect('dashboard')

        return render(request,'login.html')

    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def dashboard(request):
    
    ficha = fichas.objects.all()
    
    dados={
        'fichas' : ficha
    }
    if request.user.is_authenticated:
        return render(request,'dashboard.html',dados)
    else:
        return redirect('index')
    