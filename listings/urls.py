from django.urls import path
from listings import views, views_agencies, views_dashboard


urlpatterns = [
    path('', views.listings, name="listings"),
    path('pregled/<slug>/', views.listing, name="listing_profile"),

    # API Calls
    path('get-details/', views.get_details, name='get_details'),
    path('get-areas/', views.get_areas, name='get_areas'),
    path('get-subcategories/', views.get_subcategories, name='get_subcategories'),
    path('oglas-omiljeni/', views.add_remove_favorites, name="listing_add_remove_favorites"),

    # Delete lilisting
    path('delete/<int:id>/', views_dashboard.delete, name='delete'),

    # Edit listings

    path('edit/', views_dashboard.edit, name='edit'),
    path('save-listing/<int:pk>', views_dashboard.confirm_edit, name='confirm_edit'),

    # TODO: Redefine pages to specific models 
    path('postavi/', views_dashboard.create, name="listing_create", kwargs={'footer': 'create_listing'}),
    path('postavi/sacuvaj', views_dashboard.submit, name="listing_submit"),
    path('moji-oglasi/', views_dashboard.my_listings, name="listing_my_listings"),
    path('sacuvane-pretrage/', views_dashboard.saved_listings, name="listing_saved_listings"),
    path('profil/', views_dashboard.profile, name="listing_profile"),
    path('poruke/', views_dashboard.messages, name="listing_messages"),
    path('omiljeni-oglasi/', views_dashboard.my_favorites, name="listing_my_favorites"),
    path('pregledi/', views_dashboard.my_views, name="listing_my_views"),
    path('pretplate/', views_dashboard.subscription, name="listing_subscription"),
    path('promovisi-oglas/', views_dashboard.promote_listing, name="listing_promote_listing"),
    path('podesavanja/', views_dashboard.settings, name="listing_settings"),

    # Agency pages
    path('agencije/', views_agencies.agencies_page, name="agencies_page" ),
    path('o-agenciji/', views_agencies.about_agency, name="about_agency" ),

    # Investors pages

    path('investitori/', views_agencies.investors_page, name="investors_page"),
    path('o-investitoru/', views_agencies.about_investor, name="about_investor"),

    # My blog pages

    path('o-nama/', views_agencies.about_us, name="about_us")


]
