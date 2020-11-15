from django.urls import path
from .import views
urlpatterns = [
    path('ticketcost/',views.ticket_cost,name="ticketcost"),
    path('feedbacksection/',views.feedback,name="feedbacksection"),
    path('showavailableanimals/',views.showavailableanimals,name="showavailableanimals"),
]