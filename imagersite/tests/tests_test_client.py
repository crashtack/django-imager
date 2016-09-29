from django.core import mail
from django.test import Client, TestCase
from django.contrib.auth.models import User
from django.urls import reverse


VALID_REG_PARAMS = {
    'username': 'bob',
    'email': 'bob@bob.com',
    'password1': 'bob1234bob',
    'password2': 'bob1234bob'
}


class RegistrationTests(TestCase):

    def setUp(self):
        # self.client = Client()
        self.reg_valid = self.client.post(reverse('registration_register'), VALID_REG_PARAMS,
                                          follow=True)

    def tearDown(self):
        pass

    def test_user_in_db_after_reg(self):
        '''Test that there is one user in the database.'''
        self.assertEqual(User.objects.count(), 1)

    def test_email_on_registration(self):
        '''Test that the activation email is in the outbox.'''
        self.assertEqual(len(mail.outbox), 1)

    def test_valid_registration_redirect(self):
        '''Test valid registration redirects to complete page.'''
        self.assertIn(('/accounts/register/complete/', 302),
                      self.reg_valid.redirect_chain)

    def test_new_reg_is_not_active(self):
        '''Tests a user who has not clicked on the confirmation email is not active'''
        self.assertFalse(User.objects.first().is_active)

    def test_reg_email_sent_to_user(self):
        '''Test that email was sent to new users email.'''
        self.assertIn(VALID_REG_PARAMS['email'], mail.outbox[0].to)

    def test_reg_email_contains_a_confirmation_link(self):
        '''test registration email contains a confirmation link'''
        # import pdb; pdb.set_trace()
        self.assertIn('accounts/activate/', mail.outbox[0].body)
