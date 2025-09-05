from django.core.management.base import BaseCommand
from django.utils import timezone

from portfolio.models import (
    Skill, ProjectCategory, Project, Experience, Education,
    Service, Testimonial, SocialLink,
)


class Command(BaseCommand):
    help = "Populateaza baza de date cu date demo pentru portofoliu."

    def handle(self, *args, **options):
        # Skills
        skills = [
            ("Python", 95), ("Django", 92), ("REST APIs", 90),
            ("PostgreSQL", 85), ("Docker", 80), ("AWS", 75),
            ("JavaScript", 85), ("React", 80), ("HTML/CSS", 90),
        ]
        skill_objs = []
        for name, level in skills:
            obj, _ = Skill.objects.get_or_create(name=name, defaults={"level": level})
            obj.level = level
            obj.save()
            skill_objs.append(obj)

        # Categories
        web, _ = ProjectCategory.objects.get_or_create(name="Web App")
        site, _ = ProjectCategory.objects.get_or_create(name="Website")

        # Projects
        projects = [
            {
                "title": "Platformă management proiecte",
                "subtitle": "Django + React, autentificare, roluri, grafice",
                "description": "Aplicație web completă pentru urmărirea proiectelor și task-urilor, cu API REST și UI modern.",
                "category": web,
                "featured": True,
                "skills": ["Python", "Django", "React", "PostgreSQL"],
                "live_url": "",
                "source_url": "https://github.com/example/project-mgmt",
            },
            {
                "title": "Site prezentare agenție",
                "subtitle": "Bootstrap 5 + SEO + blog",
                "description": "Site modern, optimizat SEO, viteze excelente și design responsive.",
                "category": site,
                "featured": True,
                "skills": ["HTML/CSS", "JavaScript", "Django"],
                "live_url": "https://example.com/",
                "source_url": "",
            },
            {
                "title": "API analytics",
                "subtitle": "Serviciu agregare evenimente + rapoarte",
                "description": "Microserviciu pentru colectare evenimente și generare rapoarte periodice.",
                "category": web,
                "featured": False,
                "skills": ["Python", "Django", "Docker"],
                "live_url": "",
                "source_url": "",
            },
        ]

        for p in projects:
            obj, _ = Project.objects.get_or_create(title=p["title"], defaults={
                "subtitle": p["subtitle"],
                "description": p["description"],
                "category": p["category"],
                "featured": p["featured"],
                "live_url": p["live_url"],
                "source_url": p["source_url"],
            })
            # set M2M
            obj.skills.set([Skill.objects.get(name=n) for n in p["skills"]])

        # Experience
        Experience.objects.get_or_create(
            role="Software Engineer",
            company="Tech Corp",
            defaults={
                "start_date": timezone.now().date().replace(year=timezone.now().year - 3),
                "end_date": None,
                "description": "Lucrez la produse web scalabile cu Django, REST și infra în cloud.",
            },
        )

        # Education
        Education.objects.get_or_create(
            degree="Licență în Informatică",
            institution="Universitatea X",
            defaults={
                "start_date": timezone.now().date().replace(year=timezone.now().year - 7),
                "end_date": timezone.now().date().replace(year=timezone.now().year - 4),
                "description": "Algoritmică, structuri de date, baze de date, rețele.",
            },
        )

        # Services
        services = [
            ("Dezvoltare Web", "Aplicații și site-uri performante.", "fa-solid fa-code"),
            ("Arhitectură & Scalare", "Design scalabil, optimizări performanță.", "fa-solid fa-sitemap"),
            ("Integrare API", "REST/GraphQL, plăți, autentificare.", "fa-solid fa-plug"),
        ]
        for t, d, ic in services:
            Service.objects.get_or_create(title=t, defaults={"description": d, "icon": ic})

        # Testimonials
        Testimonial.objects.get_or_create(
            author="Andrei Pop",
            defaults={"role": "CTO, Firma Y", "content": "Colaborare excelentă, livrări la timp și calitate foarte bună."},
        )

        # Socials
        socials = [
            ("GitHub", "https://github.com/youruser", "fa-brands fa-github", 1),
            ("LinkedIn", "https://linkedin.com/in/youruser", "fa-brands fa-linkedin", 2),
            ("Email", "mailto:hello@example.com", "fa-solid fa-envelope", 3),
        ]
        for p, u, ic, order in socials:
            SocialLink.objects.get_or_create(platform=p, defaults={"url": u, "icon": ic, "order": order})

        self.stdout.write(self.style.SUCCESS("Date demo create/actualizate cu succes."))

