# SmartGuard

<img src="./assets/SmartGuard.png" align="right"
 alt="SmartGuard logo by s20 and GreenBlob" width="192" height="192">

A WeeChat addon that aids moderation by reading messages received real-time in channels and narrowing them down into suspicious messages that may contain potential swears. With this tool you don't have to read every single message in the chat you're moderating; this addon narrows everything down to a _way_ smaller collection.

## Ability
Most cases of swear filter bypass are caught.
- Blending with other words: `hellofvck3you`
- Repetition or distortion: `sSsHhh54%*IITtt!`
- Multiline:
    ```
    <player> f
    <player> u
    <player> you
    ```
- Usage of ignorable characters: `s_h_! t`
- Swear word variants: `phuq`
- All caps: `THIS MESSAGE IS ALMOST in ALL CAPS`

## Installation and Setup
- Clone the addon in any directory:
    ```
    git clone https://github.com/SG-Moderation/SmartGuard2.1.git
    ```
- Next, open the cloned folder and open `main.py` with an editor. Edit `"path/to/SmartGuard2.1/"` with the directory of the script. For example:
    ```python
    sys.path.insert(0, "/home/src4026/SmartGuard2.1/")
    ```
- To load the addon, open WeeChat and type the below command and press <kbd>Enter</kbd> (remember to replace the path in the example below with the actual directory of `main.py`):
    ```
    /script load /home/src4026/SmartGuard2.1/main.py
    ```

### Autoloading
TODO

### Important information
- By default, the addon uses your IRC account to send all flagged messages to the ##smartguard channel on IRC. You can edit the channel the flagged messages are sent to by editing the `log_irc_channel` value and the respective IRC server by editing the `log_irc_server` value in `main.py`.
- For instructions on how to add your own words to the blacklists in [`blacklist.py`](blacklist.py), read the comments mentioned in it.

## Licenses
This project is licensed under the [GNU General Public License v3.0](LICENSE). The logo of this project - [`SmartGuard.png`](./assets/SmartGuard.png) -  is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) by [s20](https://github.com/src4026/) and [GreenBlob](https://github.com/a-blob/).

