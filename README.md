# rango
Rango – A Django-Based Content Discovery &amp; Social Interaction Platform

Description
===========
Rango is a full-stack Django web application that allows users to discover, categorize, and interact with web pages in a structured way. Inspired by content-driven platforms, Rango enables users to create categories, add pages, like content, search internally and externally, manage profiles, and communicate through real-time chat features.

The project demonstrates practical Django concepts including authentication, AJAX interactions, REST-style views, session handling, and third-party API integration.

Problem it Solves
=================
Many users struggle to organize useful web resources and discover relevant content efficiently. Rango solves this by:

Structuring web content into user-defined categories

Tracking popularity through views and likes

Allowing social interaction via profiles and chat

Enhancing discovery with search suggestions and external APIs

It also serves as a real-world learning project for Django developers.

Features
========
User registration and authentication (django-registration-redux)

User profile creation and updates

Category and page management

Like system for categories

Page view tracking

AJAX-based category and page suggestions

External search integration (Bing Search API)

Real-time user chat system

Session tracking with visitor analytics

Auto logout on inactivity

Secure access control using Django decorators

Tech Stack
===========
Backend: Django (Python)

Frontend: HTML, CSS, JavaScript, AJAX

Database: SQLite (default) / MySQL (optional)

Authentication: Django Auth, django-registration-redux

APIs: Bing Search API

Other Tools: Django Sessions, JSON, Requests

Security Measures
=================
CSRF protection enabled

Login-required access control for protected views

Secure password hashing (Django default)

Session expiration & auto logout

Input validation via Django forms

Environment variables for sensitive keys (API keys, secrets)

Screenshots / Demo
==================

Home page

Category page

Profile page

Chat interface

Login/Register pages

<img width="960" height="540" alt="Annotation 2024-10-03 223122" src="https://github.com/user-attachments/assets/88403f93-b33b-44a6-a193-c07ae0eff14d" />
<img width="960" height="540" alt="Annotation 2024-10-03 223150" src="https://github.com/user-attachments/assets/e50365ce-224a-4268-893f-537f6bf6fb6e" />
<img width="960" height="540" alt="Annotation 2024-10-03 223208" src="https://github.com/user-attachments/assets/1afead76-2ab7-4b41-9cee-96c06ba23836" />
<img width="960" height="540" alt="Annotation 2024-10-03 223230" src="https://github.com/user-attachments/assets/6193fb1d-90b1-41e5-a2e7-3d26b14a967d" />
<img width="960" height="540" alt="Annotation 2024-10-03 223250" src="https://github.com/user-attachments/assets/15c1df4c-25aa-4545-94bd-c0a04df753cf" />
<img width="960" height="540" alt="Annotation 2024-10-03 223337" src="https://github.com/user-attachments/assets/822384c8-a8b1-42ae-a16c-833c68ac1a8b" />
<img width="960" height="540" alt="Annotation 2024-10-03 223356" src="https://github.com/user-attachments/assets/1b7ee4d0-0a8f-423f-aa5a-50f6bec184ed" />
<img width="960" height="540" alt="Annotation 2024-10-03 223424" src="https://github.com/user-attachments/assets/86752d8f-41ae-425f-87f6-55706cccb049" />
<img width="960" height="540" alt="Annotation 2024-10-03 223443" src="https://github.com/user-attachments/assets/9a1db3df-bafe-4bb0-9f85-96646b3c6f25" />
<img width="960" height="540" alt="Annotation 2024-10-03 223503" src="https://github.com/user-attachments/assets/d3f94f99-0fd3-4661-a669-aaeafce92587" />
<img width="960" height="540" alt="Annotation 2024-10-03 223557" src="https://github.com/user-attachments/assets/ec3ad1c9-19ad-4046-a066-c7f171b79914" />
<img width="960" height="540" alt="Annotation 2024-10-03 223631" src="https://github.com/user-attachments/assets/48bc6e1d-1831-4e93-91aa-76005086649c" />
<img width="960" height="540" alt="Annotation 2024-10-03 223726" src="https://github.com/user-attachments/assets/fa3456e6-7bf3-4766-bd03-8ebad231a864" />
<img width="960" height="540" alt="Annotation 2024-10-03 223802" src="https://github.com/user-attachments/assets/9dc2c5e4-fdae-499d-b482-7b5f768686ff" />
<img width="960" height="540" alt="Annotation 2024-10-03 223832" src="https://github.com/user-attachments/assets/af101fa4-d868-4b8d-919d-cb1c584fff26" />
<img width="960" height="540" alt="Annotation 2024-10-03 223906" src="https://github.com/user-attachments/assets/306d8fd9-3e47-4a59-9388-34f9f2959565" />
<img width="960" height="540" alt="Annotation 2024-10-03 224008" src="https://github.com/user-attachments/assets/939aa173-d52c-480c-addf-bc87e5427776" />
<img width="960" height="540" alt="Annotation 2024-10-03 224114" src="https://github.com/user-attachments/assets/4163b342-c417-4238-bf45-2494defa6805" />
<img width="960" height="540" alt="Annotation 2024-10-03 224139" src="https://github.com/user-attachments/assets/127a9774-f73d-405d-a88f-27274e360263" />

Installation
============
1. Clone the Repository
git clone https://github.com/Charliee142/rango.git
cd rango
2. Create a Virtual Environment
python -m venv myenv
myenv\Scripts\activate  # Windows
3. Install Dependencies
pip install -r requirements.txt
4 Configure Environment Variables

Create a .env file:

SECRET_KEY=your_secret_key
DEBUG=True
BING_API_KEY=your_bing_api_key
5. Run Migrations
python manage.py migrate
6. Create Superuser
python manage.py createsuperuser
Run the Server
7. python manage.py runserver


Visit: http://127.0.0.1:8000/

What I Learned
==============
Building scalable Django applications

User authentication and session management

AJAX and asynchronous requests

Third-party API integration

Secure application design

Structuring Django projects professionally

Debugging real-world Django issues

Writing production-ready code and documentation
