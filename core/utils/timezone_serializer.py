def timezone_serializer(tz_obj):
    return tz_obj.isoformat(timespec='milliseconds').replace('+00:00', 'Z')