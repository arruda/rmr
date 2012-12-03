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

def add_axis_label(flot,axis="x",label="foo"):     
    flot._options[axis+'axis'] = {
            'axisLabel':label, 
            'axisLabelUseCanvas': True,
            'axisLabelFontSizePixels':20, 
            'axisLabelFontFamily':'Arial'
    }
    return flot


@ajax_login_required
def test_flot(request):
    "testing flot ajax"
    
    graph = Flot()
    graph.add_lines([(1, 1), (2, 2), (3, 3)], label="func a",**{"fill":True})
    graph = add_axis_label(graph,"x","Label x")
    graph = add_axis_label(graph,"y","Label y")
    
    grid = {
            'backgroundColor': { 'colors': ["#fff", "#eee"] }
        }
#    graph._options['grid'] = grid
    
    content = "{\"datas\": %(DATAS)s, \"options\": %(OPTS)s }" % {"DATAS":graph.series_json, "OPTS":graph.options_json}
    return HttpResponse(content, mimetype="application/json")



