from django.shortcuts import render, redirect

# Create your views here.
from frame.error import ErrorCode
from frame.userdb import UserDb, OrderDb


#from teamproject.frame.error import ErrorCode
#from teamproject.frame.userdb import UserDb


class MainView:
    def login(request):
        context = {
            'section': 'jasmine/login.html'
        };
        return render(request, 'jasmine/login.html', context)

    def logout(request):
        if request.session['suser'] != None:
            del request.session['suser'];
        return render(request,'jasmine/home.html')

    def loginimpl(request):
        id = request.POST['id'];
        pwd = request.POST['pwd'];

        try:
            user = UserDb().selectone(id);
            if pwd == user.userpwd:
                request.session['suser'] = id;
                request.session['susernum'] = user.usernum;
                context = {
                  'section':'jasmine/loginok.html',
                  'loginuser':user
                };
            else:
                raise Exception;
        except:
            context = {
                'section': 'jasmine/error.html',
                'error': ErrorCode.e0003
            };
        return render(request, 'jasmine/home.html', context);

    def join(request):
        context = {
            'section': 'jasmine/join.html'
        };
        return render(request, 'jasmine/join.html', context)

    def joinimpl(request):
        id = request.POST['id'];
        pwd = request.POST['pwd'];
        name = request.POST['name'];
        try:
            UserDb().insert(id, pwd, name);
            context = {
                'section':'jasmine/joinok.html'
            };
        except:
            context = {
                'section': 'jasmine/error.html',
                'error': ErrorCode.e0001
            };
        return render(request, 'jasmine/home.html', context);



def mypage(request):
    return render(request, 'mypage.html')

def userdetail(request):
    id = request.GET['id'];
    #print(id)
    rsuser = UserDb().selectone(id);
    #print(rsuser)
    context = {
        'section': 'jasmine/userdetail.html',
        'userdetail':rsuser,
    };

    return render(request, 'jasmine/mypage.html', context)

def orderlist(request):
    usernum = request.GET['usernum'];
    print(usernum)
    rsusernum = OrderDb().selectone(int(usernum));
    print(rsusernum)
    context = {
        'section': 'jasmine/orderlist.html',
        'orderlist':rsusernum,
    };

    return render(request, 'jasmine/mypage.html', context)

