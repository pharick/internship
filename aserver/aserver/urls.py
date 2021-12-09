from aiohttp import web

from . import views

urls = [
    web.get('/', views.index),
]
