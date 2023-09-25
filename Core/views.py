from django.shortcuts import render, get_object_or_404, redirect,reverse
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import Speaking, Writing
from .forms import *
# Create your views here.


class Home(View):
    def get(self, request):
        # Your view logic for the HTTP GET method goes here
        return render(request, 'Core/home.html')

    def post(self, request):
        # Your view logic for the HTTP POST method goes here
        if request.POST['value']=="speaking":
            form = SpeakingForm(request.POST)
            if form.is_valid():
                author = request.user
                print(author)
                content = form.save(commit=False)
                content.user = author
                content.save()
                return redirect('Core:home')
            else:
                print(form.errors)

        elif request.POST['value'] == "writing":
            form = WritingForm(request.POST)
            if form.is_valid():
                author = request.user
                content = form.save(commit=False)
                content.user = author
                content.save()
                form.save()
                return redirect('Core:home')
            else:
                print(form.errors)
        return HttpResponse("This is a POST request response")

class Speaking_p(View):
    def get(self, request):
        # Your view logic for the HTTP GET method goes here
        speakings = Speaking.objects.filter(user=request.user.id)
        return render(request, 'Core/speaking.html', context={'speakings':speakings})

    def post(self, request):
        return HttpResponse("This is a POST request response")
class Speaking_practice(View):
    def get(self, request):
        # Your view logic for the HTTP GET method goes here
        speakings = Speaking.objects.filter(user=request.user.id).order_by('count')
        return render(request, 'Core/speaking_practice.html', context={'speakings':speakings})
    def post(self, request):
        form = SpeakingPracticeForm(request.POST)
        if form.is_valid():
            author = request.user.id
            content = form.save(commit=False)
            content.user = author
            content.save()
            # form.save()
            temp = Speaking.objects.filter(id=request.POST['problem'])[0]
            temp.count += 1
            temp.save()
            return redirect('Core:speaking_practice')
        else:
            print(form.errors)
        return HttpResponse("This is a POST request response")

class Speaking_practice_all(View):
    def get(self, request):
        # Your view logic for the HTTP GET method goes here
        speakings = PracticeS.objects.filter(user=request.user.id)
        return render(request, 'Core/speaking_practice_all.html', context={'speakings':speakings})
class Writing_practice(View):
    def get(self, request):
        # Your view logic for the HTTP GET method goes here
        writings = Writing.objects.filter(user=request.user.id).order_by('count')
        return render(request, 'Core/writing_practice.html', context={'writings':writings})
    def post(self, request):
        form = WritingPracticeForm(request.POST)
        print(request.POST)
        if form.is_valid():
            author = request.user.id
            content = form.save(commit=False)
            content.user = author
            content.save()
            # form.save()
            temp = Writing.objects.filter(id=request.POST['problem'])[0]
            temp.count += 1
            temp.save()
            return redirect('Core:writing_practice')
        else:
            print(form.errors)
        return HttpResponse("This is a POST request response")
class Writing_practice_all(View):
    def get(self, request):
        # Your view logic for the HTTP GET method goes here
        writings = PracticeW.objects.filter(user=request.user.id)
        return render(request, 'Core/writing_practice_all.html', context={'writings':writings})

def speaking_detail(request, speaking_id):

    # Ở đây, bạn có thể sử dụng giá trị speaking_id để thực hiện xử lý tương ứng
    if request.method == 'POST':
        # Xử lý yêu cầu DELETE ở đây (ví dụ: xóa một đối tượng Speaking)
        if request.POST.get('_method')=="DELETE":
            speaking = get_object_or_404(Speaking, id=speaking_id)
            speaking.delete()
            return redirect('Core:speaking')
    speakings = Speaking.objects.filter(type=speaking_id,user=request.user.id)
    return render(request, 'Core/speaking.html', context={'speakings': speakings})
def speaking_practice_detail(request, speaking_id):
    # Ở đây, bạn có thể sử dụng giá trị speaking_id để thực hiện xử lý tương ứng
    if request.method == 'POST':
        # Xử lý yêu cầu DELETE ở đây (ví dụ: xóa một đối tượng Speaking)
        if request.POST.get('_method')=="DELETE":
            speaking = get_object_or_404(PracticeS, id=speaking_id)
            speaking.delete()
            return redirect('Core:speaking_practice_all')
    speakings = PracticeS.objects.filter(type=speaking_id,user=request.user.id)
    return render(request, 'Core/speaking_practice_all.html', context={'speakings': speakings})

def writing_practice_detail(request, speaking_id):
    # Ở đây, bạn có thể sử dụng giá trị speaking_id để thực hiện xử lý tương ứng
    if request.method == 'POST':
        # Xử lý yêu cầu DELETE ở đây (ví dụ: xóa một đối tượng Speaking)
        if request.POST.get('_method')=="DELETE":
            writing = get_object_or_404(PracticeW, id=speaking_id)
            writing.delete()
            return redirect('Core:writing_practice_all')
    writings = PracticeW.objects.filter(type=speaking_id,user=request.user.id)
    return render(request, 'Core/writing_practice_all.html', context={'writings': writings})
class Writing_p(View):
    def get(self, request):
        # Your view logic for the HTTP GET method goes here
        writings = Writing.objects.all()
        return render(request, 'Core/writing.html', context={'writings':writings})

    def post(self, request):
        # Your view logic for the HTTP POST method goes here
        return HttpResponse("This is a POST request response")
def writing_detail(request, writing_id):
    if request.method == 'POST':
        # Xử lý yêu cầu DELETE ở đây (ví dụ: xóa một đối tượng Writing)
        if request.POST.get('_method') == "DELETE":
            writing = get_object_or_404(Writing, id=writing_id)
            writing.delete()
            return redirect('Core:writing')
    # Ở đây, bạn có thể sử dụng giá trị speaking_id để thực hiện xử lý tương ứng
    writings = Writing.objects.filter(type=writing_id,user=request.user.id)
    return render(request, 'Core/writing.html', context={'writings': writings})