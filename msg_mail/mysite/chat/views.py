import json
from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect, reverse
from django.utils.safestring import mark_safe

User = get_user_model()


# home page for chat app
def home(request):
    return render(request, 'chat/home.html')


"""
Following method is is used for display the all registered users
"""


@login_required(login_url='home')
def user_list(request):
    # store all logged in users in to users object
    users = User.objects.select_related('logged_in_user')

    """
    hasattr method is use to check if an object has 
    the given named attribute and return true if present, else false.
    hasattr(object, key)
    """

    # set user status
    for user in users:
        user.status = 'Online' if hasattr(user, 'logged_in_user') else 'Off-line'
    return render(request, 'example/user_list.html', {'users': users})


"""
login method use for login any user, 
if it is valid user otherwise print error and again login page display
"""


def log_in(request):
    login_form = AuthenticationForm()

    # check if request type is 'POST' or 'GET'
    if request.method == 'POST':
        login_form = AuthenticationForm(data=request.POST)

        # check user is valid or not
        if login_form.is_valid():
            # if valid then this user is authenticate and it able to go forward
            login(request, login_form.get_user())
            return redirect(reverse('example:user_list'))
        else:
            # if not valid then print error
            print(login_form.errors)

    # if request is GET type then return same page
    return render(request, 'example/log_in.html', {'form': login_form})


# this method is accessible only when user is logged in
@login_required(login_url='/login/')
def log_out(request):
    logout(request)
    return redirect(reverse('example:log_in'))


# if any new user want to register the this first have to register
def sign_up(request):
    registrationForm = UserCreationForm()

    if request.method == 'POST':
        registrationForm = UserCreationForm(data=request.POST)

        # check all new information is valid or not
        if registrationForm.is_valid():
            registrationForm.save()
            return redirect(reverse('example:log_in'))
        else:
            # if not valid then print error
            print(registrationForm.errors)
    return render(request, 'example/sign_up.html', {'form': registrationForm})


# following method is use for create a chat room by any register and logged in user
@login_required
def create_Chat_Room(request):
    return render(request, 'chat/index.html', {})


# this method use for communication in a created chat room after creating it
@login_required
def chat_room(request, room_name):
    users = User.objects.select_related('logged_in_user')

    for user in users:
        user.status = 'Online' if hasattr(user, 'logged_in_user') else 'off-line'

    return render(request, 'chat/room.html', {"room_name_json": mark_safe(json.dumps(room_name)), 'users': users})
