###     Configuration     ###

IP_ADDRESS = 'pi@192.168.125.1'
SSH_PASSWORD = 'wallaby'
ZIP_NAME = '.game.zip'
PROJECT_PATH = '/home/root/Documents/KISS/Default\\ User/botball-game'

###   End Configuration   ###

import os

def cmd(command):
    os.system(command)

sshpass = f'sshpass -p {SSH_PASSWORD}'

cmd('clear')

# Bundle the project into a .zip
print('Bundling project...\n')
cmd(f'zip -r {ZIP_NAME} . -x \\*__pycache__\\* -x .\\* -x .\\*/')

# Copy the .zip over to the robot
print('\nCopying project to robot...\n')
cmd(f'{sshpass} scp {ZIP_NAME} {IP_ADDRESS}:{PROJECT_PATH}/{ZIP_NAME}')

# Run the game on the robot
print('\nStarting game...\n')
cmd(f'{sshpass} ssh {IP_ADDRESS} python3 {PROJECT_PATH}/{ZIP_NAME}')
