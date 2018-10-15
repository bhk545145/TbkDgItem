# -*- coding: utf-8 -*-
import top.api

url = 'gw.api.taobao.com'

req=top.api.TbkDgItemCouponGetRequest(url)
req.set_app_info(top.appinfo('24594113','b1ddcab524a28c78b53d7bf6ce293f34'))

req.adzone_id=139516787
req.cat="16,18"
req.page_size=1
req.q="女装"
req.page_no=1

try:
	resp= req.getResponse()
	print(resp)
except Exception,e:
	print(e)