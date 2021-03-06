from rest_framework.routers import DefaultRouter

from . import views

api = DefaultRouter()
api.trailing_slash = "/?"

api.register(r"survey", views.SurveyViewSet)
api.register(r"contenttype", views.ContentTypeViewSet)
api.register(r"shorttermhire", views.ShortTermHireViewSet)
api.register(r"longtermhire", views.LongTermHireViewSet)
api.register(r"shorttermlack", views.ShortTermLackViewSet)
api.register(r"longtermlack", views.LongTermLackViewSet)
api.register(r"numberworkers", views.NumberWorkersViewSet)
api.register(r"nosalaryhire", views.NoSalaryHireViewSet)
api.register(r"subsidy", views.SubsidyViewSet)
api.register(r"refuse", views.RefuseViewSet)
api.register(r"populationage", views.PopulationAgeViewSet)
api.register(r"population", views.PopulationViewSet)
api.register(r"cropmarketing", views.CropMarketingViewSet)
api.register(r"livestockmarketing", views.LivestockMarketingViewSet)
api.register(r"unit", views.UnitViewSet)
api.register(r"product", views.ProductViewSet)
api.register(r"business", views.BusinessViewSet)
api.register(r"landtype", views.LandTypeViewSet)
api.register(r"landarea", views.LandAreaViewSet)
api.register(r"phone", views.PhoneViewSet)
api.register(r"addressmatch", views.AddressMatchViewSet)
api.register(r"annualincome", views.AnnualIncomeViewSet)
api.register(r"agescope", views.AgeScopeViewSet)
api.register(r"worktype", views.WorkTypeViewSet)
api.register(r"refusereason", views.RefuseReasonViewSet)
api.register(r"farmerworkday", views.FarmerWorkDayViewSet)
api.register(r"relationship", views.RelationshipViewSet)
api.register(r"refusereason", views.RefuseReasonViewSet)
api.register(r"educationlevel", views.EducationLevelViewSet)
api.register(r"lifestyle", views.LifeStyleViewSet)
api.register(r"gender", views.GenderViewSet)
api.register(r"loss", views.LossViewSet)
api.register(r"producttype", views.ProductTypeViewSet)
api.register(r"contract", views.ContractViewSet)
api.register(r"managementtype", views.ManagementTypeViewSet)
api.register(r"farmrelatedbusiness", views.FarmRelatedBusinessViewSet)
api.register(r"landstatus", views.LandStatusViewSet)
api.register(r"lack", views.LackViewSet)
api.register(r"incomerange", views.IncomeRangeViewSet)
api.register(r"markettype", views.MarketTypeViewSet)
api.register(r"month", views.MonthViewSet)
api.register(r"worktype", views.WorkTypeViewSet)
api.register(r"otherfarmerwork", views.OtherFarmWorkViewSet)
api.register(r"builder", views.BuilderFileViewSet)
