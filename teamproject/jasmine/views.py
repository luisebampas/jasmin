import logging

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
<<<<<<< HEAD
from django.utils.http import urlencode

from frame.error import ErrorCode
from frame.userdb import UserDb, OrderDb

logger = logging.getLogger('users');
=======
from frame.error import ErrorCode
from frame.userdb import UserDb

>>>>>>> 5fe25ff4563ece6559bb3547ed44bcd41e9b5cb5

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
                logger.debug(id)
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
    usernum = request.GET['usernum'];
    print(usernum)
    rsusernum = OrderDb().mainone(int(usernum));
    print(rsusernum)
    context = {
        'section': 'jasmine/mypagemain.html',
        'orderlist':rsusernum,
    };

    return render(request, 'jasmine/mypage.html', context)

def userdetail(request):
    id = request.GET['id'];
    print(id)
    rsuser = UserDb().selectone(id);
    print(rsuser)
    context = {
        'section': 'jasmine/userdetail.html',
        'userdetail':rsuser,
    };

    return render(request, 'jasmine/mypage.html', context)

def userupdate(request):
    id = request.GET['id'];
    user = UserDb().selectone(id);
    context = {
        'section':'jasmine/userupdate.html',
        'uuser':user
    };
    return render(request, 'jasmine/mypage.html',context)

def userupdateimpl(request):
    id = request.POST['id'];
    pwd = request.POST['pwd'];
    name = request.POST['name'];
    try:
        UserDb().update(id,pwd,name);
    except:
        context = {
            'section': 'jasmine/error.html',
            'error':ErrorCode.e0001
        };
        return render(request,'jasmine/home.html',context);
    qstr = urlencode({'id':id})
    return HttpResponseRedirect('%s?%s' % ('userdetail',qstr));

def userdelete(request):
    id = request.GET['id'];
    try:
        UserDb().delete(id);
        request.session['suser'] = None;
    except:
        context = {
            'section': 'jasmine/error.html',
            'error':ErrorCode.e0002
        };
<<<<<<< HEAD
        return render(request,'jasmine/home.html',context);
    return render(request,'jasmine/home.html');


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


def map(request):
    context = {
        'section': 'jasmine/map.html'
    };
    return render(request, 'jasmine/about.html', context)
=======
        return render(request, 'jasmine/home.html', context)

    def cartlist(request):
        context = {
            'section': 'jasmine/cartlist.html'
        };
        return render(request, 'jasmine/home.html', context)
>>>>>>> 5fe25ff4563ece6559bb3547ed44bcd41e9b5cb5
