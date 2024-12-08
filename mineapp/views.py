from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import SignIn
from .models import CreateUser
from django.db import IntegrityError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password


def register_page(request):
    return render(request, '../templates/reg.html')


from .serializers import PasswordCheckSerializer

class PasswordCheckView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PasswordCheckSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            password = serializer.validated_data['password']

            try:
                user = CreateUser.objects.get(name=name)
                if check_password(password, user.password):
                    return Response({"success": True, "message": "Password is correct"}, status=status.HTTP_200_OK)
                else:
                    return Response({"success": False, "message": "Invalid password"}, status=status.HTTP_400_BAD_REQUEST)
            except CreateUser.DoesNotExist:
                return Response({"success": False, "message": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



def get_user(request):
    if request.method == 'POST':
        form = SignIn(request.POST)
        print(request.POST)
        if form.is_valid():
            try:
                form.save()
                print('Пользователь успешно зарегистрирован.')
            except Exception as e:
                print(f"Ошибка при сохранении: {e}")
            else:
                print("Ошибки формы:", form.errors)
        else:
            print("Ошибки формы:", form.errors)
    else:
        form = SignIn()
    return render(request, '../templates/reg.html', {'form': form})



def title_page(request):
    return render(request, '../templates/title.html')   