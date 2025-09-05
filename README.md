# Portofoliu Personal (Django)

Un portofoliu modern, cu design profesionist, construit cu Django 5, Bootstrap 5 și WhiteNoise pentru servirea fișierelor statice. Include secțiuni pentru proiecte, abilități, experiență, servicii, testimoniale și un formular de contact.

## Cerințe
- Python 3.11+ (recomandat)
- macOS/Linux/Windows

## Instalare rapidă

1. Creează mediul și instalează dependențele:
   - `python3 -m venv .venv`
   - `. .venv/bin/activate` (Windows: `.venv\\Scripts\\activate`)
   - `pip install -r requirements.txt`
2. Migrează și adaugă date demo:
   - `python manage.py migrate`
   - `python manage.py seed_demo`
3. Rulează serverul:
   - `python manage.py runserver`

Deschide `http://127.0.0.1:8000`.

## Admin

Crează un superuser pentru a gestiona conținutul:

- `python manage.py createsuperuser`

Panoul: `http://127.0.0.1:8000/admin/`

## Structură
- `portfolio/` – aplicația principală (modele, views, admin, comenzi management)
- `templates/` – layout global + pagini (home, proiecte, rezumat, contact)
- `static/` – CSS/JS custom și resurse
- `media/` – fișiere încărcate (coperți proiecte, avatare, etc.)

## Setări
- `DEBUG=True` implicit
- `EMAIL_BACKEND=console` (emailurile se afișează în consolă în dev)
- Static/Media: `STATIC_URL=/static/`, `MEDIA_URL=/media/`

## Deployment (sumar)
- Rulează `collectstatic`
- Configurează un server (Gunicorn/Uvicorn) + reverse proxy
- WhiteNoise e deja configurat

## Personalizare
- Editează textul din template-uri (`templates/`)
- Actualizează culorile în `static/css/style.css`
- Adaugă conținut din Admin (proiecte, abilități, servicii etc.)

---
Creat cu ❤️ pentru un portofoliu elegant și rapid.
