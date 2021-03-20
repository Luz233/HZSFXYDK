#coding:utf-8
import requests
import base64
import random
import re
import datetime
import os
import sqll
import json
def upload(username,passwd):
    url_login = 'https://jkxxcj.zjhu.edu.cn/yhb/login'
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

xsxx=sqll.selectall()
success=0
fail=0
for i in xsxx:
        if(i[2]!=1):
                try:
                    upload(i[0],i[1])
                    success=success+1
                except:
                    fail=fail+1
                    continue
headers={"Content-Type":"application/json"}
posturl="https://oapi.dingtalk.com/robot/send?access_token=97e43cde118b974aaa96ec257c781297bd5f4772dd58da0554450400bc682a19"
canshu={"msgtype": "text","text": {"content":"success:"+str(success)+"\nfail:"+str(fail)}}
requests.post(headers=headers,url=posturl,data=json.dumps(canshu))
print("成功",success)
print("失败",fail)