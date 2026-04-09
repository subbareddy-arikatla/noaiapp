# from datetime import datetime
# from rest_framework import serializers
# from .models import Student

# class StudentSerializer(serializers.Serializer):
#     name=serializers.CharField(255)
#     age=serializers.IntegerField(4) 
#     phonenumber=serializers.CharField(20)
#     def create(self,validated_data):
#         return Student(**validated_data)
#     def update(self,instance,validated_data):
#         instance.name=validated_data.get('name',instance.name)
#         instance.age=validated_data.get('age',instance.age)
#         instance.phonenumber=validated_data.get('phonenumber',instance.phonenumber)
#         instance.save()
#         return instance
# s1=Student(name='subba',age=21,phonenumber='+91 8688469174')
# serializer=StudentSerializer(s1)
# print(serializers.data)

# class ContactForm(serializers.Serializer):
#     email=serializers.EmailField()
#     message=serializers.CharField()
#     def save(self):
#         email=self.validated_data['email']
#         message=self.validated_data['message']
#         # send_email( from=email,message=message)
#     class BlogPostSerializer(serializers.Serializer):
#         title=serializers.CharField(max_length=100)
#         content=serializers.CharField()
#         def validate_title(self,value):
#             if 'django' not in value.lower():
#                 raise serializers.ValidationError('Blogs post is not in django')
#             return value

# class EventSerializer(serializers.Serializer):
#     description=serializers.CharField(max_length=100)
#     start=serializers.DateTimeField()
#     finish=serializers.DateTimeField()
#     def validate(self, data):
#         if data['start']>data['finish']:
#             raise serializers.ValidationError('finish must occur after start')
#         return data

# class UserSerializer(serializers.Serializer):
#     email=serializers.EmailField()
#     username=serializers.CharField(max_length=100)
# class CommentSerializer(serializers.Serializer):
#     user=UserSerializer(required=False)
#     event=EventSerializer(many=True)
#     content=serializers.CharField(max_length=200)
#     created=serializers.DateTimeField()
# class UserSerializer(serializers.ModelSerializer):
#     profile=ProfileSerializer()
#     class Meta:
#         model=User
#         fileds=['username','email','profile']
#         def created(self,validated_data):
#             profile_data=validated_data.pop('profile')
#             user=User.objects.create(**validated_data)
#             Profile.object.create(user=user **profile)
#             return user
#         def update(self,instance,validated_data):
#             profile_data=validated_data.pop('profile')
#             profile=instance.profile
#             instance.username=validated_data.get('username',instance.username)
#             instance.email=validated_data.get('email',instance.email)
#             instance.save()
#             profile.is_premium_member = profile_data.get('is_premium_member',profile.is_premium_member)
#             profile.has_support_contract = profile_data.get('has_support_contract',profile.has_support_contract)
#             profile.save()
#             return instance

from rest_framework import serializers
from .models import Student,Question,Product,Order,Customer,ProductDemo,Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=['id','title','author','publication_date','genre']
    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty")
        return value

    def validate(self, data):
        if data['publication_date'] > serializers.DateField().to_internal_value('2100-01-01'):
            raise serializers.ValidationError("Invalid publication date")
        return data
    
class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name=serializers.CharField(max_length=255)
    age=serializers.IntegerField()
    phonenumber=serializers.CharField(max_length=20)
    def validate_name(self,value):
        if value != value.lower():
            raise serializers.ValidationError('name must be lowercase only')
        return value
    def validate_age(self,value):
        if not (18 <= value <= 100):
            raise serializers.ValidationError('age must be between the 18 to 100')
        return value

    def create(self,validated_data):
        return Student.objects.create(**validated_data)
    def update(self,instance,validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.age=validated_data.get('age',instance.age)
        instance.phonenumber=validated_data.get('phonenumber',instance.phonenumber)
        instance.save()
        return instance
    
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Question
        fields=['id','question_name','question_type','question_category','option_a','option_b','option_c','option_d','correct_ans']
        read_only_fields = ['id']

    def validate(self,data):
        correct_ans=data['correct_ans']
        options = [
            data.get('option_a'),
            data.get('option_b'),
            data.get('option_c'),
            data.get('option_d')
            ]
        if correct_ans not in options:
            raise serializers.ValidationError('correct answer must be above option a,b,c,d')
        return data
    def create(self,validated_data):
        return Question.objects.create(**validated_data)
    def update(self,instance,validated_data):
        instance.question_name=validated_data.get('question_name',instance.question_name)
        instance.question_type=validated_data.get('question_type',instance.question_type)
        instance.question_category=validated_data.get('question_category',instance.question_category)
        instance.option_a=validated_data.get('option_a',instance.option_a)
        instance.option_b=validated_data.get('option_b',instance.option_b)
        instance.option_c=validated_data.get('option_c',instance.option_c)
        instance.option_d=validated_data.get('option_d',instance.option_d)
        instance.correct_ans=validated_data.get('correct_ans',instance.correct_ans)
        instance.save()
        return instance

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name','price','quantity']

    def validate_price(self, value):
        if value < 0:
            raise Exception("Invalid price")
        return value
class ProductdemoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name=serializers.CharField(max_length=255)
    description=serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=255
        )
    image=serializers.ImageField()
    price=serializers.IntegerField()
    category=serializers.CharField()
    quantity=serializers.IntegerField()
    def create(self,validated_data):
        return ProductDemo.objects.create(**validated_data)
    def update(self,instance,validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.description=validated_data.get('description',instance.data)
        instance.image=validated_data.get('image',instance.image)
        instance.price=validated_data.get('price',instance.price)
        instance.category=validated_data.get('category',instance.category)
        instance.quantity=validated_data.get(' quantity',instance.quantity)
        instance.created_at=validated_data.get('created_at',instance.created_at)
        instance.save()
        return instance
class OrderSerializer(serializers.ModelSerializer):
    # If these are reverse relationships or ManyToMany, ensure 'many=True' is correct
    product = ProductdemoSerializer(many=True, read_only=True)
    
    class Meta:
        model = Order
        fields = ['id', 'product', 'customer', 'bill', 'address', 'created_at']
        read_only_fields = ['id', 'created_at']

class CustomerSerializer(serializers.ModelSerializer):
    order = OrderSerializer(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = ["name", "phonenumber","address","order"]