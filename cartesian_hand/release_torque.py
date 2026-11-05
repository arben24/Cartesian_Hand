"""Emergency stop: cut torque on every servo on the bus so the hand can be
moved by hand.

    python -m cartesian_hand.release_torque            # franka_hand's port
    python -m cartesian_hand.release_torque <port>     # any other adapter
"""
import sys

from cartesian_hand.servo import open_driver

PORT = '/dev/serial/by-id/usb-1a86_USB_Single_Serial_5C84287281-if00'

bus = open_driver(sys.argv[1] if len(sys.argv) > 1 else PORT)
ids = bus.scan(0, 32)
print('found', ids)
bus.enable_torques(ids, False)
bus.close()
print('torque released')
