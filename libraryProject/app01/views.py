from django.shortcuts import render,redirect
from django.utils import timezone

import app01.models
from app01 import models

guser = ''
# Create your views here.
# 新增出版社函数，负责将表单提交的数据写入数据库
def add_publisher(request):
    if request.method =="POST":
        # 获取表单数据
        publisher_name = request.POST.get('name')
        publisher_address = request.POST.get('address')
        # 保存到数据库
        models.Publisher.objects.create(name=publisher_name, address=publisher_address)
        return redirect("/app01/publisher_list")
    return render(request, "add_publisher.html")

# 出版社列表函数，以字典的形式返回数据库中所有的出版社记录给前端页面
def publisher_list(request):
    # 查询数据库中的所有信息
    publishers_list = models.Publisher.objects.all()
    return render(request, "publisher_list.html", {"publishers_list":publishers_list})

# 出版社信息编辑函数，负责将修改的数据更新到数据库
def edit_publisher(request):
    if request.method == 'POST':
        # 获取修改内容
        id = request.POST.get('id')
        name = request.POST.get('name')
        address = request.POST.get('address')
        # 根据id获取对象
        publisher = models.Publisher.objects.get(id=id)
        # 修改
        publisher.name = name
        publisher.address = address
        publisher.save()
        # 重定向到publisher_list
        return redirect('/app01/publisher_list/')
    else:
        id  = request.GET.get('id')
        publisher = models.Publisher.objects.get(id=id)
        publishers_list = models.Publisher.objects.all()
        return render(request, 'edit_publisher.html', {"publisher":publisher, "publishers_list":publishers_list})

# 删除出版社函数，负责删除数据库中指定的出版社
def delete_publisher(request):
    # 获取ID
    id = request.GET.get('id')
    # 删除
    models.Publisher.objects.filter(id=id).delete()
    return redirect("/app01/publisher_list/")

# 书籍列表函数，以字典的形式返回数据库中所有的书籍记录给前端页面
def book_list(request):
    books_list = models.Book.objects.all()
    return render(request, 'book_list.html', {"books_list": books_list})

# 新增书籍函数，将表单提交的新增书籍函数写入到数据库中
def add_book(request):
    publishers_list = models.Publisher.objects.all()
    if request.method == "POST":
        id = request.POST.get('id')
        name = request.POST.get('name')
        price = request.POST.get('price')
        nums = request.POST.get('nums')
        sales = request.POST.get('sales')
        publisher = request.POST.get('publisher')
        models.Book.objects.create(name=name, price=price, nums=nums, sales=0, publisher_id=publisher)
        return redirect('/app01/book_list/')
    else:
        return render(request, "add_book.html", {"publishers_list": publishers_list})

# 书籍删除函数，负责删除数据库中指定的书籍
def delete_book(request):
    id = request.GET.get('id')
    models.Book.objects.filter(id=id).delete()
    return redirect('/app01/book_list/')

# 编辑书籍函数，负责将表单中的信息更新到数据库
def edit_book(request):
    if request.method == "POST":
        id = request.POST.get('id')
        name = request.POST.get('name')
        price = request.POST.get('price')
        nums = request.POST.get('nums')
        sales = request.POST.get('sales')
        publisher = request.POST.get('publisher')
        book = models.Book.objects.get(id=id)
        book.name = name
        book.price = price
        book.nums = nums
        book.sales = sales
        book.publisher_id = publisher
        book.save()
        return redirect('/app01/book_list/')
    else:
        id = request.GET.get('id')
        book = models.Book.objects.get(id=id)
        publishers_list = models.Publisher.objects.all()
        return render(request, 'edit_book.html', {'book':book, 'publishers_list':publishers_list})

# 登录页面函数，负责处理用户登录请求
def index(request):
    if request.method == 'POST':
        user_name = request.POST.get('name')
        user_passwd = request.POST.get('passwd')
        user = ''
        # 若登录名为admin则重定向到管理员视图
        if user_name == 'admin' and user_passwd == '123456':
            print("admin")
            return redirect('/app01/book_list/')
        # 数据库中不存在该用户则重定向回登录页面
        try:
            user = models.User.objects.get(name=user_name)
        except app01.models.User.DoesNotExist:
            return redirect('/app01/')
        passwd = user.password
        # 比对登录密码
        if user_passwd==passwd:
            # return render(request, 'borrow_list.html', {'user':user})
            global guser
            guser = user.name
            return redirect('/app01/borrow_list/')  # 密码正确
        else:
            return redirect('/app01/')  # 密码错误
    else:
        return render(request, 'index.html')

# 新用户注册函数，负责处理用户注册请求
def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        passwd = request.POST.get('passwd')
        models.User.objects.create(name=name, password=passwd)
        return redirect('/app01/')
    else:
        return render(request, 'user_register.html')

# 可出借书籍列表函数，返回数据库中可借阅的书籍列表
def borrow_list(request):
    user = guser
    print(user)
    books_list = models.Book.objects.all()
    return render(request, 'borrow_list.html', {'user':user, 'books_list':books_list})

# 借书函数，显示当前借阅信息，并负责处理用户提交的借书请求，将借阅记录写入数据库
def borrow_book(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        book_name = request.POST.get('book_name')
        user = models.User.objects.get(name=user_name)
        book = models.Book.objects.get(name=book_name)
        book.sales += 1
        book.nums -= 1
        book.save()
        models.Borrow.objects.create(book_id=book, user_id=user, time=timezone.now())
        return redirect('/app01/borrow_list/')
    else:
        book_id = request.GET.get('id')
        book = models.Book.objects.get(id=book_id)
        user = models.User.objects.get(name=guser)
        time = timezone.now()
        print(time)
        return render(request, 'borrow_book.html', {'user':user, 'book':book, 'time':time})

# 我的借阅书籍函数，负责返回当前登录用户的所有借阅记录给前端页面
def my_books(request):
    if request.method == 'GET':
        user = models.User.objects.get(name=guser)
        record = models.Borrow.objects.filter(user_id=user)
        books = record.values_list('book_id', flat=True)
        print(books)
        blist = list()
        for i in books:
            blist.append(models.Book.objects.get(id=i))
        return render(request, 'my_books.html', {'borrowed_list':blist})

# 还书函数，负责处理用户的还书请求
def return_book(request):
    user = models.User.objects.get(name=guser)
    book = models.Book.objects.get(id=request.GET.get('id'))
    book.sales -= 1
    book.nums += 1
    book.save()
    models.Borrow.objects.filter(book_id=book, user_id=user).delete()
    return redirect('/app01/my_books/?name='+user.name)