from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView, FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

from .models import Project, Skill, Experience, Education, Service, Testimonial, SocialLink, ContactMessage
from django import forms


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "subject", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nume"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email"}),
            "subject": forms.TextInput(attrs={"class": "form-control", "placeholder": "Subiect"}),
            "message": forms.Textarea(attrs={"class": "form-control", "placeholder": "Mesaj", "rows": 5}),
        }


class HomeView(TemplateView):
    template_name = "portfolio/home.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["projects"] = Project.objects.filter(featured=True)[:6]
        ctx["skills"] = Skill.objects.all()[:12]
        ctx["experiences"] = Experience.objects.all()[:5]
        ctx["services"] = Service.objects.all()[:6]
        ctx["testimonials"] = Testimonial.objects.all()[:6]
        ctx["socials"] = SocialLink.objects.all()
        return ctx


class ProjectListView(ListView):
    model = Project
    template_name = "portfolio/project_list.html"
    context_object_name = "projects"
    paginate_by = 9


class ProjectDetailView(DetailView):
    model = Project
    template_name = "portfolio/project_detail.html"
    context_object_name = "project"
    slug_field = "slug"
    slug_url_kwarg = "slug"


class ResumeView(TemplateView):
    template_name = "portfolio/resume.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["experiences"] = Experience.objects.all()
        ctx["education"] = Education.objects.all()
        ctx["skills"] = Skill.objects.all()
        return ctx


class ContactView(FormView):
    template_name = "portfolio/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("contact")

    def form_valid(self, form):
        msg = form.save()
        # Trimite email către destinatarul din setări
        subject = f"{getattr(settings, 'EMAIL_SUBJECT_PREFIX', '')}{form.cleaned_data.get('subject') or 'Mesaj nou din formular'}"
        body = (
            f"Ai primit un mesaj nou din formularul de contact:\n\n"
            f"Nume: {form.cleaned_data.get('name')}\n"
            f"Email: {form.cleaned_data.get('email')}\n"
            f"Subiect: {form.cleaned_data.get('subject') or '-'}\n\n"
            f"Mesaj:\n{form.cleaned_data.get('message')}\n\n"
            f"Admin: {self.request.build_absolute_uri('/admin/portfolio/contactmessage/')}"
        )
        try:
            send_mail(
                subject,
                body,
                getattr(settings, 'DEFAULT_FROM_EMAIL', 'no-reply@localhost'),
                [getattr(settings, 'CONTACT_RECIPIENT_EMAIL', 'admin@localhost')],
                fail_silently=True,
                reply_to=[form.cleaned_data.get('email')],
            )
        except Exception:
            # Fail silent în prod; mesajul rămâne salvat în DB.
            pass

        messages.success(self.request, "Mulțumesc! Mesajul a fost trimis. Revin în curând.")
        return super().form_valid(form)


# Create your views here.
