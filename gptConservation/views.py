from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import Conversation
import google.generativeai as genai

genai.configure(api_key="AIzaSyCA2elCQ0_FeCDWbA1vNXoc_mg0gFNt5KU")
# The Gemini 1.5 models are versatile and work with both text-only and multimodal prompts
model = genai.GenerativeModel('gemini-1.5-flash')
from django.utils import timezone


from .forms import UserForm


# Configure the Generative AI model
model = genai.GenerativeModel('gemini-1.5-flash')

def index(request):
    response_text = ""
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data['user_input']
            response = model.generate_content(user_input)
            response_text = response.text
            
            # 대화 저장
            conversation = Conversation(user_input=user_input, bot_response=response_text)
            conversation.save()
            
            # 대화 기록 불러오기
            conversation_history = Conversation.objects.all()
            form = UserForm()
            return render(request, 'gptConservation/index.html', {
                'form': form, 
                'conversation_history': conversation_history
            })
        else:
            return render(request, 'gptConservation/index.html', {'form': form})
    else:
        form = UserForm()
        conversation_history = Conversation.objects.all()
        return render(request, 'gptConservation/index.html', {
            'form': form, 
            'conversation_history': conversation_history
        })

