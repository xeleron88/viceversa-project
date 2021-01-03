from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def reverse(request):
	user_text = request.GET['usertext']
	reversed_text = user_text[::-1]
	newlist = reversed_text.split()
	number_of_words = len(newlist)
	return render(request, 'reverse.html', {'usertext':reversed_text, 'len_words':number_of_words})