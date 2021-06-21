from django.test import TestCase

# Create your tests here.


from django.contrib.auth.models import User


class CustomerTestCase(TestCase):

    def setUp(self):
        user = User(username='cooler',email='cooler@gmail.com') 
        user_pw = 'faysalali'
        self.user_pw = user_pw
        user.is_staff=True
        user.is_superuser = True
        user.save()
        user.set_password(user_pw)
        self.user = user
        # print(user.id)


    def test_user_exists(self):
        users_number = User.objects.all().count()
        message = "First value and second value are not equal !"
        self.assertEqual(users_number,1,message)
        self.assertNotEqual(users_number,0)
        print(users_number)


    def test_user_password(self):
        # user_qs = User.objects.filter(username__iexact='cooler')
        # user_exists = user_qs.exists() and user_qs.count()==1
        # self.assertTrue(user_exists)
        # user_a = user_qs.first()
        self.assertTrue(self.user.check_password(self.user_pw))



