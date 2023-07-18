from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', "subtitle", 'author', 'cost', 'isbn')
    def validate(self, data):
        title = data.get("title", None)
        isbn = data.get('isbn', None)
        # if not title.isalpha():
        #     raise ValidationError(
        #         {
        #             'status': False,
        #             'message': 'iltimos, harflardan foydalaning'
        #         }
        #     )
        # if Book.objects.filter(title=title).exists():
        #     raise ValidationError(
        #         {
        #             'status': False,
        #             'message': 'BU kitob avval qushilgan'
        #         }
        #     )

        return data

    def validate_price(self, attrs):
        print(attrs)
# class BookSerializerEdit(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields =

