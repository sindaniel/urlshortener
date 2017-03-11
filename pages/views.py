from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Count, Sum
from django.db.models.functions import ExtractMonth, ExtractYear
from user_agents import parse
import random
import string
import json

from urls.models import Url, UrlAnalitys

def random_generator(size=8, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    return ''.join(random.choice(chars) for x in range(size))




@login_required
def index_view(request):

    qs = Url.objects.all().filter(user= request.user)
    context = {
        'object_list': qs,
    }
    return render(request, 'pages/home.html', context)


@login_required
def url_view(request, u):
    qs = Url.objects.all().filter(code= u, user=request.user).first()

    if not qs:
        return redirect('pages:index')

    browsers = UrlAnalitys.objects.filter(url=qs).values('browser').annotate(dcount=Count('browser'))
    os = UrlAnalitys.objects.filter(url=qs).values('os').annotate(dcount=Count('os'))
    months = UrlAnalitys.objects.filter(url=qs).annotate(month=ExtractMonth('created')).values('month').annotate(count=Count('id')).values('month', 'count')



    context = {
        'obj': qs,
        'months': json.dumps( [{'count': o['count'],  'month': o['month']} for o in months] ),
        'browsers': json.dumps( [{'dcount': o['dcount'],  'browser': o['browser']} for o in browsers] ),
        'os': json.dumps( [{'dcount': o['dcount'],  'os': o['os']} for o in os] ),
    }


    return render(request, 'pages/view.html', context)


@login_required
def create_view(request):

    url = request.POST['url']

    if url == '':
        messages.success(request, 'You must enter a Url')

    else:

        code = random_generator()

        u = Url()
        u.code = code
        u.user = request.user
        u.url = url
        u.save()

        # driver = webdriver.PhantomJS()
        # driver.set_window_size(1024, 768)
        # driver.get(url)
        # screen = driver.get_screenshot_as_png()
        #
        #
        # box = (0, 0, 1366, 728)
        # im = Image.open(BytesIO(screen))
        # region = im.crop(box)
        # region.save('screen7.png', 'PNG', optimize=False, quality=50)
        #response_data = {}
        # response_data['code'] = code
        # response_data['response'] = 'ok'
        #
        # return HttpResponse(json.dumps(response_data), content_type="application/json")

        messages.success(request, 'Url created')

    return redirect('pages:index')



def url_redirection(request, u):


    qs = Url.objects.all().filter(code= u, user= request.user).first()
    urlRedirect = qs.url


    ua_string = request.META['HTTP_USER_AGENT']
    user_agent = parse(ua_string)





    uA = UrlAnalitys()
    uA.url = qs
    uA.browser = user_agent.browser.family
    uA.os = user_agent.os.family
    uA.ip = request.META['REMOTE_ADDR']
    uA.save()

    return HttpResponseRedirect(urlRedirect)
