from django.shortcuts import render
from rest_framework import viewsets
from .models import Member
from .serializers import MemberSerializer
from django.shortcuts import render, redirect
from .forms import MemberForm


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

def members_list(request):
    members = Member.objects.all()
    return render(request, 'members/members_list.html', {'members': members})


def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('members_list')  # Redirect to a page displaying the list of members
    else:
        form = MemberForm()
    return render(request, 'members/add_member.html', {'form': form})
