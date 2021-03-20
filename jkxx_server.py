#coding:utf-8
import requests
import base64
import random
import re
import datetime
import os
import sqll
import txmm
from flask import Flask, render_template, request, current_app
from flask_cors import *
import hashlib
server = Flask(__name__)
CORS(server,supports_credentials=True)
import json
faketxm="""


<html data-dpr="1" style="font-size: 112.1px;"><head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no">
		<title>湖州师范学院疫情数据监控平台</title>
		<script src="https://jkxxcj.zjhu.edu.cn/js/loadres.js"></script>
<script data-ad-client="ca-pub-2181926949629728" async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<div style="display:none">
  				<script type="text/javascript" src="https://v1.cnzz.com/z_stat.php?id=1277949079&amp;web_id=1277949079">
  					</script><script src="https://c.cnzz.com/core.php?web_id=1277949079&amp;t=z" charset="utf-8" type="text/javascript"></script><a href="https://www.cnzz.com/stat/website.php?web_id=1277949079" target="_blank" title="站长统计">站长统计</a>

  					
		</div>
		<script>
			loadres({
				css: [{
						href: 'https://jkxxcj.zjhu.edu.cn/css/common.css',
						media: ''
					},
					{
						href: 'https://jkxxcj.zjhu.edu.cn/layui/css/layui.css',
						media: ''
					},
					{
						href: 'https://jkxxcj.zjhu.edu.cn/css/pc.css',
						media: 'screen and (min-width: 750px)'
					},
					{
						href: 'https://jkxxcj.zjhu.edu.cn/css/mobile.css',
						media: 'screen and (max-width: 749px)'
					}
				],
				scripts: [
					'https://jkxxcj.zjhu.edu.cn/js/jquery-2.1.0.js',
					'https://jkxxcj.zjhu.edu.cn/js/flexible.min.js',
					'https://jkxxcj.zjhu.edu.cn/js/allresize.js',
					'https://jkxxcj.zjhu.edu.cn/layui/layui.js',
					'https://jkxxcj.zjhu.edu.cn/js/common.js'
				]
			})
		</script><link type="text/css" rel="stylesheet" href="https://jkxxcj.zjhu.edu.cn/css/common.css?v=1613141838113" media=""><link type="https://jkxxcj.zjhu.edu.cn/text/css" rel="stylesheet" href="https://jkxxcj.zjhu.edu.cn/layui/css/layui.css?v=1613141838113" media=""><link type="text/css" rel="stylesheet" href="https://jkxxcj.zjhu.edu.cn/css/pc.css?v=1613141838113" media="screen and (min-width: 750px)"><link type="text/css" rel="stylesheet" href="https://jkxxcj.zjhu.edu.cn/css/mobile.css?v=1613141838113" media="screen and (max-width: 749px)"><script type="text/javascript" charset="UTF-8" src="https://jkxxcj.zjhu.edu.cn/js/jquery-2.1.0.js?v=1613141838113"></script>
	<script type="text/javascript" charset="UTF-8" src="https://jkxxcj.zjhu.edu.cn/js/flexible.min.js?v=1613141838113"></script><script type="text/javascript" charset="UTF-8" src="https://jkxxcj.zjhu.edu.cn/js/allresize.js?v=1613141838113"></script><script type="text/javascript" charset="UTF-8" src="https://jkxxcj.zjhu.edu.cn/layui/layui.js?v=1613141838113"></script><script type="text/javascript" charset="UTF-8" src="https://jkxxcj.zjhu.edu.cn/js/common.js?v=1613141838113"></script></script><link id="layuicss-layer" rel="stylesheet" href="https://jkxxcj.zjhu.edu.cn/layui/css/modules/layer/default/layer.css?v=3.1.1" media="all"><link id="layuicss-laydate" rel="stylesheet" href="https://jkxxcj.zjhu.edu.cn/layui/css/modules/laydate/default/laydate.css?v=5.0.9" media="all"></head>
	<body style="">
		<div class="forFixed">
			<div class="headerBox layui-hide-sm layui-hide-md layui-hide-lg">
				<a href="JavaScript:history.back(-1);"><img src="https://jkxxcj.zjhu.edu.cn/img/back.png"></a>
				<h4>进校码</h4>
			</div>
			<div class="mainBox jkmWrap">
				<div class="jkmBox">
					<h4 class="xsxm">
XXX的进校码</h4>
					<p class="xh">学号：</p>
					<p class="lxdh">联系电话：</p>
					<!-- <p class="gssj"></p> -->
					<p class="xsxy">学院：</p>
					<p class="xsbj">班级：</p>
					<p class="isAllowOut font-green">是否允许出校：允许</p>
					<p class="restTime"></p>
					<p class="dqzt"></p>
					<!--<img src="img/ewm.png"/>-->
					<img src="
" class="noewmimg">
					<h6>温馨提示:如果要出校，请在门口扫码出校，并在规定时间( AM 06:00 到 PM 22:00 )内返校。若超时返校，则15天内不可再次出校。</h6>
				</div>
				<button type="button" class="sqfx refresh-btn">点击查看状态</button>
			</div>
		</div>
		<!--地图-->
		<div id="allmap"></div>
		<!--弹出层-->
		<div class="tcWrap">
			<div class="tcBox">
				<div class="tcTitle">选择进校位置<i class="layui-icon layui-icon-close tcClose"></i></div>
				<div class="tcMain">
					<form class="layui-form">
						<div class="formItem">
							<div class="formLabel">进校地点</div>
							<select id="didian" name="">
								<option value="东校区南门">东校区南门</option>
								<option value="东校区西门">东校区西门</option>
								<option value="东校区北门">东校区北门</option>
								<option value="中校区南门">中校区南门</option>
								<option value="中校区西门">中校区西门</option>
								<option value="西校区南门">西校区南门</option>
								<option value="西校区北门">西校区北门</option>
								<option value="湖州高铁站">湖州高铁站</option>
							</select><div class="layui-unselect layui-form-select"><div class="layui-select-title"><input type="text" placeholder="请选择" value="东校区南门" readonly="" class="layui-input layui-unselect"><i class="layui-edge"></i></div><dl class="layui-anim layui-anim-upbit"><dd lay-value="东校区南门" class="layui-this">东校区南门</dd><dd lay-value="东校区西门" class="">东校区西门</dd><dd lay-value="东校区北门" class="">东校区北门</dd><dd lay-value="中校区南门" class="">中校区南门</dd><dd lay-value="中校区西门" class="">中校区西门</dd><dd lay-value="西校区南门" class="">西校区南门</dd><dd lay-value="西校区北门" class="">西校区北门</dd><dd lay-value="湖州高铁站" class="">湖州高铁站</dd></dl></div>
						</div>
						<div class="formItem">
							<div class="formLabel">
								体温
							</div>
							<select id="tiwen" name="">
								<option value="36.1°C~36.9°C">36.1°C~36.9°C</option>
								<option value="37°C~37.5°C">37°C~37.5°C</option>
								<option value="37.5°C以上">37.5°C以上</option>
							</select><div class="layui-unselect layui-form-select"><div class="layui-select-title"><input type="text" placeholder="请选择" value="36.1°C~36.9°C" readonly="" class="layui-input layui-unselect"><i class="layui-edge"></i></div><dl class="layui-anim layui-anim-upbit"><dd lay-value="36.1°C~36.9°C" class="layui-this">36.1°C~36.9°C</dd><dd lay-value="37°C~37.5°C" class="">37°C~37.5°C</dd><dd lay-value="37.5°C以上" class="">37.5°C以上</dd></dl></div>
						</div>
						<div class="formBtn">
							<button type="button" class="sure">确定</button>
							<button type="button" class="cancel">取消</button>
						</div>
					</form>
				</div>
			</div>
		</div>
	

<div class="layui-layer-move"></div></body></html>

"""
url_login = 'https://jkxxcj.zjhu.edu.cn/yhb/login'
def upload(username,passwd):
    user0=username
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterdaytime = (today - oneday).strftime("%Y%m%d")  # 昨天的日期
    todaytime = (today + oneday - oneday).strftime("%Y%m%d")  # 今天的日期
    todaytime = str(int(todaytime))
    yesterdaytime = str(int(yesterdaytime))
    req = requests.Session()
    username = base64.b64encode(username.encode('utf-8'))
    username = bytes.decode(username)
    username = 'Base64'+username
    passwd = passwd
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:72.0) Gecko/20100101 Firefox/72.0"
    }
    data = {
        'ZGH':username,
        'MM':passwd
    }
    result = req.post(url=url_login,data=data,headers=headers,timeout=10)
    print("ssss"+result.text)
    if('错误' in str(result.text)):
        return 0

    question_id = ['9EEE614EAF6278BDE055BAF66D78638E', '9E1F1911F0961B0EE055BAF66D78638E',
                   '9E1F1911F0971B0EE055BAF66D78638E', '9E1F1911F0981B0EE055BAF66D78638E',
                   '9E1F1911F0991B0EE055BAF66D78638E', '9E1F1911F09A1B0EE055BAF66D78638E',
                   '9E1F1911F09B1B0EE055BAF66D78638E', '9E1F1911F09C1B0EE055BAF66D78638E',
                   '9E1F1911F09D1B0EE055BAF66D78638E', '9E1F1911F09E1B0EE055BAF66D78638E',
                   '9E1F1911F09F1B0EE055BAF66D78638E', '9E1F1911F0A01B0EE055BAF66D78638E',
                   '9E1F1911F0A11B0EE055BAF66D78638E', '9E1F1911F0A21B0EE055BAF66D78638E',
                   '9E1F1911F0A31B0EE055BAF66D78638E', '9E1F1911F0A41B0EE055BAF66D78638E',
                   '9E1F1911F0A51B0EE055BAF66D78638E', '9E1F1911F0A61B0EE055BAF66D78638E',
                   'A3B606FBBA8B791AE0538713470A587B', 'A3B606FBBA8C791AE0538713470A587B','333333']

    answerquestion_data = ''
    for i in question_id:
        url_getanswer = 'https://jkxxcj.zjhu.edu.cn/healthanswer/getAnswerByQuestion'
        getanswer_data = {
            'zgh': username,
            'hdsj': yesterdaytime,
            'wtid': i
        }
        getanswer_result = req.get(url_getanswer,params=getanswer_data).text

        # 这里开始需要获得每个hdnr回答内容 bcsm补充说明 wtlx问题类型(wtid zgh的base64已经有了)
        current_hdnr = re.findall('"hdnr":"(.*?)[/|"]', getanswer_result)[0]
        current_bcsm = re.findall('bcsm\"\:(.*?)\,', getanswer_result)[0]
        current_wtlx = re.findall('wtlx\"\:\"(.*?)\"', getanswer_result)[0]
        # print(current_bcsm)
        ans_result = '{' + '\"bcsm\":' + current_bcsm + '' + ',' + '\"wtlx\":\"' + current_wtlx + '"' + ',' + '\"hdnr\":\"' + current_hdnr + '"' + ',' + '\"wtid\":\"' + i + '"' + ',' + '\"zgh\":\"' + username + '"' + ',' + '\"hdsj\":\"' + todaytime + '"' + '}'
        answerquestion_data = answerquestion_data + ',' + ans_result
    answerquestion_data = '[' + answerquestion_data[1:] + ']'
    # print(answerquestion_data)
    url_answer = 'https://jkxxcj.zjhu.edu.cn/healthanswer/answerQuestion'

    healthAnswers_me = {
        'healthAnswers':answerquestion_data
    }
#    print(healthAnswers_me)
    healthAnswer = req.post(url=url_answer,data=healthAnswers_me,headers=headers)
    # print(healthAnswer.text)
    #url_send = 'http://你的酷q地址/send_private_msg'

    if "success" in healthAnswer.text:
        print(user0,"打卡成功")
        #print(requests.get(url_send, params=param_success).text)
    else:
        print(user0,"打卡失败")
        #print(requests.get(url_send, params=param_failed).text)
@server.route('/',methods=['get','post'])
def add_user():
    if request.method == 'GET':
        xh=request.values.get("xh")
        mm=base64.b64decode(request.values.get("mm")).decode('utf-8')
        print(mm)
    if xh and mm:
        print(xh,mm)
        filename='/root/health_10.txt'
        with open(filename,'r') as f:
            for line in f:
                if xh in line:
                    f.close()
                    return xh+"  "+"  该用户已存在或已被禁用，请勿重复提交"
    #    try:
        try:
            if(upload(xh,mm)==0):
                return(xh+"  "+"  登录失败,用户名或密码错误")#登录失败返回
        except:
            return '学校服务器异常'        
#写入文件
        sqll.adduser(xh,mm)
        filename='/root/health_10.txt'
        with open(filename,'a') as file:
            file.write('\n'+xh+'\n'+mm)
            file.close()
        return xh+"  "+"  添加成功 \r\n今日打卡已完成，明日起将在11：30-12:00进行打卡\r\n请勿重复提交 如需修改信息，请在每天打卡完成后（12:00）以后登录疫情打卡系统进行修改\r\n否则修改将被覆盖"
      #  except:
        #    return xh+"  "+mm+" \r\n 添加失败"
    else:
        return "请输入学号或密码"
def encodee(m):
    c=hashlib.md5((str(m)+'f10adc3949ba59abbe56e057f20f883e').encode('utf-8')).hexdigest()
    d=base64.b32encode(c.encode('utf-8'))
    e=hashlib.md5(str(d).encode('utf-8')).hexdigest()
    #print(c,d,e)
    return e
    
@server.route('/del',methods=['get','post'])
def del_user():
    if request.method == 'GET':
        xh=request.values.get("xh")
        mm=base64.b64decode(request.values.get("mm")).decode('utf-8')
    if xh and mm:
        print(xh,mm)
    #    try:
        try:
            if(upload(xh,mm)==0):
                return(xh+"  "+"  登录失败,用户名或密码错误")#登录失败返回
        except:
            return '学校服务器异常'
        flag=0
        filename='/root/health_10.txt'
        with open(filename,'r') as f:
            for line in f:
                if xh in line:
                    flag=1
        f.close()
        if(flag==0):
            return "用户未添加"
        sqll.banuser(xh)        
        filename='/root/health_10.txt'
        with open(filename,'r+') as f:
            for line in f:
                if xh in line:
                    f.close()
                    return xh+"  "+"  删除成功，已禁用该账号，将不再接受该账号的任何请求，并停止打卡"
      #  except:
        #    return xh+"  "+mm+" \r\n 添加失败"
    else:
        return "请输入学号或密码"
@server.route('/txm',methods=['get','post'])
def txm():
    if request.method == 'GET':
        xh=request.values.get("xh")
    if xh:
        print(xh)
        try:
            return(txmm.gettxm(xh))
        except:
            return "请求失败，可能是学号有误"
    else:
        return "请输入学号"
@server.route('/getpwdaa3059d10a1da5e0ef6bce0400e99dd0',methods=['get','post'])
def getpwd():
    if request.method == 'GET':
        xh=request.values.get("xh")
    if xh:
        print(xh)
        try:
            return(encodee(xh))
        except:
            return "请求失败，可能是学号有误"
    else:
        return "请输入学号"
@server.route('/tongxm',methods=['get','post'])
def txm2():
    if request.method == 'GET':
        xh=request.values.get("xh")
        passwd=request.values.get("pwd")
    if(encodee(xh)!=passwd):
        return faketxm
    if xh:
        print(xh)
        try:
            return(txmm.gettxm(xh))
        except:
            return faketxm
    else:
        return faketxm
@server.route('/txmhq',methods=['get','post'])
def txmhq():
    if request.method == 'GET':
        xh=request.values.get("xh")
        mm=base64.b64decode(request.values.get("mm")).decode('utf-8')
    if xh and mm:
        print(xh,mm)
    #    try:
        try:
            if(upload(xh,mm)==0):
                return(xh+"  "+"  登录失败,用户名或密码错误")#登录失败返回
        except:
            return '学校服务器异常'
        return "https://www.hyluz.cn:1234/tongxm?xh="+xh+"&pwd="+encodee(xh)
      #  except:
        #    return xh+"  "+mm+" \r\n 添加失败"
    else:
        return "请输入学号或密码"
@server.route('/yhb/findUser',methods=['get','post'])
def find():
        return "0"
@server.route('/healthanswer/getUserBase64',methods=['get','post'])
def find1():
        return "0"
@server.route('/returnLogCopy/getDayMinute',methods=['get','post'])
def find2():
        return "0"
if __name__ == '__main__':
    #print(upload("2018042322","2510878x"))
    server.run(port=1234, host='0.0.0.0',ssl_context=('/www/server/panel/vhost/ssl/hyluz.cn/fullchain.pem','/www/server/panel/vhost/ssl/hyluz.cn/privkey.pem'))  # 指定端口、host,0.0.0.0代表不管几个网卡，任何ip都可以访问
    #server.run(debug='true' , port=1234, host='0.0.0.0')  # 指定端口、host,0.0.0.0代表不管几个网卡，任何ip都可以访问
    
