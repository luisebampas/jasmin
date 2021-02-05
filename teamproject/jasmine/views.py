from django.shortcuts import render


# Create your views here.
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
