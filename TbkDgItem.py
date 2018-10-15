# -*- coding: utf-8 -*-

import flask,json
import top.api
import sys
appkey = 24594113
secret= 'b1ddcab524a28c78b53d7bf6ce293f34'
adzone_id=139516787
url = 'gw.api.taobao.com'

reload(sys)  
sys.setdefaultencoding('utf8')   
# 好券清单API【导购】
def TbkDgItemCouponGetRequest(q,page_size,page_no):
    req=top.api.TbkDgItemCouponGetRequest(url)
    req.set_app_info(top.appinfo(appkey,secret))

    req.adzone_id=adzone_id
    req.page_size=page_size
    req.q=q
    req.page_no=page_no
    req.platform=2
    try:
    	resp= req.getResponse()
    	return resp
    except Exception,e:
    	print(e)

# 通用物料搜索API（导购）        
def TbkDgMaterialOptionalRequest(material_id,q,page_size,page_no):
    req=top.api.TbkDgMaterialOptionalRequest(url)
    req.set_app_info(top.appinfo(appkey,secret))

    # req.start_dsr=10
    req.page_size=page_size
    req.page_no=page_no
    # req.platform=1
    # req.end_tk_rate=1234
    # req.start_tk_rate=1234
    # req.end_price=10
    # req.start_price=10
    # req.is_overseas=0
    # req.is_tmall=0
    # req.sort="tk_rate_des"
    # req.itemloc="杭州"
    # req.cat="16,30"
    req.q=q
    req.material_id=material_id
    req.has_coupon='true'
    # req.ip="13.2.33.4"
    req.adzone_id=adzone_id
    # req.need_free_shipment=1
    # req.need_prepay=1
    # req.include_pay_rate_30=1
    # req.include_good_rate=1
    # req.include_rfd_rate=1
    # req.npx_level=2
    # req.end_ka_tk_rate=1234
    # req.start_ka_tk_rate=1234
    # req.device_encrypt="MD5"
    # req.device_value="xxx"
    # req.device_type="IMEI"
    try:
    	resp= req.getResponse()
    	return resp
    except Exception,e:
    	print(e)
        
        
# 淘宝客物料下行-导购
def TbkDgOptimusMaterialRequest(material_id,page_size,page_no):
    req=top.api.TbkDgOptimusMaterialRequest(url)
    req.set_app_info(top.appinfo(appkey,secret))

    req.page_size=page_size
    req.adzone_id=adzone_id
    req.page_no=page_no
    req.material_id=material_id
    # req.device_value="xxx"
    # req.device_encrypt="MD5"
    # req.device_type="IMEI"
    # req.content_id=323
    # req.content_source="xxx"
    try:
    	resp= req.getResponse()
    	return resp
    except Exception,e:
    	print(e)
            
# 淘宝客商品详情查询 
def TbkItemInfoGetRequest(num_iids):
    req=top.api.TbkItemInfoGetRequest(url)
    req.set_app_info(top.appinfo(appkey,secret))

    req.num_iids=num_iids

    try:
    	resp= req.getResponse()
    	return resp
    except Exception,e:
    	print(e)
        
# 淘宝客商品关联推荐查询 
def TbkItemRecommendGetRequest(num_iid):
    req=top.api.TbkItemRecommendGetRequest(url)
    req.set_app_info(top.appinfo(appkey,secret))

    req.fields="num_iid,title,pict_url,small_images,reserve_price,zk_final_price,user_type,provcity,item_url"
    req.num_iid=num_iid

    try:
    	resp= req.getResponse()
    	return resp
    except Exception,e:
    	print(e)
        
# 淘宝客店铺关联推荐查询
def TbkShopRecommendGetRequest(user_id):
    req=top.api.TbkShopRecommendGetRequest(url)
    req.set_app_info(top.appinfo(appkey,secret))

    req.fields="num_iid,title,pict_url,small_images,reserve_price,zk_final_price,user_type,provcity,item_url"
    req.user_id=user_id

    try:
    	resp= req.getResponse()
    	return resp
    except Exception,e:
    	print(e)
        
# 淘宝客淘口令 
def TbkTpwdCreateRequest(text,url,logo,ext):
    req=top.api.TbkTpwdCreateRequest(url)
    req.set_app_info(top.appinfo(appkey,secret))

    req.url=url
    req.text=text
    req.logo=logo
    req.ext=ext

    try:
    	resp= req.getResponse()
    	return resp
    except Exception,e:
    	print(e)
        
# 淘宝客猜你喜欢商品 
def TbkItemQuessLikeRequest(os,ip,ua,net,page_no,page_size):
    req=top.api.TbkTpwdCreateRequest(url)
    req.set_app_info(top.appinfo(appkey,secret))

    req.adzone_id=adzone_id
    req.os=os
    req.ua=ua
    req.net=net
    req.page_no=page_no
    req.page_size=page_size

    try:
    	resp= req.getResponse()
    	return resp
    except Exception,e:
    	print(e)

app=flask.Flask(__name__)

@app.route('/CouponGet',methods=['get','post'])
def CouponGet():
    q = flask.request.values.get('q')
    page_size = flask.request.values.get('page_size')
    page_no = flask.request.values.get('page_no')
    resp = TbkDgItemCouponGetRequest(q,page_size,page_no)
    return json.dumps(resp,ensure_ascii=False)

@app.route('/MaterialOptional',methods=['get','post'])
def MaterialOptional():
    material_id= flask.request.values.get('material_id')
    q = flask.request.values.get('q')
    page_size = flask.request.values.get('page_size')
    page_no = flask.request.values.get('page_no')
    resp = TbkDgMaterialOptionalRequest(material_id,q,page_size,page_no)
    return json.dumps(resp,ensure_ascii=False)
    
@app.route('/OptimusMaterial',methods=['get','post'])
def OptimusMaterial():
    material_id= flask.request.values.get('material_id')
    page_size = flask.request.values.get('page_size')
    page_no = flask.request.values.get('page_no')
    resp = TbkDgOptimusMaterialRequest(material_id,page_size,page_no)
    return json.dumps(resp,ensure_ascii=False)
    
@app.route('/ItemInfoGet',methods=['get','post'])
def ItemInfoGet():
    num_iids= flask.request.values.get('num_iids')
    resp = TbkItemInfoGetRequest(num_iids)
    return json.dumps(resp,ensure_ascii=False)
   
@app.route('/ItemRecommendGet',methods=['get','post'])
def ItemRecommendGet():
    num_iid= flask.request.values.get('num_iid')
    resp = TbkItemRecommendGetRequest(num_iid)
    return json.dumps(resp,ensure_ascii=False)
    
@app.route('/ShopRecommendGet',methods=['get','post'])
def ShopRecommendGet():
    user_id= flask.request.values.get('user_id')
    resp = TbkShopRecommendGetRequest(user_id)
    return json.dumps(resp,ensure_ascii=False)
    
@app.route('/TpwdCreate',methods=['get','post'])
def TpwdCreate():
    text= flask.request.values.get('text')
    url= flask.request.values.get('url')
    logo= flask.request.values.get('logo')
    ext= flask.request.values.get('ext')
    resp = TbkTpwdCreateRequest(text,url,logo,ext)
    return json.dumps(resp,ensure_ascii=False)
    
# app.run(port=4000,debug=True,host='0.0.0.0')

if __name__ == '__main__':
    app.run(port=4000,debug=True,host='0.0.0.0')



    