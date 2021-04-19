from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Equipment
from .serializers import EquipmentSerializer

#****************************** Only Employee ******************************

# returns all the equipments
@api_view(['GET'])
def equipments_list_employee(request):
    equipments = Equipment.objects.all().values('id', 'name')
    return Response(equipments)
    
# issue an equipment with pk
@api_view(['GET'])
def equipment_issue_employee(request, pk):
    try:
        equipment = Equipment.objects.get(pk=pk)
    except Equipment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if(equipment.issued):
        return Response({'notification':'[X]Already issued! Kindly submit a request to access.'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        equipment.issued = True
        equipment.save()
        message = equipment.name + ' issued Successfully!'
        return Response({'notification' : message})


# This code could have been accomodated in the 'equipment_issue()' view but this
# is not being done. The reason to this is, in future I might allow authentication
# and this may complicate the process of returning and issuing an equipment.
# Thus, the code is written in that way.

# return the equipment with pk
@api_view(['GET'])
def equipment_return_employee(request, pk):
    try:
        equipment = Equipment.objects.get(pk=pk)
    except Equipment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if(equipment.issued):
        equipment.issued = False
        equipment.save()
        message = equipment.name + ' returned Successfully!'
        return Response({'notification' : message})
    else:
        return Response({'notification':'[X]Cannot return an equipment you never issued!'}, status=status.HTTP_400_BAD_REQUEST)

# make request to access to the equipment with pk
@api_view(['GET'])
def equipment_request_access_employee(request, pk):
    try:
        equipment = Equipment.objects.get(pk=pk)
    except Equipment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if(equipment.issued):
        equipment.requests += 1
        equipment.save()
        return Response({'notification': f"Successfully submitted request to access {equipment.name}"})
    else:
        return Response({'notification' : f"[X]The '{equipment.name}' is not issued to anyone! No need to request for accessing it."}, status=status.HTTP_400_BAD_REQUEST)


#*****************************************************************************


#****************************** Only Manager *********************************

# returns a lits of available equipments
@api_view(['GET'])
def equipments_available_manager(request):
    available_equipments = Equipment.objects.filter(issued=False)
    available_equipments = [EquipmentSerializer(item).data for item in available_equipments]
    if not available_equipments:
        return Response({'notification': 'No equipment is available right now.'})
    else:
        return Response(available_equipments)
    
# returns a list of issued equipments
@api_view(['GET'])
def equipments_issued_manager(request):
    issued_equipments = Equipment.objects.filter(issued=True)
    issued_equipments = [EquipmentSerializer(item).data for item in issued_equipments]
    if not issued_equipments:
        return Response({'notification': 'No equipment is issued right now.'})
    else:
        return Response(issued_equipments)

# returns a list of access-requests made till now for all the equipments
@api_view(['GET'])
def requests_list_view_manager(request):
    equipments = Equipment.objects.all().values('id','name','requests')
    if not equipments:
        return Response({'notification': 'No equipments in the database'})
    else:
        return Response(equipments)

#****************************************************************************