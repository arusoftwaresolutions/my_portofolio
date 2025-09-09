import json
import logging
import re
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import ContactMessage

logger = logging.getLogger('contact')


@require_http_methods(["POST"])
def contact_form(request):
    """
    Handle contact form submissions and send email notifications.
    """
    try:
        # Parse JSON data
        data = json.loads(request.body)
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        message = data.get('message', '').strip()
        
        logger.info(f"Contact form received: {name}, {email}, message length: {len(message)}")
        
        # Validate required fields
        if not all([name, email, message]):
            return JsonResponse({
                'error': 'All fields are required.'
            }, status=400)
        
        # Validate email format using Django's built-in validator
        try:
            validate_email(email)
        except ValidationError:
            return JsonResponse({
                'error': 'Please enter a valid email address.'
            }, status=400)
        
        # Additional email validation
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, email):
            return JsonResponse({
                'error': 'Please enter a valid email address format.'
            }, status=400)
        
        # Save to database (with error handling)
        try:
            contact_message = ContactMessage.objects.create(
                name=name,
                email=email,
                message=message
            )
            logger.info(f"Contact message saved: {name} ({email}) - Message ID: {contact_message.id}")
        except Exception as db_error:
            logger.error(f"Database save failed: {str(db_error)}")
            # Continue anyway - we'll still try to send email
        
        # Try to send email notification (optional)
        try:
            subject = f'New Contact Form Submission from {name}'
            
            # Create email content
            email_content = f"""
            You have received a new message from your portfolio contact form:
            
            Name: {name}
            Email: {email}
            Message:
            {message}
            
            ---
            This message was sent from your portfolio website.
            """
            
            # Send email to yourself
            result = send_mail(
                subject=subject,
                message=email_content,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=True,  # Changed back to True to not fail the form
            )
            
            if result:
                logger.info(f"Email sent successfully to {settings.EMAIL_HOST_USER} for message from {name} ({email})")
            else:
                logger.warning(f"Email sending returned False for message from {name} ({email})")
            
        except Exception as email_error:
            logger.error(f"Email sending failed (but message saved): {str(email_error)}")
            logger.error(f"Email settings - HOST: {settings.EMAIL_HOST}, PORT: {settings.EMAIL_PORT}, USER: {settings.EMAIL_HOST_USER}")
            # Continue anyway - message is saved to database
        
        # Always return success since message is saved
        return JsonResponse({
            'success': True,
            'message': 'Message received! I\'ll get back to you soon.'
        })
            
    except json.JSONDecodeError:
        return JsonResponse({
            'error': 'Invalid JSON data.'
        }, status=400)
        
    except Exception as e:
        logger.error(f"Contact form error: {e}")
        return JsonResponse({
            'error': 'An error occurred while processing your message. Please try again.'
        }, status=500)


def contact_success(request):
    """
    Display success page after contact form submission.
    """
    return JsonResponse({
        'message': 'Thank you for your message!'
    })
