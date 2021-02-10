import logging
import math

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
        UserDb().delete(id);
        request.session['suser'] = None;
    except:
        context = {
            'section': 'jasmine/error.html',
            'error': ErrorCode.e0002
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
        # max items shown in a one page
        maxItemlist = 20;
        # max pages shown
        maxPageview = 5;
        try:
            catenum = int(request.GET['category']);
        except:
            catenum = 1;
        try:
            page = int(request.GET['page']);
        except:
            page = 1;
        try:
            searchmod = int(request.GET['searchmod']);
        except:
            searchmod = 0;
        try:
            searchword = request.GET['searchword'];
        except:
            searchword = '';

        if catenum == 1:
            catename = '모든 소설';
        elif catenum == 2:
            catename = '일반 소설';
        elif catenum == 12:
            catename = '장르 소설';
        else:
            catename = '';
        if searchmod == 1:
            searchmodname = '제목과 작가';
        elif searchmod == 2:
            searchmodname = '제목';
        elif searchmod == 3:
            searchmodname = '작가';
        else:
            searchmodname = '';
        itemlist = ItemDb().select(catenum, page, maxItemlist, searchmod, searchword);
        itemlistcount = ItemDb().listcount(catenum, searchmod, searchword);
        lastpage = math.ceil(itemlistcount / maxItemlist);
        pageRange = range(max(1, page-2), min(page+2, lastpage)+1)
        prevpage = page-1;
        nextpage = page+1;
        context = {
            'section': 'jasmine/itemlist.html',
            'catenum': catenum,
            'catename': catename,
            'itemlist': itemlist,
            'itemlistcount': itemlistcount,
            'pageRange': pageRange,
            'currentpage': page,
            'prevpage': prevpage,
            'nextpage': nextpage,
            'lastpage': lastpage,
            'searchmod': searchmod,
            'searchmodname': searchmodname,
            'searchword': searchword,
        };
        return render(request, 'jasmine/home.html', context)

    def itemcontent(request):
        itemnum = int(request.GET['itemnum']);
        item = ItemDb().selectone(itemnum)
        context = {
            'section': 'jasmine/itemcontent.html',
            'item': item,
        };
        return render(request, 'jasmine/home.html', context)


    def payment(request):
        try:
            userid = request.session['suser']
            userid = str(userid)
            itemnum = int(request.GET['itemnum']);
            item = ItemDb().selectone(itemnum)
            context = {
                'section': 'jasmine/payment.html',
                'item': item,
                'id': userid,
            };
            return render(request, 'jasmine/home.html', context)
        except:
            return redirect('login')


    def paydetail(request):
        itemnum = int(request.GET['itemnum']);
        item = ItemDb().selectone(itemnum)
        id = request.session['suser']
        context = {
            'section': 'jasmine/paydetail.html',
            'item': item,
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


