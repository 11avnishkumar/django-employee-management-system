from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.template.defaultfilters import slugify 
from django_countries.fields import CountryField
# function for automatically generating slug
def create_slug(first_name):
       slug = slugify(first_name)
       qs = Employee.objects.filter(slug=slug)
       exists = qs.exists()
       if exists:
           slug = "%s-%s" %(slug, qs.first().id)
       return slug

class Employee(models.Model):
    GENDER = [
        ('Male','Male'),
        ('Female','Female'),
        ('Transgender','Transgender'),
    ]
    
    DESIGNATION = [
        ('Designer','Designer'),
        ('Manager','Manager'),
        ('Developer','Developer'),
        ('Hr Manager','Hr Manager'),
        ('CEO','CEO'),
        ('MD','MD'),
        ('Director','Director'),
        ('Secretary','Secretary'),

    ]
    STATES = [
        ('DL','Delhi'),
        ('FBD','Faridabad'),
        ('MP','Madhya Pradesh'),
        ('AN','Andhra Pradesh'),
        ('AR','Arunachal Pradesh'),
    ]
    image = models.ImageField(upload_to='employee_pic',default='noimage.jpg')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    slug = models.SlugField(null=True,blank=True,unique=True)
    email = models.EmailField(max_length=160)
    phoneno = models.CharField(max_length=20)
    birthdate = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=50,choices=GENDER,default=None)
    country = CountryField(blank_label='Select Country')
    state = models.CharField(max_length=50, choices=STATES, default=None)
    designation = models.CharField(max_length=250, choices=DESIGNATION,default=None)
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(default=timezone.now)
    address = models.TextField()

    def get_absolute_url(self):
        return reverse('employee-details', kwargs={'employee_slug': self.slug})
    
    def __str__(self):
        return self.first_name
    # This will automatically generate slug
    def save(self, *args, **kwargs): 
         if not self.slug:
            self.slug = create_slug(self.first_name)
         return super().save(*args, **kwargs)    

class Upload_employee_details(models.Model):
    file_name = models.FileField(upload_to='emp_upload_file')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = 'Upload Employee Details'
    def __str__(self):
        return str(self.file_name)