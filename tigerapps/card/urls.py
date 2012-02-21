from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

                       # index
                       (r'^/?$', 'card.views.index'),
                       (r'^index/?$', 'card.views.index'),
                       (r'^index/err/?$', 'card.auth.login_err'),

                       # login page/functions for CAS (members and checkers)
                       (r'^cas/?$', 'card.auth.cas_login'),

                       # MEMBER
                       # personal
                       (r'^(?P<netid>\w+)/personal/?$', 'card.views.personal'),
                       # CHECKER
                       # Meal checking
                       (r'^(?P<netid>\w+)/checker/session/?$', 'card.checksession.open_session'),
                       (r'^(?P<netid>\w+)/checker/check/?$', 'card.checksession.open_session_check'),
#                       (r'(?P<netid>\w+)/checker/register/?$', 'card.checksession.open_session_reg'),
                       # Session
                       (r'^(?P<netid>\w+)/session/add/?$', 'card.checksession.check_session'),
#                       (r'(?P<netid>\w+)/session/add/remove/(?P<meal_idx>\w+)/?$', 'card.checksession.remove_meal'),                       
#                       (r'(?P<netid>\w+)/session/register/?$', 'card.register.reg_session'),
#                       (r'(?P<netid>\w+)/session/register/remove/(?P<mem_idx>\w+)/?$', 'card.register.remove_mem'),

                       # CLUB ACCOUNT
                       # club login
                       (r'^club/?$', 'card.auth.club_login'),
                       # default
                       (r'^(?P<club>\w+)/club/?$', 'card.club.club'),
                       # Members functions
                       (r'^(?P<club>\w+)/members/add/?$', 'card.register.registerClub'),
                       (r'^(?P<club>\w+)/members/list/?$', 'card.club.listMembers'),
                       (r'^(?P<club>\w+)/members/(?P<netid>\w+)/modify/?$', 'card.club.modMember'),
                       # Meals functions
                       (r'^(?P<club>\w+)/meals/add/?$', 'card.club.addMeals'),
                       (r'^(?P<club>\w+)/meals/(?P<mealid>\w+)/modify/?$', 'card.club.modMeals'),
                       (r'^(?P<club>\w+)/meals/list/?$', 'card.club.listMeals'),
                       # Statistics
                       (r'^(?P<club>\w+)/stats/(?P<graphtype>\w+)/?$', 'card.club.stats'),
                       # Change password
                       (r'^(?P<club>\w+)/account/?$', 'card.auth.change_password'),
                       # General logout
                       (r'^logout_cas/?$', 'card.auth.cas_logout'),
                       (r'^logout_club/?$', 'card.auth.club_logout'),

                       # static items (primarily for css)
                       (r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': '/srv/card/MealOnline/projectdjango/static'}),  #'/u/bevancha/project/projectdjango/static'}), #'/u/msgordon/cardOLD/projectdjango/static'}),
                       # help documentation
                       (r'^help/(?P<path>.*)$', 'card.views.help'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
                       (r'^admin/', include(admin.site.urls)),
                       (r'^admin', include(admin.site.urls)),
		       #(r'^admin/*(.*)',admin.site.root),
)