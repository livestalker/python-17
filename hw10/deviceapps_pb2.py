# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: deviceapps.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='deviceapps.proto',
  package='',
  serialized_pb=_b('\n\x10\x64\x65viceapps.proto\"|\n\nDeviceApps\x12\"\n\x06\x64\x65vice\x18\x01 \x01(\x0b\x32\x12.DeviceApps.Device\x12\x0c\n\x04\x61pps\x18\x02 \x03(\r\x12\x0b\n\x03lat\x18\x03 \x01(\x01\x12\x0b\n\x03lon\x18\x04 \x01(\x01\x1a\"\n\x06\x44\x65vice\x12\n\n\x02id\x18\x01 \x01(\x0c\x12\x0c\n\x04type\x18\x02 \x01(\x0c')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_DEVICEAPPS_DEVICE = _descriptor.Descriptor(
  name='Device',
  full_name='DeviceApps.Device',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='DeviceApps.Device.id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='DeviceApps.Device.type', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=110,
  serialized_end=144,
)

_DEVICEAPPS = _descriptor.Descriptor(
  name='DeviceApps',
  full_name='DeviceApps',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='device', full_name='DeviceApps.device', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='apps', full_name='DeviceApps.apps', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lat', full_name='DeviceApps.lat', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lon', full_name='DeviceApps.lon', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_DEVICEAPPS_DEVICE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=144,
)

_DEVICEAPPS_DEVICE.containing_type = _DEVICEAPPS
_DEVICEAPPS.fields_by_name['device'].message_type = _DEVICEAPPS_DEVICE
DESCRIPTOR.message_types_by_name['DeviceApps'] = _DEVICEAPPS

DeviceApps = _reflection.GeneratedProtocolMessageType('DeviceApps', (_message.Message,), dict(

  Device = _reflection.GeneratedProtocolMessageType('Device', (_message.Message,), dict(
    DESCRIPTOR = _DEVICEAPPS_DEVICE,
    __module__ = 'deviceapps_pb2'
    # @@protoc_insertion_point(class_scope:DeviceApps.Device)
    ))
  ,
  DESCRIPTOR = _DEVICEAPPS,
  __module__ = 'deviceapps_pb2'
  # @@protoc_insertion_point(class_scope:DeviceApps)
  ))
_sym_db.RegisterMessage(DeviceApps)
_sym_db.RegisterMessage(DeviceApps.Device)


# @@protoc_insertion_point(module_scope)
