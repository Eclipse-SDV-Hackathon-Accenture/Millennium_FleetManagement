import sys
import time

import ecal.core.core as ecal_core
from ecal.core.publisher import ProtoPublisher

import proto_struct.vss_data_pb2 as vss_data_pb2

from piracer.vehicles import PiRacerStandard
from piracer.gamepads import ShanWanGamepad

ecal_core.initialize(sys.argv, "Python Protobuf")

pub = ProtoPublisher("vss_data_python_protobuf_topic_1", vss_data_pb2.VssData)

piracer = PiRacerStandard()
shanwan_gamepad = ShanWanGamepad()

while ecal_core.ok():
    gamepad_input = shanwan_gamepad.read_data()

    throttle = gamepad_input.analog_stick_right.y * 0.5
    steering = -gamepad_input.analog_stick_left.x
    if steering > 0.9:
        steering = 0.9
    elif steering < -0.9:
        steering = -0.9

    piracer.set_throttle_percent(throttle)
    piracer.set_steering_percent(steering)

    throttle = throttle * 100.0
    protobuf_message = vss_data_pb2.VssData()
    protobuf_message.vss_code = "Vehicle.Speed"
    protobuf_message.data = throttle
    pub.send(protobuf_message)
    
    steering = steering * 20.0
    protobuf_message = vss_data_pb2.VssData()
    protobuf_message.vss_code = "Vehicle.Chassis.SteeringWheel.Angle"
    protobuf_message.data = steering
    pub.send(protobuf_message)

    print("speed : {:.2f} steering : {:.2f}".format(throttle, steering))

ecal_core.finalize()
