from django.urls import path
from .views import (
    equipments_list_employee,
    equipment_issue_employee,
    equipment_return_employee,
    equipment_request_access_employee,

    equipments_available_manager,
    equipments_issued_manager,
    requests_list_view_manager,
)

app_name = 'api'

urlpatterns = [
    # URLs for an employee
    path('employee/equipments', equipments_list_employee),
    path('employee/issue/<int:pk>/', equipment_issue_employee),
    path('employee/return/<int:pk>/', equipment_return_employee),
    path('employee/request-access/<int:pk>/', equipment_request_access_employee),

    # # URLs for a manager
    path('manager/available/', equipments_available_manager),
    path('manager/issued/', equipments_issued_manager),
    path('manager/requests/', requests_list_view_manager)
]