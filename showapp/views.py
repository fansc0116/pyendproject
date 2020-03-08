from django.core.paginator import Paginator
import random
import re
import string
import json
from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from redis import Redis
from fsc_cmfw1 import settings
from utils.send_mess import YunPian
from showapp.models import TSlideshow,TUser
import time
from django.db.models import Count
red = Redis(host='localhost', port=6379)  # 连接redis数据库


# 登录页面
def login(request):
    return render(request, 'login.html')

# 显示主页
def index(request):
    uname = request.GET.get('uname')
    return render(request, 'index.html', {'uname':uname})

# 发送验证码
@csrf_exempt
def get_code(request):
    mobile = request.POST.get('mobile')
    code = red.get(mobile)
    print(code)
    # 检测60秒内没有获取过验证码
    if re.match(r"^1[35678]\d{9}$", mobile) and not code:
        yun_pian = YunPian(settings.APIKEY)
        code = ''.join(random.sample(string.digits, 6))
        yun_pian.send_message(mobile=mobile,code=code)
        red.setex(mobile, 60, code)  ##将验证码存入redis中，并设置存活时间
        red.setex(mobile+'_1', 300, code)
        return HttpResponse('ok')
    else:
        print('error')
        return HttpResponse('error')

# 验证用户信息
@csrf_exempt
def check_user(request):
    code_input = request.POST.get('code_input')
    mobile = request.POST.get('mobile')
    print(code_input,mobile)
    code = red.get(mobile + '_1').decode()
    print(code)
    if code_input == code:
        return HttpResponse('ok')
    else:
        return HttpResponse('error')

#获取轮播图
def loadbanner(request):
    rowNum = request.GET.get('rows')
    pageNum = request.GET.get('page')
    reqs = TSlideshow.objects.all()
    # page对象
    pgntor = Paginator(reqs, rowNum)
    pg = pgntor.page(pageNum)
    # 生成数据
    data = {
        "page": pageNum,  # 当前页号
        "total": pgntor.num_pages,  # 总页数
        "records": pgntor.count,  # 总数据条
        "rows": list(pg)
    }
    # 转json
    def my_default(obj):
        if isinstance(obj, TSlideshow):
            print(obj.t_url)
            dict = {'id': obj.t_id, 'title': obj.t_title, 'status': obj.t_flag, 'create_time': obj.t_createtime,
                    'pic': str(obj.t_url)}
            return dict
    str_json = json.dumps(data,default=my_default)
    print(str_json)
    return HttpResponse(str_json)

# 添加/修改轮播图
@csrf_exempt
def add_banner(request):
    id = request.POST.get("id")
    title = request.POST.get("title")
    status = request.POST.get("status")
    time1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    pic = request.FILES.get("pic")
    print(id,title, status, pic, type(pic))
    if pic:
        a = TSlideshow.objects.create(t_url='img/'+pic.name,t_title=title,t_flag=status,t_createtime=time1)
        if a:
            return HttpResponse("createok")
        else:
            return HttpResponse('createerror')
    else:
        try:
            b = TSlideshow.objects.get(t_id=id)
            b.t_title=title
            b.t_flag=status
            b.save()
            return HttpResponse("changeok")
        except:
            return HttpResponse('changeerror')

# 删除轮播图
@csrf_exempt
def del_banner(request):
    id  = request.POST.get('id')
    print(id)
    try:
        d = TSlideshow.objects.get(t_id=id)
        print(d)
        d.delete()
        return HttpResponse('ok')
    except:
        return HttpResponse('error')

#获取用户信息
def loadusers(request):
    rowNum = request.GET.get('rows')
    pageNum = request.GET.get('page')
    reqs = TUser.objects.all()
    # page对象
    pgntor = Paginator(reqs, rowNum)
    pg = pgntor.page(pageNum)
    # 生成数据
    data = {
        "page": pageNum,  # 当前页号
        "total": pgntor.num_pages,  # 总页数
        "records": pgntor.count,  # 总数据条
        "rows": list(pg)
    }
    # 转json
    def my_default(obj):
        if isinstance(obj, TUser):
            dict = {'id': obj.t_id, 'name': obj.t_name, 'tel': obj.t_tel, 'pwd': obj.t_pwd, 'salt': obj.t_salt,
                    'add': obj.t_add,'pic': str(obj.t_pic), 'nota': obj.t_nota, 'sex': obj.t_sex,
                    'flag': obj.t_flag,'add1': obj.t_add1}
            return dict
    str_json = json.dumps(data,default=my_default)
    print(str_json)
    return HttpResponse(str_json)

# 添加/修改用户信息
@csrf_exempt
def add_user(request):
    id = request.POST.get("id")
    name = request.POST.get("name")
    tel = request.POST.get("tel")
    pwd = request.POST.get("pwd")
    add = request.POST.get("add")
    nota = request.POST.get("nota")
    sex = request.POST.get("sex")
    flag = request.POST.get("flag")
    add1 = request.POST.get("add1")
    pic = request.FILES.get("pic")
    print(id,name,tel,pwd,add,nota,sex,flag,add1, pic, type(pic))
    if pic:
        a = TUser.objects.create(t_pic='img/'+pic.name,t_name=name,t_tel=tel,t_pwd=pwd,
                                 t_add=add,t_nota=nota,t_sex=sex,t_flag=flag,t_add1=add1)
        if a:
            return HttpResponse("createok")
        else:
            return HttpResponse('createerror')
    else:
        try:
            b = TUser.objects.get(t_id=id)
            b.t_name=name
            b.t_tel=tel
            b.t_pwd=pwd
            b.t_add=add
            b.t_nota=nota
            b.t_sex=sex
            b.t_flag=flag
            b.t_add1=add1
            b.save()
            return HttpResponse("changeok")
        except:
            return HttpResponse('changeerror')

# 删除用户信息
@csrf_exempt
def del_user(request):
    id  = request.POST.get('id')
    print(id)
    try:
        d = TUser.objects.get(t_id=id)
        print(d)
        d.delete()
        return HttpResponse('ok')
    except:
        return HttpResponse('error')

# 获取地区对应的用户数量
def get_maplist(request):
    citylist=TUser.objects.values('t_add').annotate(Count('t_id'))
    print('citylist:',citylist)
    data=[]
    for i in citylist:
        data.append({"name": i['t_add'], "value": i['t_id__count']})
    print('data:',data)
    return JsonResponse(data, safe=False)

# 获取用户注册情况
def get_initlist(request):
    data = {
        "x": ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"],
        "y": [5, 20, 36, 10, 10, 20]
    }
    return JsonResponse(data)
