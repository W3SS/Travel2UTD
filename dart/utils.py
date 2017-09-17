from . import models
import json

def get_bus(bus_id):
    return models.Bus.objects.get(id=bus_id)

def get_buses():
    return models.Bus.objects.all()

def get_bus_location(bus_id):
    bus = get_bus(bus_id)
    return (bus.latitude , bus.longitude)

def get_all_bus_location():
    buses = get_buses()
    result = []
    for bus in buses:
        result.append({'id':bus.id,'latitude': str(bus.latitude),'longitude':str(bus.longitude),
                       'last_updated_at':str(bus.timestamp)})
    return json.dumps(result)

def update_bus_location(bus_id, latitude, longitude,timestamp):
    bus = get_bus(bus_id)
    bus.latitude=latitude
    bus.longitude=longitude
    bus.timestamp=timestamp
    bus.save()

def register_bus(bus_number, latitude, longitude, timestamp):
    if len(models.Bus.objects.filter(id=bus_number)) > 0:
        return False
    bus = models.Bus(id=bus_number, latitude=latitude, longitude=longitude, timestamp=timestamp)
    bus.save()
    return True

def delete_bus(bus_id):
    bus = models.Bus.objects.filter(id=bus_id)
    bus.delete()