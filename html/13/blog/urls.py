import re
import views
urlpatterns = [
    (r'^$',views.index),
    (r'^login$',views.login),
    (r'^dologin$',views.doLogin),
    (r'^studentlist$',views.studentList),
    (r'^student/(\d+)$',views.studentInfo),
    (r'^register$',views.register),
    (r'^static/',views.loadStatic),
    (r'^yzm',views.yzm),
    (r'^test$',views.test),
]