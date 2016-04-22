#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Mr Hamer'

import logging; logging.basicConfig(level = logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

#这是一个“请求处理器”，接收request实例作为唯一参数，返回response实例
#“请求处理器”通过在某一个特定的route上注册处理器，进而处理请求
def index(request):
    return web.Response(body=b'<h1>Perfect!</h1>')

'''@asyncio.coroutine yield from'''
async def init(loop):
    app = web.Application(loop = loop)      #Application相当于一个web服务器
    app.router.add_route('GET', '/', index) #此处注册处理器用于处理这个路径的请求
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)  #app.make_handler是一个请求工厂
    logging.info('server start at http://127.0.0.1:9000 ...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()