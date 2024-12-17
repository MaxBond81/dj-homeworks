from django.urls import path

from measurement.views import SensorUpdateView, SensorListView, MeasurementView, SensorView, SensorCreateView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorCreateView.as_view(), name="sensor_create"),
    path('measurements/', MeasurementView.as_view(), name="measurement"),
    path('sensors/', SensorListView.as_view(), name="sensor_list"),
    path('sensors/<pk>/', SensorView.as_view(), name="sensor_show"),
    path('sensors/<pk>/', SensorUpdateView.as_view(), name="sensor_update"),

]
