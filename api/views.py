from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Note
from .serializers import NoteSerializer
from .utils import updateNote, getNoteDetail, deleteNote, getNotesList, createNote

# Create your views here.

# /notes GET
# /notes POST
# /notes/<id> GET
# /notes/<id> PUT
# /notes/<id> DELETE

# mentioning the type of the request
@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]

    return Response(routes) # safe = False -> to return more data than the python dictionary

@api_view(['GET', 'POST'])
def getNotes(request):

    if request.method == 'GET':
        return getNotesList(request)

    if request.method == 'POST':
        return createNote(request)


@api_view(['GET', 'PUT', 'DELETE'])
def getNote(request, pk):

    if request.method == 'GET':
        return getNoteDetail(request, pk)

    if request.method == 'PUT':
        return updateNote(request, pk)

    if request.method == 'DELETE':
        return deleteNote(request, pk)

# @api_view(['GET'])
# def getNotes(request):
#     # these are the python objects, we need to convert them into json, so we have to create serializers
#     notes = Note.objects.all().order_by('-updated') # order the tasks by the increasing timestamp
#     serializer = NoteSerializer(notes, many=True) # serialize multiple fields
#     return Response(serializer.data)

# @api_view(['GET'])
# def getNote(request, pk): # pk = primary key, input params
#     # these are the python objects, we need to convert them into json, so we have to create serializers
#     note = Note.objects.get(id=pk) 
#     serializer = NoteSerializer(note, many=False) # serialize single field
#     return Response(serializer.data)

# @api_view(['POST'])
# def createNote(request):
#     data = request.data
#     note = Note.objects.create(
#         body=data['body'] # created and updated fields will be populated themselves
#     )
#     serializer = NoteSerializer(note, many=False)
#     return Response(serializer.data)


# @api_view(['PUT'])
# def updateNote(request, pk):
#     data = request.data # gives the json data
#     note = Note.objects.get(id=pk)
#     serializer = NoteSerializer(instance = note, data=data)
    
#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)


# @api_view(['DELETE'])
# def deleteNote(request,pk):
#     note = Note.objects.get(id=pk)
#     note.delete()
#     return Response('Note was deleted!')