from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import user_passes_test,login_required
from django.contrib import messages
from .models import *
from datetime import datetime
from django.db.models import Q

# Create your views here.
def home(request):
    return render( request,'home.html')

def page1(request):
    return render(request,'page1.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request,'page1.html') # redirect to dashboard or homepage
        else:
            return render(request, 'home.html', {'error': 'Invalid credentials'})
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']

         # Create user
        user = User.objects.create_user(username=username, password=password,first_name=first_name,last_name=last_name,email=email)
        user.save()

         # Log the user in after signup
        login(request, user)
        return render(request,'page1.html')  # or your dashboard
    
    return render(request, 'home.html')

def guest(request):
    return render(request ,'page1.html')

def services(request):
    return render(request,'services.html')

def graveyard_info(request):

    return render(request,'graveyard_details.html')

def digital(request):
    

   
    return render(request,'digital.html',{'info':range(5)})



@login_required(login_url='/')
@user_passes_test(lambda u: u.is_staff, login_url='/')
def staffdash(request):
    if not request.user.is_staff:
        messages.error(request, "You are not authorized to view this page.")
        return redirect('home')
    return render(request, 'staffdash.html')

def signout(request):
    logout(request)
    return render(request,'home.html')

def firstlog(request):
    return render(request,'home.html')

def upload_deceased(request):
    if request.method=='POST':
        deceased_name=request.POST['deceased_name']
        deceased_dob=request.POST['deceased_dob']
        deceased_dod=request.POST['deceased_dod']
        deceased_add=request.POST['deceased_add']
        phoneno=request.POST['phoneno']
        deceased_info=request.POST['info']
        grave_id=request.POST['grave_id']
        
        open_section=request.POST.get('open_section','0')

        gp=graveplots.objects.get(pk=grave_id)
        status=gp.status
        if status=='available':
            try:
                grave=graveplots.objects.get(pk=grave_id)
                grave.status='buried'
                grave.save()
            except graveplots.DoesNotExist:
                return render(request,'staffdash.html',{'error':'invalid grave id','open_section':open_section})
        
            de=deceased.objects.create(
            deceased_name=deceased_name,
            deceased_dob=deceased_dob,
            deceased_dod=deceased_dod,
            deceased_add=deceased_add,
            deceased_phoneno=phoneno,
            deceased_info=deceased_info,
            grave_id=grave

            )


            return render(request,'staffdash.html',{'error':f'deceased information uploaded ,deceased ID:{de.deceased_id}','open_section':open_section})
        return render(request,'staffdash.html',{'error':'grave your are trying is either buried or reserved'})
    return render(request,'staffdash.html',{'error':'error try again'})

def graveyard_upload(request):
    if request.method=='POST':
        name=request.POST['name']
        add=request.POST['add']
        phoneno=request.POST['phoneno']
        plots=int(request.POST['number'])
        city=request.POST['city']
        rows=int(request.POST['rows'])
        column=int(request.POST['column'])
        
        open_section=request.POST.get('open_section','2')

        if rows*column>=plots:
            gy=graveyard.objects.create(
            graveyard_name=name,
            graveyard_add=add,
            graveyard_phoneno=phoneno,
            graveyard_plots=plots,
            graveyard_city=city,
            graveyard_column=column,
            graveyard_row=rows
            )
            a=1
            for i in range(1,rows+1):
                for j in range(1,column+1):
                    graveplots.objects.create(
                    grave_no=a,
                    status="available",
                    graveyard_id=gy,
                    grave_row=i,
                    grave_column=j
                )
                a+=1
        else:
            return render(request,'staffdash.html',{'error':'Incorrect information,plz try again','open_section':open_section})
        
        

        return render(request,'staffdash.html',{'error':f'Graveyard information succesfully uploaded and graveyard id:{gy.graveyard_id}! and grave plot also created','open_section':open_section})
    
    return render(request,'staffdash.html',{'error':'error try again'})

def memorial_upload(request):
    if request.method=='POST':
        name=request.POST['name']
        message=request.POST['message']
        id=request.POST['id']
        open_section=request.POST.get('open_section','1')

        try:
            deceased_id=deceased.objects.get(pk=id)
        except deceased.DoesNotExist:
            return render(request,'digital.html',{'error':'deceased id does not exists','open_section':open_section})
        
        digital_memorial.objects.create(
            memorial_name=name,
            memorial_message=message,
            memorial_deceased_id=deceased_id
        )

        return render(request,'digital.html',{'error':'memorial details uploaded!!','open_section':open_section})
    
    return render(request,'digital.html',{'error':'error try again'})

def search_graveyard(request):
    info=None
    if request.method=="POST":
        query=request.POST.get('location','').strip()
        if query:
            results = graveyard.objects.filter( Q(graveyard_name__icontains=query) |Q(graveyard_city__icontains=query)| Q(graveyard_id__iexact=query))
        if results:
            return render(request,'graveyard_details.html',{'info':results})
        return render(request,'graveyard_details.html',{'error':'Invalid name'})

def search_memorial(request):
    memo=None
    if request.method=="POST":
        name=request.POST['name']
        open_section=request.POST.get('open_section','0')
        info=digital_memorial.objects.filter(memorial_name=name)
        if info.exists():
            return render(request,'digital.html',{'memo':info,'open_section':open_section})
        return render(request,'digital.html',{'error':'memorial not present ','open_section':open_section})
    return render(request,'digital.html',{'error':"something went wrong ,plz try again"})
    

    
def graveyard_name(request):
    if request.method=="POST":
        name=request.POST['graveyard_name']
        info=graveyard.objects.filter(graveyard_name=name)
        if info.exists():
            return render(request,'services.html',{'info':info})
        return render(request,'services.html',{'error':'graveyard doesnt exists'})
    return render(request,'services.html',{'error':'try again'})


    
def maintainance(request):
    if request.method=="POST":
        name=request.POST['name']
        phoneno=request.POST.get('phoneno')
        graveid=request.POST['graveid']
        disc=request.POST['disc']
        date=request.POST['date']
        open_section=request.POST.get('open_section','0')

        try:
            grave=graveplots.objects.get(pk=graveid)
        except graveplots.DoesNotExist:
            return render(request ,'services.html',{'error':'The grave id you entered doesnot exists','open_section':open_section})
        if grave.status=="available":
            return render(request,'services.html',{'error':'grave plot u entered is not occupied,check grave id and try again','open_section':open_section}) 
        if maintain.objects.filter(main_grave_id=grave,main_status="pending").exists():
            ma=maintain.objects.filter(main_grave_id=grave,main_status="pending").first()
            
            return render(request,'services.html',{'error':f'Your previous maintainance request is still in progress and its Maintainance id is {ma.main_id}','open_section':open_section})


        ma=maintain.objects.create(
            main_name=name,
            main_contact=phoneno,
            main_completebydate=date,
            main_status="pending",
            main_grave_id=grave,
            main_disc=disc,
        )

        return render(request,'services.html',{'error':f'your services request is place and your maintainance id is {ma.main_id}','open_section':open_section})
    
    return render(request,'services.html',{'error':'try again '})

def pendingmaintainance(request):
    if request.method == "POST":
        id = request.POST['id']
        open_section = request.POST.get('open_section', '1')
        try:
            gy = graveyard.objects.get(pk=id)
        except graveyard.DoesNotExist:
            return render(request, 'staffdash.html', {'error': 'Invalid graveyard ID', 'open_section': open_section})

        gp_list = graveplots.objects.filter(graveyard_id=gy)
        maintainance = maintain.objects.filter(main_status="pending", main_grave_id__in=gp_list)
        if maintainance.exists():
            return render(request, 'staffdash.html', {'maintainboard': "PENDING WORKS", 'maintain': maintainance, 'open_section': open_section})

        return render(request, 'staffdash.html', {'maintainboard': 'NO PENDING MAINTAINANCE WORK', 'open_section': open_section})
    return render(request, 'staffdash.html', {'error': 'try again'})

def viewgrid(request):
    if request.method=="POST":
        query=request.POST.get('graveyard_id','').strip()
        if query:
            gy = graveyard.objects.filter( Q(graveyard_name__icontains=query) | Q(graveyard_id__iexact=query)).first()
        if gy:
            plots=graveplots.objects.filter(graveyard_id=gy).order_by('grave_row','grave_column')
            rows=gy.graveyard_row
            columns=gy.graveyard_column
            grid=[]
            for r in range(1, rows+1):
                row_cells=[]
                for c in range(1, columns+1):
                    plot=plots.filter(grave_row=r,grave_column=c).first()
                    row_cells.append(plot)
                grid.append(row_cells)
            return render(request,'graveyard_details.html',{'graveyard':gy,'grid':grid,'plot':plots})
        return render(request,'graveyard_details.html',{'error':'try again'})

def update_maintainance(request):
    if request.method=="POST":
        id=request.POST['main_id']
        eid=request.POST['employeeid']
        comdate=request.POST['date']
        
        open_section=request.POST.get('open_section','1')
        try:
            ma=maintain.objects.get(pk=id)
        except maintain.DoesNotExist:
            return render(request,'staffdash.html',{'error':'Maintainance ID does not exists','open_section':open_section})
        try:
            em=employee.objects.get(pk=eid)
        except employee.DoesNotExist:
            return render(request,'staffdash.html',{'error':'Employee ID doesnot exists','open_section':open_section})

       
          
        ma.main_status="completed"
        ma.save()

        performed_by.objects.create(
            employee_id=em,
            main_id=ma,
            completed_at=comdate
            
        )
        return render(request,'staffdash.html',{'error':'maintainance status updated to completed','open_section':open_section})


def upload_emp(request):
    if request.method=="POST":
        name=request.POST['name']
        add=request.POST['address']
        no=request.POST['phoneno']
        gid=request.POST.get('graveyard_id')
        
        open_section=request.POST.get('open_section','3')

        try:
            gy=graveyard.objects.get(pk=gid)
        except graveyard.DoesNotExist:
            return render(request,'staffdash.html',{'error':'Graveyard Does not exists','open_section':open_section})
        
        em=employee.objects.create(
            employee_name=name,
            employee_add=add,
            employee_no=no,
            employee_work_at=gy
        )

        id=em.employee_id
        return render(request,'staffdash.html',{'error':f'Employee details entered and Employee ID is {id}','open_section':open_section})
    return render(request,'staffdash.html',{'error':'try again'})

def reserve(request):
    if request.method=="POST":
        name=request.POST['name']
        no=request.POST['phoneno']
        proof=request.POST['proof']
        grave_id=request.POST['grave_id']
        
        
        open_section=request.POST.get('open_section','1')

        try:
            gy=graveplots.objects.get(pk=grave_id)
        except graveplots.DoesNotExist:
            return render(request,'services.html',{'error':'Grave ID does not exists','open_section':open_section})
        
        if gy.status=="available":
            gy.status="reserved"
            gy.save()
            bo=booking.objects.create(
                booking_reserver_name=name,
                booking_reserver_contact=no,
                booking_grave_id=gy,
                booking_proof=proof,
                booking_status="reserved",

            )
            return render(request,'services.html',{'error':f' Grave id {gy} is reserved and Booking ID is {bo.booking_id}','open_section':open_section})
        return render(request,'services.html',{'error':'The grave your are trying to reserve is aleady reserved by other..plz try other','open_section':open_section})
    
def search_deceased(request):
    if request.method == "POST":
        id = request.POST['id']
        open_section = request.POST.get('open_section', '2')
        try:
            de = deceased.objects.get(pk=id)
        except deceased.DoesNotExist:
            return render(request, 'digital.html', {'error': 'Deceased id does not exists', 'open_section': open_section})
        try:
            me = digital_memorial.objects.get(memorial_deceased_id=id)
            m_id = me.memorial_id
        except digital_memorial.DoesNotExist:
            m_id = 'No digital memorial'
        return render(request, 'digital.html', {'dinfo': de, 'm_id': m_id, 'open_section': open_section})

def main_status(request):
    if request.method=="POST":
        id=request.POST['id']
        open_section=request.POST.get('open_section','0')
        try:
            ma=maintain.objects.get(pk=id)
        except maintain.DoesNotExist:
            return render(request,'services.html',{'error':'Maintainance ID does not exists','open_section':open_section})
        if ma.main_status=='pending':
            return render(request,'services.html',{'ma':ma,'open_section':open_section})
        pb=performed_by.objects.filter(main_id=ma).first()
        if pb:
            return render(request,'services.html',{'ma':ma,'pb':pb,'open_section':open_section})
        return render(request,'services.html',{'ma':ma,'open_section':open_section})