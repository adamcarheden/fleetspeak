# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fleetspeak/src/common/proto/fleetspeak/common.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='fleetspeak/src/common/proto/fleetspeak/common.proto',
  package='fleetspeak',
  syntax='proto3',
  serialized_pb=_b('\n3fleetspeak/src/common/proto/fleetspeak/common.proto\x12\nfleetspeak\x1a\x19google/protobuf/any.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"2\n\x07\x41\x64\x64ress\x12\x11\n\tclient_id\x18\x01 \x01(\x0c\x12\x14\n\x0cservice_name\x18\x02 \x01(\t\"q\n\x0eValidationInfo\x12\x32\n\x04tags\x18\x01 \x03(\x0b\x32$.fleetspeak.ValidationInfo.TagsEntry\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xc3\x03\n\x07Message\x12\x12\n\nmessage_id\x18\x01 \x01(\x0c\x12#\n\x06source\x18\x02 \x01(\x0b\x32\x13.fleetspeak.Address\x12\x19\n\x11source_message_id\x18\x03 \x01(\x0c\x12(\n\x0b\x64\x65stination\x18\x04 \x01(\x0b\x32\x13.fleetspeak.Address\x12\x14\n\x0cmessage_type\x18\x05 \x01(\t\x12\x31\n\rcreation_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\"\n\x04\x64\x61ta\x18\x07 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x33\n\x0fvalidation_info\x18\x08 \x01(\x0b\x32\x1a.fleetspeak.ValidationInfo\x12)\n\x06result\x18\t \x01(\x0b\x32\x19.fleetspeak.MessageResult\x12.\n\x08priority\x18\n \x01(\x0e\x32\x1c.fleetspeak.Message.Priority\x12\x12\n\nbackground\x18\x0b \x01(\x08\")\n\x08Priority\x12\n\n\x06MEDIUM\x10\x00\x12\x07\n\x03LOW\x10\x01\x12\x08\n\x04HIGH\x10\x02\"j\n\rMessageResult\x12\x32\n\x0eprocessed_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06\x66\x61iled\x18\x03 \x01(\x08\x12\x15\n\rfailed_reason\x18\x04 \x01(\t\",\n\x05Label\x12\x14\n\x0cservice_name\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\"F\n\tSignature\x12\x13\n\x0b\x63\x65rtificate\x18\x01 \x01(\x0c\x12\x11\n\talgorithm\x18\x02 \x01(\x05\x12\x11\n\tsignature\x18\x03 \x01(\x0c\"l\n\x12WrappedContactData\x12\x14\n\x0c\x63ontact_data\x18\x01 \x01(\x0c\x12)\n\nsignatures\x18\x02 \x03(\x0b\x32\x15.fleetspeak.Signature\x12\x15\n\rclient_labels\x18\x03 \x03(\t\"\x80\x01\n\x0b\x43ontactData\x12\x18\n\x10sequencing_nonce\x18\x01 \x01(\x04\x12%\n\x08messages\x18\x02 \x03(\x0b\x32\x13.fleetspeak.Message\x12\x30\n\x0c\x63lient_clock\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x0e\n\x0c\x45mptyMessageb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])



_MESSAGE_PRIORITY = _descriptor.EnumDescriptor(
  name='Priority',
  full_name='fleetspeak.Message.Priority',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MEDIUM', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOW', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HIGH', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=705,
  serialized_end=746,
)
_sym_db.RegisterEnumDescriptor(_MESSAGE_PRIORITY)


_ADDRESS = _descriptor.Descriptor(
  name='Address',
  full_name='fleetspeak.Address',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_id', full_name='fleetspeak.Address.client_id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='service_name', full_name='fleetspeak.Address.service_name', index=1,
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
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=127,
  serialized_end=177,
)


_VALIDATIONINFO_TAGSENTRY = _descriptor.Descriptor(
  name='TagsEntry',
  full_name='fleetspeak.ValidationInfo.TagsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='fleetspeak.ValidationInfo.TagsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='fleetspeak.ValidationInfo.TagsEntry.value', index=1,
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
  serialized_start=249,
  serialized_end=292,
)

_VALIDATIONINFO = _descriptor.Descriptor(
  name='ValidationInfo',
  full_name='fleetspeak.ValidationInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tags', full_name='fleetspeak.ValidationInfo.tags', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_VALIDATIONINFO_TAGSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=179,
  serialized_end=292,
)


_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='fleetspeak.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message_id', full_name='fleetspeak.Message.message_id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source', full_name='fleetspeak.Message.source', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source_message_id', full_name='fleetspeak.Message.source_message_id', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='destination', full_name='fleetspeak.Message.destination', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message_type', full_name='fleetspeak.Message.message_type', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='creation_time', full_name='fleetspeak.Message.creation_time', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='fleetspeak.Message.data', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='validation_info', full_name='fleetspeak.Message.validation_info', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result', full_name='fleetspeak.Message.result', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='priority', full_name='fleetspeak.Message.priority', index=9,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='background', full_name='fleetspeak.Message.background', index=10,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MESSAGE_PRIORITY,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=295,
  serialized_end=746,
)


_MESSAGERESULT = _descriptor.Descriptor(
  name='MessageResult',
  full_name='fleetspeak.MessageResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='processed_time', full_name='fleetspeak.MessageResult.processed_time', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='failed', full_name='fleetspeak.MessageResult.failed', index=1,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='failed_reason', full_name='fleetspeak.MessageResult.failed_reason', index=2,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=748,
  serialized_end=854,
)


_LABEL = _descriptor.Descriptor(
  name='Label',
  full_name='fleetspeak.Label',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='service_name', full_name='fleetspeak.Label.service_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='label', full_name='fleetspeak.Label.label', index=1,
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
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=856,
  serialized_end=900,
)


_SIGNATURE = _descriptor.Descriptor(
  name='Signature',
  full_name='fleetspeak.Signature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='certificate', full_name='fleetspeak.Signature.certificate', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='algorithm', full_name='fleetspeak.Signature.algorithm', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signature', full_name='fleetspeak.Signature.signature', index=2,
      number=3, type=12, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=902,
  serialized_end=972,
)


_WRAPPEDCONTACTDATA = _descriptor.Descriptor(
  name='WrappedContactData',
  full_name='fleetspeak.WrappedContactData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='contact_data', full_name='fleetspeak.WrappedContactData.contact_data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signatures', full_name='fleetspeak.WrappedContactData.signatures', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='client_labels', full_name='fleetspeak.WrappedContactData.client_labels', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=974,
  serialized_end=1082,
)


_CONTACTDATA = _descriptor.Descriptor(
  name='ContactData',
  full_name='fleetspeak.ContactData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sequencing_nonce', full_name='fleetspeak.ContactData.sequencing_nonce', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='messages', full_name='fleetspeak.ContactData.messages', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='client_clock', full_name='fleetspeak.ContactData.client_clock', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1085,
  serialized_end=1213,
)


_EMPTYMESSAGE = _descriptor.Descriptor(
  name='EmptyMessage',
  full_name='fleetspeak.EmptyMessage',
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
  serialized_start=1215,
  serialized_end=1229,
)

_VALIDATIONINFO_TAGSENTRY.containing_type = _VALIDATIONINFO
_VALIDATIONINFO.fields_by_name['tags'].message_type = _VALIDATIONINFO_TAGSENTRY
_MESSAGE.fields_by_name['source'].message_type = _ADDRESS
_MESSAGE.fields_by_name['destination'].message_type = _ADDRESS
_MESSAGE.fields_by_name['creation_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_MESSAGE.fields_by_name['data'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_MESSAGE.fields_by_name['validation_info'].message_type = _VALIDATIONINFO
_MESSAGE.fields_by_name['result'].message_type = _MESSAGERESULT
_MESSAGE.fields_by_name['priority'].enum_type = _MESSAGE_PRIORITY
_MESSAGE_PRIORITY.containing_type = _MESSAGE
_MESSAGERESULT.fields_by_name['processed_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_WRAPPEDCONTACTDATA.fields_by_name['signatures'].message_type = _SIGNATURE
_CONTACTDATA.fields_by_name['messages'].message_type = _MESSAGE
_CONTACTDATA.fields_by_name['client_clock'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['Address'] = _ADDRESS
DESCRIPTOR.message_types_by_name['ValidationInfo'] = _VALIDATIONINFO
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
DESCRIPTOR.message_types_by_name['MessageResult'] = _MESSAGERESULT
DESCRIPTOR.message_types_by_name['Label'] = _LABEL
DESCRIPTOR.message_types_by_name['Signature'] = _SIGNATURE
DESCRIPTOR.message_types_by_name['WrappedContactData'] = _WRAPPEDCONTACTDATA
DESCRIPTOR.message_types_by_name['ContactData'] = _CONTACTDATA
DESCRIPTOR.message_types_by_name['EmptyMessage'] = _EMPTYMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Address = _reflection.GeneratedProtocolMessageType('Address', (_message.Message,), dict(
  DESCRIPTOR = _ADDRESS,
  __module__ = 'fleetspeak.src.common.proto.fleetspeak.common_pb2'
  # @@protoc_insertion_point(class_scope:fleetspeak.Address)
  ))
_sym_db.RegisterMessage(Address)

ValidationInfo = _reflection.GeneratedProtocolMessageType('ValidationInfo', (_message.Message,), dict(

  TagsEntry = _reflection.GeneratedProtocolMessageType('TagsEntry', (_message.Message,), dict(
    DESCRIPTOR = _VALIDATIONINFO_TAGSENTRY,
    __module__ = 'fleetspeak.src.common.proto.fleetspeak.common_pb2'
    # @@protoc_insertion_point(class_scope:fleetspeak.ValidationInfo.TagsEntry)
    ))
  ,
  DESCRIPTOR = _VALIDATIONINFO,
  __module__ = 'fleetspeak.src.common.proto.fleetspeak.common_pb2'
  # @@protoc_insertion_point(class_scope:fleetspeak.ValidationInfo)
  ))
_sym_db.RegisterMessage(ValidationInfo)
_sym_db.RegisterMessage(ValidationInfo.TagsEntry)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGE,
  __module__ = 'fleetspeak.src.common.proto.fleetspeak.common_pb2'
  # @@protoc_insertion_point(class_scope:fleetspeak.Message)
  ))
_sym_db.RegisterMessage(Message)

MessageResult = _reflection.GeneratedProtocolMessageType('MessageResult', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGERESULT,
  __module__ = 'fleetspeak.src.common.proto.fleetspeak.common_pb2'
  # @@protoc_insertion_point(class_scope:fleetspeak.MessageResult)
  ))
_sym_db.RegisterMessage(MessageResult)

Label = _reflection.GeneratedProtocolMessageType('Label', (_message.Message,), dict(
  DESCRIPTOR = _LABEL,
  __module__ = 'fleetspeak.src.common.proto.fleetspeak.common_pb2'
  # @@protoc_insertion_point(class_scope:fleetspeak.Label)
  ))
_sym_db.RegisterMessage(Label)

Signature = _reflection.GeneratedProtocolMessageType('Signature', (_message.Message,), dict(
  DESCRIPTOR = _SIGNATURE,
  __module__ = 'fleetspeak.src.common.proto.fleetspeak.common_pb2'
  # @@protoc_insertion_point(class_scope:fleetspeak.Signature)
  ))
_sym_db.RegisterMessage(Signature)

WrappedContactData = _reflection.GeneratedProtocolMessageType('WrappedContactData', (_message.Message,), dict(
  DESCRIPTOR = _WRAPPEDCONTACTDATA,
  __module__ = 'fleetspeak.src.common.proto.fleetspeak.common_pb2'
  # @@protoc_insertion_point(class_scope:fleetspeak.WrappedContactData)
  ))
_sym_db.RegisterMessage(WrappedContactData)

ContactData = _reflection.GeneratedProtocolMessageType('ContactData', (_message.Message,), dict(
  DESCRIPTOR = _CONTACTDATA,
  __module__ = 'fleetspeak.src.common.proto.fleetspeak.common_pb2'
  # @@protoc_insertion_point(class_scope:fleetspeak.ContactData)
  ))
_sym_db.RegisterMessage(ContactData)

EmptyMessage = _reflection.GeneratedProtocolMessageType('EmptyMessage', (_message.Message,), dict(
  DESCRIPTOR = _EMPTYMESSAGE,
  __module__ = 'fleetspeak.src.common.proto.fleetspeak.common_pb2'
  # @@protoc_insertion_point(class_scope:fleetspeak.EmptyMessage)
  ))
_sym_db.RegisterMessage(EmptyMessage)


_VALIDATIONINFO_TAGSENTRY.has_options = True
_VALIDATIONINFO_TAGSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
