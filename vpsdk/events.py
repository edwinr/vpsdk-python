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
