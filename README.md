# tbkpython

python TbkDgItem.py
vim /etc/nginx/conf.d/default.conf
service nginx restart

gunicorn -w 4 -b 127.0.0.1:4000 TbkDgItem:app   //独立 WSGI 容器
netstat -lnp|grep 4000   //查端口占用
