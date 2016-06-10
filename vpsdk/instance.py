__all__ = ["Instance"]
from vpsdk.api import *
from vpsdk.constants import *
from vpsdk.events import *

def check_error(rc):
    if rc != 0:
        raise(RuntimeError("VPSDK error " + VPReturnCodes[rc] + "(" + str(rc) + ")"))


class EventWrapper(object):
    def __init__(self, instance, handler):
        self.instance = instance
        self.handler = handler
    def __call__(self, sender):
        self.handler(self.instance)

class Instance(object):
    def __init__(self):
        self.instance = vp_create()
        self.events = [None] * 24
        self.callbacks = [None] * 17
        if self.instance == None:
            raise(RuntimeError("Could not create VPSDK instance"))
    def __del__(self):
        self.release()
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        self.release()
    def release(self):
        if self.instance is not None:
            check_error(vp_destroy(self.instance))
            self.instance = None
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
    def set_event_chat(self, handler):
        self.set_event(VP_EVENT_CHAT, lambda sender:
            handler(sender, ChatEventData(sender.instance)))
    def set_event_avatar_add(self, handler):
        self.set_event(VP_EVENT_AVATAR_ADD, lambda sender:
            handler(sender, AvatarAddEventData(sender.instance)))
    def set_event_avatar_change(self, handler):
        self.set_event(VP_EVENT_AVATAR_CHANGE, lambda sender:
            handler(sender, AvatarAddEventData(sender.instance)))
    def set_event_avatar_delete(self, handler):
        self.set_event(VP_EVENT_AVATAR_DELETE, lambda sender:
            handler(sender, AvatarAddEventData(sender.instance)))
    def set_event_object(self, handler):
        self.set_event(VP_EVENT_OBJECT, lambda sender:
            handler(sender, ObjectAddEventData(sender.instance)))
    def say(self, message):
        check_error(vp_say(self.instance, message))
    def query_cell(self, x, z, revision):
        check_error(vp_query_cell_revision(self.instance, x, z, revision))
