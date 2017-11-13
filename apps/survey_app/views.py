from django.shortcuts import render, redirect


def index(request):
    return render(request, 'survey_app/index.html')


def submitted(request):
    try:
        request.session['count']
    except KeyError:
        request.session['count'] = 0
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['loc'] = request.POST['location']
        request.session['lang'] = request.POST['language']
        request.session['comm'] = request.POST['comment']
        print "submitted"
        request.session['count'] += 1
        return redirect('/results')
    else:
        print "Not Submitted"
        return redirect('/')


def results(request):
    return render(request, 'survey_app/results.html')


def reset(request):
    del request.session['name']
    del request.session['loc']
    del request.session['lang']
    del request.session['comm']
    return redirect('/')
