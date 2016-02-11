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
import json
from django.http import JsonResponse

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
        error = 'POST request not sent'
        return render(request, 'registration/login.html',{'error':error})



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
            user_ob = user
            user = authenticate(username=username, password=password)
            login(request, user)                
            registered = False
            if choice == '1':
                artist_ob= Artist(user=user_ob,name='', gender='')
                artist_ob.save()
                return HttpResponseRedirect('../updateprofile/')
                # return render(request, 'registration/.html',{'a_form': artist_form, 'registered': registered, 'choice' : '1' })
                # artist_registration(request)
            elif choice == '2':
                allied_ob= Allied(user=user_ob,name='', category='', sub_category='',location='')
                allied_ob.save()
                return HttpResponseRedirect('../updateprofile/')
            elif choice == '3':
                prod_ob= Production(user=user_ob,name='', location='')
                prod_ob.save()
                return HttpResponseRedirect('../updateprofile/')
        else:
            print user_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        error = 'Server side error'
        return render(request, 'registration/registration1.html', {'user_form' :user_form, 'error':error})
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
    
def get_google_json(request):
    if request.method == 'POST':
        json_ob= json.loads(data)
        return JsonResponse(json_ob)         



# @csrf_exempt
# def register_google(request):
#     import requests
#     if request.method == 'POST':
#         k = requests.get('http://filmboard.ml/register_gmail/')
#         data = k.json()






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
        user= request.user
        artist_ob = Artist.objects.filter(user = user)
        allied_ob = Allied.objects.filter(user = user)
        prod_ob = Production.objects.filter(user = user)
        if artist_ob:
            artist_ob=artist_ob[0]
            messages=user.notifications_set.filter(sent=False)
            exp = artist_ob.past_experiences.all()
            rec= artist_ob.recommendations.all()
            for msg in messages:
                msg.sent=True
                msg.save()
            context = {
                'artist' : artist_ob,
                'exp' : exp,
                'rec' : rec,
                'msg' : messages,
            }
            return render(request, 'registration/dashboard.html', context)    
        elif allied_ob:
            allied_ob = allied_ob[0]
            exp= allied_ob.past_experiences.all()
            rec= allied_ob.recommendations.all()
            context = {
                'allied' : allied_ob,
                'exp' : exp,
                'rec' : rec,
            }
            return render(request, 'registration/dashboard_allied.html', context)
        elif prod_ob:
            prod_ob = prod_ob[0]
            exp= prod_ob.past_experiences.all()
            rec= prod_ob.recommendations.all()
            messages=user.notifications_set.filter(sent=False)
            for msg in messages:
                msg.sent=True
                msg.save()
            context = {
                'production' : prod_ob,
                'exp' : exp,
                'rec' : rec,
                'msg' : messages,
            }
            return render(request, 'registration/dashboard_production.html', context)
    else:
        pass

# @login_required
# def dashboard_allied(request):
#     if request.user.is_authenticated():
#         try:
#             user= request.user
#             allied = request.user.allied
#             exp= allied.past_experiences.all()
#             rec= allied.recommendations.all()
#             context = {
#                 'allied' : allied,
#                 'exp' : exp,
#                 'rec' : rec,
#             }
#             return render(request, 'registration/dashboard_allied.html', context)
#         except:
#             return dashboard_prod(request)
#         # errors = []
#     else:
#         pass


# @login_required
# def dashboard_prod(request):
#     if request.user.is_authenticated():
#         user= request.user
#         prod = request.user.production
#         exp= prod.past_experiences.all()
#         rec= prod.recommendations.all()
#         if prod:
#             messages=user.notifications_set.filter(sent=False)
#             for msg in messages:
#                 msg.sent=True
#                 msg.save()
#         errors = []

#         context = {
#             'production' : prod,
#             'exp' : exp,
#             'rec' : rec,
#             'msg' : messages,
#         }
#         return render(request, 'registration/dashboard_production.html', context)
    # try:
    # except IndexError:
    #     return redirect('../login/')


#FUNCTIONALITIES FOR UPDATING AND EDITING PROFILE
@csrf_exempt
def update_profile(request):
    user = request.user
    # try:
    #     artist_ob=request.user.artist
    # except:
    #     try:
    #         allied_ob=request.user.allied
    #     except:
    #         try:
    #             prod_ob=request.user.production
    #         except:
    #             pass
    artist_ob = Artist.objects.filter(user = user)
    allied_ob = Allied.objects.filter(user = user)
    prod_ob = Production.objects.filter(user = user)

    if request.method == 'POST':
        if artist_ob:
            artist_ob= artist_ob[0]
            artist_ob.name = request.POST['name']
            artist_ob.gender = request.POST['gender']
            # arti_obst.dob = request.POST['dob']
            artist_ob.profile_pic= request.FILES['0']
            artist_ob.height = request.POST['height']
            artist_ob.weight = request.POST['weight']
            artist_ob.email_id = request.POST['email_id']
            artist_ob.body_type = request.POST['body_type']
            artist_ob.location = request.POST['location']
            artist_ob.skills = request.POST['skills']
            artist_ob.education_background = request.POST['ed_back']
            artist_ob.certifications = request.POST['certifications']
            artist_ob.save()
        elif allied_ob:
            allied_ob= allied_ob[0]
            allied_ob.name = request.POST['name']
            allied_ob.category = request.POST['category']
            # arti_obst.dob = request.POST['dob']
            allied_ob.sub_category = request.POST['sub_category']
            allied_ob.services = request.POST['services']
            allied_ob.phone = request.POST['phone']
            allied_ob.location = request.POST['location']
            allied_ob.certifications = request.POST['certifications']
            allied_ob.save()
        elif prod_ob:
            prod_ob= prod_ob[0]
            prod_ob.name = request.POST['name']
            prod_ob.location= request.POST['location']
            prod_ob.aboutus= request.POST['aboutus']
            prod_ob.phone = request.POST['phone']         
            prod_ob.save()

        return HttpResponse('done')
    

    else:
        if artist_ob:
            return render(request,'registration/update_profile.html', {'user':user, 'artist' : artist_ob, 'loc':ct})
        elif allied_ob:
            return render(request,'registration/update_profile_allied.html', {'user':user, 'allied' : allied_ob, 'loc': ct})
        elif prod_ob:
            return render(request,'registration/update_profile_prod.html', {'user':user, 'prod' : prod_ob, 'loc' : ct})
#FUNCTIONALITIES FOR ADDING EXPERIENCE
@login_required
def add_exp(request):
    if request.method == 'POST':
        user = request.user
        artist_ob = Artist.objects.filter(user = user)
        allied_ob = Allied.objects.filter(user = user)
        prod_ob = Production.objects.filter(user = user)
        if artist_ob:
            artist_ob = artist_ob[0]
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
        elif allied_ob:
            allied_ob=allied_ob[0]
            proj_type = request.POST['type']
            proj_name = request.POST['name']
            proj_status = request.POST['status']
            skills = request.POST['skills']
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
            allied_ob.past_experiences.add(exp_ob)
            allied_ob.save()
            return HttpResponseRedirect('../dashboard/')
        elif prod_ob:
            prod_ob=prod_ob[0]
            proj_type = request.POST['type']
            proj_name = request.POST['name']
            proj_status = request.POST['status']
            skills = request.POST['skills']
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
            prod_ob.past_experiences.add(exp_ob)
            return HttpResponseRedirect('../dashboard/')
            
        # elif allied_ob:
        #     proj_type = request.POST['type']
        #     proj_name = request.POST['name']
        #     proj_status = request.POST['status']
        #     skills = request.POST['skills']
        #     char_name = request.POST['char_name']
        #     role_played = request.POST['role_played']
        #     duration_start= request.POST['start']
        #     duration_end= request.POST['end']
        #     remarks = request.POST['remarks']
        #     special_mention = request.POST['mention']
        #     exp_ob =PastExperiences(project_type=proj_type, project_name=proj_name, project_status= proj_status, skills= skills, character_name=char_name, role_played=role_played, duration_start= duration_start, duration_end= duration_end, remarks=remarks,special_mention=special_mention)
        #     exp_ob.save()
        #     # proj_type = request.POST['name']
        #     allied_ob.past_experiences.add(exp_ob)

        #     allied_ob.save()
        #     return HttpResponseRedirect('../dashboard/')
        # elif prod_ob:
        #     proj_type = request.POST['type']
        #     proj_name = request.POST['name']
        #     proj_status = request.POST['status']
        #     skills = request.POST['skills']
        #     char_name = request.POST['char_name']
        #     role_played = request.POST['role_played']
        #     duration_start= request.POST['start']
        #     duration_end= request.POST['end']
        #     remarks = request.POST['remarks']
        #     special_mention = request.POST['mention']
        #     exp_ob =PastExperiences(project_type=proj_type, project_name=proj_name, project_status= proj_status, skills= skills, character_name=char_name, role_played=role_played, duration_start= duration_start, duration_end= duration_end, remarks=remarks,special_mention=special_mention)
        #     exp_ob.save()
        #     # proj_type = request.POST['name']
        #     prod_ob.past_experiences.add(exp_ob)

        #     prod_ob.save()
        #     return HttpResponseRedirect('../dashboard/')

    else:
        return render(request,'registration/add_exp.html')      


#FUNC FOR VIEW EXPERIENCE
@login_required
def view_experiences(request):
    artist= request.user.artist
    past_experiences = artist.past_experiences.all()
    return render(request,'registration/view_exp.html' , {'exp' : past_experiences})

# @login_required
# def update_profile_allied(request):
#     if request.method == 'POST':
#         user = request.user
#         allied_ob=request.user.allied
#         allied_ob.name = request.POST['name']
#         allied_ob.category = request.POST['category']
#         # arti_obst.dob = request.POST['dob']
#         allied_ob.sub_category = request.POST['sub_category']
#         allied_ob.services = request.POST['services']
#         allied_ob.phone = request.POST['phone']
#         allied_ob.location = request.POST['location']
#         allied_ob.certifications = request.POST['certifications']
#         allied_ob.save()
#         return HttpResponseRedirect('../dashboard/')

#     else:
#         user= request.user
#         try:
#         except IndexError:
#             return redirect('../login/')




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


#FUNCTIONALITIES FOR UPDATING AND EDITING PROFILE




def mail_test(request):
    body= '''This is a test mail '''
    send_mail('test', body, 'info@aranyaproject.com', ['ronu66@gmail.com'])
    # email.send()    
    return HttpResponse('done')

def show_projects(request):
    projectlist = Projects.objects.all()
    context = {
        'projectlist':projectlist
    }
    return render(request, 'registration/projectlist.html',context)

def show_project_details(request, project_id):
    p = Projects.objects.get(id = project_id)
    requirements = ProjectRequirements.objects.filter(project = p)
    prod = Production.objects.filter(projects = p)
    context = {
        'p':p,
        'requirements':requirements,
        'prod':prod,
    }
    return render(request, 'registration/project_details.html',context)

@login_required
def apply_for_project(request,requirement_id):
    user = request.user
    req = ProjectRequirements.objects.get(id = requirement_id)
    proj = req.project
    requirements = ProjectRequirements.objects.filter(project = proj)
    artist_ob = Artist.objects.filter(user = user)
    allied_ob = Allied.objects.filter(user = user)
    prod_ob_list= proj.producer.all()

    production_ob = Production.objects.filter(user = user)
    error = ''
    choice = 0
    if artist_ob:
        if req.req_type == 'Artist':
            req.user.add(user)
            req.save()
            choice=1
        else:
            choice=2
            error = 'You can only apply for a postition applicable for Artists.'
        if prod_ob_list:
            prod_ob = prod_ob_list[0]
            user_ob = prod_ob.user
            message= str(artist_ob[0].name) + ' Applied For ' + str(proj.project_name)
            notify_ob= Notifications(user=user_ob, message=message,url='', sent=False)
            notify_ob.save()

    elif allied_ob:
        if req.req_type == 'Allied Service':
            req.user.add(user)
            req.save()
            choice=1
        else:
            choice=2
            error = 'You can only apply for a postition applicable for Allied services.'    
        if prod_ob_list:
            prod_ob = prod_ob_list[0]
            user_ob = prod_ob.user
            message= str(artist_ob[0].name) + ' Applied For ' + str(proj.project_name)
            notify_ob= Notifications(user=user_ob, message=message,url='', sent=False)
            notify_ob.save()

    elif production_ob:
        if req.req_type == 'Production':
            req.user.add(user)
            req.save()
            choice=1
        else:
            choice=2
            error = 'You can only apply for a postition applicable for Production houses.'
    else:
        choice=2
        error = 'Error'
    context={
    'error':error,
    'choice':choice,
    'req':req,
    'p':proj,
    'requirements':requirements
    }
    return render(request,'registration/project_details.html',context)


@login_required
def add_project(request):
    user = request.user
    prod_ob = Production.objects.filter(user = user)    
    if request.method == 'POST':
        if prod_ob:
            pname = request.POST['name']
            ptype = request.POST['type']
            cost = request.POST['cost']
            status = request.POST['status']
            location = request.POST['location']
            language = request.POST['language']
            duration_start = request.POST['dstart']
            duration_end = request.POST['dend']
            description = request.POST['desc']
            producer = prod_ob[0]
            proj = Projects(project_type = ptype, project_name = pname, project_status = status, project_cost = cost, location = location, languages = language, duration_start = duration_start,  duration_end = duration_end, description = description)
            proj.save()
            proj.producer.add(producer)
            proj.save()
            pid = str(proj.id)
            return HttpResponseRedirect('../addrequirements/'+pid+'/')
    else:
        return render(request,'registration/add_project.html')


@login_required
def add_req(request, project_id):
    if request.POST:
        rskills = request.POST.get('skills','')
        if 'rreq_type' in request.POST:
            rreq_type = request.POST.get('rreq_type',False)
        else:
            rreq_type = 'Artist'
        rnumbers = request.POST['numbers']
        rcharacter = request.POST['character']
        rrole = request.POST['role']
        rdesc = request.POST['desc']
        rproj = Projects.objects.get(id = project_id)
        req = ProjectRequirements(req_type = rreq_type,skills = rskills, numbers = rnumbers, character = rcharacter, role = rrole, description = rdesc, project = rproj)
        req.save()
        if "save_add" in request.POST:
            return render(request,'registration/add_req.html')
        elif "save_quit" in request.POST:
            return HttpResponseRedirect('../../dashboard/')
    else:
        return render(request,'registration/add_req.html')

def guest_artist_dashboard(request):
    return show_projects(request)

def guest_allied_dashboard(request):
    return show_projects(request)

def guest_producer_dashboard(request):
    return show_artist(request)

def show_artist(request):
    artistlist = Artist.objects.all()
    context={
    'artistlist':artistlist,
    }
    return render(request,'registration/artistlist.html',context)

@login_required
def my_projects(request):
    user = request.user
    prod_ob = Production.objects.filter(user=user)
    artist_ob= Artist.objects.filter(user=user)
    allied_ob= Allied.objects.filter(user=user)
    choice = 'myproj'
    if prod_ob:
        prod = prod_ob[0]
        projlist = prod.projects_set.all()
        context={
            'projectlist':projlist,
            'choice':choice 
        }
        return render(request,'registration/projectlist.html',context)

@login_required
def my_project_details(request, project_id):
    user= request.user
    prod_ob = Production.objects.filter(user=user)
    artist_ob= Artist.objects.filter(user=user)
    allied_ob= Allied.objects.filter(user=user)
    choice = 'myproj'
    if prod_ob:
        p = Projects.objects.get(id = project_id)
        requirements = ProjectRequirements.objects.filter(project = p)
        prod = Production.objects.filter(projects = p)
        context = {
            'p':p,
            'requirements':requirements,
            'prod':prod,
            'choice':choice,
        }
        return render(request, 'registration/project_details.html',context)

@login_required
def my_project_requirements(request, requirement_id):
    user=request.user
    req=ProjectRequirements.objects.filter(id = requirement_id)
    req=req[0]
    applied = req.user.all()
    artlist=[]
    alllist=[]
    for u in applied:
        if u.artist:
            art=u.artist
            artlist.append(art)
        elif u.allied:
            alliedser=u.allied
            alllist.append(alliedser)
    context={
    'artlist':artlist,
    'alllist':alllist,
    'req':req,
    }
    return render(request,'registration/applied_details.html',context)

@login_required
def artist_search(request):
    if request.POST:
        inp= str(request.POST.get('search','') )
        proj_respx=[]
        proj_list = Projects.objects.filter(project_name__icontains=inp).order_by('project_name')
        proj_list2 = Projects.objects.filter(location__icontains=inp).order_by('location')
        proj_respx+=proj_list 
        proj_respx+=proj_list2
        proj_resp= [] 
        for i in proj_respx:
            if i not in proj_resp:
                proj_resp.append(i)

        prod_respx=[]
        prod_list = Production.objects.filter(name__icontains=inp).order_by('name')
        prod_list2 = Production.objects.filter(location__icontains=inp).order_by('location')
        prod_respx+= prod_list
        prod_respx+= prod_list2
        prod_resp= [] 
        for i in prod_respx:
            if i not in prod_resp:
                prod_resp.append(i)

        try:
            artist= request.user.artist
        except:
            try:
                artist= request.user.allied            
            except:
                try:
                    artist= request.user.production               
                except:
                    pass                        


        # try request.user.allied:
        #     artist= request.user.allied
        # elif request.user.production:
        #     artist= request.user.production                        
        artlistx= []
        art_list= Artist.objects.filter(name__icontains=inp).order_by('name')
        art_list2 = Artist.objects.filter(location__icontains=inp).order_by('location')
        artlistx+= art_list 
        artlistx+= art_list2
        artlist= [] 
        for i in artlistx:
            if i not in artlist:
                artlist.append(i)

        context={
        'artist': artist,
        'proj_resp' : proj_resp,
        'prod_resp' : prod_resp,
        'artlist' :artlist, 
        }
        return render(request,'registration/artist_search.html',context)
    else:
        return HttpResponseRedirect('http://www.filmboard.ml/dashboard/')

@login_required
def show_profile(request,art_id):
    user= request.user
    if request.user.is_authenticated():
        myartist= Artist.objects.filter(user=user)
        if myartist:
            myartist=myartist[0]
    artist = Artist.objects.get(id=int(art_id))
    exp = artist.past_experiences.all()
    rec= artist.recommendations.all()
    context = {
        'artist' : artist,
        'exp' : exp,
        'rec' : rec,
        'myartist' : myartist,
    }
    return render(request, 'registration/art_profile.html', context)

@login_required
def show_profile_prod(request,prod_id):
    prod = Production.objects.get(id=int(prod_id))
    # exp = artist.past_experiences.all()
    # rec= artist.recommendations.all()
    context = {
        'production' : prod,
        # 'exp' : exp,
        # 'rec' : rec,
        # 'myartist' : myartist,
    }
    return render(request, 'registration/prod_profile.html', context)    
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
