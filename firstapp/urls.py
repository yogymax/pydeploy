from rest_framework import routers
from firstapp.views import *
router = routers.SimpleRouter()
router.register(r'address', AddressViewSets)
router.register(r'companies', CompanyViewSets)
router.register(r'emps', EmployeeViewSet)
urlpatterns = router.urls