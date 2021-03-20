if curl -sL --fail https://www.hyluz.cn:1234/tongxm -o /dev/null; then
    echo "Success"
    kill -KILL $(lsof -i:1234|tail -1|awk '"$1"!=""{print $2}')
else
    echo "Fail"
    curl -H "Content-Type: application/json" -X POST  https://oapi.dingtalk.com/robot/send?access_token=97e43cde118b974aaa96ec257c781297bd5f4772dd58da0554450400bc682a19 -d '{"msgtype": "text","text":{"content":"daka_server错误"}}'
    curl https://sc.ftqq.com/SCU76448T3c3140299eabeab0cf2e5c73d8c1d8405e1438fc2c05d.send?text=servererror
    kill -KILL $(lsof -i:1234|tail -1|awk '"$1"!=""{print $2}')
    source "jkxx/jkxx_venv/bin/activate" && cd "/jkxx" && python3 "jkxx_server.py"
fi
