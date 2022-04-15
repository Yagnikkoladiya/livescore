import json

from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from .forms import ViewerRegistrationForm, ViewerProfileForm
from django.utils.decorators import method_decorator
from django.contrib import messages
from .models import Viewer
import requests
from django.http import JsonResponse


# Create your views here.
def Homepage(request):
    return render(request, 'app/homepage.html')


def search(request):
    data = request.GET.get('search')
    return render(request, 'app/search.html')

def live(request):
    # score_card = requests.get("https://lt-fn-cdn001.akamaized.net/common/en/Etc:UTC/cricket/get_scorecard/33070465")
    # response = json.loads(score_card.text)
    # print(response)
    return render(request, 'app/live.html')

def point_table(request):
    point_table_request = requests.get('https://ipl-stats-sports-mechanic.s3.ap-south-1.amazonaws.com/ipl/feeds/stats/60-groupstandings.js')
    response = json.loads(point_table_request.text.split('(')[1].split(')')[0])


    print(response)
    return render(request, 'app/pointtable.html',{'data': response['points']})


@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        form = ViewerProfileForm()
        return render(request, 'app/profile.html', {'form': form,
                                                    'active': 'btn-primary'})

    def post(self, request):
        form = ViewerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Viewer(user=user, name=name, locality=locality, city=city, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request, 'Profile Update Successfully...')
        return render(request, 'app/profile.html', {'form': form, 'active': 'btn_primary'})


class ViewerRegistrationView(View):
    def get(self, request):
        form = ViewerRegistrationForm()
        return render(request, 'app/Viewerregistration.html', {'form': form})

    def post(self, request):
        form = ViewerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Registration successfully!!')
            form.save()
        return render(request, 'app/Viewerregistration.html', {'form': form})
