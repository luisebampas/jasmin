from django.shortcuts import render


# Create your views here.
from frame.error import ErrorCode
from frame.itemdb import ItemDb
from frame.userdb import UserDb


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
            if pwd == user.pwd:
                request.session['suser'] = id;
                context = {
                    'section': 'shop2/loginok.html',
                    'loginuser': user
                };
            else:
                raise Exception;

        except:
            context = {
                'section': 'jasmine/error.html',
                'error': ErrorCode.e0003
            };
        return render(request, 'jasmine/home', context);

    def join(request):
        context = {
            'section': 'jasmine/join.html'
        };
        return render(request, 'jasmine/join.html', context)


class mainSectionView:
    def mainSection(request):
        context = {
            'main_section': 'jasmine/mainsection.html'
        };
        return render(request, 'jasmine/home.html', context)

    def itemlist(request):
        catenum = request.GET['category'];
        page = request.GET['page'];
        selectedItems = ItemDb().select(int(catenum), int(page));
        context = {
            'main_section': 'jasmine/itemlist.html',
            'itemlist': selectedItems,
        };
        return render(request, 'jasmine/home.html', context)

    def itemcontent(request):
        context = {
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