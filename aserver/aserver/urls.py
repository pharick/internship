from aiohttp import web

from aserver import views

urls = [
    web.get('/', views.index),
]
