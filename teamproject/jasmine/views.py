import logging

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
<<<<<<< HEAD
<<<<<<< HEAD
from frame.error import ErrorCode
from frame.itemdb import ItemDb
from frame.userdb import UserDb

=======
<<<<<<< HEAD
=======
logger = logging.getLogger('users');

>>>>>>> 33290ac3561c317a71cf05b90f58fcb29eeb4d1a
from django.utils.http import urlencode

from frame.error import ErrorCode
from frame.userdb import UserDb, OrderDb


<<<<<<< HEAD
>>>>>>> 5fe25ff4563ece6559bb3547ed44bcd41e9b5cb5
>>>>>>> master
=======
>>>>>>> 33290ac3561c317a71cf05b90f58fcb29eeb4d1a

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

<<<<<<< HEAD
class mainSectionView:
    def mainSection(request):
        context = {
            'main_section': 'jasmine/mainsection.html'
=======
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
>>>>>>> master
        };
        return render(request,'jasmine/home.html',context);
    qstr = urlencode({'id':id})
    return HttpResponseRedirect('%s?%s' % ('userdetail',qstr));

<<<<<<< HEAD
    def itemlist(request):
        catenum = request.GET['category'];
        page = request.GET['page'];
        selectedItems = ItemDb().select(int(catenum), int(page));
        context = {
            'main_section': 'jasmine/itemlist.html',
            'itemlist': selectedItems,
=======
def userdelete(request):
    id = request.GET['id'];
    try:
        UserDb().delete(id);
        request.session['suser'] = None;
    except:
        context = {
            'section': 'jasmine/error.html',
<<<<<<< HEAD
            'error':ErrorCode.e0002
>>>>>>> master
=======
            'error': ErrorCode.e0002
>>>>>>> 33290ac3561c317a71cf05b90f58fcb29eeb4d1a
        };
    return render(request,'jasmine/home.html',context);



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

<<<<<<< HEAD
    def cartlist(request):
        context = {
<<<<<<< HEAD
            'main_section': 'jasmine/itemcontent.html'
        };
        return render(request, 'jasmine/home.html', context)

    def payment(request):
        context = {
            'main_section': 'jasmine/payment.html'
        };
        return render(request, 'jasmine/home.html', context)

    def paydetail(request):
        context = {
            'main_section': 'jasmine/paydetail.html'
        };
        return render(request, 'jasmine/home.html', context)


class sideSectionView:
    def sideSection(request):
        context = {
            'side_section': 'jasmine/sidesection.html'
        };
        return render(request, 'jasmine/home.html', context)

    def category(request):
        context = {
            'side_section': 'jasmine/category.html'
        };
        return render(request, 'jasmine/sidesection.html', context)
=======
            'section': 'jasmine/cartlist.html'
        };
        return render(request, 'jasmine/home.html', context)
>>>>>>> 5fe25ff4563ece6559bb3547ed44bcd41e9b5cb5
>>>>>>> master
=======

def cartlist(request):
    context = {
        'section': 'jasmine/cartlist.html'
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

def paydetail(request):
    context = {
        'section': 'jasmine/paydetail.html'
    };
    return render(request, 'jasmine/home.html', context)

def payment(request):
    context = {
        'section': 'jasmine/payment.html'
    };
    return render(request, 'jasmine/home.html', context)
>>>>>>> 33290ac3561c317a71cf05b90f58fcb29eeb4d1a
