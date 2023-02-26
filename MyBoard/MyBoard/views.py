from django.shortcuts import render, redirect, get_object_or_404
from .models import MyBoard, MyMember
from django.utils import timezone
from django.core.paginator import Paginator

def register(request):
    if request.method == "GET":
        return render(request,'register.html')
    elif request.method == "POST":
        myname = request.POST['myname1']
        mypassword = request.POST['mypassword']
        myemail = request.POST['myemail']

        result = MyMember.objects.create(myname=myname,mypassword=mypassword,myemail=myemail)

        return redirect('index1')

        # myboard_all = MyBoard.objects.all().order_by('-id')
        # return render(request,'index.html',{'board_all':myboard_all})
        
def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    elif request.method == 'POST':
        myname = request.POST['myname']
        mypassword = request.POST['mypassword']
        

        # mymember = MyMember.objects.get(myname=myname)
        mymember = MyMember.objects.filter(myname=myname)
        # mymember = get_object_or_404(MyMember,myname=myname)
        print('--------post myname------')
        print(myname)
        print('---------MyMember myname--------')
        print(mymember[0].myname, mymember[1].myname)

        if mypassword == mymember[0].mypassword :
            # 성공했으니 로그인이 된 페이지
            
            request.session['myname'] = mymember.myname
            return redirect('index1')
        else:
            # 다시 로그인 페이지
            return redirect('login')

def logout(request):
    del request.session['myname']
    return redirect('index1')

def index(request):
    myboard_all = MyBoard.objects.all().order_by('-id')
    # select * from MyBoard_MyBoard

    paginator = Paginator(myboard_all,5)  #5개씩 paging을 합니다.
    page_num = request.GET.get('page','1') #page 값이 없으면 default 1
    #페이지에 맞는 모델
    page_obj = paginator.get_page(page_num)


    #총개시물 수
    # print('--------count-------')    
    # print(page_obj.count)
    # print('------number - 현재 페이지번호-------')  
    # print(page_obj.number)

    # print('------paginator.num_pages 총 페이지 수-----')
    # print(page_obj.paginator.num_pages)

    # #총 페이지 range객체
    # print('------총 페이지 range객체-----')
    # print(page_obj.paginator.page_range)

    # print('------다음페이지has_next(), 이전페이지has_previous()-----')    
    # print(page_obj.has_next())
    # print(page_obj.has_previous())


    # try : 
    #     print('----- 다음페이지 next_page_number() -----')    
    #     print(page_obj.next_page_number())  #없으면 에러 발생

    #     print('----- 이전페이지 previous_page_number()-----')    
    #     print(page_obj.previous_page_number()) #없으면 에러 발생
    # except:
    #     pass

    # print('------- start_index()--------')
    # print(page_obj.start_index())
    # print('------- end_index()--------')
    # print(page_obj.end_index())



    return render(request,'index.html',{'board_all':page_obj})
    # return render(request,'index.html',{'board_all':myboard_all})
    #render 리턴값이 HttpResponse 임

def insert_form(request):
    return render(request,'insert_form.html')
    
def insert_proc(request):
    name = request.POST['myname']
    title = request.POST['mytitle']
    content = request.POST['mycontent']

    result = MyBoard.objects.create(myname=name,mytitle=title,mycontent=content,
                            mydate=timezone.now())
    # MyBoard.objects.create(myname='1',mytitle='1',mycontent='1',
    #                         mydate=timezone.now())
    # from django.utils import timezone
    print ('==================')
    print (result)
    print ('==================')
    # def __str__(self): 정의된 내용이 result값으로 보내짐

    if result :
        return redirect('index1')
        # return redirect('/')
        # from django.shortcuts import render, redirect
        # http://127.0.0.1/
    else:
        return redirect('forminsert')
        # return redirect('/insert_form')
        # http://127.0.0.1/insert_form

def detail(request,id):
    dto = MyBoard.objects.get(id=id)
    return render(request,'detail.html',{'dto':dto})

def delete_proc(request,id):
    result = MyBoard.objects.get(id=id).delete()
    if result[0] :
      return redirect('index1')

def update_proc(request,id):
    post = MyBoard.objects.get(id=id)
    return render(request,'update_form.html',{'dto':post})

def update_res(request,id):
    mytitle = request.POST['mytitle']
    name = request.POST['myname']
    content = request.POST['mycontent']
    # id = request.POST['id']
    print ('----------title 확인--------------')
    print (mytitle)
    print ('----------title 확인--------------')
    post = MyBoard.objects.filter(id=id)
    result1 = post.update(mytitle=mytitle)
    result2 = post.update(myname=name)
    result3 = post.update(mycontent=content)

    if result1 + result2 + result3 == 3 :
        return redirect('detail',id=id)
        #http://127.0.0.1/detail/id

