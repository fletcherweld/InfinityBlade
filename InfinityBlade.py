from sys import exit
from textwrap import dedent
from sys import argv

script, user_name, world_name = argv


has_infinity_blade = False
has_crystal_key = False
has_key = False
tries = 1
prompt = '> '


def start():
    print(dedent(f"""
        
        A loud voice booms from the walls:
        "{user_name}! You are trapped here on {world_name} Island.
        To escape, find the Infinity Blade and defeat the Boss Monster."
        """))

    start_room()


def start_room():
    print(dedent("""
        You stand in the center of a brightly lit, large room with
        no windows. You see a large door under an archway, a small door
        on the opposite wall, and a trapdoor set in the ground.
        Which do you open?
        """))

    while True:
        choice = input(prompt).lower()

        if "large door" in choice or "archway" in choice:
            bridge()
        elif "small door" in choice:
            dark_room("start")
        elif "trapdoor" in choice:
            trapdoor_fall_room()
        else:
            print(dedent("""
                Try something else!
                """))

    


def bridge():
    global has_infinity_blade

    print(dedent("""
        The door closes slowly behind you. You are at the end of a long
        glass bridge without sides. The door behind you is set into a
        cliff, and below you rolls a thunderous ocean. Halfway across
        the bridge stands a ferocious monster.
        What do you do?
        """))

    while True:
        choice = input(prompt).lower()

        if "open" in choice or "door" in choice:
            print(dedent("""
                You try the door but it is locked behind you, with no place
                for a key. You must fight the monster or try to flee.
                """))
        elif "flee" in choice or "run" in choice:
            print(dedent("""
                Do you want to try to flee past the monster or jump over the
                edge of the bridge?
                """))
            choice = input(prompt).lower()
            if "past" in choice or "flee" in choice:
                dead("You try to make it past the monster but do not succeed. It tears you to pieces.")
            elif "jump" in choice or "dive" in choice or "swim" in choice:
                dead("You drown in the cold depths of the ocean.")
            else:
                print(dedent("""
                    Try something else!
                    """))
        elif "jump" in choice or "dive" in choice or "swim" in choice:
            dead("You drown in the cold depths of the ocean.")
        elif "fight" in choice or "attack" in choice or "kill" in choice:
            if has_infinity_blade:
                print(dedent(f"""
                    You swing the Infinity Blade, killing the monster, and walk
                    to the other side. You are free!

                    It took you {tries} tries.
                    """))
                exit(0)
            else:
                dead("You feebly try to fight the monster but it picks you up and throws you into the ocean.")
        elif choice == "cheat! monty python": # A little easter egg.
            has_infinity_blade = True
            print('')
        else:
            print(dedent("""
                Try something else!
                """))


def dark_room(entry):
    if entry == "start":
        print(dedent("""
            You enter a fairly small, dark room. There is a torch over
            the small door behind you. The room is empty except for two
            other doors. A stone door to your left, and a wooden door
            to your right.
            Which do you open?
            """))
    elif entry == "ladder":
        print(dedent("""
            You enter a fairly small, dark room through the stone door.
            There is a torch over one small door. There is also a wooden
            door in front of you.
            Which do you open?
            """))
    elif entry == "key":
        print(dedent("""
            You enter a fairly small, dark room through the wooden door.
            There is a torch over one small door. There is also a stone
            door in front of you.
            Which do you open?
            """))
    else:
        dead("Error in dark_room")

    while True:
        choice = input(prompt).lower()

        if "small door" in choice or ("door" in choice and "torch" in choice):
            start_room()
        elif "left" in choice or "stone" in choice:
            ladder_room("dark")
        elif "right" in choice or "wood" in choice:
            key_room("dark")
        else:
            print(dedent("""
                Try something else!
                """))



def ladder_room(entry):
    if entry == "dark":
        print(dedent("""
            You enter a tiny room through the stone door.
            There is as a trapdoor set into the floor.
            What do you do?
            """))
    elif entry == "stone":
        print(dedent("""
            You climb the ladder and enter a tiny room through the
            trapdoor. There is a stone door in front of you.
            What do you do?
            """))
    else:
        dead("Error in ladder_room")

    while True:
        choice = input(prompt).lower()

        if "trapdoor" in choice:
            stone_platform("ladder")
        elif "door" in choice or "stone" in choice:
            dark_room("ladder")
        else:
            print(dedent("""
                Try something else!
                """))



def key_room(entry):
    global has_crystal_key
    global has_key

    if  entry == "dark":
        print(dedent("""
            The wooden door closes behind you as you enter a well lit room.
            There is a vault door on the other side of the room. There are
            three keys on a table in the middle of the room. One is made
            of gold, one is made of ruby, and one is made of crystal.
            What do you do?
            """))
    elif entry == "sword":
        print(dedent("""
            The vault door closes behind you as you enter a well lit room.
            There is a wooden door on the other side of the room. There are
            three keys on a table in the middle of the room. One is made
            of gold, one is made of ruby, and one is made of crystal.
            What do you do?
            """))
    else:
        print("Error in key_room")
    
    while True:
        choice = input(prompt).lower()

        if "door" in choice and "vault" not in choice:
            dark_room("key")
        elif "vault" in choice and has_crystal_key:
            sword_room()
        elif "vault" in choice and not has_key:
            print(dedent("""
                You try to open the vault door but you need a key!
                """))
        elif "vault" in choice and has_key and not has_crystal_key:
            print(dedent("""
                You try the key but the door won't unlock. Try another key!
                What do you do?
                """))
        elif "crystal" in choice and "key" in choice:
            has_crystal_key = True
            has_key = True
            print(dedent("""
                You pick up the crystal key.
                What do you do?
                """))
            continue
        elif "ruby" in choice and "key" in choice:
            has_key = True
            print(dedent("""
                You pick up the ruby key.
                What do you do?
                """))
            continue
        elif "gold" in choice and "key" in choice:
            has_key = True
            print(dedent("""
                You pick up the gold key.
                What do you do?
                """))
            continue
        else:
            print(dedent("""
                Try something else!
                """))

        
def sword_room():
    global has_infinity_blade

    print(dedent("""
        You push open the vault door to reveal a large circular room.
        The room is empty except for the door and a huge, beautiful
        sword set in the middle. A sign labels it: Infinity Blade.
        What do you do?
        """))

    while True:
        choice = input(prompt).lower()

        if "door" in choice:
            key_room("sword")
        elif ("sword" in choice or "blade" in choice) and not has_infinity_blade:
            has_infinity_blade = True
            print(dedent(f"""
                You lift the mighty Infinty Blade and feel its power course
                through your body. You now stand in the middle of the room.

                The voice booms again:
                "Congratulations {user_name}! You have found the Infinity Blade.
                You must now find and kill the monster who defends {world_name} Island."
                What do you do?
                """))
        else:
            print(dedent("""
                Try something else!
                """))


def trapdoor_fall_room():
    print(dedent("""
        You fall down a ten foot drop into some cold water. Floundering
        to the surface, you see the water flows into a large room. The
        only other opening is the stone chute above you.
        What do you do?
        """))

    while True:
        choice = input(prompt).lower()

        if "swim" in choice:
            water_room("fall_room")
        elif "climb" in choice:
            print(dedent("""
                You try to scramble up the wall but there is no ladder.
                You fall back into the water.
                What do you do?
                """))
        elif "tread water" in choice:
            print(dedent("""
                You tread water, staying in place. Nothing happens.
                What do you do?
                """))
        else:
            print(dedent("""
                Try something else!
                """))


def water_room(entry):
    if entry == "fall_room":
        print(dedent("""
            You swim into a cavernous room filled with water. There is a
            dark tunnel leading into the distance in one wall, and a stone
            platform with a ladder in one corner.
            """))
    elif entry == "stone":
        print(dedent("""
            You dive into the cavernous room filled with water. There is a
            dark tunnel leading into the distance in one wall, and the stone
            platform with a ladder in one corner.
            """))
    else:
        dead("Error in water_room")

    while True:
        choice = input(prompt).lower()

        if "swim" in choice and "platform" in choice:
            stone_platform("water")
        elif "tread water" in choice:
            print(dedent("""
                You tread water, staying in place. Nothing happens.
                What do you do?
                """))
        elif "swim" in choice and "tunnel" in choice:
            dead("You swim into the tunnel and get pulled over a waterfall.")
        else:
            print(dedent("""
                Try something else!
                """))

        


def stone_platform(entry):
    if entry == "water":
        print(dedent("""
            You crawl up onto the stone platform in the corner of the
            water room. There is a ladder leading up to a trapdoor.
            What do you do?
            """))
    elif entry == "ladder":
        print(dedent("""
            You climb down the ladder onto a stone platform. It is in
            the corner of a cavernous room filled with water.
            What do you do?
            """))
    else:
        dead("Error in stone_platform")

    while True:
        choice = input(prompt).lower()

        if "ladder" in choice or "climb" in choice:
            ladder_room("stone")
        elif "swim" in choice or "water" in choice:
            water_room("stone")
        else:
            print(dedent("""
                Try something else!
                """))


def dead(how):
    global has_crystal_key
    global has_infinity_blade
    global has_key
    global tries

    print(dedent(f"""
        {how}

        Press RETURN to try again!
        """))

    tries += 1
    has_key = False
    has_crystal_key = False
    has_infinity_blade = False

    choice = input(prompt)
    start()

start()