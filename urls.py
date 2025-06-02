
from django.urls import path
from myapp.views import*

urlpatterns = [
    path('',index,name='home'),
    path('company/',company,name='company'),
    path('service/',service,name='service'),
    path('products/',products,name='products'),
    path('reviews/',reviews,name='reviews'),
    path('cart/',cart,name='cart'),
    path('contact/',contact,name='contact'),
    path('join/',joinUS,name='join'),
    path('delivery/',delivery,name='delivery'),
    path('interior/',interior,name='interior'),
    path('assemblyservice/',assemblyservice,name='assemblyservice'),
    path('warrantysupport/',warrantysupport,name='warrantysupport'),
    path('emioptions/',emioptions,name='emioptions'),
    path('checkout/',checkout,name='checkout'),
    path('beds/', beds, name='beds'),
    path('sofas/', sofas, name='sofas'),
    path('loungechairs/', loungechairs, name='loungechairs'),
    path('dressingtables/', dressingtables, name='dressingtables'),
    path('wardrobes/', wardrobes, name='wardrobes'),
    path('studytables/', studytables, name='studytables'),
    path('diningtable/', diningtable, name='diningtable'),
    path('mattresses/', mattresses, name='mattresses'),
    path('bedpillows/', bedpillows, name='bedpillows'),
    path('sofapillows/', sofapillows, name='sofapillows'),
    path('shoerack/', shoerack, name='shoerack'),
    path('tvunit/', tvunit, name='tvunit'),
]