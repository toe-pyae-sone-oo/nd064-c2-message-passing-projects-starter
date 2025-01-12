# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: udaconnect.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='udaconnect.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10udaconnect.proto\"l\n\x0fLocationMessage\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x11\n\tperson_id\x18\x02 \x01(\x03\x12\x11\n\tlongitude\x18\x03 \x01(\t\x12\x10\n\x08latitude\x18\x04 \x01(\t\x12\x15\n\rcreation_time\x18\x05 \x01(\x03\":\n\x15\x43reateLocationRequest\x12!\n\x07payload\x18\x01 \x01(\x0b\x32\x10.LocationMessage\"\x18\n\x16\x43reateLocationResponse2E\n\x08Location\x12\x39\n\x06\x43reate\x12\x16.CreateLocationRequest\x1a\x17.CreateLocationResponseb\x06proto3'
)




_LOCATIONMESSAGE = _descriptor.Descriptor(
  name='LocationMessage',
  full_name='LocationMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='LocationMessage.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='person_id', full_name='LocationMessage.person_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='LocationMessage.longitude', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='LocationMessage.latitude', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='creation_time', full_name='LocationMessage.creation_time', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=128,
)


_CREATELOCATIONREQUEST = _descriptor.Descriptor(
  name='CreateLocationRequest',
  full_name='CreateLocationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='payload', full_name='CreateLocationRequest.payload', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=130,
  serialized_end=188,
)


_CREATELOCATIONRESPONSE = _descriptor.Descriptor(
  name='CreateLocationResponse',
  full_name='CreateLocationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=190,
  serialized_end=214,
)

_CREATELOCATIONREQUEST.fields_by_name['payload'].message_type = _LOCATIONMESSAGE
DESCRIPTOR.message_types_by_name['LocationMessage'] = _LOCATIONMESSAGE
DESCRIPTOR.message_types_by_name['CreateLocationRequest'] = _CREATELOCATIONREQUEST
DESCRIPTOR.message_types_by_name['CreateLocationResponse'] = _CREATELOCATIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LocationMessage = _reflection.GeneratedProtocolMessageType('LocationMessage', (_message.Message,), {
  'DESCRIPTOR' : _LOCATIONMESSAGE,
  '__module__' : 'udaconnect_pb2'
  # @@protoc_insertion_point(class_scope:LocationMessage)
  })
_sym_db.RegisterMessage(LocationMessage)

CreateLocationRequest = _reflection.GeneratedProtocolMessageType('CreateLocationRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATELOCATIONREQUEST,
  '__module__' : 'udaconnect_pb2'
  # @@protoc_insertion_point(class_scope:CreateLocationRequest)
  })
_sym_db.RegisterMessage(CreateLocationRequest)

CreateLocationResponse = _reflection.GeneratedProtocolMessageType('CreateLocationResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATELOCATIONRESPONSE,
  '__module__' : 'udaconnect_pb2'
  # @@protoc_insertion_point(class_scope:CreateLocationResponse)
  })
_sym_db.RegisterMessage(CreateLocationResponse)



_LOCATION = _descriptor.ServiceDescriptor(
  name='Location',
  full_name='Location',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=216,
  serialized_end=285,
  methods=[
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='Location.Create',
    index=0,
    containing_service=None,
    input_type=_CREATELOCATIONREQUEST,
    output_type=_CREATELOCATIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_LOCATION)

DESCRIPTOR.services_by_name['Location'] = _LOCATION

# @@protoc_insertion_point(module_scope)
