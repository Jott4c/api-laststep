from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User, Types, Address


class AddressSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    street = serializers.CharField(max_length=100)
    number = serializers.CharField(max_length=10)
    state = serializers.CharField(max_length=2)
    city = serializers.CharField(max_length=50)


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(
        max_length=20,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="username already taken.",
            )
        ],
    )
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(
        max_length=127,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="email already registered.",
            )
        ],
    )
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    age = serializers.DateField()
    phone = serializers.CharField(max_length=14)
    url_image = serializers.CharField(max_length=270, required=False)
    type = serializers.ChoiceField(
        choices=Types.choices,
    )
    spec_or_cond = serializers.CharField(max_length=250, required=False)
    address = AddressSerializer(required=False)

    def create(self, validated_data: dict):
        address_dict = validated_data.get("address")

        if address_dict:
            address_dict = validated_data.pop("address")
        user = User.objects.create_user(**validated_data)

        if address_dict:
            Address.objects.create(**address_dict, user=user)
        return user

    def update(self, instance: User, validated_data: dict):

        address_dict: dict = validated_data.pop("address", None)

        if address_dict:
            address_obj, created = Address.objects.get_or_create(user=instance)
            for key, value in address_dict.items():
                setattr(address_obj, key, value)
            address_obj.save()

        for key, value in validated_data.items():
            print(value)
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)

        instance.save()

        return instance
