from django.template import RequestContext
from django.shortcuts import render, render_to_response, redirect
# from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from registration.models import *
# from events.models import/ EventNew
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect,Http404,HttpResponse, JsonResponse
from django.template.loader import get_template
from django.template import Context
from django.core.mail import send_mail, EmailMessage
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
import difflib
from registration.forms import *

@csrf_exempt
def home(request):
    return render(request,'registration/home.html')


#LOGIN FUNCTIONALITY
@csrf_exempt
def user_login_test(request):

    context = RequestContext(request)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                if user.is_staff:
                    login(request, user)
                    return HttpResponseRedirect('../dashboard/')
                else:
                    login(request, user)
                    return HttpResponseRedirect('../dashboard/')
            else:
                context = {'error_heading' : "Account Inactive", 'error_message' :  'Your account is currently INACTIVE. To activate it, call the following members of the Department of Publications and Correspondence depending on the region of your college.<br> <strong> North India :- Ankit Dube | +91 9983083610 </strong> <br> <strong>Delhi/NCR :- Aditya Shetty :- +91 7240105157 </strong><br><strong>Central India :- Poonam Brar | +91 7240105158 </strong><br><strong>Rajasthan, Gujarat & Maharashtra :- Karthik Maddipoti | +91 8003193680 </strong><br><strong>East India :- Tanhya Chitle | +91 7240105155 </strong><br><strong>South India :- Archana Tatavarti |+91 7240105150 </strong><br />Return back <a href="/">home</a>'}
                return render(request, 'registration/error.html', context)
        else:
            context = {'error_heading' : "Invalid Login Credentials", 'error_message' :  'Please <a href=".">try again</a>'}
            return render(request, 'registration/error.html', context)
    else:
        return render(request, 'registration/logintest.html')

@csrf_exempt
def user_login(request):

    context = RequestContext(request)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                if user.is_staff:
                    login(request, user)
                    return HttpResponseRedirect('../dashboard/')
                else:
                    login(request, user)
                    return HttpResponseRedirect('../dashboard/')
            else:
                context = {'error_heading' : "Account Inactive", 'error_message' :  'Your account is currently INACTIVE. To activate it, call the following members of the Department of Publications and Correspondence depending on the region of your college.<br> <strong> North India :- Ankit Dube | +91 9983083610 </strong> <br> <strong>Delhi/NCR :- Aditya Shetty :- +91 7240105157 </strong><br><strong>Central India :- Poonam Brar | +91 7240105158 </strong><br><strong>Rajasthan, Gujarat & Maharashtra :- Karthik Maddipoti | +91 8003193680 </strong><br><strong>East India :- Tanhya Chitle | +91 7240105155 </strong><br><strong>South India :- Archana Tatavarti |+91 7240105150 </strong><br />Return back <a href="/">home</a>'}
                return render(request, 'registration/error.html', context)
        else:
            context = {'error_heading' : "Invalid Login Credentials", 'error_message' :  'Please <a href=".">try again</a>'}
            return render(request, 'registration/error.html', context)
    else:
        error='Server error'
        context = {'error':error}
        return render(request, 'registration/login.html', context)



def user_logout(request):
    logout(request)
    return redirect('../home/')









###########     REGISTRATION FUNCTIONS     ############

@csrf_exempt
def initial_registration(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        choice = request.POST['choice']
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserartistForm.
        user_form = UserForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            # emailadds = [k.email for k in User.objects.all()]
            # if user_form.email in emailadds:
            #   return HttpResponse('Email Address not unique')
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            password= user.password
            user.set_password(user.password)
            user.is_active = True
            user.save()
            username =user.username
            user = authenticate(username=username, password=password)
            login(request, user)            
            registered = False
            if choice == '1':
                artist_form = ArtistForm()
                return render(request, 'registration/register.html',{'a_form': artist_form, 'registered': registered, 'choice' : '1' })
                # artist_registration(request)
            elif choice == '2':
                allied_form = AlliedForm()
                return render(request, 'registration/register.html',{'a_form': allied_form, 'registered': registered,'choice' : '2' })
            elif choice == '3':
                production_form = ProductionForm()
                return render(request, 'registration/register.html',{'a_form': production_form, 'registered': registered, 'choice' : '3' })
        else:
            print user_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()


    return render(request, 'registration/registration1.html', {'user_form' :user_form})
    # Render the template depending on the context.
    # return render(request, 'registration/register.html',
    #         {'user_form': user_form, 'artist_form': artist_form, 'registered': registered})

@csrf_exempt
def register_profile(request):
    # Like before, get the request's context.
    if request.POST:
        choice = request.POST['choice']
        if choice == '1':
            artist_registration(request)
            # artist_registration(request)
        elif choice == '2':
            allied_registration(request)
        elif choice == '3':
            production_registration(request)

        registered = True
        return render(request, 'registration/register.html',
                { 'registered': registered}) 
    




#ARTIST REGISTRATION FUNCTION
@csrf_exempt
def artist_registration(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserartistForm.
        artist_form = ArtistForm(data=request.POST)

        # If the two forms are valid...
        if artist_form.is_valid():
            # Save the user's form data to the database.
            # emailadds = [k.email for k in User.objects.all()]
            # if user_form.email in emailadds:
            #   return HttpResponse('Email Address not unique')

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.

            # Now sort out the Userartist instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            user_ob =request.user
            artist = artist_form.save(commit=False)
            artist.user = user_ob
            artist.email_id = user_ob.email
            # Now we save the Userartist model instance.
            artist.save()

            # Update our variable to tell the template registration was successful.
            registered = True
            return render(request, 'registration/register.html',
                    {'artist_form': artist_form, 'registered': registered})            
        else:
            print artist_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        artist_form = ArtistForm()

    # Render the template depending on the context.
    return render(request, 'registration/register.html',
            {'artist_form': artist_form, 'registered': registered})
            #send an Email

@csrf_exempt
def allied_registration(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserartistForm.
        allied_form = AlliedForm(data=request.POST)

        # If the two forms are valid...
        if allied_form.is_valid():
            # Save the user's form data to the database.
            # emailadds = [k.email for k in User.objects.all()]
            # if user_form.email in emailadds:
            #   return HttpResponse('Email Address not unique')

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.

            # Now sort out the Userartist instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            user_ob =request.user
            allied = allied_form.save(commit=False)
            allied.user = user_ob
            # allied.email_id = user_ob.email
            # Now we save the Userallied model instance.
            allied.save()

            # Update our variable to tell the template registration was successful.
            registered = True
            # return render(request, 'registration/register.html',
            #         {'artist_form': artist_form, 'registered': registered})            
        else:
            print allied_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        allied_form = AlliedForm()

    # # Render the template depending on the context.
    # return render(request, 'registration/register.html',
    #         {'artist_form': artist_form, 'registered': registered})


@csrf_exempt
def production_registration(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserartistForm.
        production_form = ProductionForm(data=request.POST)

        # If the two forms are valid...
        if production_form.is_valid():
            # Save the user's form data to the database.
            # emailadds = [k.email for k in User.objects.all()]
            # if user_form.email in emailadds:
            #   return HttpResponse('Email Address not unique')

            # Now sort out the Userartist instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            user_ob =request.user
            product = production_form.save(commit=False)
            product.user = user_ob
            # allied.email_id = user_ob.email
            # Now we save the Userallied model instance.
            product.save()

            # Update our variable to tell the template registration was successful.
            registered = True


#'''EMAIL CODE BELOW'''
            # send_to = user.email
            # body = unicode(u''' ''')

            # try:
            #     email = EmailMessage('Registration Confirmation', body, 'register@xyz.com', [send_to])
            #     email.send()
            # except:
            #     return HttpResponse('Mail Error message')



        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print production_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        production_form = ProductionForm()
        # artist_form = ArtistForm()

    # Render the template depending on the context.
    # return render(request, 'registration/register.html',
            # { 'production_form': registered})












# THIS IS FOR ARTISTS
# CODE FOR MAIN DASHBOARD PAGE
@login_required
def dashboard(request):
    if request.user.is_authenticated():
        try:
            artist = request.user.artist
            context = {
                'artist' : artist
            }
            return render(request, 'registration/dashboard.html', context)
        except:
            return dashboard_allied(request)

        errors = []

        
    else:
        pass


#FUNCTIONALITIES FOR UPDATING AND EDITING PROFILE
@login_required
def update_profile(request):
    if request.method == 'POST':
        user = request.user
        try:
            artist_ob=request.user.artist
            artist_ob.name = request.POST['name']
            artist_ob.gender = request.POST['gender']
            # arti_obst.dob = request.POST['dob']
            artist_ob.height = request.POST['height']
            artist_ob.weight = request.POST['weight']
            artist_ob.email_id = request.POST['email_id']
            artist_ob.body_type = request.POST['body_type']
            artist_ob.location = request.POST['location']
            artist_ob.skills = request.POST['skills']
            artist_ob.education_background = request.POST['ed_back']
            artist_ob.certifications = request.POST['certifications']
            artist_ob.save()
            return HttpResponseRedirect('../dashboard/')
        except:
            return update_profile_allied(request)
    else:
        user= request.user
        try:
            artist_ob= request.user.artist
            return render(request,'registration/update_profile.html', {'user':user, 'artist' : artist_ob})
        except:
            return update_profile_allied(request)









#FUNCTIONALITIES FOR ADDING EXPERIENCE
@login_required
def add_exp(request):
    if request.method == 'POST':
        user = request.user
        artist_ob=request.user.artist
        proj_type = request.POST['type']
        proj_name = request.POST['name']
        proj_status = request.POST['status']
        skills = request.POST['skills']
        char_name = request.POST['char_name']
        role_played = request.POST['role_played']
        duration_start= request.POST['start']
        duration_end= request.POST['end']
        remarks = request.POST['remarks']
        special_mention = request.POST['mention']
        exp_ob =PastExperiences(project_type=proj_type, project_name=proj_name, project_status= proj_status, skills= skills, character_name=char_name, role_played=role_played, duration_start= duration_start, duration_end= duration_end, remarks=remarks,special_mention=special_mention)
        exp_ob.save()
        # proj_type = request.POST['name']
        artist_ob.past_experiences.add(exp_ob)

        artist_ob.save()
        return HttpResponseRedirect('../dashboard/')

    else:
        return render(request,'registration/add_exp.html')      


#FUNC FOR VIEW EXPERIENCE
@login_required
def view_experiences(request):
    artist= request.user.artist
    past_experiences = artist.past_experiences.all()
    return render(request,'registration/view_exp.html' , {'exp' : past_experiences})





#Functionalities for recommendations below. Will be applied accordingly as frontend develops for the previous one 

@login_required
def seek_rec(request):
    if request.method == 'POST':
        user = request.user
        artist_ob=request.user.artist
        proj_type = request.POST['type']
        proj_name = request.POST['name']
        proj_status = request.POST['status']
        skills = request.POST['skills']
        char_name = request.POST['char_name']
        role_played = request.POST['role_played']
        duration_start= request.POST['start']
        duration_end= request.POST['end']
        seek_from_type = request.POST['seek_type']
        seek_from_name = request.POST['seek_name']
        message = request.POST['message']
        email_id = request.POST['email']
        rec_ob =Recommendations(project_type=proj_type, project_name=proj_name, project_status= proj_status, skills= skills, character_name=char_name, role_played=role_played, duration_start= duration_start, duration_end= duration_end, seek_from_name=seek_from_name, seek_from_type=seek_from_type , add_msg=message ,email_id=email_id)
        rec_ob.save()
        # proj_type = request.POST['name']
        artist_ob.recommendations.add(rec_ob)

        artist_ob.save()
        return HttpResponseRedirect('../dashboard/')

    else:
        return render(request,'registration/seek_rec.html')     

@login_required
def view_rec(request):
    artist= request.user.artist
    recommendations = artist.recommendations.all()
    return render(request,'registration/view_rec.html' , {'rec' : recommendations}) 










# THIS IS FOR ALLIED SERVICES
# CODE FOR MAIN DASHBOARD PAGE
@login_required
def dashboard_allied(request):
    if request.user.is_authenticated():
        try:
            allied = request.user.allied
        except IndexError:
            return redirect('../login/')

        errors = []

        context = {
            'allied' : allied
        }
        return render(request, 'registration/dashboard_allied.html', context)
    else:
        pass


#FUNCTIONALITIES FOR UPDATING AND EDITING PROFILE
@login_required
def update_profile_allied(request):
    if request.method == 'POST':
        user = request.user
        allied_ob=request.user.allied
        allied_ob.name = request.POST['name']
        allied_ob.category = request.POST['category']
        # arti_obst.dob = request.POST['dob']
        allied_ob.sub_category = request.POST['sub_category']
        allied_ob.services = request.POST['services']
        allied_ob.phone = request.POST['phone']
        allied_ob.location = request.POST['location']
        allied_ob.certifications = request.POST['certifications']
        allied_ob.save()
        return HttpResponseRedirect('../dashboard/')

    else:
        user= request.user
        try:
            allied_ob= request.user.allied
            return render(request,'registration/update_profile_allied.html', {'user':user, 'allied' : allied_ob})
        except IndexError:
            return redirect('../login/')









# #FUNCTIONALITIES FOR ADDING EXPERIENCE
# @login_required
# def add_exp(request):
#     if request.method == 'POST':
#         user = request.user
#         artist_ob=request.user.artist
#         proj_type = request.POST['type']
#         proj_name = request.POST['name']
#         proj_status = request.POST['status']
#         skills = request.POST['skills']
#         char_name = request.POST['char_name']
#         role_played = request.POST['role_played']
#         duration_start= request.POST['start']
#         duration_end= request.POST['end']
#         remarks = request.POST['remarks']
#         special_mention = request.POST['mention']
#         exp_ob =PastExperiences(project_type=proj_type, project_name=proj_name, project_status= proj_status, skills= skills, character_name=char_name, role_played=role_played, duration_start= duration_start, duration_end= duration_end, remarks=remarks,special_mention=special_mention)
#         exp_ob.save()
#         # proj_type = request.POST['name']
#         artist_ob.past_experiences.add(exp_ob)

#         artist_ob.save()
#         return HttpResponseRedirect('../dashboard/')

#     else:
#         return render(request,'registration/add_exp.html')      


# #FUNC FOR VIEW EXPERIENCE
# @login_required
# def view_experiences(request):
#     artist= request.user.artist
#     past_experiences = artist.past_experiences.all()
#     return render(request,'registration/view_exp.html' , {'exp' : past_experiences})

#FB login tests
# def fb_login(request):
#     return render_to_response('registration/fblogin.html') 
