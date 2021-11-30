import requests
from flask import flash, render_template, request, url_for, redirect
from app.user.views import user_login_require

from . import jiujia
from .forms import JiujiaForm


# @jiujia.route("/jiujia", methods=['GET', 'POST'])
# @user_login_require
# def jiujia_index():
#     global re
#     form = JiujiaForm()
#     url = 'https://cloud.cn2030.com/sc/wx/HandlerSubscribe.ashx'
#     if request.method == 'POST':
#         date = request.form['date']
#         params = {'act': 'GetCustSubscribeDateAll', 'pid': '1', 'id': '1921', 'month': date}
#     re = requests.get(url, params)
#     print(re)
#     return render_template('jiujia/jiujia.html')


@jiujia.route("/jiujia", methods=['GET', 'POST'])
@user_login_require
def jiujia_index():
    url = 'https://cloud.cn2030.com/sc/wx/HandlerSubscribe.ashx'
    headers = {'User-Agent':'Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36',
               'cookie': 'ASP.NET_SessionId=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MzgxNTQzNDQuMzE5ODY1MiwiZXhwIjoxNjM4MTU3OTQ0LjMxOTg2NTIsInN1YiI6IllOVy5WSVAiLCJqdGkiOiIyMDIxMTEyOTEwNTIyNCIsInZhbCI6Ik1va01BUUlBQUFBUU4yWmpPRGN4TW1FMk5qSTJNelEwWVJ4dmNYSTFielZCUkdFeVgwRlJNbFp4WlVWSVJVZzBRbUo0U1hnd0FCeHZcclxuVlRJMldIUXdSVVYyT1RGTmJFdElNR3ByWDFkNUxUbFVTRXRKRHpJeE9TNHhOVGN1TWpVMUxqSTFNUUFBQUFBQUFBQT0ifQ.5RmPrmU9FAIVDR-dm_nOJFd5vO-kYozgB2JHyusqFWM; path=/',
               'Referer': 'https://servicewechat.com/wx2c7f0f3c30d99445/91/page-frame.html'}
    params = {'act': 'GetCustSubscribeDateAll', 'pid': '1', 'id': '1921', 'month': '202111'}
    re = requests.get(url, params=params, headers=headers)
    text = re.json()
    li = text['list']
    return render_template('jiujia/jiujia.html', text=li)
