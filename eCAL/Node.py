import sys
import time

import ecal.core.core as ecal_core
from ecal.core.subscriber import ProtoSubscriber
from ecal.core.publisher import ProtoPublisher

import proto_struct.vss_data_pb2 as vss_data_pb2


ecal_core.initialize(sys.argv, "Python Protobuf")

sub = ProtoSubscriber("vss_data_python_protobuf_topic_1", vss_data_pb2.VssData)
pub = ProtoPublisher("vss_data_python_protobuf_topic_2", vss_data_pb2.VssData)

def callback(topic_name, vss_data_proto_msg, time):
  protobuf_message = vss_data_pb2.VssData()
  protobuf_message.vss_code = vss_data_proto_msg.vss_code
  protobuf_message.data = vss_data_proto_msg.data

  pub.send(protobuf_message)
  # pub.send(vss_data_proto_msg)
  print("sub and pub")

sub.set_callback(callback)  

while ecal_core.ok():
  time.sleep(1)

ecal_core.finalize()
