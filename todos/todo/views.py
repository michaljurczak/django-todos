from django.shortcuts import render, redirect
from .forms import CreateUserForm, TodoForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from .decoratos import unauthenticated_user, allowed_users

from .models import Todo
# Create your views here.


# @login_required(login_url='sign_in')
# @allowed_users(allowed_roles=['customer'])

REQ_TYPES = (
    'all',
    'to_do',
    'done'
)

def update_todo(request, todo_id, space):
    todo = Todo.objects.get(id=todo_id)
    todo.is_completed = not todo.is_completed
    todo.save()
    return redirect(to=f"/{request.user}/{space}")

def home_view(request, username, req_type):
    if (username != str(request.user)) or (req_type not in REQ_TYPES):
        return redirect(to=f"/{request.user}/all")
    if request.method == "GET":
        user = User.objects.get(username=request.user)
        if req_type == REQ_TYPES[0]:
            todos = user.todo_set.all()
        elif req_type == REQ_TYPES[1]:
            todos = user.todo_set.filter(is_completed=False)
        elif req_type == REQ_TYPES[2]:
            todos = user.todo_set.filter(is_completed=True)

    if request.method == "POST":
        new_todo = TodoForm(request.POST)
        if new_todo.is_valid():
            new_record = new_todo.save(commit=False)
            new_record.is_completed = False
            new_record.user = request.user
            new_record.save()
        return redirect(to=f"/{request.user}/all")
    
    context = {'todos': todos, 'form': TodoForm, 'space': req_type}
    return render(request, 'todo/home.html', context)


def logoutUser(request):
    logout(request)
    return redirect('/')


@unauthenticated_user
def sign_in_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(to=f'/{request.user}/all')
    context = {}
    return render(request, 'todo/sign_in.html', context)


@unauthenticated_user
def sign_up_view(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            return redirect(to='/')
    context = {'form': CreateUserForm}
    return render(request, 'todo/sign_up.html', context)
