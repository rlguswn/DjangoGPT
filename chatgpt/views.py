from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from dotenv import load_dotenv
import openai
import os
from chatgpt.models import Conversation
from chatgpt.serializers import ConversationSerializer

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')


class ChatView(View):
    def get(self, request, *args, **kwargs):
        conversations = request.session.get('conversations', [])
        return render(request, 'chatgpt/chat.html', {'conversations': conversations})

    def post(self, request, *args, **kwargs):
        prompt = request.POST.get('prompt')
        if prompt:
            # 이전 대화 기록 가져오기
            session_conversations = request.session.get('conversations', [])
            previous_conversations = "\n".join([f"User: {c['prompt']}\nAI: {c['response']}" for c in session_conversations])
            prompt_with_previous = f"{previous_conversations}\nUser: {prompt}\nAI:"

            model_engine = "text-davinci-003"
            completions = openai.Completion.create(
                engine=model_engine,
                prompt=prompt_with_previous,
                max_tokens=1024,
                n=5,
                stop=None,
                temperature=0.5,
            )
            response = completions.choices[0].text.strip()

            conversation = {'prompt': prompt, 'response': response}

            # 대화 기록에 새로운 응답 추가
            session_conversations.append(conversation)
            request.session['conversations'] = session_conversations

        return self.get(request, *args, **kwargs)


class ChatList(APIView):
    def get(self, request):
        conversations = Conversation.get.all(user=request.user)
        serializer = ConversationSerializer(conversations)
        return Response(serializer.data, status=status.HTTP_200_OK)
