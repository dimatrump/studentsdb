# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

# Views for students

def students_list(request):
	students = (
		{
		'id': 1,
		'first_name': u'Дмитро',
		'last_name': u'Дяченко',
		'ticket': 10,
		'image': 'img/dima.jpg'},
		{
		'id': 2,
		'first_name': u'Анатолій',
		'last_name': u'Кустливий',
		'ticket': 16,
		'image': 'img/tolia.jpg'},
		{
		'id': 3,
		'first_name': u'Микола',
		'last_name': u'Кустливий',
		'ticket': 17,
		'image': 'img/kolia.jpg'},
		)
	return render(request, 'students/students_list.html', {'students': students})

def students_add(request):
	return HttpResponse('<h1>Student add form</h1>')

def students_edit(request, sid):
	return HttpResponse('<h1>Edit Student %s</h1>' % sid) 
	
def students_delete(request, sid):
	return HttpResponse('<h1>Student Delete %s</h1>' % sid)

# Views for groups

def groups_list(request):
	return HttpResponse('<h1>Groups List</h1>')
	
def groups_add(request):
	return HttpResponse('<h1>Add Group Form</h1>')
	
def groups_edit(request, gid):
	return HttpResponse('<h1>Edit Group %s</h1>' % gid)
	
def groups_delete(request, gid):
	return HttpResponse('<h1>Delete Group %s</h1>' % gid)
