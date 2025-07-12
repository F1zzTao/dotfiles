import os
import random

ICON_PATH = "~/.config/hypr/scripts/HuTaoIcons/"

ICON_PATH = os.path.expanduser(ICON_PATH)

# Some Hu Tao quotes pulled from the wiki
QUOTES = (
    ("One client, two clients, three clients!",),
    (
        "When the sun's out, bathe in sunlight.",
        "But when the moon's out, bathe in moonlight~",
    ),
    ("Oh, you sleepy?", "Get some rest, I'm gonna take a walk by myself..."),
    ("My hat's gonna get blown away!",),
    (
        "Well are those who rise in the early morn,",
        "while those late to bed I shall forewarn~",
    ),
    ("Hee-hee, moon's out, and so am I!",),
    (
        'Hu as in "Who put me in this coffin?" and Tao as in "I can\'t geT OUt!"',
        "Hehe... No, not funny?",
    ),
    (
        "Lemme show you some fire tricks.",
        "First... Fire! And then... Whoosh! Fire butterfly! Be free!",
    ),
    (
        "Run around all you like during the day, but",
        "you should be careful during the night. When I'm not around, best keep your wits about you.",
    ),
    (
        "Need a hand, need a hand? I'm here!",
        "If you need some assistance, I'm here to give it my all to the very end!",
    ),
    (
        "Have you seen Qiqi? Tell me where",
        "she is, quickly. I need to go seal her away, hee-hee!",
    ),
    (
        "♪ Silly-churl, billy-churl, silly-billy hilichurl.",
        "Frilly-churl, willy-churl, frilly-willy hilichurl ♪ Ah, hehe...",
    ),
    (
        "A bright moon aloft amid the vast,",
        "clear skies... Moments like these are just perfect for writing poetry.",
    ),
    ("O-ya?", "O-ya-ya-ya?"),
)

random_quote = random.choice(QUOTES)

with os.scandir(ICON_PATH) as files:
    # Scanning the entire directory and picking files only
    icons = [entry.path for entry in files if entry.is_file()]

random_icon = random.choice(icons)

# `notify-send` command builder
cmd = f'notify-send -i "{random_icon}"'
cmd += f' "{random_quote[0]}"'

if len(random_quote) > 1:
    cmd += f' "{random_quote[1]}"'

os.system(cmd)
