from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removefunc = request.POST.get('removefunc', 'off')

    uppercse = request.POST.get('uppercse', 'off')
    newline = request.POST.get('newline', 'off')
    extraspe = request.POST.get('extraspe', 'off')

    if removefunc == "on":
        punctutions = r'''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctutions:
                analyzed += char
        params = {'purpose': 'Remove punctuations', 'analyzed_text': analyzed}
        djtext=analyzed

    if uppercse == "on":
        analyzed =""
        for char in djtext:
                analyzed = analyzed + char.upper()
        params = {'purpose': 'Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
    if newline == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
            else:
                print ("no")
            # print("pre",analyzed)
        params = {'purpose': 'Remove Newlines', 'analyzed_text': analyzed}
        djtext = analyzed

    if extraspe == "on":

        analyzed =""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and index + 1 < len(djtext) and djtext[index + 1] == " "):
                analyzed += char

        params = {'purpose': 'Remove Extra Spaces', 'analyzed_text': analyzed}

        djtext = analyzed


    if (removefunc != "on" and uppercse != "on" and newline != "on" and extraspe != "on"):
        return HttpResponse("Error")
    return render(request, 'analyze.html', params)