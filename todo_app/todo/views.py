from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, FormView
from django.contrib.auth.views import LoginView
from .models import Tasks, Login, Register
from .forms import RegisterForm,LoginForm



# Create your views here.


#
#
# class CustomLoginView(LoginView):
#     template_name='login.html'
#     fields='__all__'
#     redirect_authenticated_user=True
#
#     def get_success_url(self):
#         return reverse_lazy('task')
# class RegisterPage(FormView):
#     template_name = 'register.html'
#     form_class = UserCreationForm
#     redirect_authenticated_user = True
#     success_url = reverse_lazy('task')
#
#     def form_valid(self, form):
#         user = form.save()
#         if user is not None:
#             login(self.request, user)
#         return super(RegisterPage, self).form_valid(form)
#
#     def get(self, *args, **kwargs):
#         if self.request.user.is_authenticated:
#             return redirect('tasks')
#         return super(RegisterPage, self).get(*args, **kwargs)

class TaskList(ListView):
    model=Tasks
    context_object_name='task'
    template_name='tasklist.html'
class TaskCreate(CreateView):
    model = Tasks
    fields='__all__'
    success_url = reverse_lazy('task')
    template_name = 'taskcreate.html'

class TaskUpdate(UpdateView):
    model = Tasks
    fields = '__all__'
    success_url = reverse_lazy('task')
    template_name = 'taskcreate.html'

class TaskDelete(DeleteView):
    model = Tasks
    fields = '__all__'
    success_url = reverse_lazy('task')
    template_name = 'taskdelete.html'
class TaskDetailView(DetailView):
    model = Tasks
    template_name='taskdetail.html'

def login_fun(request):
    login = Login.objects.all()
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/task-list/')
    context = {'login': login, 'form': form}
    return render(request, 'login.html', context)
def register_fun(request):
    register=Register.objects.all()
    form=RegisterForm()
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/login/')
    context = {'register': register, 'form': form}
    return render(request, 'register.html', context)


