__all__ = ["Instance"]
from vpsdk.api import *
from vpsdk.constants import *

def check_error(rc):
    if rc != 0:
        raise(RuntimeError("VPSDK error " + str(rc)))


class EventWrapper(object):
    def __init__(self, instance, handler):
        self.instance = instance
        self.handler = handler
    def __call__(self, sender):
        self.handler(self.instance)

class Instance(object):
    instance = vp_create()
    events = [None] * 24
    callbacks = [None] * 17
    
    if instance == None:
        raise(RuntimeError("Could not create VPSDK instance"))

    def connect(self, host, port):
        check_error(vp_connect_universe(self.instance, host, port))
    def login(self, username, password, bot_name):
        check_error(vp_login(self.instance, username, password, bot_name))
    def enter(self, world):
        check_error(vp_enter(self.instance, world))
    def set_avatar(self, avatar_type, x, y, z, yaw, pitch):
        vp_int_set(self.instance, VP_MY_TYPE, avatar_type)
        vp_float_set(self.instance, VP_MY_X, x)
        vp_float_set(self.instance, VP_MY_Y, y)
        vp_float_set(self.instance, VP_MY_Z, z)
        vp_float_set(self.instance, VP_MY_YAW, yaw)
        vp_float_set(self.instance, VP_MY_PITCH, pitch)
        check_error(vp_state_change(self.instance))
    def wait(self, timeout):
        check_error(vp_wait(self.instance, timeout))
    def set_event(self, event, handler):
        native_handler = VP_EVENT_HANDLER_FUNC(EventWrapper(self, handler))
        self.events[event] = native_handler
        check_error(vp_event_set(self.instance, event, native_handler))
    def say(self, message):
        check_error(vp_say(self.instance, message))
