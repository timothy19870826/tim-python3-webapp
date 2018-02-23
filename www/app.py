
#!/usr/bin/env python3

# -*- coding: utf-8 -*-



__author__ = 'Tim Cat'



'''

async web application.

'''

import logging
logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
	response = web.Response(body=b'<h1>TimCat</h1>', content_type='text/html')
	logging.info('server response from index: %s' % response.body)
	return response

async def init(loop):
	app = web.Application(loop=loop)
	app.router.add_route('GET', '/', index)
	srv = await loop.create_server(app.make_handler(), "127.0.0.1", 9000)
	logging.info('server started at http://127.0.0.1:9000...')
	return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()