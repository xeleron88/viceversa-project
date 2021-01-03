from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def reverse(request):
	user_text = request.GET['usertext']
	reversed_text = user_text[::-1]
	reversed_text = str(reversed_text)
	return render(request, 'reverse.html', {'usertext':reversed_text, 'len_words':(len(set(reversed_text.split())))})