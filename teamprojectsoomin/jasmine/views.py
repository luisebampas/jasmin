import logging

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils.http import urlencode
from frame.itemdb import ItemDb
from frame.error import ErrorCode
from frame.userdb import UserDb, OrderDb

logger = logging.getLogger('users');



class MainView:
    def login(request):
        context = {
            'section': 'jasmine/login.html'
        };
        return render(request, 'jasmine/login.html', context)

    def logout(request):
        if request.session['suser']!= None:
            del request.session['suser'];
        return render(request,'jasmine/home.html')

    def loginimpl(request):
        id = request.POST['id'];
        pwd = request.POST['pwd'];
        try:
            user = UserDb().selectone(id);
            if pwd == user.userpwd:
                if user.userid == 'admin':
                    request.session['suser'] = id;
                    context = {
                        'section': 'jasmine/loginok.html',
                        'loginuser': user
                    };
                else:
                    logger.debug(id)
                    request.session['suser'] = id;
                    request.session['susernum'] = user.usernum;
                    context = {
                        'section': 'jasmine/loginok.html',
                        'loginuser': user
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
    #print(usernum)
    rsusernum = OrderDb().mainone(int(usernum));
    #print(rsusernum)
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
        if id == 'admin':
            context={
                'section': 'jasmine/error.html',
                'error': ErrorCode.e0004
            }
            return render(request, 'admin/manage.html', context)
        else:
            UserDb().delete(id);
            request.session['suser'] = None;
    except:
        context = {
            'section': 'jasmine/error.html',
            'error': ErrorCode.e0002
        };
    return redirect('home');



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

def cart(request):
    usernum = request.GET['usernum'];
    #print(usernum)
    rsusernum = OrderDb().cart(int(usernum));
    #print(rsusernum)
    context = {
        'section': 'jasmine/cart.html',
        'cartlist':rsusernum,
    };

    return render(request, 'jasmine/mypage.html', context)

def cartdelete(request):
    cartnum = request.GET['cartnum'];
    print(cartnum)
    try:
        OrderDb().cartdelete(int(cartnum));
        context = {
            'section': 'jasmine/cart.html',
        };
    except:
        context = {
            'section': 'jasmine/error.html',
            'error':ErrorCode.e0002
        };
        return render(request,'jasmine/mypage.html',context);

    usernm = request.session['susernum']
    qstr = urlencode({'usernum': usernm})
    return HttpResponseRedirect('%s?%s' % ('cart', qstr))

def manage(request):
    return render(request, 'admin/manage.html')

def userlist(request):
    ruserlist = UserDb().select();
    context = {
        'section':'admin/userlist.html',
        'userlist' : ruserlist
    };
    return render(request, 'admin/manage.html',context)




def map(request):
    context = {
        'section': 'jasmine/map.html'
    };
    return render(request, 'jasmine/about.html', context)


def cartlist(request):
    context = {
        'section': 'jasmine/cartlist.html'
    };
    return render(request, 'jasmine/home.html', context)


class mainSectionView:
    def mainSection(request):
        context = {
            'section': 'jasmine/mainsection.html'
        };
        return render(request, 'jasmine/home.html', context)

    def itemlist(request):
        catenum = request.GET['category'];
        page = request.GET['page'];
        selectedItems = ItemDb().select(int(catenum), int(page));
        context = {
            'section': 'jasmine/itemlist.html',
            'itemlist': selectedItems,
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

class sideSectionView:
    def sideSection(request):
        context = {
            'section': 'jasmine/sidesection.html'
        };
        return render(request, 'jasmine/home.html', context)

    def category(request):
        context = {
            'section': 'jasmine/category.html'
        };
        return render(request, 'jasmine/sidesection.html', context)
