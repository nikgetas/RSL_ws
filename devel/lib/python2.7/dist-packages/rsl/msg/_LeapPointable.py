# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from rsl/LeapPointable.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg

class LeapPointable(genpy.Message):
  _md5sum = "17349b2abd8a7a1f31586b0c52c91cb7"
  _type = "rsl/LeapPointable"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# Leap Motion v6 Pointable JSON-based submessage
# https://developer.leapmotion.com/documentation/v2/javascript/supplements/Leap_JSON.html#version-6
#
#

# Leap uses a two dimensional array for the bases but ROS messages only support one dimension
# Unroll the Leap bases into individual bone basis instead
# geometry_msgs/Vector3[3][] bases          # the 3 basis vectors for each bone, in index order, wrist to tip, metacarpal, proximal, intermediate, and distal.
geometry_msgs/Vector3[3] metacarpalBasis
geometry_msgs/Vector3[3] proximalBasis
geometry_msgs/Vector3[3] intermediateBasis
geometry_msgs/Vector3[3] distalBasis
geometry_msgs/Point btipPosition            # the position of the tip of the distal phalanx as an array of 3 floats.
geometry_msgs/Point carpPosition            # the position of the base of metacarpal bone as an array of 3 floats.
geometry_msgs/Point dipPosition             # the position of the base of the distal phalanx as an array of 3 floats.
geometry_msgs/Vector3 direction
bool extended
uint32 handId
uint32 ID
float64 length
geometry_msgs/Point mcpPosition             # a position vector as an array of 3 floating point numbers
geometry_msgs/Point pipPosition             # a position vector as an array of 3 floating point numbers
geometry_msgs/Point stabilizedTipPosition   # array of floats (vector)
float64 timeVisible
geometry_msgs/Point tipPosition             #  array of floats (vector)
geometry_msgs/Vector3 tipVelocity           #  array of floats (vector)
bool tool
float64 touchDistance
string touchZone                            # string - one of "none", "hovering", "touching"
uint32 pointableType                        # integer - 0 is thumb; 4 is pinky
float64 width

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z
================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z
"""
  __slots__ = ['metacarpalBasis','proximalBasis','intermediateBasis','distalBasis','btipPosition','carpPosition','dipPosition','direction','extended','handId','ID','length','mcpPosition','pipPosition','stabilizedTipPosition','timeVisible','tipPosition','tipVelocity','tool','touchDistance','touchZone','pointableType','width']
  _slot_types = ['geometry_msgs/Vector3[3]','geometry_msgs/Vector3[3]','geometry_msgs/Vector3[3]','geometry_msgs/Vector3[3]','geometry_msgs/Point','geometry_msgs/Point','geometry_msgs/Point','geometry_msgs/Vector3','bool','uint32','uint32','float64','geometry_msgs/Point','geometry_msgs/Point','geometry_msgs/Point','float64','geometry_msgs/Point','geometry_msgs/Vector3','bool','float64','string','uint32','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       metacarpalBasis,proximalBasis,intermediateBasis,distalBasis,btipPosition,carpPosition,dipPosition,direction,extended,handId,ID,length,mcpPosition,pipPosition,stabilizedTipPosition,timeVisible,tipPosition,tipVelocity,tool,touchDistance,touchZone,pointableType,width

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(LeapPointable, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.metacarpalBasis is None:
        self.metacarpalBasis = [geometry_msgs.msg.Vector3(),geometry_msgs.msg.Vector3(),geometry_msgs.msg.Vector3()]
      if self.proximalBasis is None:
        self.proximalBasis = [geometry_msgs.msg.Vector3(),geometry_msgs.msg.Vector3(),geometry_msgs.msg.Vector3()]
      if self.intermediateBasis is None:
        self.intermediateBasis = [geometry_msgs.msg.Vector3(),geometry_msgs.msg.Vector3(),geometry_msgs.msg.Vector3()]
      if self.distalBasis is None:
        self.distalBasis = [geometry_msgs.msg.Vector3(),geometry_msgs.msg.Vector3(),geometry_msgs.msg.Vector3()]
      if self.btipPosition is None:
        self.btipPosition = geometry_msgs.msg.Point()
      if self.carpPosition is None:
        self.carpPosition = geometry_msgs.msg.Point()
      if self.dipPosition is None:
        self.dipPosition = geometry_msgs.msg.Point()
      if self.direction is None:
        self.direction = geometry_msgs.msg.Vector3()
      if self.extended is None:
        self.extended = False
      if self.handId is None:
        self.handId = 0
      if self.ID is None:
        self.ID = 0
      if self.length is None:
        self.length = 0.
      if self.mcpPosition is None:
        self.mcpPosition = geometry_msgs.msg.Point()
      if self.pipPosition is None:
        self.pipPosition = geometry_msgs.msg.Point()
      if self.stabilizedTipPosition is None:
        self.stabilizedTipPosition = geometry_msgs.msg.Point()
      if self.timeVisible is None:
        self.timeVisible = 0.
      if self.tipPosition is None:
        self.tipPosition = geometry_msgs.msg.Point()
      if self.tipVelocity is None:
        self.tipVelocity = geometry_msgs.msg.Vector3()
      if self.tool is None:
        self.tool = False
      if self.touchDistance is None:
        self.touchDistance = 0.
      if self.touchZone is None:
        self.touchZone = ''
      if self.pointableType is None:
        self.pointableType = 0
      if self.width is None:
        self.width = 0.
    else:
      self.metacarpalBasis = [geometry_msgs.msg.Vector3(),geometry_msgs.msg.Vector3(),geometry_msgs.msg.Vector3()]
      self.proximalBasis = [geometry_msgs.msg.Vector3(),geometry_msgs.msg.Vector3(),geometry_msgs.msg.Vector3()]
      self.intermediateBasis = [geometry_msgs.msg.Vector3(),geometry_msgs.msg.Vector3(),geometry_msgs.msg.Vector3()]
      self.distalBasis = [geometry_msgs.msg.Vector3(),geometry_msgs.msg.Vector3(),geometry_msgs.msg.Vector3()]
      self.btipPosition = geometry_msgs.msg.Point()
      self.carpPosition = geometry_msgs.msg.Point()
      self.dipPosition = geometry_msgs.msg.Point()
      self.direction = geometry_msgs.msg.Vector3()
      self.extended = False
      self.handId = 0
      self.ID = 0
      self.length = 0.
      self.mcpPosition = geometry_msgs.msg.Point()
      self.pipPosition = geometry_msgs.msg.Point()
      self.stabilizedTipPosition = geometry_msgs.msg.Point()
      self.timeVisible = 0.
      self.tipPosition = geometry_msgs.msg.Point()
      self.tipVelocity = geometry_msgs.msg.Vector3()
      self.tool = False
      self.touchDistance = 0.
      self.touchZone = ''
      self.pointableType = 0
      self.width = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      for val1 in self.metacarpalBasis:
        _x = val1
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
      for val1 in self.proximalBasis:
        _x = val1
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
      for val1 in self.intermediateBasis:
        _x = val1
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
      for val1 in self.distalBasis:
        _x = val1
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
      _x = self
      buff.write(_struct_12dB2I17dBd.pack(_x.btipPosition.x, _x.btipPosition.y, _x.btipPosition.z, _x.carpPosition.x, _x.carpPosition.y, _x.carpPosition.z, _x.dipPosition.x, _x.dipPosition.y, _x.dipPosition.z, _x.direction.x, _x.direction.y, _x.direction.z, _x.extended, _x.handId, _x.ID, _x.length, _x.mcpPosition.x, _x.mcpPosition.y, _x.mcpPosition.z, _x.pipPosition.x, _x.pipPosition.y, _x.pipPosition.z, _x.stabilizedTipPosition.x, _x.stabilizedTipPosition.y, _x.stabilizedTipPosition.z, _x.timeVisible, _x.tipPosition.x, _x.tipPosition.y, _x.tipPosition.z, _x.tipVelocity.x, _x.tipVelocity.y, _x.tipVelocity.z, _x.tool, _x.touchDistance))
      _x = self.touchZone
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_Id.pack(_x.pointableType, _x.width))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.metacarpalBasis is None:
        self.metacarpalBasis = None
      if self.proximalBasis is None:
        self.proximalBasis = None
      if self.intermediateBasis is None:
        self.intermediateBasis = None
      if self.distalBasis is None:
        self.distalBasis = None
      if self.btipPosition is None:
        self.btipPosition = geometry_msgs.msg.Point()
      if self.carpPosition is None:
        self.carpPosition = geometry_msgs.msg.Point()
      if self.dipPosition is None:
        self.dipPosition = geometry_msgs.msg.Point()
      if self.direction is None:
        self.direction = geometry_msgs.msg.Vector3()
      if self.mcpPosition is None:
        self.mcpPosition = geometry_msgs.msg.Point()
      if self.pipPosition is None:
        self.pipPosition = geometry_msgs.msg.Point()
      if self.stabilizedTipPosition is None:
        self.stabilizedTipPosition = geometry_msgs.msg.Point()
      if self.tipPosition is None:
        self.tipPosition = geometry_msgs.msg.Point()
      if self.tipVelocity is None:
        self.tipVelocity = geometry_msgs.msg.Vector3()
      end = 0
      self.metacarpalBasis = []
      for i in range(0, 3):
        val1 = geometry_msgs.msg.Vector3()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        self.metacarpalBasis.append(val1)
      self.proximalBasis = []
      for i in range(0, 3):
        val1 = geometry_msgs.msg.Vector3()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        self.proximalBasis.append(val1)
      self.intermediateBasis = []
      for i in range(0, 3):
        val1 = geometry_msgs.msg.Vector3()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        self.intermediateBasis.append(val1)
      self.distalBasis = []
      for i in range(0, 3):
        val1 = geometry_msgs.msg.Vector3()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        self.distalBasis.append(val1)
      _x = self
      start = end
      end += 250
      (_x.btipPosition.x, _x.btipPosition.y, _x.btipPosition.z, _x.carpPosition.x, _x.carpPosition.y, _x.carpPosition.z, _x.dipPosition.x, _x.dipPosition.y, _x.dipPosition.z, _x.direction.x, _x.direction.y, _x.direction.z, _x.extended, _x.handId, _x.ID, _x.length, _x.mcpPosition.x, _x.mcpPosition.y, _x.mcpPosition.z, _x.pipPosition.x, _x.pipPosition.y, _x.pipPosition.z, _x.stabilizedTipPosition.x, _x.stabilizedTipPosition.y, _x.stabilizedTipPosition.z, _x.timeVisible, _x.tipPosition.x, _x.tipPosition.y, _x.tipPosition.z, _x.tipVelocity.x, _x.tipVelocity.y, _x.tipVelocity.z, _x.tool, _x.touchDistance,) = _struct_12dB2I17dBd.unpack(str[start:end])
      self.extended = bool(self.extended)
      self.tool = bool(self.tool)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.touchZone = str[start:end].decode('utf-8')
      else:
        self.touchZone = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.pointableType, _x.width,) = _struct_Id.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      for val1 in self.metacarpalBasis:
        _x = val1
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
      for val1 in self.proximalBasis:
        _x = val1
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
      for val1 in self.intermediateBasis:
        _x = val1
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
      for val1 in self.distalBasis:
        _x = val1
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
      _x = self
      buff.write(_struct_12dB2I17dBd.pack(_x.btipPosition.x, _x.btipPosition.y, _x.btipPosition.z, _x.carpPosition.x, _x.carpPosition.y, _x.carpPosition.z, _x.dipPosition.x, _x.dipPosition.y, _x.dipPosition.z, _x.direction.x, _x.direction.y, _x.direction.z, _x.extended, _x.handId, _x.ID, _x.length, _x.mcpPosition.x, _x.mcpPosition.y, _x.mcpPosition.z, _x.pipPosition.x, _x.pipPosition.y, _x.pipPosition.z, _x.stabilizedTipPosition.x, _x.stabilizedTipPosition.y, _x.stabilizedTipPosition.z, _x.timeVisible, _x.tipPosition.x, _x.tipPosition.y, _x.tipPosition.z, _x.tipVelocity.x, _x.tipVelocity.y, _x.tipVelocity.z, _x.tool, _x.touchDistance))
      _x = self.touchZone
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_Id.pack(_x.pointableType, _x.width))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.metacarpalBasis is None:
        self.metacarpalBasis = None
      if self.proximalBasis is None:
        self.proximalBasis = None
      if self.intermediateBasis is None:
        self.intermediateBasis = None
      if self.distalBasis is None:
        self.distalBasis = None
      if self.btipPosition is None:
        self.btipPosition = geometry_msgs.msg.Point()
      if self.carpPosition is None:
        self.carpPosition = geometry_msgs.msg.Point()
      if self.dipPosition is None:
        self.dipPosition = geometry_msgs.msg.Point()
      if self.direction is None:
        self.direction = geometry_msgs.msg.Vector3()
      if self.mcpPosition is None:
        self.mcpPosition = geometry_msgs.msg.Point()
      if self.pipPosition is None:
        self.pipPosition = geometry_msgs.msg.Point()
      if self.stabilizedTipPosition is None:
        self.stabilizedTipPosition = geometry_msgs.msg.Point()
      if self.tipPosition is None:
        self.tipPosition = geometry_msgs.msg.Point()
      if self.tipVelocity is None:
        self.tipVelocity = geometry_msgs.msg.Vector3()
      end = 0
      self.metacarpalBasis = []
      for i in range(0, 3):
        val1 = geometry_msgs.msg.Vector3()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        self.metacarpalBasis.append(val1)
      self.proximalBasis = []
      for i in range(0, 3):
        val1 = geometry_msgs.msg.Vector3()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        self.proximalBasis.append(val1)
      self.intermediateBasis = []
      for i in range(0, 3):
        val1 = geometry_msgs.msg.Vector3()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        self.intermediateBasis.append(val1)
      self.distalBasis = []
      for i in range(0, 3):
        val1 = geometry_msgs.msg.Vector3()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        self.distalBasis.append(val1)
      _x = self
      start = end
      end += 250
      (_x.btipPosition.x, _x.btipPosition.y, _x.btipPosition.z, _x.carpPosition.x, _x.carpPosition.y, _x.carpPosition.z, _x.dipPosition.x, _x.dipPosition.y, _x.dipPosition.z, _x.direction.x, _x.direction.y, _x.direction.z, _x.extended, _x.handId, _x.ID, _x.length, _x.mcpPosition.x, _x.mcpPosition.y, _x.mcpPosition.z, _x.pipPosition.x, _x.pipPosition.y, _x.pipPosition.z, _x.stabilizedTipPosition.x, _x.stabilizedTipPosition.y, _x.stabilizedTipPosition.z, _x.timeVisible, _x.tipPosition.x, _x.tipPosition.y, _x.tipPosition.z, _x.tipVelocity.x, _x.tipVelocity.y, _x.tipVelocity.z, _x.tool, _x.touchDistance,) = _struct_12dB2I17dBd.unpack(str[start:end])
      self.extended = bool(self.extended)
      self.tool = bool(self.tool)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.touchZone = str[start:end].decode('utf-8')
      else:
        self.touchZone = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.pointableType, _x.width,) = _struct_Id.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_Id = struct.Struct("<Id")
_struct_12dB2I17dBd = struct.Struct("<12dB2I17dBd")
_struct_3d = struct.Struct("<3d")
