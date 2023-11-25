from django.test import TestCase

from control_post.models import blogpost


class PosTest(TestCase):


    def test_crear_post(self):

        post= blogpost(gen="prueba",fecha="2023-11-20", titulo="test test", content="dascqweqwfasd" )

        post.save()


        self.assertEqual(blogpost.objects.count(), 1)
        self.assertEqual(post.titulo, "test test")
        self.assertEqual(post.gen, "prueba")


# Create your tests here.
