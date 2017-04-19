import os.path
from utils.BaseLoader import BaseLoader

from utils.errors.CouldNotFindMarkdownFileError import CouldNotFindMarkdownFileError
from utils.errors.EmptyMarkdownFileError import EmptyMarkdownFileError
from utils.errors.MarkdownFileMissingTitleError import MarkdownFileMissingTitleError
from utils.errors.UnitPlanHasNoLessonsError import UnitPlanHasNoLessonsError

from ._LessonsLoader import LessonsLoader


class UnitPlanLoader(BaseLoader):
    '''Loader for unit plans'''

    def __init__(self, load_log, structure_file_path, topic, BASE_PATH):
        '''Initiates the loader for unit plans

        Args:
            structure_file_path: file path (string)
            topic: Topic model object
        '''
        super().__init__(BASE_PATH, load_log)
        self.unit_plan_slug = os.path.split(structure_file_path)[0]
        self.structure_file_path = os.path.join(self.BASE_PATH, structure_file_path)
        self.BASE_PATH = os.path.join(self.BASE_PATH, self.unit_plan_slug)
        self.topic = topic

    def load(self):
        '''Load the content for unit plans

        Raises:
            CouldNotFindMarkdownFileError:
            MarkdownFileMissingTitleError:
            EmptyMarkdownFileError:
            UnitPlanHasNoLessonsError:
        '''

        # Convert the content to HTML
        unit_plan_content = self.convert_md_file(
            os.path.join(
                self.BASE_PATH,
                '{}.md'.format(self.unit_plan_slug)
            ),
            self.structure_file_path
        )

        unit_plan_structure = self.load_yaml_file(self.structure_file_path)

        unit_plan = self.topic.topic_unit_plans.create(
            slug=self.unit_plan_slug,
            name=unit_plan_content.title,
            content=unit_plan_content.html_string,
        )
        unit_plan.save()  # TODO shouldn't have to save? create does this?

        self.log('Added Unit Plan: {}'.format(unit_plan.name), 1)

        # Load the lessons for the unit plan

        # If there is nothing in the structure dictionary there
        # are obviously no lessons! Error!
        if len(unit_plan_structure) == 0:
            raise UnitPlanHasNoLessonsError()
        # Call the loader to save the lessons into the db
        lessons_structure = unit_plan_structure
        LessonsLoader(
            self.structure_file_path,
            self.load_log,
            lessons_structure,
            self.topic,
            unit_plan,
            self.BASE_PATH
        ).load()
