from django.template import Context

def config(request):
    from constance import config
    return {'config': config}

def this_year(request):
    from datetime import date
    return {'this_year': date.today().year}
