# encoding: utf-8
# module google.protobuf.pyext._message
# from C:\Users\akharin\PycharmProjects\pythonProject\venv\lib\site-packages\google\protobuf\pyext\_message.cp39-win_amd64.pyd
# by generator 1.147
"""
python-proto2 is a module that can be used to enhance proto2 Python API
performance.

It provides access to the protocol buffers C++ reflection API that
implements the basic protocol buffer functions.
"""

# imports
import collections.abc as __collections_abc


# functions

def SetAllowOversizeProtos(*args, **kwargs): # real signature unknown
    """ Enable/disable oversize proto parsing. """
    pass

# classes

class Descriptor(DescriptorBase):
    """ A Message Descriptor """
    def CopyToProto(self, *args, **kwargs): # real signature unknown
        pass

    def EnumValueName(self, *args, **kwargs): # real signature unknown
        pass

    def GetOptions(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    containing_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Containing type"""

    enum_types = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Enum sequence"""

    enum_types_by_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Enum types by name"""

    enum_values_by_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Enum values by name"""

    extensions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Extensions Sequence"""

    extensions_by_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Extensions by name"""

    extension_ranges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Extension ranges"""

    fields = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Fields sequence"""

    fields_by_camelcase_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Fields by camelCase name"""

    fields_by_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Fields by name"""

    fields_by_number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Fields by number"""

    file = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """File descriptor"""

    full_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Full name"""

    has_options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Has Options"""

    is_extendable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Last name"""

    nested_types = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Nested types sequence"""

    nested_types_by_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Nested types by name"""

    oneofs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Oneofs by name"""

    oneofs_by_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Oneofs by name"""

    syntax = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Syntax"""

    _concrete_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """concrete class"""

    _options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Options"""

    _serialized_options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Serialized Options"""



class DescriptorPool(object):
    """ A Descriptor Pool """
    def Add(self, *args, **kwargs): # real signature unknown
        """ Adds the FileDescriptorProto and its types to this pool. """
        pass

    def AddDescriptor(self, *args, **kwargs): # real signature unknown
        """ No-op. Add() must have been called before. """
        pass

    def AddEnumDescriptor(self, *args, **kwargs): # real signature unknown
        """ No-op. Add() must have been called before. """
        pass

    def AddExtensionDescriptor(self, *args, **kwargs): # real signature unknown
        """ No-op. Add() must have been called before. """
        pass

    def AddFileDescriptor(self, *args, **kwargs): # real signature unknown
        """ No-op. Add() must have been called before. """
        pass

    def AddSerializedFile(self, *args, **kwargs): # real signature unknown
        """ Adds a serialized FileDescriptorProto to this pool. """
        pass

    def AddServiceDescriptor(self, *args, **kwargs): # real signature unknown
        """ No-op. Add() must have been called before. """
        pass

    def FindAllExtensions(self, *args, **kwargs): # real signature unknown
        """ Gets all known extensions of the given message descriptor. """
        pass

    def FindEnumTypeByName(self, *args, **kwargs): # real signature unknown
        """ Searches for enum type descriptor by full name. """
        pass

    def FindExtensionByName(self, *args, **kwargs): # real signature unknown
        """ Searches for extension descriptor by full name. """
        pass

    def FindExtensionByNumber(self, *args, **kwargs): # real signature unknown
        """ Gets the extension descriptor for the given number. """
        pass

    def FindFieldByName(self, *args, **kwargs): # real signature unknown
        """ Searches for a field descriptor by full name. """
        pass

    def FindFileByName(self, *args, **kwargs): # real signature unknown
        """ Searches for a file descriptor by its .proto name. """
        pass

    def FindFileContainingSymbol(self, *args, **kwargs): # real signature unknown
        """ Gets the FileDescriptor containing the specified symbol. """
        pass

    def FindMessageTypeByName(self, *args, **kwargs): # real signature unknown
        """ Searches for a message descriptor by full name. """
        pass

    def FindMethodByName(self, *args, **kwargs): # real signature unknown
        """ Searches for method descriptor by full name. """
        pass

    def FindOneofByName(self, *args, **kwargs): # real signature unknown
        """ Searches for oneof descriptor by full name. """
        pass

    def FindServiceByName(self, *args, **kwargs): # real signature unknown
        """ Searches for service descriptor by full name. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class EnumDescriptor(DescriptorBase):
    """ A Enum Descriptor """
    def CopyToProto(self, *args, **kwargs): # real signature unknown
        pass

    def GetOptions(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    containing_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Containing type"""

    file = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """File descriptor"""

    full_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Full name"""

    has_options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Has Options"""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """last name"""

    values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """values"""

    values_by_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Enum values by name"""

    values_by_number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Enum values by number"""

    _options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Options"""

    _serialized_options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Serialized Options"""



class EnumValueDescriptor(DescriptorBase):
    """ A EnumValue Descriptor """
    def GetOptions(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    has_options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Has Options"""

    index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """index"""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """name"""

    number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """number"""

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """index"""

    _options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Options"""

    _serialized_options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Serialized Options"""



class ExtensionDict(object):
    """ An extension dict """
    def _FindExtensionByName(self, *args, **kwargs): # real signature unknown
        """ Finds an extension by name. """
        pass

    def _FindExtensionByNumber(self, *args, **kwargs): # real signature unknown
        """ Finds an extension by field number. """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    __hash__ = None


class ExtensionIterator(object):
    """ A scalar map iterator """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        """ Implement next(self). """
        pass


class FieldDescriptor(DescriptorBase):
    """ A Field Descriptor """
    def GetOptions(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    camelcase_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Camelcase name"""

    containing_oneof = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Containing oneof"""

    containing_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Containing type"""

    cpp_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """C++ Type"""

    default_value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Default Value"""

    enum_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Enum type"""

    extension_scope = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Extension scope"""

    file = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """File Descriptor"""

    full_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Full name"""

    has_default_value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    has_options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Has Options"""

    has_presence = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Has Presence"""

    id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ID"""

    index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Index"""

    is_extension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ID"""

    json_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Json name"""

    label = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Label"""

    message_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Message type"""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Unqualified name"""

    number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number"""

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """C++ Type"""

    _cdescriptor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """HAACK REMOVE ME"""

    _options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Options"""

    _serialized_options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Serialized Options"""


    CPPTYPE_BOOL = 7
    CPPTYPE_DOUBLE = 5
    CPPTYPE_ENUM = 8
    CPPTYPE_FLOAT = 6
    CPPTYPE_INT32 = 1
    CPPTYPE_INT64 = 2
    CPPTYPE_MESSAGE = 10
    CPPTYPE_STRING = 9
    CPPTYPE_UINT32 = 3
    CPPTYPE_UINT64 = 4
    LABEL_OPTIONAL = 1
    LABEL_REPEATED = 3
    LABEL_REQUIRED = 2
    TYPE_BOOL = 8
    TYPE_BYTES = 12
    TYPE_DOUBLE = 1
    TYPE_ENUM = 14
    TYPE_FIXED32 = 7
    TYPE_FIXED64 = 6
    TYPE_FLOAT = 2
    TYPE_GROUP = 10
    TYPE_INT32 = 5
    TYPE_INT64 = 3
    TYPE_MESSAGE = 11
    TYPE_SFIXED32 = 15
    TYPE_SFIXED64 = 16
    TYPE_SINT32 = 17
    TYPE_SINT64 = 18
    TYPE_STRING = 9
    TYPE_UINT32 = 13
    TYPE_UINT64 = 4


class FileDescriptor(DescriptorBase):
    """ A File Descriptor """
    def CopyToProto(self, *args, **kwargs): # real signature unknown
        pass

    def GetDebugString(self, *args, **kwargs): # real signature unknown
        pass

    def GetOptions(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    dependencies = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Dependencies"""

    enum_types_by_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Enums by name"""

    extensions_by_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Extensions by name"""

    has_options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Has Options"""

    message_types_by_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Messages by name"""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """name"""

    package = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """package"""

    pool = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """pool"""

    public_dependencies = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Dependencies"""

    serialized_pb = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    services_by_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Services by name"""

    syntax = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Syntax"""

    _options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Options"""

    _serialized_options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Serialized Options"""



class MapIterator(object):
    """ A scalar map iterator """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        """ Implement next(self). """
        pass


class Message(object):
    """ A ProtocolMessage """
    def ByteSize(self, *args, **kwargs): # real signature unknown
        """ Returns the size of the message in bytes. """
        pass

    def Clear(self, *args, **kwargs): # real signature unknown
        """ Clears the message. """
        pass

    def ClearExtension(self, *args, **kwargs): # real signature unknown
        """ Clears a message field. """
        pass

    def ClearField(self, *args, **kwargs): # real signature unknown
        """ Clears a message field. """
        pass

    def CopyFrom(self, *args, **kwargs): # real signature unknown
        """ Copies a protocol message into the current message. """
        pass

    def DiscardUnknownFields(self, *args, **kwargs): # real signature unknown
        """ Discards the unknown fields. """
        pass

    def FindInitializationErrors(self, *args, **kwargs): # real signature unknown
        """ Finds unset required fields. """
        pass

    @classmethod
    def FromString(cls, *args, **kwargs): # real signature unknown
        """ Creates new method instance from given serialized data. """
        pass

    def HasExtension(self, *args, **kwargs): # real signature unknown
        """ Checks if a message field is set. """
        pass

    def HasField(self, *args, **kwargs): # real signature unknown
        """ Checks if a message field is set. """
        pass

    def IsInitialized(self, *args, **kwargs): # real signature unknown
        """ Checks if all required fields of a protocol message are set. """
        pass

    def ListFields(self, *args, **kwargs): # real signature unknown
        """ Lists all set fields of a message. """
        pass

    def MergeFrom(self, *args, **kwargs): # real signature unknown
        """ Merges a protocol message into the current message. """
        pass

    def MergeFromString(self, *args, **kwargs): # real signature unknown
        """ Merges a serialized message into the current message. """
        pass

    def ParseFromString(self, *args, **kwargs): # real signature unknown
        """ Parses a serialized message into the current message. """
        pass

    @classmethod
    def RegisterExtension(cls, *args, **kwargs): # real signature unknown
        """ Registers an extension with the current message. """
        pass

    def SerializePartialToString(self, *args, **kwargs): # real signature unknown
        """ Serializes the message to a string, even if it isn't initialized. """
        pass

    def SerializeToString(self, *args, **kwargs): # real signature unknown
        """ Serializes the message to a string, only for initialized messages. """
        pass

    def SetInParent(self, *args, **kwargs): # real signature unknown
        """ Sets the has bit of the given field in its parent message. """
        pass

    def UnknownFields(self, *args, **kwargs): # real signature unknown
        """ Parse unknown field set """
        pass

    def WhichOneof(self, *args, **kwargs): # real signature unknown
        """ Returns the name of the field set inside a oneof, or None if no field is set. """
        pass

    def _CheckCalledFromGeneratedFile(self, *args, **kwargs): # real signature unknown
        """ Raises TypeError if the caller is not in a _pb2.py file. """
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        """ Makes a deep copy of the class. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __unicode__(self, *args, **kwargs): # real signature unknown
        """ Outputs a unicode representation of the message. """
        pass

    Extensions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Extension dict"""

    _extensions_by_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _extensions_by_number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    DESCRIPTOR = None


class MessageMapContainer(__collections_abc.MutableMapping):
    # no doc
    def clear(self, *args, **kwargs): # real signature unknown
        """ Removes all elements from the map. """
        pass

    def get(self, *args, **kwargs): # real signature unknown
        """ Gets the value for the given key if present, or otherwise a default """
        pass

    def GetEntryClass(self, *args, **kwargs): # real signature unknown
        """ Return the class used to build Entries of (key, value) pairs. """
        pass

    def get_or_create(self, *args, **kwargs): # real signature unknown
        """ Alias for getitem, useful to make explicit that the map is mutated. """
        pass

    def MergeFrom(self, *args, **kwargs): # real signature unknown
        """ Merges a map into the current map. """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Tests whether the map contains this element. """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass


class MessageMeta(type):
    """ The metaclass of ProtocolMessages """
    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    _extensions_by_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _extensions_by_number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class MethodDescriptor(DescriptorBase):
    """ A Method Descriptor """
    def CopyToProto(self, *args, **kwargs): # real signature unknown
        pass

    def GetOptions(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    client_streaming = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Client streaming"""

    containing_service = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Containing service"""

    full_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Full name"""

    index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Index"""

    input_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Input type"""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Name"""

    output_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Output type"""

    server_streaming = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Server streaming"""



class OneofDescriptor(DescriptorBase):
    """ A Oneof Descriptor """
    def GetOptions(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    containing_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Containing type"""

    fields = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Fields"""

    full_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Full name"""

    has_options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Has Options"""

    index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Index"""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Name"""

    _options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Options"""

    _serialized_options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Serialized Options"""



class RepeatedCompositeContainer(object):
    """ A Repeated scalar container """
    def add(self, *args, **kwargs): # real signature unknown
        """ Adds an object to the repeated container. """
        pass

    def append(self, *args, **kwargs): # real signature unknown
        """ Appends a message to the end of the repeated container. """
        pass

    def extend(self, *args, **kwargs): # real signature unknown
        """ Adds objects to the repeated container. """
        pass

    def insert(self, *args, **kwargs): # real signature unknown
        """ Inserts a message before the specified index. """
        pass

    def MergeFrom(self, *args, **kwargs): # real signature unknown
        """ Adds objects to the repeated container. """
        pass

    def pop(self, *args, **kwargs): # real signature unknown
        """ Removes an object from the repeated container and returns it. """
        pass

    def remove(self, *args, **kwargs): # real signature unknown
        """ Removes an object from the repeated container. """
        pass

    def reverse(self, *args, **kwargs): # real signature unknown
        """ Reverses elements order of the repeated container. """
        pass

    def sort(self, *args, **kwargs): # real signature unknown
        """ Sorts the repeated container. """
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        """ Makes a deep copy of the class. """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    __hash__ = None


class RepeatedScalarContainer(object):
    """ A Repeated scalar container """
    def append(self, *args, **kwargs): # real signature unknown
        """ Appends an object to the repeated container. """
        pass

    def extend(self, *args, **kwargs): # real signature unknown
        """ Appends objects to the repeated container. """
        pass

    def insert(self, *args, **kwargs): # real signature unknown
        """ Inserts an object at the specified position in the container. """
        pass

    def MergeFrom(self, *args, **kwargs): # real signature unknown
        """ Merges a repeated container into the current container. """
        pass

    def pop(self, *args, **kwargs): # real signature unknown
        """ Removes an object from the repeated container and returns it. """
        pass

    def remove(self, *args, **kwargs): # real signature unknown
        """ Removes an object from the repeated container. """
        pass

    def reverse(self, *args, **kwargs): # real signature unknown
        """ Reverses elements order of the repeated container. """
        pass

    def sort(self, *args, **kwargs): # real signature unknown
        """ Sorts the repeated container. """
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        """ Makes a deep copy of the class. """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Outputs picklable representation of the repeated field. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    __hash__ = None


class ScalarMapContainer(__collections_abc.MutableMapping):
    # no doc
    def clear(self, *args, **kwargs): # real signature unknown
        """ Removes all elements from the map. """
        pass

    def get(self, *args, **kwargs): # real signature unknown
        """ Gets the value for the given key if present, or otherwise a default """
        pass

    def GetEntryClass(self, *args, **kwargs): # real signature unknown
        """ Return the class used to build Entries of (key, value) pairs. """
        pass

    def MergeFrom(self, *args, **kwargs): # real signature unknown
        """ Merges a map into the current map. """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Tests whether a key is a member of the map. """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass


class ServiceDescriptor(DescriptorBase):
    """ A Service Descriptor """
    def CopyToProto(self, *args, **kwargs): # real signature unknown
        pass

    def FindMethodByName(self, *args, **kwargs): # real signature unknown
        pass

    def GetOptions(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    file = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """File descriptor"""

    full_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Full name"""

    index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Index"""

    methods = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Methods"""

    methods_by_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Methods by name"""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Name"""



class UnknownField(object):
    """ unknown field """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    field_number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    wire_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __hash__ = None


class UnknownFieldSet(object):
    """ unknown field set """
    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    __hash__ = None


# variables with complex values

default_pool = None # (!) real value is '<google.protobuf.pyext._message.DescriptorPool object at 0x000002D830CA5A00>'

proto_API = None # (!) real value is '<capsule object "google.protobuf.pyext._message.proto_API" at 0x000002D832A46150>'

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000002D832A46910>'

__spec__ = None # (!) real value is "ModuleSpec(name='google.protobuf.pyext._message', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000002D832A46910>, origin='C:\\\\Users\\\\akharin\\\\PycharmProjects\\\\pythonProject\\\\venv\\\\lib\\\\site-packages\\\\google\\\\protobuf\\\\pyext\\\\_message.cp39-win_amd64.pyd')"

