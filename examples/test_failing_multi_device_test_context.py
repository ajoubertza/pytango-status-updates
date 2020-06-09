from tango import DeviceProxy
from tango.server import Device, command
from tango.test_context import MultiDeviceTestContext


class MyDevice(Device):
    @command(dtype_in=str, dtype_out=int)
    def ping_via_command(self, friend):
        dp = DeviceProxy(friend)
        return dp.ping()


def test_access():
    devices_info = (
        {"class": MyDevice, "devices": [{"name": "my/dev/1"}, {"name": "my/dev/2"}]},
    )
    with MultiDeviceTestContext(devices_info) as context:
        proxy1 = context.get_device("my/dev/1")
        dev2_fqdn = context.get_device_access("my/dev/2")
        assert proxy1.ping_via_command(dev2_fqdn) < 1000  # works
        assert proxy1.ping_via_command("my/dev/2") < 1000  # fails in PyTango v9.3.2
