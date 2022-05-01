from django.shortcuts import render, redirect
from .forms import addEmployee ,Employee_uploaded_details
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from employee.models import Employee, Upload_employee_details
from django.core.paginator import Paginator
import csv

# Home Page
@login_required
def homePage(request):
    queryset = Employee.objects.all()

    page = Paginator(queryset,6) #setting up paginator
    new_page = request.GET.get('page')
    new_list = page.get_page(new_page)

    total_active_employee = queryset.filter(is_active=True).count() #count how many are Active user
    total_de_active_employee = queryset.filter(is_active=False).count() #count how many are InActive user
    search_by_email = request.GET.get('email')
    search_by_phone_no = request.GET.get('phone_no')
    search_by_gender = request.GET.get('gender')
    if search_by_email != '' and search_by_email is not None:
        queryset = queryset.filter(email__icontains=search_by_email)
    else:
       queryset = Employee.objects.all()     
    context = {
        'employee_details' : new_list,
        'total_active_employee':total_active_employee,
        'total_de_active_employee':total_de_active_employee,
        'page':new_list,
    }
    template_name = 'employee/index.html'
    return render(request, template_name, context)

# Add Employee
@login_required
def add_employee(request):
    if request.method == 'POST':
        form = addEmployee(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Employee has been added successfully')
            return redirect('home-page') #redirect the user to homepage
        # else:
        #     print(form.errors) for debuggin purpose       
    else:
        form = addEmployee()
    context = {
        'form': form
    }
    template_name = 'employee/add_new_employee.html'
    return render(request, template_name, context)

# Show Employee Details
@login_required
def viewEmployeeDetails(request, employee_slug):
    queryset = Employee.objects.get(slug=employee_slug)
    context = {

        'employee_details': queryset
    }
    template_name = 'employee/view_single_employee_details.html'
    return render(request, template_name, context)

# Update Employee Record
@login_required
def updateEmployee(request, id):
    edit = Employee.objects.get(id=id)
    form = addEmployee(instance=edit)
    if request.method == 'POST':
        form = addEmployee(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            messages.success(request, f'Employee has been updated successfully')
            return redirect('home-page')
        else:
            print(form.errors)    
    context = {
        'form': form
    }
    template_name = 'employee/update_employee.html'
    return render(request, template_name, context)

# Delete/Make user inactive or Vice-Versa
# This method getting the value from the hyperlink
@login_required
def inactive_employee(request, id):
    if request.method == 'GET':
        employee = Employee.objects.get(id=id)
        if employee.is_active==True:
            employee.is_active=False #this will assign is_active a false value
            # messages.success(request, 'Employee has been Inactive successfully')
        else:
            employee.is_active=True   
        employee.save()
        # messages.success(request, 'Employee has been active successfully')
    return redirect('home-page')

#upload_file_view
@login_required
def upload_file_view(request):
    if request.method == 'POST':
       form = Employee_uploaded_details(request.POST or None,request.FILES or None)
       if form.is_valid():
          form.save()
          form = Employee_uploaded_details() #clear the form once data saved
          obj = Upload_employee_details.objects.get(activated=False)
          with open(obj.file_name.path,'r') as f:
              reader = csv.reader(f)
              for i,row in reader:
                  if i == 0:
                      pass
                  else:  
                   print(row)
    else:
        form = Employee_uploaded_details()   
    context = {'form': form }
    template_name = 'employee/upload_emp_detail.html'
    return render(request,template_name,context)