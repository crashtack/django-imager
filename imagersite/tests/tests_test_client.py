from django.core import mail
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


INVALID_REG_PARAMS = {
    'username': 'bob',
    'email': 'bob@bobcom',
    'password1': 'bob',
    'password2': 'boc'
}

VALID_REG_PARAMS = {
    'username': 'bob',
    'email': 'bob@bob.com',
    'password1': 'bob1234bob',
    'password2': 'bob1234bob'
}


class InValidRegistrationTests(TestCase):

    def setUp(self):
        self.reg_invalid = self.client.post(reverse('registration_register'), INVALID_REG_PARAMS,)

    def test_user_not_in_db_after_invalid_reg(self):
        '''Test that there is no user in the database.'''
        self.assertEqual(User.objects.count(), 0)

    def test_no_email_on_registration(self):
        '''Test that the activation email is in the outbox.'''
        self.assertEqual(len(mail.outbox), 0)

    def test_invalid_registration_no_redirect(self):
        '''Test valid registration redirects to complete page.'''
        self.assertEqual(self.reg_invalid.context['request'].path, '/accounts/register/')

    def test_invalid_registration_validity(self):
        '''Test valid registration redirects to complete page.'''
        self.assertFalse(self.reg_invalid.context['form'].is_valid())


class ValidRegistrationTests(TestCase):

    def setUp(self):
        self.reg_valid = self.client.post(reverse('registration_register'), VALID_REG_PARAMS,
                                          follow=True)

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


class RegistrationViewTests(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse('registration_register'))

    def test_reg_page_exists(self):
        '''assert the reg page responds 200'''
        self.assertEquals(self.response.status_code, 200)

    def test_uses_correct_template(self):
        '''assert the home page view is rendered with our templates'''
        for template_name in ["imagersite/base.html", 'registration/registration_form.html']:
            self.assertTemplateUsed(self.response, template_name, count=1)

    def test_for_registration_form(self):
        '''assert that theresponse contains a link to the resirataion page'''
        form_tag = b'<form method="POST">'
        assert form_tag in self.response.content
