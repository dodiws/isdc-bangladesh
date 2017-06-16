# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2017 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################


from django.conf.urls import url

from geonode.contrib.monitoring import views

urlpatterns = [
                # serve calculated metrics
                url(r'^api/metrics/$', views.api_metrics, name='api_metrics'),
                url(r'^api/services/$', views.api_services, name='api_services'),
                url(r'^api/hosts/$', views.api_hosts, name='api_hosts'),
                url(r'^api/labels/$', views.api_labels, name='api_labels'),
                url(r'^api/resources/$', views.api_resources, name='api_resources'),
                url(r'^api/exceptions/$', views.api_exceptions, name='api_exceptions'),
                url(r'^api/exceptions/(?P<exception_id>[\d\+]+)/$', views.api_exception, name='api_exception'),
                url(r'^api/metric_data/(?P<metric_name>[\w\.]+)/$', views.api_metric_data, 
                                                                    name='api_metric_data'),
                # serve raw check data to outside
                url(r'^api/beacon/$', views.api_beacon, name='api_beacon'),
                url(r'^api/beacon/(?P<exposed>.*?)/$', views.api_beacon, name='api_beacon_exposed'),
              ]
