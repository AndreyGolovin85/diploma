from django.urls import path

from .views import GoalCategoryCreateView, GoalCategoryListView, GoalCategoryView, GoalCreateView, GoalListView, \
    GoalView, GoalCommentCreateView, GoalCommentListView, GoalCommentView

urlpatterns = [
    path('goal_category/create', GoalCategoryCreateView.as_view(), name='create'),
    path('goal_category/list', GoalCategoryListView.as_view(), name='list'),
    path('goal_category/<pk>', GoalCategoryView.as_view(), name='pk'),
    path('goal/create', GoalCreateView.as_view(), name='create'),
    path('goal/list', GoalListView.as_view(), name='list'),
    path('goal/<pk>', GoalView.as_view(), name='pk'),
    path('goal_comment/create', GoalCommentCreateView.as_view(), name='create'),
    path('goal_comment/list', GoalCommentListView.as_view(), name='list'),
    path('goal_comment/<pk>', GoalCommentView.as_view(), name='pk'),
]
