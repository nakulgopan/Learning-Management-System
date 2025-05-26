from copy import error
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from djangoapp.models import  Folder, Notice, application_form, cefacaulty, course, csefacaulty, ecefaculty, faculty_login,student_login,gallery,File,courseselected, studentsubjects
from djangoapp.forms import Attendanceform, FacultyForm, StudentForm,Liveform, applicationform, selectedform, subject_form, tutorapproval_form
# from django.contrib.auth import authenticate,login
from django.contrib import messages
# Create your views here.

#student_registration
def student(request):
    if request.method =="POST":
        form=StudentForm(request.POST,request.FILES)
        if form.is_valid():
            print('valid')
            try:
                form.save()
                print('Save')
                return redirect('/stulogin/')
            except:
                pass
    else:
        form=StudentForm()
    
    return render(request,'studentlog.html',{'form':form})

#faculty_registration
def Faculty(request):
    if request.method =="POST":
        form = FacultyForm(request.POST,request.FILES)
        if form.is_valid():
            print('valid')
            try:
                faculty =form.save()
                print(vars(faculty))
                print("done")
                messages.success(request, 'Account was created for ')
                return redirect('/fac_login/')
                
            except:
                pass
    else:
        form=FacultyForm()
    return render(request,'facultylog.html',{'form':form})

#student_loginpage
def studentlogin(request):
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            print(username)
            print(password)
            
            user = student_login.objects.filter(username=username, s_password=password).first()
            print(user)
            if user :
               request.session['s_fname'] = user.s_fname
               request.session['username'] = username
               return redirect('/studentdashboard')
            else:
                messages.error(request, 'Username or password is incorrect')
        return render(request, 'stulogin.html')

#faculty_loginpage   
def faclogin(request):
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            print(username)
            print(password)
            
            user = faculty_login.objects.filter(f_username=username, f_password=password).first()
            print(user)
            if user:
               request.session['f_username'] = username
               request.session['f_fname']=user.f_fname
               print(user.f_fname)
               print(user) 
               return redirect('/facultydashboard')
            else:
                # Add error handling here. Consider providing a message to the user.
                messages.error(request,"Invalid Username or Password.....!")
        
        return render(request, 'faclogin.html')


#main_page
def index(request):
    return render(request, 'index.html')

#campus
def campus(request):
    return render(request,"campus.html")

#notices        
def notices(request):
    jobs=Notice.objects.all()
    return render(request, 'notices.html', {'jobs': jobs})
#courses
def courses(request):
    return render(request,"courses.html")
#ugc
def ugc(request):
    return render(request,"UGC.html")
#collegeunion
def collegeunion(request):
    return render(request,"collegeunion.htm.html")
#ourcollege
def ourcollege(request):
    return render(request,"ourcollege.html")
#contactus
def contactus(request):
    return render(request,"contacts.html")
#gallery
def pics(request):
    files= gallery.objects.all()
    return render(request,'gallery.html',{'files':files})

#governing body

def governingbody(request):
    return render(request,"governingbody.html")

#PTA
def pta(request):
    return render(request,"pta.html")

#principaldesk
def principaldesk(request):
    return render(request,"principaldesk.html")

#liveclass
def file_list(request):
    # Fetch all folders and prefetch related files for better performance
    folders = Folder.objects.prefetch_related('files').all()

    # Organize files by their folder name
    folder_wise_files = {folder.name: folder.files.all() for folder in folders}

    return render(request, 'live_class.html', {'folder_wise_files': folder_wise_files})
    

def live_class_update(request):
    if request.method == "POST":
        form = Liveform(request.POST, request.FILES)  # Handle file uploads
        if form.is_valid():
            form.save()
            return redirect('/liveclass')  # Redirect to avoid duplicate form submission
    else:
        form = Liveform()

    return render(request, 'facultyliveclass.html', {'form': form,})

#dashboard_student
def studentdashboard(request):
    if 'username' in request.session:  # Check if user is logged in
        username = request.session.get('username')  # Get logged-in username
        
        try:
            user = student_login.objects.get(username=username)  # Fetch student details
        except student_login.DoesNotExist:
            return redirect('studentlogin')  # Redirect if user not found

        # Get image URL (if available) and first name
        profile_picture = user.picture.url if user.picture else None
        current_user = user.s_fname  

        context = {
            'current_user': current_user,
            'profile_picture': profile_picture
        }
        return render(request, 'student_dashboard.html', context)
    
    else:
        return redirect('studentlogin')

def logout(request):
    if 'username' in request.session:
        del request.session['username']  # Remove session key safely
    return redirect('/stulogin')  


#dashboard_faculty

def facultydashboard(request):
    if 'f_username' in request.session:  # Corrected condition
       username = request.session.get('f_username')
       try:
           user=faculty_login.objects.get(f_username = username)
       except faculty_login.DoesNotExist:
           return redirect('faclogin')
       profile_picture= user.images.url if user.images else None
       current_user = user.f_fname
       context= {
           'current_user':current_user,
           'profile_picture':profile_picture
       }
       return render(request,'facultydashboard.html',context)
    else:
       return redirect('faclogin')
   
def logout_faculty(request):
    if 'f_username' in request.session:
        del request.session['f_username']  # Remove session key safely
    return redirect('/fac_login')
   
#department
def civilengineering(request):
   return render(request, 'civil.html')

def cse(request):
   return render(request, 'cse.html')

def ece(request):
   return render(request, 'ece.html')

def eee(request):
   return render(request, 'eee.html')

def Me_engineering(request):
   return render(request, 'mechanical.html')

def applied(request):
    return render(request,'appliedscience.html')

def csehod(request):
    return render(request,'csehod.html')

def csefacilities(request):
    return render(request,'csefacilities.html')

def csepublications(request):
    return render(request,'csepublications.html')
def cseplacement(request):
    return render(request,'cseplacement.html')
def cseclubs(request):
    return render(request,'cseclubs.html')
#department_civil
def cefaculty(request):
    files= cefacaulty.objects.all()
    return render(request,'civilfaculty.html',{'files':files})

def cehod(request):
    return render(request,"cehod.html")
def cevission(request):
    return render(request,"cevissionmission.html")

def ceclubs(request):
    return render(request,"clubs.html")

def cefacilities(request):
    return render(request,"cefacilities.html")

def cepublications(request):
    return render(request,"cepublications.html")

def ceplacement(request):
    return render(request,"ceplacement.html")

def ceevents(request):
    return render(request,"ceevents.html")

#computerscience_department
def csevission(request):
    return render(request,"csevission.html")

def cseevents(request):
    return render(request,"cseevents.html")

def csefaculty(request):
     staff= csefacaulty.objects.all()
     return render(request,'csefaculty.html',{'staff':staff})
 
def ece_faculty(request):
     staff= ecefaculty.objects.all()
     return render(request,'ecefaculty.html',{'staff':staff})

def ecevission(request):
    return render(request,'ecevission.html')

def ecehod(request):
    return render(request,'ecehod.html')

def ecepublications(request):
    return render(request,'ecepublications.html')

def ecefacilities(request):
    return render(request,'ecefacilities.html')

def newsemester(request):
    
    username = request.session.get('username')
    
    if not username:
        return redirect('stulogin')
    try:
        user = student_login.objects.get(username=username)  
    except student_login.DoesNotExist:
        return redirect('stulogin')

    profile_picture = user.picture.url if user.picture else None
    current_user = user.s_fname
    # students=student_login.objects.get(username=username)
    context = {
        'current_user': current_user,
        'profile_picture': profile_picture,
        'details':[user],
    }
   
    return render(request, "newsem_reg.html", context)

def semformupdate(request,username):
    try:
        students = student_login.objects.get(username=username)
    except student_login.DoesNotExist:
        return redirect('newsemester')

    if request.method == "POST":
        form = StudentForm(request.POST, instance=students)
        if form.is_valid():
            print("formvalid")
            try:
                form.save()
                print("Form saved successfully.")
                return redirect('/courseselection/')
            except Exception as e:
                print(f"Error saving form: {e}")
        else:
            print("Form is not valid:", form.errors)
    else:
        form = StudentForm(instance=students)  

    return render(request, 'newsem_reg.html', {'form': form})



#applicationof student
def application(request):
    username = request.session.get('username')
    
    if not username:
        return redirect('stu_login')

    try:
        user = student_login.objects.get(username=username)
    except student_login.DoesNotExist:
        return redirect('stu_login')

    if request.method == "POST":  
        form = applicationform(request.POST)
        if form.is_valid():
            try:
                form.save()
                print("Form saved successfully.")
                return redirect('/applicationform/')
            except Exception as e:
                print(f"Error saving form: {e}")
        else:
            print("Form is not valid:", form.errors)
    else:
        form = applicationform()  
        
    app = application_form.objects.filter(university_no=user.univ_no)
    profile_picture = user.picture.url if user.picture else None
    current_user = user.s_fname
    tutors = faculty_login.objects.filter(role='Tutor')
    hods = faculty_login.objects.filter(role='HOD')
    principals = faculty_login.objects.filter(role='Principal')
    print(tutors)


    context = {
        'current_user': current_user,
        'profile_picture': profile_picture,
        'details': [user],
        'tutors': tutors,
        'hods': hods,
        'principals': principals,
        'form': form,
        'app':app
    }
    return render(request, "applicationform_stu.html", context)


#studentcourseselection
def courseselection(request):
    
    username = request.session.get('username')
   
    if not username:
        return redirect('courseselection')

    try:
        user = student_login.objects.get(username=username)
        print(user.Semester,user.s_branch)
        
    except student_login.DoesNotExist:
        return redirect('courseselection')
    x = studentsubjects.objects.filter(Semester=user.Semester, university_no=user.univ_no).first()
    showcourses = courseselected.objects.filter(Semester=user.Semester, Branch=user.s_branch)
    
    profile_picture = user.picture.url if user.picture else None
    current_user = user.s_fname
    
    # Filtering courses based on category and branch
    Course_1 = course.objects.filter(Branch=user.s_branch,Semester=user.Semester)
    Course_2 = course.objects.filter(Branch=user.s_branch,Semester=user.Semester)
    Course_3 = course.objects.filter(Branch=user.s_branch,Semester=user.Semester)  
    Course_4 = course.objects.filter(Branch=user.s_branch,Semester=user.Semester)
    Course_5 = course.objects.filter(Branch=user.s_branch,Semester=user.Semester)

    context = {
        'current_user': current_user,
        'profile_picture': profile_picture,
        'details': [user],
        'Course_1': Course_1,
        'Course_2': Course_2,
        'Course_3': Course_3,
        'Course_4': Course_4,
        'Course_5': Course_5,
        'showcourses': showcourses,
        # 'subjects':subjects
       
       
    }

    return render(request, "courseselection.html", context)

def cousre_update(request, username):
    username = request.session.get('username')

    if not username:
        return redirect('stulogin')

    try:
        students = student_login.objects.get(username=username)
    except student_login.DoesNotExist:
        return redirect('stulogin')
    student_subjects = studentsubjects.objects.filter(
        university_no=students.univ_no,
        Semester=students.Semester
    ).first()

    if not student_subjects:
        student_subjects = studentsubjects(
            firstname=students.s_fname,
            lastname=students.s_lname,
            admission_no=students.adm_no,
            university_no=students.univ_no,
            Branch=students.s_branch,
            Semester=students.Semester
        )

    # ✅ Use student_subjects in the form, not students
    if request.method == "POST":
        form = subject_form(request.POST, instance=student_subjects)
        if form.is_valid():
            print("formvalid")
            try:
                saved = form.save()
                print(vars(saved))  # ✅ Now shows Course_1 to Course_5
                print("Form saved successfully.")
                return redirect('/courseselection/')
            except Exception as e:
                print(f"Error saving form: {e}")
        else:
            print("Form is not valid:", form.errors)
    else:
        form = subject_form(instance=student_subjects)  # ✅ Same fix for GET
    
    fetchcourse = studentsubjects.objects.get(Semester = student_subjects.Semester, university_no = student_subjects.university_no)

    # Keep everything else as-is
    all_courses = courseselected.objects.filter(Branch=students.s_branch, Semester=students.Semester)
    Course_1 = course.objects.filter(Branch=students.s_branch, Semester=students.Semester)
    Course_2 = course.objects.filter(Branch=students.s_branch, Semester=students.Semester)
    Course_3 = course.objects.filter(Branch=students.s_branch, Semester=students.Semester)  
    Course_4 = course.objects.filter(Branch=students.s_branch, Semester=students.Semester)
    Course_5 = course.objects.filter(Branch=students.s_branch, Semester=students.Semester)

    context = {
        'current_user': students.s_fname,
        'profile_picture': students.picture.url if students.picture else None,
        'details': [students],
        'courses': all_courses,
        'showcourses': courseselected.objects.filter(Semester=students.Semester, Branch=students.s_branch),
        'form': form,
        'Course_1': Course_1,
        'Course_2': Course_2,
        'Course_3': Course_3,
        'Course_4': Course_4,
        'Course_5': Course_5,
        'fetchcourse':fetchcourse
    }

    return render(request, 'courseselection.html', context)

    
#facultycourse
def facultycourse(request):
    if 'f_username' not in request.session:
        return redirect('faclogin')

    username = request.session.get('f_username')
    try:
        user = faculty_login.objects.get(f_username=username)
    except faculty_login.DoesNotExist:
        return redirect('faclogin')

    # Handle form submission
    if request.method == "POST":
        form = selectedform(request.POST)
        if form.is_valid():
            print(user)
            try:
                instance = form.save(commit=False)
                instance.faculty = user  # assuming the model has a `faculty` field
                instance.save()
                print(user, "saved")
                return redirect('/facultycourseselection/')
            except Exception as e:
                print("Error saving form:", e)
        else:
            print("Form is not valid:", form.errors)
    else:
        form = selectedform()
    username = request.session.get('f_username')
    showcourses = courseselected.objects.filter(faculty = user).values()
   
    print(showcourses)
    profile_picture = user.images.url if user.images else None
    current_user = user.f_fname

    # Course lists (you could combine this if needed)
    Courses = course.objects.filter(Branch = user.f_branch)
   
    

    context = {
        'current_user': current_user,
        'profile_picture': profile_picture,
        'details': [user],
        'Courses': Courses,
        'form': form,
        'showcourses': showcourses
       
    }

    return render(request, "facultycourse.html", context)


def tutorapproval(request):
    if 'f_username' not in request.session:
        return redirect('faclogin')

    username = request.session.get('f_username')
    try:
        user = faculty_login.objects.get(f_username=username)
    except faculty_login.DoesNotExist:
        return redirect('faclogin')

    # Handle form submission
    if request.method == "POST":
        form = tutorapproval_form(request.POST)
        if form.is_valid():
            print("Error saving form:", e)
            try:
                instance = form.save(commit=False)
                instance.faculty = user  # assuming the model has a `faculty` field
                instance.save()
                print(user, "saved")
                return redirect('/admin/')
            except Exception as e:
                print("Error saving form:", e)
        else:
            print("Form is not valid:", form.errors)
    else:
        form = tutorapproval_form()
    username = request.session.get('f_username')
    showapplications = application_form.objects.filter(Branch = user.f_branch,Tutor= user)
    print(showapplications)
    profile_picture = user.images.url if user.images else None
    current_user = user.f_fname
    
    context = {
        'current_user': current_user,
        'profile_picture': profile_picture,
        'details': [user],
        'form': form,
        'showapplications': showapplications,
       
    }

    return render(request, "applicationapproval.html", context)

#attendace faculty

# def attendance_faculty(request):
    # if 'f_username' not in request.session:
    #     return redirect('faclogin')

    # username = request.session.get('f_username')
    # try:
    #     user = faculty_login.objects.get(f_username=username)
    # except faculty_login.DoesNotExist:
    #     return redirect('faclogin')
    # if request.method == "POST":
    #     form = Attendanceform(request.POST)
    #     if form.is_valid():
    #         print("Error saving form:", e)
    #         try:
    #             instance = form.save(commit=False)
    #             instance.faculty = user  # assuming the model has a `faculty` field
    #             instance.save()
    #             print("Attendance marked")
    #             return redirect('/admin/')
    #         except Exception as e:
    #             print("Error saving form:", e)
    #     else:
    #         print("Form is not valid:", form.errors)
    # else:
    #     form = Attendanceform()
    
    # faculty = courseselected.objects.get(user = faculty)    
    # Courses = courseselected.objects.filter(Branch = faculty.Branch, Semester = faculty.Semester,Subject = faculty.Courses)
    # profile_picture = user.images.url if user.images else None
    # current_user = user.f_fname
    # context = {
    #     'current_user': current_user,
    #     'profile_picture': profile_picture,
    #     'details': [user],
    #     'form':form,
    #     'Courses':Courses
       
       
    # }
    # return render(request,"attendancebyfaculty.html",context)
def attendance_faculty(request):
    if 'f_username' not in request.session:
        return redirect('faclogin')

    username = request.session.get('f_username')

    try:
        user = faculty_login.objects.get(f_username=username)
    except faculty_login.DoesNotExist:
        return redirect('faclogin')

    if request.method == "POST":
        form = Attendanceform(request.POST)
        if form.is_valid():
            try:
                instance = form.save(commit=False)
                instance.faculty = user  # Only if Attendance model has a ForeignKey to faculty_login
                instance.save()
                print("Attendance marked")
                return redirect('/admin/')  # Or any success page
            except Exception as e:
                print("Error saving form:", e)
        else:
            print("Form is not valid:", form.errors)
    else:
        form = Attendanceform()

    # Fetch course details based on faculty's username
   
    # Change from .get() to .filter() to handle multiple courses
    faculty_data = courseselected.objects.filter(faculty=user)  # This returns a queryset
    Courses = courseselected.objects.filter(
        Branch__in=[course.Branch for course in faculty_data],  # Filter courses by Branch and Semester
        Semester__in=[course.Semester for course in faculty_data],
        Courses__in=[course.Courses for course in faculty_data]
    )
    
    # You need to adjust how you fetch studentdetails to account for multiple courses
    # If you want to fetch students based on the same semester, use filter
    studentdetails = studentsubjects.objects.filter(Semester__in=[course.Semester for course in faculty_data])
    
    profile_picture = user.images.url if user.images else None
    current_user = user.f_fname

    context = {
        'current_user': current_user,
        'profile_picture': profile_picture,
        'details': [user],
        'form': form,
        'Courses': Courses,
        'studentdetails': studentdetails
    }

    return render(request, "attendancebyfaculty.html", context)
