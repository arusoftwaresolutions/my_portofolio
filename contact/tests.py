from django.test import TestCase
from django.urls import reverse
from django.core import mail
from .models import ContactMessage
import json


class ContactFormTestCase(TestCase):
    def setUp(self):
        self.contact_url = reverse('contact:contact_form')
        self.valid_data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'message': 'This is a test message.'
        }
    
    def test_contact_form_valid_data(self):
        """Test contact form with valid data"""
        response = self.client.post(
            self.contact_url,
            data=json.dumps(self.valid_data),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 200)
        self.assertTrue(ContactMessage.objects.filter(name='John Doe').exists())
    
    def test_contact_form_missing_fields(self):
        """Test contact form with missing fields"""
        invalid_data = {'name': 'John Doe'}  # Missing email and message
        
        response = self.client.post(
            self.contact_url,
            data=json.dumps(invalid_data),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())
    
    def test_contact_form_invalid_email(self):
        """Test contact form with invalid email"""
        invalid_data = self.valid_data.copy()
        invalid_data['email'] = 'invalid-email'
        
        response = self.client.post(
            self.contact_url,
            data=json.dumps(invalid_data),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())
    
    def test_contact_message_model(self):
        """Test ContactMessage model"""
        message = ContactMessage.objects.create(
            name='Test User',
            email='test@example.com',
            message='Test message'
        )
        
        self.assertEqual(str(message), f"Message from Test User - {message.created_at.strftime('%Y-%m-%d %H:%M')}")
        self.assertFalse(message.is_read)
