from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomClaimTokenObtainSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        #custom Claims
        token['username']=user.username
        token['email']=user.email
        
        return token