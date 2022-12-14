from django.urls import path

from .views import GoalCategoryCreateView, GoalCategoryListView, GoalCategoryView, GoalCreateView, GoalListView, \
    GoalView, GoalCommentCreateView, GoalCommentListView, GoalCommentView, BoardCreateView, BoardListView, BoardView

urlpatterns = [
    path('goal_category/create', GoalCategoryCreateView.as_view(), name='create category'),
    path('goal_category/list', GoalCategoryListView.as_view(), name='list category'),
    path('goal_category/<pk>', GoalCategoryView.as_view(), name='pk category'),

    path('goal/create', GoalCreateView.as_view(), name='create Goal'),
    path('goal/list', GoalListView.as_view(), name='list Goal'),
    path('goal/<pk>', GoalView.as_view(), name='pk Goal'),

    path('goal_comment/create', GoalCommentCreateView.as_view(), name='create Comment'),
    path('goal_comment/list', GoalCommentListView.as_view(), name='list Comment'),
    path('goal_comment/<pk>', GoalCommentView.as_view(), name='pk Comment'),

    path('board/create', BoardCreateView.as_view(), name='create board'),
    path('board/list', BoardListView.as_view(), name='list board'),
    path('board/<pk>', BoardView.as_view(), name='pk board'),
]
