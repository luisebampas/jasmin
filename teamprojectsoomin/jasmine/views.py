import logging
import math

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils.http import urlencode
from frame.authordb import AuthorDb
from frame.itemdb import ItemDb, OrdersDb, PaymentDb
from frame.error import ErrorCode
from frame.userdb import UserDb, OrderDb

logger = logging.getLogger('users');


class MainView:

    def login(request):
        context = {
            'section': 'jasmine/login.html'
        };
        return render(request, 'jasmine/home.html', context)

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
        return render(request, 'jasmine/home.html', context)

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

def cartdelete(request):
    itemnum = int(request.GET['itemnum']);
    OrderDb().cartdelet(itemnum)
    request.session['suser'] = None;
    return render(request,'jasmine/cartlist.html');


def cartlist(request):
    try:
        itemnum = int(request.GET['itemnum']);
    except:
        return redirect('login');
    finally:
        userid = str(request.session['suser']);
        user = UserDb().selectone(userid)

        OrderDb().cartinsert(user.usernum, itemnum);  # 총 주문기록에 새로운 내역 추가.
        cartlist = OrderDb().cart(user.usernum);
        context = {
            'section': 'jasmine/cartlist.html',
            'cartlist': cartlist,
        };
    return render(request, 'jasmine/home.html', context)


class admin:
    def adminpage(request):
        context = {
            'section': None
        };
        return render(request, 'jasmine/admin/adminpage.html', context)

    def additemspage(request):
        context = {
            'section': 'jasmine/admin/admin_additems.html',
        };
        return render(request, 'jasmine/admin/adminpage.html', context)

    def searchauthor(request):
        # max recent published list shown in each authors
        limit = 5;
        search_authorname = request.POST['search_authorname'];
        authorlist = AuthorDb().searchauthor(search_authorname);
        publistAll = [];
        for author in authorlist:
            publist = ItemDb().recentPublished(author.authornum, limit);
            publistAll.append(publist)
        context = {
            'section': 'jasmine/admin/admin_additems.html',
            'authorlist': authorlist,
            'publistAll': publistAll,
        };
        return render(request, 'jasmine/admin/adminpage.html', context)

    def addauthor(request):
        authorname = request.POST['add_authorname'];
        authorinfo = request.POST['add_authorinfo'];
        try:
            AuthorDb().insert(authorname, authorinfo);
            context = {
                'section': 'jasmine/admin/admin_additems.html',
            };
        except:
            context = {
                'section': 'jasmine/admin/admin_additems.html',
                'error': ErrorCode.e0011
            };
        return render(request, 'jasmine/admin/adminpage.html', context)

    def additem(request):
        category = int(request.POST['category']);
        item_authornum = int(request.POST['item_authornum']);
        itemname = request.POST['itemname'];
        price = int(request.POST['price']);
        itemdate = request.POST['itemdate'];
        iteminfo = request.POST['iteminfo'];
        sells = int(request.POST['sells']);
        series = int(request.POST['series']);
        try:
            ItemDb().insert(category, item_authornum, itemname, price, itemdate, iteminfo, sells, series);
            context = {
                'section': 'jasmine/admin/admin_additems.html',
            };
        except:
            context = {
                'section': 'jasmine/admin/admin_additems.html',
                'error': ErrorCode.e0011
            };
        return render(request, 'jasmine/admin/adminpage.html', context)


def map(request):
    context = {
        'section': 'jasmine/map.html'
    };
    return render(request, 'jasmine/about.html', context)




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
        try:
            ordercon = int(request.GET['ordercon']);
        except:
            ordercon = 1;
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
        itemlist = ItemDb().select(catenum, page, maxItemlist, searchmod, searchword, ordercon);
        itemlistcount = ItemDb().listcount(catenum, searchmod, searchword);
        lastpage = math.ceil(itemlistcount / maxItemlist);
        pagerange = range(max(1, page-2), min(page+2, lastpage)+1)
        prevpage = page-1;
        nextpage = page+1;
        context = {
            'section': 'jasmine/itemlist.html',
            'catenum': catenum,
            'catename': catename,
            'itemlist': itemlist,
            'itemlistcount': itemlistcount,
            'pageRange': pagerange,
            'currentpage': page,
            'prevpage': prevpage,
            'nextpage': nextpage,
            'lastpage': lastpage,
            'searchmod': searchmod,
            'searchmodname': searchmodname,
            'searchword': searchword,
            'ordercon': ordercon,
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

        userid = str(request.session['suser']);
        itemnum = int(request.GET['itemnum']);
        item = ItemDb().selectone(itemnum);
        context = {
            'section': 'jasmine/payment.html',
            'item': item,
            'id': userid,
            };
        return render(request, 'jasmine/home.html', context);

    def pay2(request):
        userid = str(request.session['suser']);
        itemlist = [];
        for n in range(1,3):
            data = request.POST[str(n)];
            itemlist.append(data);
        item1 = ItemDb().selectone(itemlist[0]);
        item2 = ItemDb().selectone(itemlist[1]);
        context = {
            'section': 'jasmine/pay2.html',
            'id': userid,
            'item1': item1,
            'item2': item2,
        };
        return render(request, 'jasmine/home.html', context);



    def payimpl(request):
        itemnum = int(request.POST['itemnum']);
        userid = request.POST['id'];
        paymethod = request.POST['PayMethod'];
        user = UserDb().selectone(userid);
        item = ItemDb().selectone(itemnum);

        # 해당 아이템 주문/결제정보 생성
        OrdersDb().insert(user.usernum, itemnum, paymethod); # 총 주문기록에 새로운 내역 추가.
        ordernum = int(OrdersDb().selectone(user.usernum));
        OrderDb().listinsert(ordernum, user.usernum, itemnum); # 사용자의 주문내역에 추가.
        PaymentDb().insert(ordernum, user.usernum, item.itemname, item.price); # 결제정보 추가.
        paylist = PaymentDb().selectone(user.usernum); # 유저의 지난 구매기록 모두 불러오기
        ItemDb().sellitem(itemnum); # 아이템 판매처리, 판매수량 + 1
        context = {
            'section': 'jasmine/payresult.html',
            'paylist': paylist,
        };
        return render(request, 'jasmine/home.html', context);

    def paycart(request):
        itemnum = int(request.GET['itemnum']);
        userid = request.GET['id'];
        paymethod = request.GET['paymethod'];
        user = UserDb().selectone(userid);
        item = ItemDb().selectone(itemnum);

        # 해당 아이템 주문/결제정보 생성
        OrdersDb().insert(user.usernum, itemnum, paymethod); # 총 주문기록에 새로운 내역 추가.
        ordernum = int(OrdersDb().selectone(user.usernum));
        OrderDb().listinsert(ordernum, user.usernum, itemnum); # 사용자의 주문내역에 추가.
        PaymentDb().insert(ordernum, user.usernum, item.itemname, item.price); # 결제정보 추가.
        paylist = PaymentDb().selectone(user.usernum); # 유저의 지난 구매기록 모두 불러오기
        ItemDb().sellitem(itemnum); # 아이템 판매처리, 판매수량 + 1
        context = {
            'section': 'jasmine/paycart.html',
            'paylist': paylist,
        };
        return render(request, 'jasmine/home.html', context);

    def viewpage(request):
        context = {
            'section': 'jasmine/viewpage.html',
        };
        return render(request,'jasmine/home.html', context);


    def pdfview(request):

        context = {
            'section': 'jasmine/pdfview.html',
        };
        return render(request,'jasmine/home.html', context);


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


