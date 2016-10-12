# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: services.proto

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
  name='services.proto',
  package='services',
  syntax='proto3',
  serialized_pb=_b('\n\x0eservices.proto\x12\x08services\"\r\n\x0b\x43odeRequest\"\x1c\n\x0c\x43odeResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\"\x0f\n\rStatusRequest\" \n\x0eStatusResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\">\n\tAttendant\x12\x11\n\tfirstName\x18\x01 \x01(\t\x12\x10\n\x08lastName\x18\x02 \x01(\t\x12\x0c\n\x04\x63ode\x18\x03 \x01(\t\"\x84\x01\n\x07\x41ppData\x12\x0f\n\x07\x63ounter\x18\x01 \x01(\x05\x12\x35\n\nattendants\x18\x02 \x03(\x0b\x32!.services.AppData.AttendantsEntry\x1a\x31\n\x0f\x41ttendantsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x32\x8f\x01\n\x0fRegisterService\x12@\n\tGetStatus\x12\x17.services.StatusRequest\x1a\x18.services.StatusResponse\"\x00\x12:\n\x07GetCode\x12\x15.services.CodeRequest\x1a\x16.services.CodeResponse\"\x00\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CODEREQUEST = _descriptor.Descriptor(
  name='CodeRequest',
  full_name='services.CodeRequest',
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
  serialized_start=28,
  serialized_end=41,
)


_CODERESPONSE = _descriptor.Descriptor(
  name='CodeResponse',
  full_name='services.CodeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='services.CodeResponse.code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=43,
  serialized_end=71,
)


_STATUSREQUEST = _descriptor.Descriptor(
  name='StatusRequest',
  full_name='services.StatusRequest',
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
  serialized_start=73,
  serialized_end=88,
)


_STATUSRESPONSE = _descriptor.Descriptor(
  name='StatusResponse',
  full_name='services.StatusResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='services.StatusResponse.status', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=90,
  serialized_end=122,
)


_ATTENDANT = _descriptor.Descriptor(
  name='Attendant',
  full_name='services.Attendant',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='firstName', full_name='services.Attendant.firstName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lastName', full_name='services.Attendant.lastName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='code', full_name='services.Attendant.code', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=124,
  serialized_end=186,
)


_APPDATA_ATTENDANTSENTRY = _descriptor.Descriptor(
  name='AttendantsEntry',
  full_name='services.AppData.AttendantsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='services.AppData.AttendantsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='services.AppData.AttendantsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=272,
  serialized_end=321,
)

_APPDATA = _descriptor.Descriptor(
  name='AppData',
  full_name='services.AppData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='counter', full_name='services.AppData.counter', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attendants', full_name='services.AppData.attendants', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_APPDATA_ATTENDANTSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=189,
  serialized_end=321,
)

_APPDATA_ATTENDANTSENTRY.containing_type = _APPDATA
_APPDATA.fields_by_name['attendants'].message_type = _APPDATA_ATTENDANTSENTRY
DESCRIPTOR.message_types_by_name['CodeRequest'] = _CODEREQUEST
DESCRIPTOR.message_types_by_name['CodeResponse'] = _CODERESPONSE
DESCRIPTOR.message_types_by_name['StatusRequest'] = _STATUSREQUEST
DESCRIPTOR.message_types_by_name['StatusResponse'] = _STATUSRESPONSE
DESCRIPTOR.message_types_by_name['Attendant'] = _ATTENDANT
DESCRIPTOR.message_types_by_name['AppData'] = _APPDATA

CodeRequest = _reflection.GeneratedProtocolMessageType('CodeRequest', (_message.Message,), dict(
  DESCRIPTOR = _CODEREQUEST,
  __module__ = 'services_pb2'
  # @@protoc_insertion_point(class_scope:services.CodeRequest)
  ))
_sym_db.RegisterMessage(CodeRequest)

CodeResponse = _reflection.GeneratedProtocolMessageType('CodeResponse', (_message.Message,), dict(
  DESCRIPTOR = _CODERESPONSE,
  __module__ = 'services_pb2'
  # @@protoc_insertion_point(class_scope:services.CodeResponse)
  ))
_sym_db.RegisterMessage(CodeResponse)

StatusRequest = _reflection.GeneratedProtocolMessageType('StatusRequest', (_message.Message,), dict(
  DESCRIPTOR = _STATUSREQUEST,
  __module__ = 'services_pb2'
  # @@protoc_insertion_point(class_scope:services.StatusRequest)
  ))
_sym_db.RegisterMessage(StatusRequest)

StatusResponse = _reflection.GeneratedProtocolMessageType('StatusResponse', (_message.Message,), dict(
  DESCRIPTOR = _STATUSRESPONSE,
  __module__ = 'services_pb2'
  # @@protoc_insertion_point(class_scope:services.StatusResponse)
  ))
_sym_db.RegisterMessage(StatusResponse)

Attendant = _reflection.GeneratedProtocolMessageType('Attendant', (_message.Message,), dict(
  DESCRIPTOR = _ATTENDANT,
  __module__ = 'services_pb2'
  # @@protoc_insertion_point(class_scope:services.Attendant)
  ))
_sym_db.RegisterMessage(Attendant)

AppData = _reflection.GeneratedProtocolMessageType('AppData', (_message.Message,), dict(

  AttendantsEntry = _reflection.GeneratedProtocolMessageType('AttendantsEntry', (_message.Message,), dict(
    DESCRIPTOR = _APPDATA_ATTENDANTSENTRY,
    __module__ = 'services_pb2'
    # @@protoc_insertion_point(class_scope:services.AppData.AttendantsEntry)
    ))
  ,
  DESCRIPTOR = _APPDATA,
  __module__ = 'services_pb2'
  # @@protoc_insertion_point(class_scope:services.AppData)
  ))
_sym_db.RegisterMessage(AppData)
_sym_db.RegisterMessage(AppData.AttendantsEntry)


_APPDATA_ATTENDANTSENTRY.has_options = True
_APPDATA_ATTENDANTSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities


class RegisterServiceStub(object):
  """The greeting service definition.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetStatus = channel.unary_unary(
        '/services.RegisterService/GetStatus',
        request_serializer=StatusRequest.SerializeToString,
        response_deserializer=StatusResponse.FromString,
        )
    self.GetCode = channel.unary_unary(
        '/services.RegisterService/GetCode',
        request_serializer=CodeRequest.SerializeToString,
        response_deserializer=CodeResponse.FromString,
        )


class RegisterServiceServicer(object):
  """The greeting service definition.
  """

  def GetStatus(self, request, context):
    """Sends a greeting
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetCode(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RegisterServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetStatus': grpc.unary_unary_rpc_method_handler(
          servicer.GetStatus,
          request_deserializer=StatusRequest.FromString,
          response_serializer=StatusResponse.SerializeToString,
      ),
      'GetCode': grpc.unary_unary_rpc_method_handler(
          servicer.GetCode,
          request_deserializer=CodeRequest.FromString,
          response_serializer=CodeResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'services.RegisterService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class BetaRegisterServiceServicer(object):
  """The greeting service definition.
  """
  def GetStatus(self, request, context):
    """Sends a greeting
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def GetCode(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


class BetaRegisterServiceStub(object):
  """The greeting service definition.
  """
  def GetStatus(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    """Sends a greeting
    """
    raise NotImplementedError()
  GetStatus.future = None
  def GetCode(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()
  GetCode.future = None


def beta_create_RegisterService_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  request_deserializers = {
    ('services.RegisterService', 'GetCode'): CodeRequest.FromString,
    ('services.RegisterService', 'GetStatus'): StatusRequest.FromString,
  }
  response_serializers = {
    ('services.RegisterService', 'GetCode'): CodeResponse.SerializeToString,
    ('services.RegisterService', 'GetStatus'): StatusResponse.SerializeToString,
  }
  method_implementations = {
    ('services.RegisterService', 'GetCode'): face_utilities.unary_unary_inline(servicer.GetCode),
    ('services.RegisterService', 'GetStatus'): face_utilities.unary_unary_inline(servicer.GetStatus),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)


def beta_create_RegisterService_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  request_serializers = {
    ('services.RegisterService', 'GetCode'): CodeRequest.SerializeToString,
    ('services.RegisterService', 'GetStatus'): StatusRequest.SerializeToString,
  }
  response_deserializers = {
    ('services.RegisterService', 'GetCode'): CodeResponse.FromString,
    ('services.RegisterService', 'GetStatus'): StatusResponse.FromString,
  }
  cardinalities = {
    'GetCode': cardinality.Cardinality.UNARY_UNARY,
    'GetStatus': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'services.RegisterService', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)
