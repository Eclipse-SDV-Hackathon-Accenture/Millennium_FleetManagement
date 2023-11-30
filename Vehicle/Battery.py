import sys
import time

import ecal.core.core as ecal_core
from ecal.core.publisher import ProtoPublisher

import proto_struct.vss_data_pb2 as vss_data_pb2

from piracer.vehicles import PiRacerStandard

piracer = PiRacerStandard()

ecal_core.initialize(sys.argv, "Python Protobuf")

pub = ProtoPublisher("vss_data_python_protobuf_topic_1", vss_data_pb2.VssData)

while ecal_core.ok():
    voltage = piracer.get_battery_voltage()
    battery = int((voltage - 2.8 * 3.0) / (12.3 - 2.8 * 3.0) * 100.0)

    if battery > 100:
        battery = 100
    elif battery < 0:
        battery = 0

    protobuf_message = vss_data_pb2.VssData()
    protobuf_message.vss_code = "Vehicle.Powertrain.TractionBattery.StateOfCharge.Current"
    protobuf_message.data = battery

    print("battery")

    pub.send(protobuf_message)
      
    time.sleep(1)

ecal_core.finalize()

