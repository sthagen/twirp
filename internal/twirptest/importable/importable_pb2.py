# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: importable.proto

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
  name='importable.proto',
  package='twirp.internal.twirptest.importable',
  syntax='proto3',
  serialized_pb=_b('\n\x10importable.proto\x12#twirp.internal.twirptest.importable\"\x05\n\x03Msg2a\n\x03Svc\x12Z\n\x04Send\x12(.twirp.internal.twirptest.importable.Msg\x1a(.twirp.internal.twirptest.importable.MsgB\x0cZ\nimportableb\x06proto3')
)




_MSG = _descriptor.Descriptor(
  name='Msg',
  full_name='twirp.internal.twirptest.importable.Msg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=57,
  serialized_end=62,
)

DESCRIPTOR.message_types_by_name['Msg'] = _MSG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Msg = _reflection.GeneratedProtocolMessageType('Msg', (_message.Message,), dict(
  DESCRIPTOR = _MSG,
  __module__ = 'importable_pb2'
  # @@protoc_insertion_point(class_scope:twirp.internal.twirptest.importable.Msg)
  ))
_sym_db.RegisterMessage(Msg)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z\nimportable'))

_SVC = _descriptor.ServiceDescriptor(
  name='Svc',
  full_name='twirp.internal.twirptest.importable.Svc',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=64,
  serialized_end=161,
  methods=[
  _descriptor.MethodDescriptor(
    name='Send',
    full_name='twirp.internal.twirptest.importable.Svc.Send',
    index=0,
    containing_service=None,
    input_type=_MSG,
    output_type=_MSG,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SVC)

DESCRIPTOR.services_by_name['Svc'] = _SVC

# @@protoc_insertion_point(module_scope)
