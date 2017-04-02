from tests.BaseTest import BaseTest
from topics.models import CurriculumArea


class CurriculumAreaModelTest(BaseTest):

    def __init__(self, *args, **kwargs):
        BaseTest.__init__(self, *args, **kwargs)

    def test_curriculum_area(self):
        new_curriculum_area = CurriculumArea.objects.create(
            slug='slug',
            name='name',
        )
        query_result = CurriculumArea.objects.get(pk=1)
        self.assertEqual(query_result, new_curriculum_area)
