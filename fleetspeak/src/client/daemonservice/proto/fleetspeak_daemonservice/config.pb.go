// Code generated by protoc-gen-go. DO NOT EDIT.
// source: fleetspeak/src/client/daemonservice/proto/fleetspeak_daemonservice/config.proto

/*
Package fleetspeak_daemonservice is a generated protocol buffer package.

It is generated from these files:
	fleetspeak/src/client/daemonservice/proto/fleetspeak_daemonservice/config.proto
	fleetspeak/src/client/daemonservice/proto/fleetspeak_daemonservice/messages.proto

It has these top-level messages:
	Config
	StdOutputData
*/
package fleetspeak_daemonservice

import proto "github.com/golang/protobuf/proto"
import fmt "fmt"
import math "math"
import google_protobuf "github.com/golang/protobuf/ptypes/duration"

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion2 // please upgrade the proto package

// The configuration information expected by daemonservice.Factory in
// ClientServiceConfig.config.
type Config struct {
	Argv []string `protobuf:"bytes,1,rep,name=argv" json:"argv,omitempty"`
	// If set, process will be killed after this much inactivity. Any message to
	// or from the process, and any stdin/stderr output counts as inactivity.
	InactivityTimeout *google_protobuf.Duration `protobuf:"bytes,2,opt,name=inactivity_timeout,json=inactivityTimeout" json:"inactivity_timeout,omitempty"`
	// If set, start the process only when there is a message for it to work on.
	// Forced to true when inactivity timeout is set.
	LazyStart bool `protobuf:"varint,3,opt,name=lazy_start,json=lazyStart" json:"lazy_start,omitempty"`
	// By default, daemon services report resource usage every 10 minutes. This
	// flag disables this if set.
	DisableResourceMonitoring bool `protobuf:"varint,4,opt,name=disable_resource_monitoring,json=disableResourceMonitoring" json:"disable_resource_monitoring,omitempty"`
	// How many samples to aggregate into a report when monitoring resource usage.
	// If unset, defaults to 20.
	ResourceMonitoringSampleSize int32 `protobuf:"varint,5,opt,name=resource_monitoring_sample_size,json=resourceMonitoringSampleSize" json:"resource_monitoring_sample_size,omitempty"`
	// How long to wait between resource monitoring samples. If unset, defaults to
	// 30.
	ResourceMonitoringSamplePeriodSeconds int32 `protobuf:"varint,6,opt,name=resource_monitoring_sample_period_seconds,json=resourceMonitoringSamplePeriodSeconds" json:"resource_monitoring_sample_period_seconds,omitempty"`
	// If set, Fleetspeak will kill and restart the child if it exceeds this
	// memory limit, in bytes.
	MemoryLimit int64 `protobuf:"varint,7,opt,name=memory_limit,json=memoryLimit" json:"memory_limit,omitempty"`
	// If set, Fleetspeak will monitor child's heartbeat messages and kill
	// unresponsive processes. The values below should be set to configure the
	// heartbeat monitoring.
	MonitorHeartbeats bool `protobuf:"varint,8,opt,name=monitor_heartbeats,json=monitorHeartbeats" json:"monitor_heartbeats,omitempty"`
	// How long to wait for initial heartbeat.
	HeartbeatUnresponsiveGracePeriodSeconds int32 `protobuf:"varint,9,opt,name=heartbeat_unresponsive_grace_period_seconds,json=heartbeatUnresponsiveGracePeriodSeconds" json:"heartbeat_unresponsive_grace_period_seconds,omitempty"`
	// How long to wait for subsequent heartbeats.
	HeartbeatUnresponsiveKillPeriodSeconds int32 `protobuf:"varint,10,opt,name=heartbeat_unresponsive_kill_period_seconds,json=heartbeatUnresponsiveKillPeriodSeconds" json:"heartbeat_unresponsive_kill_period_seconds,omitempty"`
}

func (m *Config) Reset()                    { *m = Config{} }
func (m *Config) String() string            { return proto.CompactTextString(m) }
func (*Config) ProtoMessage()               {}
func (*Config) Descriptor() ([]byte, []int) { return fileDescriptor0, []int{0} }

func (m *Config) GetArgv() []string {
	if m != nil {
		return m.Argv
	}
	return nil
}

func (m *Config) GetInactivityTimeout() *google_protobuf.Duration {
	if m != nil {
		return m.InactivityTimeout
	}
	return nil
}

func (m *Config) GetLazyStart() bool {
	if m != nil {
		return m.LazyStart
	}
	return false
}

func (m *Config) GetDisableResourceMonitoring() bool {
	if m != nil {
		return m.DisableResourceMonitoring
	}
	return false
}

func (m *Config) GetResourceMonitoringSampleSize() int32 {
	if m != nil {
		return m.ResourceMonitoringSampleSize
	}
	return 0
}

func (m *Config) GetResourceMonitoringSamplePeriodSeconds() int32 {
	if m != nil {
		return m.ResourceMonitoringSamplePeriodSeconds
	}
	return 0
}

func (m *Config) GetMemoryLimit() int64 {
	if m != nil {
		return m.MemoryLimit
	}
	return 0
}

func (m *Config) GetMonitorHeartbeats() bool {
	if m != nil {
		return m.MonitorHeartbeats
	}
	return false
}

func (m *Config) GetHeartbeatUnresponsiveGracePeriodSeconds() int32 {
	if m != nil {
		return m.HeartbeatUnresponsiveGracePeriodSeconds
	}
	return 0
}

func (m *Config) GetHeartbeatUnresponsiveKillPeriodSeconds() int32 {
	if m != nil {
		return m.HeartbeatUnresponsiveKillPeriodSeconds
	}
	return 0
}

func init() {
	proto.RegisterType((*Config)(nil), "fleetspeak.daemonservice.Config")
}

func init() {
	proto.RegisterFile("fleetspeak/src/client/daemonservice/proto/fleetspeak_daemonservice/config.proto", fileDescriptor0)
}

var fileDescriptor0 = []byte{
	// 406 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0x7c, 0x92, 0x5d, 0x8b, 0xd4, 0x30,
	0x14, 0x40, 0xa9, 0x33, 0x3b, 0xee, 0x64, 0x7d, 0xd9, 0x3c, 0x65, 0xfd, 0xac, 0x82, 0x5a, 0x15,
	0x5b, 0xd0, 0x77, 0x5f, 0x54, 0x5c, 0x50, 0x51, 0x3a, 0x0a, 0x22, 0x42, 0xc8, 0xa4, 0x77, 0xea,
	0x65, 0xd3, 0xa4, 0x24, 0x69, 0x61, 0xe6, 0x67, 0xfb, 0x0b, 0xa4, 0x69, 0xed, 0x58, 0x77, 0xc7,
	0xb7, 0x72, 0xef, 0x39, 0xa7, 0xb7, 0x50, 0xf2, 0x69, 0xa3, 0x00, 0xbc, 0xab, 0x41, 0x5c, 0x64,
	0xce, 0xca, 0x4c, 0x2a, 0x04, 0xed, 0xb3, 0x42, 0x40, 0x65, 0xb4, 0x03, 0xdb, 0xa2, 0x84, 0xac,
	0xb6, 0xc6, 0x9b, 0x6c, 0x4f, 0xf2, 0xe9, 0x5a, 0x1a, 0xbd, 0xc1, 0x32, 0x0d, 0x14, 0x65, 0x7b,
	0x2c, 0x9d, 0x60, 0x37, 0xef, 0x96, 0xc6, 0x94, 0x6a, 0xa8, 0xad, 0x9b, 0x4d, 0x56, 0x34, 0x56,
	0x78, 0x34, 0xba, 0x37, 0x1f, 0xfc, 0x9a, 0x93, 0xc5, 0xeb, 0x90, 0xa2, 0x94, 0xcc, 0x85, 0x2d,
	0x5b, 0x16, 0xc5, 0xb3, 0x64, 0x99, 0x87, 0x67, 0x7a, 0x4e, 0x28, 0x6a, 0x21, 0x3d, 0xb6, 0xe8,
	0xb7, 0xdc, 0x63, 0x05, 0xa6, 0xf1, 0xec, 0x5a, 0x1c, 0x25, 0x27, 0x2f, 0xce, 0xd2, 0xbe, 0x9d,
	0xfe, 0x69, 0xa7, 0x6f, 0x86, 0x76, 0x7e, 0xba, 0x97, 0xbe, 0xf4, 0x0e, 0xbd, 0x43, 0x88, 0x12,
	0xbb, 0x2d, 0x77, 0x5e, 0x58, 0xcf, 0x66, 0x71, 0x94, 0x1c, 0xe7, 0xcb, 0x6e, 0xb2, 0xea, 0x06,
	0xf4, 0x15, 0xb9, 0x55, 0xa0, 0x13, 0x6b, 0x05, 0xdc, 0x82, 0x33, 0x8d, 0x95, 0xc0, 0x2b, 0xa3,
	0xd1, 0x1b, 0x8b, 0xba, 0x64, 0xf3, 0xc0, 0x9f, 0x0d, 0x48, 0x3e, 0x10, 0x1f, 0x47, 0x80, 0xbe,
	0x25, 0xf7, 0xae, 0xf0, 0xb8, 0x13, 0x55, 0xad, 0x80, 0x3b, 0xdc, 0x01, 0x3b, 0x8a, 0xa3, 0xe4,
	0x28, 0xbf, 0x6d, 0x2f, 0xc9, 0xab, 0x00, 0xad, 0x70, 0x07, 0xf4, 0x1b, 0x79, 0xf2, 0x9f, 0x4c,
	0x0d, 0x16, 0x4d, 0xc1, 0x1d, 0x48, 0xa3, 0x0b, 0xc7, 0x16, 0x21, 0xf8, 0xf0, 0x50, 0xf0, 0x73,
	0xa0, 0x57, 0x3d, 0x4c, 0xef, 0x93, 0x1b, 0x15, 0x54, 0xc6, 0x6e, 0xb9, 0xc2, 0x0a, 0x3d, 0xbb,
	0x1e, 0x47, 0xc9, 0x2c, 0x3f, 0xe9, 0x67, 0x1f, 0xba, 0x11, 0x7d, 0x4e, 0xe8, 0xf0, 0x4e, 0xfe,
	0x13, 0x84, 0xf5, 0x6b, 0x10, 0xde, 0xb1, 0xe3, 0xf0, 0xe9, 0xa7, 0xc3, 0xe6, 0x7c, 0x5c, 0xd0,
	0x1f, 0xe4, 0xd9, 0x88, 0xf1, 0x46, 0x5b, 0x70, 0xb5, 0xd1, 0x0e, 0x5b, 0xe0, 0xa5, 0x15, 0xf2,
	0xd2, 0xb5, 0xcb, 0x70, 0xed, 0xe3, 0x51, 0xf9, 0xfa, 0x97, 0xf1, 0xae, 0x13, 0xa6, 0xf7, 0x7e,
	0x27, 0x4f, 0x0f, 0xd4, 0x2f, 0x50, 0xa9, 0x7f, 0xe3, 0x24, 0xc4, 0x1f, 0x5d, 0x19, 0x7f, 0x8f,
	0x4a, 0x4d, 0xda, 0xeb, 0x45, 0xf8, 0x63, 0x5e, 0xfe, 0x0e, 0x00, 0x00, 0xff, 0xff, 0x56, 0x45,
	0x64, 0x22, 0x08, 0x03, 0x00, 0x00,
}
