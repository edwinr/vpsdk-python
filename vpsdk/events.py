from vpsdk.api import *
from vpsdk.constants import *

class ChatEventData:
	def __init__(self, instance):
		self.session = vp_int(instance, VP_AVATAR_SESSION)
		self.name = vp_string(instance, VP_AVATAR_NAME)
		self.message = vp_string(instance, VP_CHAT_MESSAGE)
		self.chat_type = vp_int(instance, VP_CHAT_TYPE)
		if self.chat_type == VP_CHAT_CONSOLE_MESSAGE:
			self.color = [vp_int(instance, VP_CHAT_COLOR_RED),
						  vp_int(instance, VP_CHAT_COLOR_GREEN),
						  vp_int(instance, VP_CHAT_COLOR_BLUE)]
			self.effects = vp_int(instance, VP_CHAT_EFFECTS)
class AvatarAddEventData:
	def __init__(self, instance):
		self.session = vp_int(instance, VP_AVATAR_SESSION)
		self.name = vp_string(instance, VP_AVATAR_NAME)
		self.position = [vp_float(instance, VP_AVATAR_X),
						 vp_float(instance, VP_AVATAR_Y),
						 vp_float(instance, VP_AVATAR_Z)]
		self.pitch = vp_float(instance, VP_AVATAR_PITCH)
		self.yaw = vp_float(instance, VP_AVATAR_YAW)
		self.avatar_type = vp_int(instance, VP_AVATAR_TYPE)
		self.user = vp_int(instance, VP_USER_ID)
class AvatarChangeEventData:
	def __init__(self, instance):
		self.session = vp_int(instance, VP_AVATAR_SESSION)
		self.name = vp_string(instance, VP_AVATAR_NAME)
class AvatarDeleteEventData:
	def __init__(self, instance):
		self.session = vp_int(instance, VP_AVATAR_SESSION)
		self.name = vp_string(instance, VP_AVATAR_NAME)
		self.position = [vp_float(instance, VP_AVATAR_X),
						 vp_float(instance, VP_AVATAR_Y),
						 vp_float(instance, VP_AVATAR_Z)]
		self.pitch = vp_float(instance, VP_AVATAR_PITCH)
		self.yaw = vp_float(instance, VP_AVATAR_YAW)
class ObjectAddEventData:
	def __init__(self, instance):
		self.model = vp_string(instance, VP_OBJECT_MODEL)
		self.description = vp_string(instance, VP_OBJECT_DESCRIPTION)
		self.action = vp_string(instance, VP_OBJECT_ACTION)
		self.position = [vp_double(instance, VP_OBJECT_X),
						 vp_double(instance, VP_OBJECT_Y),
						 vp_double(instance, VP_OBJECT_Z)]
		self.rotation = [vp_float(instance, VP_OBJECT_ROTATION_X),
						 vp_float(instance, VP_OBJECT_ROTATION_Y),
						 vp_float(instance, VP_OBJECT_ROTATION_Z),
						 vp_float(instance, VP_OBJECT_ROTATION_ANGLE)]
		self.object_type = vp_int(instance, VP_OBJECT_TYPE)
		self.data = vp_data(instance, VP_OBJECT_DATA)
		self.session = vp_int(instance, VP_AVATAR_SESSION)
