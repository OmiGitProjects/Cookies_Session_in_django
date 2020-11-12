from django.shortcuts import render

def index(request):
    ''' Homepage '''
    
    username = request.session.get('username')
    context = {'username': username}
    return render(request, 'profile_/index.html', context)