from rest_framework import serializers


class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()



class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField()
    re_new_password = serializers.CharField()

    def validate_old_password(self , value):
        """
        
        """

        if not self.context["request"].user.check_password(value) :
            raise serializers.ValidationError("this pasword is not your password")

        return value

    def validate(self, attrs):
        if attrs["re_new_password"] != attrs["new_password"] :
            raise serializers.ValidationError("passwords not same")

        return attrs

    
    def create(self, validated_data):
        
        user = self.context["request"].user.set_password(validated_data["new_password"])
        return user