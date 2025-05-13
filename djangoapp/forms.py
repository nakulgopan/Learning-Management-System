from django import forms  
from djangoapp.models import File, HoDapproval, application_form, attendance_faculty, course, courseselected, faculty_login, student_login, studentsubjects, tutorapprovalform

class StudentForm(forms.ModelForm):  
    s_password=forms.CharField(widget=forms.PasswordInput)
    class Meta:  
        model = student_login  
        fields = "__all__"  
        
class FacultyForm(forms.ModelForm):
    f_password= forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=faculty_login
        fields ="__all__"
        
class Liveform(forms.ModelForm):
    class Meta:
        model = File
        fields ="__all__"

class courseform(forms.ModelForm):
    class Meta:
        model = course 
        fields = "__all__"

class selectedform(forms.ModelForm):
    class Meta:
        model = courseselected
        fields =['Semester','Courses','Branch','faculty']
        
class subjectform(forms.ModelForm):
    class Meta:
        model = studentsubjects
        fields = "__all__"

class applicationform(forms.ModelForm):
    class Meta:
        model = application_form
        fields = "__all__"
        
class tutorapproval_form(forms.ModelForm):
    class Meta:
        model = tutorapprovalform
        fields = "__all__"

class Hodformapproval(forms.ModelForm):
    class Meta:
        model = HoDapproval
        fields ="__all__"
    
class Attendanceform(forms.ModelForm):
    class Meta:
        model = attendance_faculty
        fields ="__all__"