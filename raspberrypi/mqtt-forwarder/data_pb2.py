# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: data.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='data.proto',
  package='pb',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=b'\n\ndata.proto\x12\x02pb\"{\n\x0bWeatherData\x12\x10\n\x08\x64\x65viceId\x18\x01 \x02(\x05\x12\x13\n\x0btemperature\x18\x02 \x02(\x02\x12\x10\n\x08humidity\x18\x03 \x02(\x02\x12\x10\n\x08pressure\x18\x04 \x02(\x02\x12\x0b\n\x03IAQ\x18\x05 \x02(\x02\x12\x14\n\x0ciaq_accuracy\x18\x06 \x02(\x05'
)




_WEATHERDATA = _descriptor.Descriptor(
  name='WeatherData',
  full_name='pb.WeatherData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='deviceId', full_name='pb.WeatherData.deviceId', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='temperature', full_name='pb.WeatherData.temperature', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='humidity', full_name='pb.WeatherData.humidity', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pressure', full_name='pb.WeatherData.pressure', index=3,
      number=4, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='IAQ', full_name='pb.WeatherData.IAQ', index=4,
      number=5, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='iaq_accuracy', full_name='pb.WeatherData.iaq_accuracy', index=5,
      number=6, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=141,
)

DESCRIPTOR.message_types_by_name['WeatherData'] = _WEATHERDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WeatherData = _reflection.GeneratedProtocolMessageType('WeatherData', (_message.Message,), {
  'DESCRIPTOR' : _WEATHERDATA,
  '__module__' : 'data_pb2'
  # @@protoc_insertion_point(class_scope:pb.WeatherData)
  })
_sym_db.RegisterMessage(WeatherData)


# @@protoc_insertion_point(module_scope)