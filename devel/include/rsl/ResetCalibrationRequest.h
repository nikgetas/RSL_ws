// Generated by gencpp from file rsl/ResetCalibrationRequest.msg
// DO NOT EDIT!


#ifndef RSL_MESSAGE_RESETCALIBRATIONREQUEST_H
#define RSL_MESSAGE_RESETCALIBRATIONREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace rsl
{
template <class ContainerAllocator>
struct ResetCalibrationRequest_
{
  typedef ResetCalibrationRequest_<ContainerAllocator> Type;

  ResetCalibrationRequest_()
    : resetRequest(0)  {
    }
  ResetCalibrationRequest_(const ContainerAllocator& _alloc)
    : resetRequest(0)  {
  (void)_alloc;
    }



   typedef uint8_t _resetRequest_type;
  _resetRequest_type resetRequest;




  typedef boost::shared_ptr< ::rsl::ResetCalibrationRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::rsl::ResetCalibrationRequest_<ContainerAllocator> const> ConstPtr;

}; // struct ResetCalibrationRequest_

typedef ::rsl::ResetCalibrationRequest_<std::allocator<void> > ResetCalibrationRequest;

typedef boost::shared_ptr< ::rsl::ResetCalibrationRequest > ResetCalibrationRequestPtr;
typedef boost::shared_ptr< ::rsl::ResetCalibrationRequest const> ResetCalibrationRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::rsl::ResetCalibrationRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::rsl::ResetCalibrationRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace rsl

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'rsl': ['/home/dzhi/catkin_ws/src/rsl/msg'], 'std_msgs': ['/opt/ros/indigo/share/std_msgs/cmake/../msg'], 'sensor_msgs': ['/opt/ros/indigo/share/sensor_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/indigo/share/geometry_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::rsl::ResetCalibrationRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::rsl::ResetCalibrationRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::rsl::ResetCalibrationRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::rsl::ResetCalibrationRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::rsl::ResetCalibrationRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::rsl::ResetCalibrationRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::rsl::ResetCalibrationRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "65b5a0f951bad2a491fc17152c517af8";
  }

  static const char* value(const ::rsl::ResetCalibrationRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x65b5a0f951bad2a4ULL;
  static const uint64_t static_value2 = 0x91fc17152c517af8ULL;
};

template<class ContainerAllocator>
struct DataType< ::rsl::ResetCalibrationRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "rsl/ResetCalibrationRequest";
  }

  static const char* value(const ::rsl::ResetCalibrationRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::rsl::ResetCalibrationRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "char resetRequest\n\
";
  }

  static const char* value(const ::rsl::ResetCalibrationRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::rsl::ResetCalibrationRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.resetRequest);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ResetCalibrationRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::rsl::ResetCalibrationRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::rsl::ResetCalibrationRequest_<ContainerAllocator>& v)
  {
    s << indent << "resetRequest: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.resetRequest);
  }
};

} // namespace message_operations
} // namespace ros

#endif // RSL_MESSAGE_RESETCALIBRATIONREQUEST_H
