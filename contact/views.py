import json
import logging
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from .models import ContactMessage

logger = logging.getLogger('contact')


@csrf_exempt
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
        
        # Validate required fields
        if not all([name, email, message]):
            return JsonResponse({
                'error': 'All fields are required.'
            }, status=400)
        
        # Validate email format
        if '@' not in email or '.' not in email:
            return JsonResponse({
                'error': 'Please enter a valid email address.'
            }, status=400)
        
        # Save to database
        contact_message = ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )
        
        # Send email notification
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
            send_mail(
                subject=subject,
                message=email_content,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )
            
            # Send confirmation email to the sender
            confirmation_subject = 'Thank you for contacting Araya Haftu'
            confirmation_message = f"""
            Hi {name},
            
            Thank you for reaching out! I have received your message and will get back to you as soon as possible.
            
            Your message:
            {message}
            
            Best regards,
            Araya Haftu
            Fullstack Developer & Prompt Engineer
            
            ---
            This is an automated response. Please do not reply to this email.
            """
            
            send_mail(
                subject=confirmation_subject,
                message=confirmation_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
                fail_silently=False,
            )
            
            logger.info(f"Contact form submitted successfully by {name} ({email})")
            
            return JsonResponse({
                'success': True,
                'message': 'Message sent successfully! I\'ll get back to you soon.'
            })
            
        except Exception as email_error:
            logger.error(f"Failed to send email for contact form: {email_error}")
            # Still return success since the message was saved to database
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
