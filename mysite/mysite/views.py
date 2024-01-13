from django.http import HttpResponse 
from django.shortcuts import render



def index(request):
    return render(request, 'index.html')

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    # check checkbox value
    removepunc = request.POST.get('removepunc', 'off') 
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charactercount', 'off')
    # check which checkbox is on 
    if removepunc == "on":
        punctuations = '''!()-[]{};'"\,<>./?@#$%^&*_~''' 
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char 
        params = {'purpose':'Removed Punctuation', 'analyzed_text':analyzed} 
        # analyze the text
        djtext = analyzed
       
    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'changed to uppercase','analyzed_text':analyzed}
        djtext = analyzed
    
    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose':'new line removed','analyzed_text':analyzed}
        djtext = analyzed
    
    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose':'Space Removed','analyzed_text':analyzed}
        djtext = analyzed
       
    if charcount == "on":
        analyzed = ('Number of the words in given string are:'+str(len(djtext)))
        params = {'purpose':'Character count', 'analyzed_text':analyzed}
        djtext = analyzed
       
    
    if(removepunc!="on" and newlineremover!="on" and extraspaceremover!="on" and charcount!="on" and fullcaps!="on"):
        return HttpResponse("Please select any operation to proceed")

    return render(request, 'analyze.html', params)
 

