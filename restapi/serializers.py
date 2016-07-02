from rest_framework import serializers
from .models import Animal
import base64

class AnimalSerializer(serializers.HyperlinkedModelSerializer):

    imgenc = serializers.SerializerMethodField('get_image_enc')

    class Meta:
        model = Animal
        fields = ('nome', 'imagem', 'dono', 'imgenc')

    def get_image_enc(self, obj):

        img = open( obj.imagem.path, "rb" )
        encoded_string = base64.b64encode(img.read())
        return encoded_string


    '''
     class PictureSerialiser(serializers.ModelSerializer):

    image_url = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = Picture
        fields = ('field', 'image', 'image_url')

    def get_image_url(self, obj):
        return obj.image.url
     '''