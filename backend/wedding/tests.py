from django.test import TestCase, Client

c = Client(enforce_csrf_checks=True)

response = c.get('/csrf/', {})
print(response.data)


