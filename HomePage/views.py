import textwrap
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View

# Create your views here.
class HomePage(View):
    def dispatch(request, *args, **kwargs):
        response_text = textwrap.dedent('''\
                <html>
                <head>
                    <title>Corobox Project</title>
                </head>
                <body>
                    <p align="center">Corobox Project</p>
                
                </body>
                </html>
            ''')
        return HttpResponse(response_text)