# -*- coding: utf-8 -*-
"""
    apps.reports.views
    ~~~~~~~~~~~~~~

    views related to reports and stats
    
    :copyright: (c) 2012 by arruda.
"""

from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from pyflot import Flot

from utils.decorators import ajax_login_required, JsonResponse

from books.models import Book
from annoying.decorators import render_to

def add_axis_label(flot,axis="x",label="foo"):  
    old_axis = flot._options.get(axis+'axis',{})
    old_axis.update({
            'axisLabel':label, 
            'axisLabelUseCanvas': True,
            'axisLabelFontSizePixels':20, 
            'axisLabelFontFamily':'Arial'
    })
    flot._options[axis+'axis'] = old_axis
    return flot

@ajax_login_required
def test_flot(request):
    "testing flot ajax"
    import datetime
    import time
    
    m1 = datetime.date.today()
    m0 = m1 - datetime.timedelta(days=30)
    m2 = m1+datetime.timedelta(days=30)
    m3 = m2+datetime.timedelta(days=30)
    graph = Flot()
    graph.add_lines([(m1, 1), (m2, 2), (m3, 3)], label="func a",**{"fill":True})
#    graph.add_bars([(1, 1), (2, 1), (3, 3)], label="func b")
    graph = add_axis_label(graph,"x","Label x")
    graph = add_axis_label(graph,"y","Label y")
    graph._options['xaxis'].update({"minTickSize": [1, "month"]})
    
#    graph._options['xaxis'].update({"min": time.mktime(m0.timetuple())*100 })
#    graph._options['xaxis'].update({"min": 1354154400000 })
    
    
    
    content = "{\"datas\": %(DATAS)s, \"options\": %(OPTS)s }" % {"DATAS":graph.series_json, "OPTS":graph.options_json}
    return HttpResponse(content, mimetype="application/json")


@ajax_login_required
def monthly_expenses_vs_quota(request):
    """
     return flot data/options for the expenses of all months with their quota
    """
    import datetime
    import time
    graph = Flot()
    user_profile = request.user.get_profile()
    quotas = user_profile.quotas.all()
    num_months = quotas.count()
    
    used_quota_datas = []
    quota_datas = []
    for i in xrange(0,num_months):
        quota = quotas[i]             
        used_quota = float(user_profile.used_monthly_quota(i))   
        xaxis = quota.date
        
        quota_datas.append([xaxis,float(quota.quota)])
        used_quota_datas.append([xaxis,used_quota])

        
    
    
    graph.add_lines(used_quota_datas, label="Expenses",**{"fill":True,"steps":True})
    graph.add_lines(quota_datas, label="Quota",**{"steps":True})
    
    graph = add_axis_label(graph,"x","Months")
    graph = add_axis_label(graph,"y","Amount ($)")
    graph._options['xaxis'].update({"minTickSize": [1, "month"]})
    
#    #show a month before
#    date0 = quotas[num_months-1].date - datetime.timedelta(days=30)
#    graph._options['xaxis'].update({"min": time.mktime(date0.timetuple())*1000 })
    
    
    content = "{\"datas\": %(DATAS)s, \"options\": %(OPTS)s }" % {"DATAS":graph.series_json, "OPTS":graph.options_json}
    return HttpResponse(content, mimetype="application/json")



@login_required
@render_to("reports/stats.html")
def stats(request):
    "show some general stats and reports"
    
    return locals()


