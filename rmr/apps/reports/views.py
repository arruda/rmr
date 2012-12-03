# -*- coding: utf-8 -*-
"""
    apps.reports.views
    ~~~~~~~~~~~~~~

    views related to reports and stats
    
    :copyright: (c) 2012 by arruda.
"""

from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404

from pyflot import Flot

from utils.decorators import ajax_login_required, JsonResponse

from books.models import Book



@ajax_login_required
def test_flot(request):
    "testing flot ajax"
    
    graph = Flot()
    graph.add_lines([(1, 1), (2, 2), (3, 3)])
    content = "{\"datas\": %(DATAS)s, \"options\": %(OPTS)s }" % {"DATAS":graph.series_json, "OPTS":graph.options_json}
    return HttpResponse(content, mimetype="application/json")



