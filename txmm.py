#coding:utf-8
import requests
import json
import time
import base64
#import importlib
#importlib.reload(sys)
headers={
'Host': 'jkxxcj.zjhu.edu.cn',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
'Connection': 'close',
'Upgrade-Insecure-Requests': '1'
}

a1="""
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
"""

a2="""的进校码</h4>
					<p class="xh">学号："""

a3="""</p>
					<p class="lxdh">联系电话："""

a4="""</p>
					<!-- <p class="gssj"></p> -->
					<p class="xsxy">学院："""

a5="""</p>
					<p class="xsbj">班级："""

a6="""</p>
					<p class="isAllowOut font-green">是否允许出校：允许</p>
					<p class="restTime"></p>
					<p class="dqzt"></p>
					<!--<img src="img/ewm.png"/>-->
					<img src="https://jkxxcj.zjhu.edu.cn/qrcode/isBlue?zgh=Base64"""

a7="""&date="""

a8="""
" class="noewmimg">
					<h6>温馨提示:如果要出校，请在门口扫码出校，并在规定时间( AM 06:00 到 PM 22:00 )内返校。若超时返校，则15天内不可再次出校。</h6>
				</div>
<div><br><br><br><br><br><br></div>
				<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- lll -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-2181926949629728"
     data-ad-slot="5677025402"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
								<a  href = "https://www.hyluz.cn/" >
<button type="button" class="sqfx refresh-btn">点击查看状态</button>
</a>
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
def gettxm(xh):
    print(xh)
    a=json.loads(requests.get("https://jkxxcj.zjhu.edu.cn/yhb/findUser?ZGH="+xh,headers=headers).text)
    result=a1+a['xm']
    resu=a1+a['xm']+a2+a['zgh']+a3+a['lxdh']+a4+a['xymc']+a5+a['bjmc']+a6+str(base64.b64encode(xh.encode('utf-8')))[2:-1]+a7+str(time.strftime('%Y%m%d'))+a8
    return resu