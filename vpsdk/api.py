from ctypes import *

try:
    lib = CDLL("vpsdk.dll")
except:
    try:
        lib = CDLL("libvpsdk.so")
    except:
        raise(OSError("Could not load VPSDK"))


def check_error(rc):
    if rc != 0:
        raise(RuntimeError("VPSDK error " + str(rc)))


check_error(lib.vp_init(c_int(3)))
lib.vp_create.restype = c_void_p
lib.vp_string.restype = c_char_p
lib.vp_data.restype = c_char_p
lib.vp_float.restype = c_float
lib.vp_double.restype = c_double

VP_EVENT_HANDLER_FUNC = CFUNCTYPE(None, c_void_p)
VP_EVENT_CALLBACK_FUNC = CFUNCTYPE(None, c_void_p, c_int, c_int)

def vp_create():
    return c_void_p(lib.vp_create())
def vp_destroy(instance):
    return lib.vp_destroy(instance)
def vp_connect_universe(instance, host, port):
    return lib.vp_connect_universe(instance, c_char_p(host.encode("utf-8")), c_ushort(port))
def vp_login(instance, username, password, bot_name):
    return lib.vp_login(instance,
                        c_char_p(username.encode("utf-8")),
                        c_char_p(password.encode("utf-8")),
                        c_char_p(bot_name.encode("utf-8")))
def vp_enter(instance, world_name):
    return lib.vp_enter(instance, c_char_p(world_name.encode("utf-8")))
def vp_wait(instance, timeout):
    return lib.vp_wait(instance, c_int(timeout))
def vp_leave(instance):
    return lib.vp_leave(instance)
def vp_say(instance, message):
    return lib.vp_say(instance, c_char_p(message.encode("utf-8")))
def vp_console_message(instance, session, name, message, effects, reg, green, blue):
    return lib.vp_console_message(instance, c_int(session), c_char_p(name.encode("utf-8")),
                                  c_char_p(message.encode("utf-8")), c_int(effects),
                                  c_ubyte(red), c_ubyte(green), c_ubyte(blue))
def vp_event_set(instance, event, handler):
    return lib.vp_event_set(instance, c_int(event), handler)
def vp_callback_set(instance, callback, handler):
    return lib.vp_callback_set(instance, c_int(callback), handler)
#def vp_user_data(instance):
#    return lib.vp_user_data(instance)
#def vp_user_data_set(instance, data):
#    return lib.vp_user_data_set(instance, c_void_p(data))
def vp_state_change(instance):
    return lib.vp_state_change(instance)
def vp_int(instance, key):
    return lib.vp_int(instance, key)
def vp_float(instance, key):
    return lib.vp_float(instance, key)
def vp_double(instance, key):
    return lib.vp_double(instance, key)
def vp_string(instance, key):
    return lib.vp_string(instance, key).decode("utf-8")
def vp_data(instance, key):
    length = c_int(0)
    src = lib.vp_data(instance, c_int(key), byref(length))
    if length.value > 0:
        dst = create_string_buffer(length.value)
        memmove(dst, src, length.value)
        return dst
    else:
        return None
def vp_int_set(instance, key, value):
    return lib.vp_int_set(instance, c_int(key), c_int(value))
def vp_float_set(instance, key, value):
    return lib.vp_float_set(instance, c_int(key), c_float(value))
def vp_double_set(instance, key, value):
    return lib.vp_float_set(instance, c_int(key), c_double(value))
def vp_string_set(instance, key, value):
    return lib.vp_string_set(instance, c_int(key), c_char_p(value))
def vp_query_cell(instance, x, z):
    return lib.vp_query_cell(instance, c_int(x), c_int(z))
def vp_query_cell_revision(instance, x, z, revision):
    return lib.vp_query_cell_revision(instance, c_int(x), c_int(z), c_int(revision))
def vp_object_add(instance):
    return lib.vp_object_add(instance)
def vp_object_load(instance):
    return lib.vp_object_load(instance)
def vp_object_bump_begin(instance, object_id, session_to):
    return lib.vp_object_bump_begin(instance, c_int(object_id), c_int(session_to))
def vp_object_bump_end(instance, object_id, session_to):
    return lib.vp_object_bump_end(instance, c_int(object_id), c_int(session_to))
def vp_object_change(instance):
    return lib.vp_object_change(instance)
def vp_object_click(instance, object_id, session_to, hit_x, hit_y, hit_z):
    return lib.vp_object_click(instance, c_int(object_id), c_int(session_to),
                               c_float(hit_x), c_float(hit_y), c_float(hit_z))
def vp_object_delete(instance, object_id):
    return lib.vp_object_delete(instance, c_int(object_id))
def vp_object_get(instance, object_id):
    return lib.vp_object_get(instance, c_int(object_id))
def vp_world_list(instance):
    return lib.vp_world_list(instance, c_int(0))
def vp_user_attributes_by_id(instance, user_id):
    return lib.vp_user_attributes_by_id(instance, c_int(user_id))
def vp_user_attributes_by_name(instance, name):
    return lib.vp_user_attributes_by_name(instance, c_char_p(name.encode("utf-8")))
##def vp_friends_get(instance):
##def vp_friend_add_by_name(instance, name):
##def vp_friend_delete(instance, friend_user_id):
##def vp_terrain_node_set(instance, tile_x, tile_z, node_x, node_z, cells):
##def vp_avatar_click(instance, avatar_session):
##def vp_teleport_avatar(instance, target_session, world, x, y, z, yaw, pitch):
##def vp_url_send(instance, session_id, url, url_target):
##def vp_join(instance, user_id):
##def vp_join_accept(instance, retuest_id, world, x, y, z, yaw, pitch):
##def vp_join_decline(instance, request_id):
##def vp_world_permission_user_set(instance, permission, user_id, enable):
##def vp_world_permission_session_set(instance, permission, session_id, enable):
##def vp_world_setting_set(instance, setting, value, session_to):

