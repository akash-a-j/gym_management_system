import os
import sys
from pathlib import Path

# Ensure project root is on sys.path so `project1` package can be imported
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

os.environ.setdefault('DJANGO_SETTINGS_MODULE','project1.settings')
import django
django.setup()
from django.test import Client
from django.contrib.auth.models import User

c = Client()

username = '9999999999'
# Cleanup existing test user
User.objects.filter(username=username).delete()

print('GET /signup/')
r = c.get('/signup/')
print('status', r.status_code)

print('POST /signup/')
r = c.post('/signup/', {'usernumber': username, 'email':'testuser@example.com','pass1':'password123','pass2':'password123'})
print('status', r.status_code, 'redirect_to:', getattr(r, 'url', None))

print('POST /login/')
r2 = c.post('/login/', {'usernumber': username, 'pass1':'password123'})
print('status', r2.status_code, 'redirect_to:', getattr(r2, 'url', None))

print('GET /join/ with logged-in client')
r4 = c.get('/join/')
print('status', r4.status_code)
print('content snippet length:', len(r4.content))

print('GET /attendance/ with logged-in client')
r5 = c.get('/attendance/')
print('status', r5.status_code)

print('GET /profile/ with logged-in client')
r6 = c.get('/profile/')
print('status', r6.status_code)

# Attempt an enroll POST (requires logged in user)
print('POST /join/ (enroll)')
post_data = {
	'FullName': 'Test User',
	'email': 'testuser@example.com',
	'gender': 'Male',
	'PhoneNumber': username,
	'DOB': '1990-01-01',
	'member': 'Basic - 100',
	'trainer': '',
	'reference': '',
	'address': 'Test Address'
}
r7 = c.post('/join/', post_data)
print('status', r7.status_code, 'redirect_to:', getattr(r7, 'url', None))
