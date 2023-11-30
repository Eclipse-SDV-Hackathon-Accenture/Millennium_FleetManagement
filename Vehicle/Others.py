import sys
import time

import ecal.core.core as ecal_core
from ecal.core.publisher import ProtoPublisher

import proto_struct.vss_data_pb2 as vss_data_pb2

ecal_core.initialize(sys.argv, "Python Protobuf")

pub = ProtoPublisher("vss_data_python_protobuf_topic_1", vss_data_pb2.VssData)

while ecal_core.ok():
    protobuf_message = vss_data_pb2.VssData()
    protobuf_message.vss_code = "Vehicle.Powertrain.ElectricMotor.Temperature"
    protobuf_message.data = 80
    pub.send(protobuf_message)
    time.sleep(1)
    
    protobuf_message = vss_data_pb2.VssData()
    protobuf_message.vss_code = "Vehicle.Cabin.HVAC.IsAirConditioningActive"
    protobuf_message.data = 1
    pub.send(protobuf_message)
    time.sleep(1)
    
    protobuf_message = vss_data_pb2.VssData()
    protobuf_message.vss_code = "Vehicle.Cabin.Door.Row1.Left.Window.Position"
    protobuf_message.data = 30
    pub.send(protobuf_message)
    time.sleep(1)

    break

ecal_core.finalize()

