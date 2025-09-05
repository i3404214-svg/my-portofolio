from django.db import models
from django.utils.text import slugify


class TimestampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)
    level = models.PositiveIntegerField(default=80, help_text="Percent 0-100")

    class Meta:
        ordering = ["-level", "name"]

    def __str__(self):
        return f"{self.name} ({self.level}%)"


class ProjectCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Project(TimestampedModel):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    subtitle = models.CharField(max_length=250, blank=True)
    description = models.TextField(blank=True)
    cover = models.ImageField(upload_to="projects/covers/", blank=True, null=True)
    category = models.ForeignKey(ProjectCategory, null=True, blank=True, on_delete=models.SET_NULL)
    skills = models.ManyToManyField(Skill, blank=True, related_name="projects")
    live_url = models.URLField(blank=True)
    source_url = models.URLField(blank=True)
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Experience(TimestampedModel):
    role = models.CharField(max_length=150)
    company = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["-start_date"]

    def __str__(self):
        return f"{self.role} · {self.company}"


class Education(TimestampedModel):
    degree = models.CharField(max_length=150)
    institution = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["-start_date"]

    def __str__(self):
        return f"{self.degree} · {self.institution}"


class Service(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    icon = models.CharField(max_length=64, blank=True, help_text="FontAwesome class, ex: fa-solid fa-code")

    def __str__(self):
        return self.title


class Testimonial(TimestampedModel):
    author = models.CharField(max_length=120)
    role = models.CharField(max_length=120, blank=True)
    content = models.TextField()
    avatar = models.ImageField(upload_to="testimonials/", blank=True, null=True)

    def __str__(self):
        return f"{self.author} — {self.role}"


class SocialLink(models.Model):
    platform = models.CharField(max_length=50)
    url = models.URLField()
    icon = models.CharField(max_length=64, blank=True, help_text="FontAwesome class, ex: fa-brands fa-github")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "platform"]

    def __str__(self):
        return self.platform


class ContactMessage(TimestampedModel):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=150, blank=True)
    message = models.TextField()
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"{self.name}: {self.subject or (self.message[:30] + '…')}"


# Create your models here.
