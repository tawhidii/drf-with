import email
from django.contrib.auth.models import User
from rest_framework import serializers

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)

    class Meta:
        model = User
        fields = ['username','email','password','password2']
        extra_kwargs = {
            'password' : {'write_only':True}
        }

    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'error':'Password Are not same !!'})
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error':'Email already taken !!'})
        account = User(username=self.validated_data['username'],
                        email=self.validated_data['email'],
                        )
        account.set_password(self.validated_data['password'])
        account.save()
        return account

        


