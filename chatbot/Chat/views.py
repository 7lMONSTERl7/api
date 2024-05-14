from rest_framework.views import APIView
from rest_framework.response import Response
from .AIModel import AIModel
import datetime

ai_model = AIModel()
ai_model.load_model()
if not ai_model.trained:
    ai_model.train_model()

class chat(APIView):
    def get(self, request):
        user_input = request.GET.get('q')
        if user_input:
            response_message = ai_model.model(user_input)
            return Response(
                {
                    "message": str(response_message),
                    "time": datetime.datetime.now().strftime("%H:%M"),
                    "date": datetime.date.today(),
                    "Author":"MonsTer",
                    "name": 'BOT',
                }
            )
        else:
            return Response(None)
