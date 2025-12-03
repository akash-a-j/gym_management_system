import os
import django
import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project1.settings')
django.setup()

from authapp.models import Attendance, Gallery, Trainer, Enrollment, Contact, MembershipPlan

print("Testing Attendance instantiation...")
try:
    a = Attendance(phonenumber="123", Login="10:00", Logout="11:00")
    print("Attendance OK")
except Exception as e:
    print(f"Attendance FAILED: {e}")

print("\nTesting Gallery instantiation...")
try:
    g = Gallery(title="Test", img="test.jpg")
    print("Gallery OK")
except Exception as e:
    print(f"Gallery FAILED: {e}")

print("\nTesting Trainer instantiation...")
try:
    t = Trainer(name="Test", gender="M", email="t@t.com")
    print("Trainer OK")
except Exception as e:
    print(f"Trainer FAILED: {e}")

print("\nTesting Enrollment instantiation...")
try:
    e = Enrollment(FullName="Test", Email="t@t.com", PhoneNumber="123")
    print("Enrollment OK")
except Exception as e:
    print(f"Enrollment FAILED: {e}")

print("\nTesting Contact instantiation...")
try:
    c = Contact(name="Test", email="t@t.com", phonenumber="123", description="desc")
    print("Contact OK")
except Exception as e:
    print(f"Contact FAILED: {e}")

print("\nTesting MembershipPlan instantiation...")
try:
    m = MembershipPlan(plan="Basic", price=100, description="desc")
    print("MembershipPlan OK")
except Exception as e:
    print(f"MembershipPlan FAILED: {e}")
