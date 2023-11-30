# eCAL requirement
import sys
import time

import ecal.core.core as ecal_core
from ecal.core.subscriber import ProtoSubscriber

import proto_struct.vss_data_pb2 as vss_data_pb2

# KUKSA requirement
from kuksa_client.grpc import VSSClient
from kuksa_client.grpc import Datapoint


ecal_core.initialize(sys.argv, "Python Protobuf")

sub = ProtoSubscriber("vss_data_python_protobuf_topic_2", vss_data_pb2.VssData)

def callback(topic_name, vss_data_proto_msg, time):
  with VSSClient('127.0.0.1', 55555) as client:
    client.set_current_values({
    vss_data_proto_msg.vss_code: Datapoint(vss_data_proto_msg.data),
    })
    
    print("feed {}".format(vss_data_proto_msg.vss_code))

sub.set_callback(callback)

while ecal_core.ok():
  time.sleep(1)

ecal_core.finalize()
