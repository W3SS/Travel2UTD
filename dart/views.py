import os
from django.http import HttpResponse
from . import utils
from django.template import loader
from django.views.generic import TemplateView
# Create your views here.


def open_html(relative_file_path):
    cwd = os.path.dirname(__file__)
    html_file_path = relative_file_path
    html_file = os.path.join(cwd, html_file_path)
    print(html_file)
    return open(html_file, 'r')

def index (request):
    template = loader.get_template('dart/index.html')
    return HttpResponse(template.render(None, request))

def driver (request):
    template = loader.get_template('dart/driver.html')
    return HttpResponse(template.render(None, request))

def return_error(message):
    response = HttpResponse(message)
    response.status_code = 500
    return response

# def location(request,bus_id):
#     if request.method == 'GET':
#         if bus_id == None:
#             return HttpResponse("Incorrect URL format")
#         else:
#             bus_location = utils.get_bus_location(bus_id)
#             return HttpResponse(str(bus_location[0]) + " , " + str(bus_location[1]))
#     elif request.method == 'PUT':
#         bus_id = request.POST['id']
#         latitude = request.POST['latitude']
#         longitude = request.POST['longitude']
#         timestamp = request.POST['timestamp']
#         utils.update_bus_location(bus_id, latitude, longitude, timestamp)
#         return HttpResponse("Success")
#     else:
#         return HttpResponse("Invalid URL")

def set_bus_location(request,bus_id):
    if request.method == 'POST':
        print(request.body)
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        timestamp = request.POST.get('timestamp')
        utils.update_bus_location(bus_id,latitude,longitude,timestamp)
        return HttpResponse("Success")
    else:
        return return_error("Invalid URL")

def get_bus_location(request, bus_id):
    if request.method == 'GET':
        bus_location = utils.get_bus_location(bus_id)
        return HttpResponse(str(bus_location[0])+" , "+str(bus_location[1]))
    else:
        return return_error("Invalid URL")

def get_all_bus_location(request):
    return HttpResponse(utils.get_all_bus_location())

def register_bus(request):
    if request.method == 'POST':
        bus_number = request.POST.get('id')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        timestamp= request.POST.get('timestamp')
        if utils.register_bus(bus_number,latitude,longitude,timestamp):
            return HttpResponse("Success")
        else:
            return return_error("Error! Bus number already exists.")
    else:
        return return_error("Invalid URL")

def delete_bus(request, bus_id):
    if request.method == 'DELETE':
        utils.delete_bus(bus_id)
        return HttpResponse("Success")
    else:
        return return_error("Invalid URL")