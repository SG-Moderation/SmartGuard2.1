import weechat
import re
import sys

# Replce "path/to/SmartGuard2.1/" with the path to SmartGuard2.0 on your device.
# For e.g., "/home/src4026/SmartGuard2.1"
sys.path.insert(0, "path/to/SmartGuard2.1/")

mod_channels = [
        "##minetest-ctf"
]

log_irc_server = "libera"
log_irc_channel = "##smartguard"

from blacklist import blacklist1, blacklist2
from smartguard import SmartGuard

PLUGIN_NAME = "SmartGuard2.1"
PLUGIN_DESCRIPTION = "Aids moderation by narrowing messages down to suspicious ones."
PLUGIN_AUTHOR = "GreenBlob and s20"
PLUGIN_VERSION = "2.1.0.0"
PLUGIN_LICENSE = "GPL-3.0"



def strip_color_codes(message):
  pattern = re.compile(r"\x03(?:\d{1,2}(?:,\d{1,2})?)?|\x0f", re.UNICODE)
  return pattern.sub("", message)


def hook_print_cb(data, signal, signal_data):
    weechat.prnt("", signal_data)
    parsed_message = weechat.info_get_hashtable("irc_message_parse", {"message": signal_data})
    if parsed_message["channel"] in mod_channels:
        message_original = strip_color_codes(parsed_message["text"])
        msg_org = message_original.split(maxsplit=1)
        msg_auth = msg_org[0]
        msg_cont = msg_org[1] if len(msg_org) > 1 else ""
        sus_check = SmartGuard()
        buffer = weechat.info_get("irc_buffer", f"{log_irc_server},{log_irc_channel}")
        if sus_check.is_sus(msg_cont, msg_auth, blacklist1, blacklist2):
            log_message = f'Player {msg_auth} said "{msg_cont}"'
            weechat.command(buffer, log_message)
    return weechat.WEECHAT_RC_OK


if __name__ == '__main__':
    weechat.register(
            PLUGIN_NAME,
            PLUGIN_AUTHOR,
            PLUGIN_VERSION,
            PLUGIN_LICENSE,
            PLUGIN_DESCRIPTION,
            "",
            ""
    )

    hook = weechat.hook_signal("*,irc_in2_privmsg", "hook_print_cb", "")

