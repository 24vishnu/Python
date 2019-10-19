import json
import logging

import jwt
from django.contrib import messages
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.utils.safestring import mark_safe
from django.views.decorators.csrf import csrf_exempt

from .event_emitter import ee
from .forms import SignupForm
from .models import ChatRoom

User = get_user_model()
file_dir = __file__
file_dir = file_dir.replace('views.py', 'chat_logfile.log')
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename=file_dir,
                    level=logging.DEBUG,
                    format=LOG_FORMAT, filemode='w')
logger = logging.getLogger()

# home page for chat app
def home(request):
    # return render(request, 'example/change_password.html')
    return render(request, 'chat/home.html')


"""
Following method is is used for display the all registered users
"""


@login_required(login_url='/')
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

    username = request.user
    all_rooms = ChatRoom.objects.all()
    unique_rooms = []
    for i in range(len(all_rooms.values())):
        if all_rooms.values()[i]["room_name"] not in unique_rooms:
            unique_rooms.append(all_rooms.values()[i]["room_name"])
    # print(all_rooms)
    logging.info('List of all users done with status')
    return render(request, 'example/user_list.html', {'users': users, 'username': username, 'rooms': unique_rooms})


"""
login method use for login any user, 
if it is valid user otherwise print error and again login page display
"""


def log_in(request):
    # check if request type is 'POST' or 'GET'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            # check user validation
            if username == "" or password == "":
                messages.info(request, "username / password field should not be empty!")
                logging.error("username / password field should not be empty!")
                raise Exception("username / password field should not be empty!")

            # check user verification
            user = authenticate(username=username, password=password)

            if user is not None:
                # if valid then this user is authenticate and it able to go forward
                # login_token = jwt.encode({username: password}, 'private_key', algorithm='HS256').decode('utf-8')
                login(request, user)
                logging.info("Login successfully")
                return redirect(reverse('example:user_list'))
            else:
                messages.info(request, "Incurrect username / password")
                logging.error("Incurrect username / password")
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return redirect('/login')
    # if request is GET type then return same page
    logging.info('Login view')
    return render(request, 'example/log_in.html')


def reset_link(request):
    form = PasswordResetForm
    if request.method == 'POST':
        # form = PasswordResetForm(request.POST)
        to_email = request.POST['email']
        try:
            if not User.objects.filter(email=to_email).exists():
                messages.info(request, "This email not registered/ register now")
                raise Exception("Invalid Email address.")
            current_site = get_current_site(request)

            mail_subject = 'Reset your password.'
            jwt_token = jwt.encode({'Email': to_email}, 'private_key', algorithm='HS256').decode("utf-8")

            mail_url = 'http://' + str(current_site.domain) + '/chat/reset_password/' + jwt_token + '/'
            ee.emit('messageEvent', mail_subject, to_email, mail_url)
            return render(request, 'example/check_mail_link.html')
        except:
            return redirect('/reset_link_send')
    return render(request, "example/reset_password.html", {"form": form})


# this method is accessible only when user is logged in
@login_required(login_url='/login/')
def log_out(request):
    logging.info(str(request.user)+" : successfully logout.")
    logout(request)
    return redirect(reverse('example:log_in'))


# following method is use for create a chat room by any register and logged in user
@login_required(login_url='/login')
def create_Chat_Room(request):
    return render(request, 'chat/index.html', {})


# this method use for communication in a created chat room after creating it
@login_required(login_url='/')
def chat_room(request, room_name):
    users = User.objects.select_related('logged_in_user')

    username = request.user

    for user in users:
        user.status = 'Online' if hasattr(user, 'logged_in_user') else 'off-line'

    messages = ChatRoom.objects.filter(room_name=room_name).values('message')
    message = list(messages)

    return render(request, 'chat/room.html',
                  {"room_name_json": room_name, 'message': mark_safe(json.dumps(message)), 'users': users,
                   'username': username})


"""
Following sign_up() method is used for send the a activation link on user mail id 
with adding JWT token for activate the user profile 
"""


@csrf_exempt
def sign_up(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            # user profile is created but user is not active for log in now so set activation false and save
            user.is_active = False
            user.save()

            current_site = get_current_site(request)

            mail_subject = 'Activate your account.'

            # create a json token by using json format payload, private key and an algorithm
            jwt_token = jwt.encode({user.username: user.email}, 'private_key', algorithm='HS256').decode("utf-8")

            # get user email from saved data
            to_email = form.cleaned_data.get('email')

            mail_url = 'http://' + str(current_site.domain) + '/chat/activate/' + jwt_token + '/'
            ee.emit('messageEvent', mail_subject, to_email, mail_url)

            return render(request, 'chat/mail_send.html')
    else:
        form = SignupForm()
    return render(request, 'example/sign_up.html', {'form': form})


# following activate method is used for activate user account if user is valid and
# that link have valid user and also if user already used this link this become invalid
def activate(request, token):
    decoded_token = jwt.decode(token, 'private_key', algorithms='HS256')

    # check given token information is store in database or not
    try:
        user = User.objects.get(username=list(decoded_token.keys())[0])
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        # if this is not store in our database then user should have first signup because user in invalid
        return HttpResponse('you are not registered yet, please sign up first')
        # user = None
    if user is not None and not user.is_active:
        # if user valid then activate user account and save
        user.is_active = True
        user.save()
        # login(request, user)
        return render(request, 'chat/confirm_mail.html')
    else:
        # this link already activated or (this link was one time use )
        return render(request, template_name='chat/home.html')


def reset_password(request, token):
    decoded_token = jwt.decode(token, 'private_key', algorithms='HS256')

    # check given token information is store in database or not
    try:
        user = User.objects.get(email=list(decoded_token.values())[0])
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        # if this is not store in our database then user should have first signup because user in invalid
        # return HttpResponse('you are not registered yet, please sign up first')
        user = None
    if user is not None:
        context = {'userReset': user.username}
        print(context)
        return redirect('/resetpassword/' + str(user))
    else:

        # this link already activated or (this link was one time use )
        return render(request, template_name='chat/home.html')


def new_password(request, userReset):
    if request.method == 'POST':
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        try:
            if password1 != password2 or password2 == "" or password1 == "":
                messages.info(request, "password does not match ")
                return render(request, 'example/confirm_password.html')

            user = User.objects.get(username=userReset)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            # if this is not store in our database then user should have first signup because user in invalid
            # return HttpResponse('you are not registered yet, please sign up first')
            user = None
        if user is not None:
            # set password
            user.set_password(password1)
            # here we will save the user password in the database
            user.save()
            messages.info(request, "password reset done")
            # return redirect('/login/')
            return render(request, 'example/reset_done.html')
    else:
        return render(request, 'example/confirm_password.html')
