from datetime import datetime
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(255)
    age=serializers.IntegerField(4) 
    phonenumber=serializers.CharField(20)
    def create(self,validated_data):
        return Student(**validated_data)
    def update(self,instance,validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.age=validated_data.get('age',instance.age)
        instance.phonenumber=validated_data.get('phonenumber',instance.phonenumber)
        instance.save()
        return instance
s1=Student(name='subba',age=21,phonenumber='+91 8688469174')
serializer=StudentSerializer(s1)
print(serializers.data)

class ContactForm(serializers.Serializer):
    email=serializers.EmailField()
    message=serializers.CharField()
    def save(self):
        email=self.validated_data['email']
        message=self.validated_data['message']
        # send_email( from=email,message=message)
    class BlogPostSerializer(serializers.Serializer):
        title=serializers.CharField(max_length=100)
        content=serializers.CharField()
        def validate_title(self,value):
            if 'django' not in value.lower():
                raise serializers.ValidationError('Blogs post is not in django')
            return value

class EventSerializer(serializers.Serializer):
    description=serializers.CharField(max_length=100)
    start=serializers.DateTimeField()
    finish=serializers.DateTimeField()
    def validate(self, data):
        if data['start']>data['finish']:
            raise serializers.ValidationError('finish must occur after start')
        return data

class UserSerializer(serializers.Serializer):
    email=serializers.EmailField()
    username=serializers.CharField(max_length=100)
class CommentSerializer(serializers.Serializer):
    user=UserSerializer(required=False)
    event=EventSerializer(many=True)
    content=serializers.CharField(max_length=200)
    created=serializers.DateTimeField()
class UserSerializer(serializers.ModelSerializer):
    profile=ProfileSerializer()
    class Meta:
        model=User
        fileds=['username','email','profile']
        def created(self,validated_data):
            profile_data=validated_data.pop('profile')
            user=User.objects.create(**validated_data)
            Profile.object.create(user=user **profile)
            return user
        def update(self,instance,validated_data):
            profile_data=validated_data.pop('profile')
            profile=instance.profile
            instance.username=validated_data.get('username',instance.username)
            instance.email=validated_data.get('email',instance.email)
            instance.save()
            profile.is_premium_member = profile_data.get('is_premium_member',profile.is_premium_member)
            profile.has_support_contract = profile_data.get('has_support_contract',profile.has_support_contract)
            profile.save()
            return instance