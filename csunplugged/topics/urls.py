from django.conf.urls import url

from . import views

app_name = 'topics'
urlpatterns = [
    # eg: /topics/
    url(
        r'^$',
        views.IndexView.as_view(),
        name='index'
    ),
    # eg: /topics/binary-numbers/
    url(
        r'^(?P<topic_slug>[-\w]+)/$',
        views.TopicView.as_view(),
        name='topic'
    ),
    # eg: /topics/binary-numbers/activities
    url(
        r'^(?P<topic_slug>[-\w]+)/activities/$',
        views.ActivityList.as_view(),
        name='activity_list'
    ),
    # eg: /topics/binary-numbers/activities/binary-bracelets
    url(
        r'^(?P<topic_slug>[-\w]+)/activities/(?P<activity_slug>[-\w]+)/$',
        views.ActivityView.as_view(),
        name='activity'
    ),
    # eg: /topics/binary-numbers/other-resources
    url(
        r'^(?P<topic_slug>[-\w]+)/other-resources/$',
        views.OtherResourcesView.as_view(),
        name='other_resources'
    ),
    # eg: /topics/binary-numbers/plugged-in/
    url(
        r'^(?P<topic_slug>[-\w]+)/plugged-in/$',
        views.ProgrammingExerciseList.as_view(),
        name='programming_exercises_list'
    ),
    # eg: /topics/binary-numbers/plugged-in/exercise-1
    url(
        r'^(?P<topic_slug>[-\w]+)/plugged-in/(?P<programming_exercise_slug>[-\w]+)$',
        views.ProgrammingExerciseView.as_view(),
        name='programming_exercise'
    ),
    # eg: /topics/binary-numbers/plugged-in/exercise-1/python-solution
    url(
        r'^(?P<topic_slug>[-\w]+)/plugged-in/(?P<programming_exercise_slug>[-\w]+)/(?P<programming_language_slug>[-\w]+)-solution$',  # noqa: E501
        views.ProgrammingExerciseLanguageSolutionView.as_view(),
        name='programming_exercise_language_solution'
    ),
    # eg: /topics/binary-numbers/unit-plan
    url(
        r'^(?P<topic_slug>[-\w]+)/(?P<unit_plan_slug>[-\w]+)/$',
        views.UnitPlanView.as_view(),
        name='unit_plan'
    ),
    # eg: /topics/binary-numbers/unit-plan/5-7/lesson-1
    url(
        r'^(?P<topic_slug>[-\w]+)/(?P<unit_plan_slug>[-\w]+)/lesson/(?P<lesson_slug>[-\w]+)/$',
        views.LessonView.as_view(),
        name='lesson'
    ),
    # eg: /topics/plugged-in/difficulty/1
    url(
        r'^plugged-in/difficulty/(?P<programming_exercise_difficulty_level>[0-9]+)$',
        views.ProgrammingExerciseDifficultyView.as_view(),
        name='programming_exercise_difficulty'
    ),
]
