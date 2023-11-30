from kuksa_client.grpc import VSSClient

with VSSClient('127.0.0.1', 55555) as client:
    for updates in client.subscribe_current_values([
        'Vehicle.Speed',
        'Vehicle.Acceleration.Longitudinal',
    ]):
        if 'Vehicle.Speed' in updates and type(updates['Vehicle.Speed']) != type(None):
            speed = updates['Vehicle.Speed'].value
            print(f"Received updated speed: {speed}")

        if 'Vehicle.Acceleration.Longitudinal' in updates and type(updates['Vehicle.Acceleration.Longitudinal']) != type(None):
            acceleration = updates['Vehicle.Acceleration.Longitudinal'].value
            print(f"Received updated acceleration: {acceleration}")
        