import logging

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


# Create your views here.
from django.utils.http import urlencode

from frame.error import ErrorCode
from frame.userdb import UserDb
logger = logging.getLogger('users');

class MainView:
    def login(request):
        context = {
            'section': 'jasmine/login.html'
        };
        return render(request, 'jasmine/login.html', context)

    def logout(request):
        if request.session['suser'] != None:
            del request.session['suser'];
        return render(request, 'jasmine/home.html')

    def loginimpl(request):
        id = request.POST['id'];
        pwd = request.POST['pwd'];
        try:
            user = UserDb().selectone(id);
            if pwd == user.userpwd:
                logger.debug(id)
                request.session['suser'] = id;
                context = {
<<<<<<< HEAD
                  'section':'jasmine/loginok.html',
                    'loginuser':user
=======
                    'section': 'shop2/loginok.html',
                    'loginuser': user
>>>>>>> aad851d185dadcdc087b7f21a795bba5c1a79d51
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

<<<<<<< HEAD
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
    return render(request, 'mypage.html');

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
        return render(request,'jasmine/home.html',context);
    return render(request,'jasmine/home.html');


=======

class sectionView:
    def mainSection(request):
        context = {
            'section': 'jasmine/mainsection.html'
        };
        return render(request, 'jasmine/home.html', context)

    def itemlist(request):
        context = {
            'section': 'jasmine/itemlist.html'
        };
        return render(request, 'jasmine/home.html', context)

    def itemcontent(request):
        context = {
            'section': 'jasmine/itemcontent.html'
        };
        return render(request, 'jasmine/home.html', context)

    def payment(request):
        context = {
            'section': 'jasmine/payment.html'
        };
        return render(request, 'jasmine/home.html', context)

    def paydetail(request):
        context = {
            'section': 'jasmine/paydetail.html'
        };
        return render(request, 'jasmine/home.html', context)
>>>>>>> aad851d185dadcdc087b7f21a795bba5c1a79d51
