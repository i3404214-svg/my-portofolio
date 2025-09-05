from .models import SocialLink


def socials(request):
    return {"socials": SocialLink.objects.all()}

