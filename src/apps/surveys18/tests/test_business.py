from django.test import TestCase
from .setup import setup_fixtures
from apps.surveys18.models import Survey, Business, FarmRelatedBusiness


class ModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # load fixtures
        setup_fixtures()

    def test_create_business(self):
        survey_id = Survey.objects.get(id=3)
        relatedbusiness_a = FarmRelatedBusiness.objects.get(id=3)

        business_list_before_size = len(Business.objects.all())

        # new value
        Business.objects.create(survey=survey_id)
        new_business = Business.objects.get(survey=survey_id)
        new_business.farm_related_businesses = relatedbusiness_a
        new_business.save()

        business_list_after_size = len(Business.objects.all())
        self.assertEquals(business_list_after_size, business_list_before_size + 1)

    def test_survey_delete(self):
        Survey.objects.filter(id=1).delete()
        business_list = Business.objects.filter(survey__id=1)
        self.assertEquals(business_list.count(), 0)

    def test_survey_delete_all(self):
        relatedbusiness_list_before = FarmRelatedBusiness.objects.all()
        Survey.objects.all().delete()
        business_list = Business.objects.all()
        relatedbusiness_list_after = FarmRelatedBusiness.objects.all()

        self.assertEquals(len(business_list), 0)
        self.assertEquals(
            len(relatedbusiness_list_before), len(relatedbusiness_list_after)
        )
