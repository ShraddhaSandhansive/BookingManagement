
from django.conf.urls import url,include
from AppointmentBookingSystem.views import *

urlpatterns = [
 url(r'^login/', test ),
 url(r'^SignUp/', SignUp),
 url(r'^storeUser/', storeUser ),
 url(r'^loginUser/', login_user),
 url(r'^storeService/', storeService),
 url(r'^renderServices/', render_services),
 url(r'^renderAllServices/', render_all_services),
 url(r'^serviceSelected/(?P<serviceId>\d+)/', serviceSelected),
 url(r'^bookServices/', bookServices),
 url(r'^logout/', logout_from_system ),
 url(r'^aboutus/', about_us), 
]
