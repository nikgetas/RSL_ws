// Generated by gencpp from file my_leapmotion/ResetCalibrationResponse.msg
// DO NOT EDIT!


#ifndef MY_LEAPMOTION_MESSAGE_RESETCALIBRATIONRESPONSE_H
#define MY_LEAPMOTION_MESSAGE_RESETCALIBRATIONRESPONSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace my_leapmotion
{
template <class ContainerAllocator>
struct ResetCalibrationResponse_
{
  typedef ResetCalibrationResponse_<ContainerAllocator> Type;

  ResetCalibrationResponse_()
    {
    }
  ResetCalibrationResponse_(const ContainerAllocator& _alloc)
    {
  (void)_alloc;
    }






  typedef boost::shared_ptr< ::my_leapmotion::ResetCalibrationResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::my_leapmotion::ResetCalibrationResponse_<ContainerAllocator> const> ConstPtr;

}; // struct ResetCalibrationResponse_

typedef ::my_leapmotion::ResetCalibrationResponse_<std::allocator<void> > ResetCalibrationResponse;

typedef boost::shared_ptr< ::my_leapmotion::ResetCalibrationResponse > ResetCalibrationResponsePtr;
typedef boost::shared_ptr< ::my_leapmotion::ResetCalibrationResponse const> ResetCalibrationResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::my_leapmotion::ResetCalibrationResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::my_leapmotion::ResetCalibrationResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace my_leapmotion

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'my_leapmotion': ['/home/dzhi/catkin_ws/src/my_leapmotion/msg'], 'std_msgs': ['/opt/ros/indigo/share/std_msgs/cmake/../msg'], 'sensor_msgs': ['/opt/ros/indigo/share/sensor_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/indigo/share/geometry_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::my_leapmotion::ResetCalibrationResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::my_leapmotion::ResetCalibrationResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::my_leapmotion::ResetCalibrationResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::my_leapmotion::ResetCalibrationResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::my_leapmotion::ResetCalibrationResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::my_leapmotion::ResetCalibrationResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::my_leapmotion::ResetCalibrationResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d41d8cd98f00b204e9800998ecf8427e";
  }

  static const char* value(const ::my_leapmotion::ResetCalibrationResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd41d8cd98f00b204ULL;
  static const uint64_t static_value2 = 0xe9800998ecf8427eULL;
};

template<class ContainerAllocator>
struct DataType< ::my_leapmotion::ResetCalibrationResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "my_leapmotion/ResetCalibrationResponse";
  }

  static const char* value(const ::my_leapmotion::ResetCalibrationResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::my_leapmotion::ResetCalibrationResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n\
\n\
";
  }

  static const char* value(const ::my_leapmotion::ResetCalibrationResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::my_leapmotion::ResetCalibrationResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream&, T)
    {}

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ResetCalibrationResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::my_leapmotion::ResetCalibrationResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream&, const std::string&, const ::my_leapmotion::ResetCalibrationResponse_<ContainerAllocator>&)
  {}
};

} // namespace message_operations
} // namespace ros

#endif // MY_LEAPMOTION_MESSAGE_RESETCALIBRATIONRESPONSE_H