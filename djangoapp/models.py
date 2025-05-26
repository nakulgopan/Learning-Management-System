from django.db import models

# Create your models here.
branch=(
    ('Select','Select'),
     ('EEE','Electrical & Electronics'),
    ('ME','Mechanical'),
    ('CSE', 'Computer Science'),
    ('CE','Civil Engineering '),
    ('EC','Electroncs')
)
Semester=(('0','Select'),
          ('1','S1'),
          ('2','S2'),
          ('3','S3'),
          ('4','S4'),
          ('5','S5'),
          ('6','S6'),
          ('7','S7'),
          ('8','S8'))

Att_choice =(('True','Present'),
             ('False','Absents'))

period = (('1','1'),
          ('2','2'),
          ('3','3'),
          ('4','4'),
          ('5','5'),
          ('6','6'))

class student_login(models.Model):
    s_fname=models.CharField(max_length=50)
    s_lname=models.CharField(max_length=50)
    s_DOB=models.CharField(max_length=50)
    semail=models.EmailField(max_length=254,unique='True')
    sphone=models.CharField(max_length=50)
    adm_no=models.CharField(max_length=50)
    s_branch = models.CharField(max_length=6, choices=branch, default='Select')
    Semester=models.CharField(max_length=10, choices=Semester ,default='Select')
    picture=models.ImageField(upload_to='images/',blank=True,null=True) 
    univ_no=models.CharField(max_length=50)
    username=models.CharField(max_length=50,unique='True')
    s_password =models.CharField(max_length=50,unique='True')
    
    class meta:
        db_table='Studentdb'
    def __str__(self):
        return f"{self.s_fname} {self.s_lname}-{self.s_branch}-{self.univ_no}"
        
class faculty_login(models.Model):
    f_fname=models.CharField(max_length=50)
    f_lname=models.CharField(max_length=50)
    f_Dob=models.CharField(max_length=50)
    f_email=models.EmailField(max_length=254,unique='True')
    f_phone=models.CharField(max_length=50)
    images =models.FileField(upload_to='images/',null=True ,blank = True)
    Faculty_id=models.CharField(max_length=10)
    join_date=models.CharField(max_length=20)
    f_branch = models.CharField(max_length=6, choices=branch, default='Select')
    f_username=models.CharField(max_length=50,unique='True')
    f_password =models.CharField(max_length=50,unique='True')
    role =models.CharField(max_length=20)
    
    class meta:
        db_table='Facultydb'
    def __str__(self):
        return f"{self.f_fname} {self.f_lname} - {self.f_branch}({self.Faculty_id})"


class Notice(models.Model):
    title = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='pdfs/', null=True, blank=True)  # Store the PDF
    apply_link = models.URLField(null=True, blank=True)  # Store the apply now link

    class meta:
        db_table='noticetable'

class gallery(models.Model):
    title=models.CharField(max_length=255)
    images =models.FileField(upload_to='images/',null=True ,blank = True)
    video = models.FileField(upload_to='videos/',null=True, blank=True)
    Description=models.CharField(max_length=500)
    
    class meta:
        db_table='gallerydb'

class Folder(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = 'folder_table' 

    def __str__(self):
        return self.name  

class File(models.Model):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name='files')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)

    class Meta:
        db_table = 'file_table'
    
class cefacaulty(models.Model):
    images =models.FileField(upload_to='images/',null=True ,blank = True)
    Name=models.CharField(max_length=255)
    Position=models.CharField(max_length=255)
    Qualification = models.CharField(max_length=255)
    
    def __str__(self):
        return self.Name  
    
class csefacaulty(models.Model):
    images =models.FileField(upload_to='images/',null=True ,blank = True)
    Name=models.CharField(max_length=255)
    Position=models.CharField(max_length=255)
    Qualification = models.CharField(max_length=255)
    
    def __str__(self):
        return self.Name  
    

class course(models.Model):
    Branch = models.CharField(max_length=6, choices=branch, default='Select')  
    Semester = models.CharField(max_length=10, choices=Semester ,default='Select')
    Course_1= models.CharField(max_length=255)
    Course_2= models.CharField(max_length=255)
    Course_3= models.CharField(max_length=255)
    Course_4= models.CharField(max_length=255)
    Course_5= models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.Branch} -{self.Semester}"

class courseselected(models.Model):
    Courses = models.CharField(max_length=255)
    faculty = models.CharField(max_length=255)
    Branch = models.CharField(max_length=6, choices=branch, default='Select')  
    Semester = models.CharField(max_length=10, choices=Semester ,default='Select')
    
    def __str__(self):
        return self.faculty
    
    
class studentsubjects(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    admission_no = models.CharField(max_length=255)
    university_no =  models.CharField(max_length=255)
    Branch = models.CharField(max_length=6, choices=branch, default='Select')  
    Semester = models.CharField(max_length=10, choices=Semester ,default='Select')
    Course_1= models.CharField(max_length=255)
    Course_2= models.CharField(max_length=255)
    Course_3= models.CharField(max_length=255)
    Course_4= models.CharField(max_length=255)
    Course_5= models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.firstname}{self.lastname}-{self.Semester}-{self.Branch}"
    
class application_form(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    admission_no = models.CharField(max_length=255)
    university_no =  models.CharField(max_length=255)
    Branch = models.CharField(max_length=6, choices=branch, default='Select')  
    Tutor = models.ForeignKey(faculty_login, on_delete=models.CASCADE)
    HoD = models.CharField(max_length=255)
    Principal = models.CharField(max_length=255)
    Subject = models.CharField(max_length=500)
    Details = models.CharField(max_length=1500)
    Semester =models.CharField(max_length=10, choices=Semester ,default='Select')
    
    def __str__(self):
        return f"{self.firstname}{self.lastname}- {self.Semester}-{self.Branch}"


class tutorapprovalform(models.Model):
    Studentname=models.CharField(max_length=255)
    admission_no = models.CharField(max_length=255)
    university_no =  models.CharField(max_length=255)
    Branch = models.CharField(max_length=6, choices=branch, default='Select')  
    Subject = models.CharField(max_length=500)
    Details = models.CharField(max_length=1500)
    Semester =models.CharField(max_length=10, choices=Semester ,default='Select')
    HoD = models.ForeignKey(faculty_login, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.Studentname}-{self.Semester}-{self.Branch}"

class HoDapproval(models.Model):
    Studentname=models.CharField(max_length=255)
    admission_no = models.CharField(max_length=255)
    university_no =  models.CharField(max_length=255)
    Branch = models.CharField(max_length=6, choices=branch, default='Select')  
    Subject = models.CharField(max_length=500)
    Details = models.CharField(max_length=1500)
    Semester =models.CharField(max_length=10, choices=Semester ,default='Select')
    Tutor =  models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.Studentname}-{self.Semester}-{self.Branch}-{self.Tutor}"
    
class attendance_faculty(models.Model):
    Branch = models.CharField(max_length=6, choices=branch, default='Select') 
    Semester = models.CharField(max_length=6, choices=branch, default='Select') 
    Subject = models.CharField(max_length=500)
    Student_name = models.CharField(max_length=255)
    Register_no =models.CharField(max_length =255)
    Period = models.CharField(max_length=6, choices = period, default='select')
    Date = models.DateField()
    Attendance = models.CharField(max_length=6, choices=Att_choice, default='Select') 
    
    def __str__(self):
        return f"{self.Student_name}-{self.Semester}-{self.Branch}"

class ecefaculty(models.Model):
    images =models.FileField(upload_to='images/',null=True ,blank = True)
    Name=models.CharField(max_length=255)
    Position=models.CharField(max_length=255)
    Qualification = models.CharField(max_length=255)
    
    def __str__(self):
        return self.Name  
    
class mefaculty(models.Model):
    images =models.FileField(upload_to='images/',null=True ,blank = True)
    Name=models.CharField(max_length=255)
    Position=models.CharField(max_length=255)
    Qualification = models.CharField(max_length=255)
    
    def __str__(self):
        return self.Name  

class eeefaculty(models.Model):
    images =models.FileField(upload_to='images/',null=True ,blank = True)
    Name=models.CharField(max_length=255)
    Position=models.CharField(max_length=255)
    Qualification = models.CharField(max_length=255)
    
    def __str__(self):
        return self.Name  

class asfaculty(models.Model):
    images =models.FileField(upload_to='images/',null=True ,blank = True)
    Name=models.CharField(max_length=255)
    Position=models.CharField(max_length=255)
    Qualification = models.CharField(max_length=255)
    
    def __str__(self):
        return self.Name  