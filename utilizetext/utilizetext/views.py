from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def analyze(request):
    iptext = request.POST.get('text', 'default')

    removepunc = request.POST.get('removepunc', 'off')
    tocaps = request.POST.get('tocaps', 'off')
    removenewline = request.POST.get('removenewline', 'off')
    removeextraspace = request.POST.get('removeextraspace', 'off')
    charcount = request.POST.get('charcount', 'off')

    if (removepunc == "on"):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""

        for char in iptext:
            if char not in punctuations:
                analyzed = analyzed + char

        parameters = {'purpose': 'Punctuations Removal', 'analyzed_text': analyzed}
        iptext = analyzed

    if (tocaps == "on"):
        analyzed = ""

        for char in iptext:
            analyzed = analyzed + char.upper()

        parameters = {'purpose': 'Capitalize text', 'analyzed_text': analyzed}
        iptext = analyzed

    if (removenewline == "on"):
        analyzed = ""

        for char in iptext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        parameters = {'purpose': 'New line Removal', 'analyzed_text': analyzed}
        iptext = analyzed

    if (removeextraspace == "on"):
        analyzed = ""

        for i, char in enumerate(iptext):
            if not (iptext[i] == " " and iptext[i+1] == " "):
                analyzed = analyzed + char

        parameters = {'purpose': 'Extra space Removal', 'analyzed_text': analyzed}
        iptext = analyzed

    if (charcount == "on"):
        count = 0

        for char in iptext:
            if char != " ":
                count = count + 1
                analyzed = count

        parameters = {'purpose': 'Count Characters', 'analyzed_text': analyzed}

    if (removepunc != "on" and removenewline != "on" and removeextraspace != "on" and tocaps != "on" and charcount!="on"):
        return HttpResponse("You have not selected any options!")


    return render(request, 'analyze.html', parameters)
