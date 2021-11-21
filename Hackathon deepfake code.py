import mcpi.minecraft as minecraft
import mcpi.block as block
from time import sleep
import mcpi.entity as Entity
from mcpi.vec3 import Vec3

mc = minecraft.Minecraft.create()
# player one's id (whoever is going to be recording)
player = mc.getPlayerEntityId('febitt1')
# player two's id (the target player)
player_two = mc.getPlayerEntityId('Borseman')

record = 0
replay = 0
replay_time_amount = 45
recorded_pos = []
recorded_dir = []
loaded_pos = []
loaded_dir = []
timer = 5

try:
    #   load the positions file and append each line to a list
    a_file = open('positions.txt', 'r')
    for line in a_file:
        stripped_line = line.strip()
        stripped_line_vec = Vec3(stripped_line)
        loaded_pos.append(stripped_line)

    print("positional file has been opened")

    a_file.close()
    #   load the directions file and append each line to a list
    b_file = open('directions.txt', 'r')
    for line in b_file:
        stripped_line = line.strip()
        stripped_line_vec = Vec3(stripped_line)
        loaded_dir.append(stripped_line)

    print("directional file has been opened")

    b_file.close()
    mc.postToChat("Replay file has been found!")

    mc.postToChat("Starting Replay in...")
    while timer > 0:
        sleep(1)
        time = str(timer)
        mc.postToChat(time)
        timer -= 1

    # replaying loaded save files is still in alpha stages (not functional)
    index_value = 0
    replay = 0
    while replay < replay_time_amount:
        ### for position
        inputpos = loaded_pos[index_value]
        # split the pos line into 3 elements, convert them from strings to float data types
        string = inputpos.split(",")
        x_str = float(string[0])
        y_str = float(string[1])
        z_str = float(string[2])
        # combine those elements into a vector 3
        final_pos_vector = Vec3(x_str, y_str, z_str)
        ### for direction
        inputdir = loaded_dir[index_value]
        # split the dir line into 3 elements, convert them from strings to float data types
        dir_string = inputdir.split(",")
        x_dir = float(dir_string[0])
        y_dir = float(dir_string[1])
        z_dir = float(dir_string[2])
        # combine those elements into a vector 3
        final_dir_vector = Vec3(x_dir, y_dir, z_dir)

        # set player pos and dir to the two vector 3 variables
        mc.entity.setPos(player_two, final_pos_vector)
        mc.entity.setDirection(player_two, final_dir_vector)

        sleep(0.14)

        index_value += 1
        replay += 1

    mc.postToChat("Replay Complete!")

except:
    mc.postToChat("no file found, creating new sequence")
    print("no file found, creating new sequence")
    # starting countdown for user to get ready
    while timer > 0:
        sleep(1)
        time = str(timer)
        mc.postToChat(time)
        timer -= 1

    mc.postToChat("Recording..")
    # iterate for however long you want to record for
    index_loop = 0
    while record < replay_time_amount:
        # collect P1 positional and directional arguments, append them to a list
        playerPos = mc.entity.getPos(player)
        playDir = mc.entity.getDirection(player)

        recorded_pos.append(playerPos)
        recorded_dir.append(playDir)
        record = record + 1
        sleep(0.1)
        index_loop += 1

    # format and write the contents of the list on to a file in the main directory
    with open('positions.txt', 'w') as fp:
        for x in recorded_pos:
            replacer = str(x).replace("Vec3", "")
            replacer2 = replacer.replace("(", "")
            replacer3 = replacer2.replace(")", '')
            fp.write(str(replacer3) + "\n")
            # print(replacer3)

    with open('directions.txt', 'w') as fp:
        for x in recorded_dir:
            replacer = str(x).replace("Vec3", "")
            replacer2 = replacer.replace("(", "")
            replacer3 = replacer2.replace(")", '')
            fp.write(str(replacer3) + "\n")
            # print(replacer3)

    mc.postToChat("Replay Started!")
    # iterate for the same amount of time
    index_value = 0
    while replay < replay_time_amount:
        # index the positional and directional lists for the nth iteration in the list
        second_player_pos = recorded_pos[index_value]
        second_player_dir = recorded_dir[index_value]

        # set the second players positional and direction values to that of the current index
        mc.entity.setPos(player_two, second_player_pos)
        mc.entity.setDirection(player_two, second_player_dir)

        sleep(0.14)

        index_value += 1
        replay += 1

    mc.postToChat("Replay Complete!")