from django.test import TestCase
from .models import Post

# Create your tests here.
class PostText(TestCase):

    def setUp(self):

        instance = Post.objects.create(title='Curso de Django', description='....', type='PUBLIC')
        instance.save()

        instance = Post.objects.create(title='Curso de Unreal', description='****', type='PUBLIC')
        instance.save()

        instance = Post.objects.create(title='Angular vs React', type='PRIVATE')
        instance.save()

    def test_for_post(self):
        #
        print(Post.objects.all())
        print(Post.objects.filter(type='PUBLIC'))
        #print(Post.objects.filter(title='Curso de Django'))
        #print(Post.objects.filter(title__icontains='Curso'))
        #print(Post.objects.filter(created_at__range=['2021-01-01', '2021-02-01']))
        instance = Post.objects.get(pk=1)
        instance.title = 'Django REST'
        instance.save()

        instance = Post.objects.get(pk=2)
        instance.title = 'Unreal'
        instance.save()

        print(Post.objects.all())
        instance = Post.objects.get(pk=3)
        instance.delete()
        print(Post.objects.all())
        instance = Post.objects.get(pk=2)
        instance.delete()
        print(Post.objects.all())