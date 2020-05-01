from djangourls import path
from . import views

urlpaterns = [
	path('', checkout, name='checkout')
]