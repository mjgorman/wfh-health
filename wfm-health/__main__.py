import sys
import json
from time import sleep
from datetime import datetime
from os.path import expanduser
from notipy_osx import notify, choice_prompt, dialog_prompt


def setup(config: dict) -> None:
    config['name'] = dialog_prompt(text='Give us your name', default_answer='').text_returned
    config['messaging'] = choice_prompt(['nice', 'mean'], ['nice'], text=f'Okay, {config["name"]}, What theme should the messaging take?')
    confirm_messaging = dialog_prompt(text=f'Okay, {config["messaging"]} it is...', buttons=['Ok', 'Maybe not..'])
    if confirm_messaging.button_returned == 'Maybe not..':
        notify(title='Aborted',
               identity_image='icons/house.png')
        sys.exit(1)
    with open(expanduser('~') + '/.wfh-health', 'w') as f:
        f.write(json.dumps(config))

def check_for_transition(time_diff: int, transition_time: bool = False) -> bool:
    if time_diff % 90 == 0:
        transition_time = True
    return transition_time

def check_for_break(time_diff: int, break_time: bool = False) -> bool:
    if time_diff % 20 == 0:
        break_time = True
    return break_time

def transition(position: str) -> str:
    if position == 'Stainding':
        position == 'Sitting'
    else:
      position == 'Standing'

    notify(title='CHANGE PLACES!',
           subtitle=f'Alright, time to start {position}',
           sound=True)
    return position

def take_a_break() -> None:
    notify(title='Take a break',
           subtitle='Stretch out, maybe get some water',
           sound=True)

def main_loop(config: dict)-> None:
    position = choice_prompt(['Sitting', 'Standing'], ['Sitting'], text='How will you be starting?')
    start_time = datetime.now()
    tracking = True
    notify(title=f'Tracking Started, {config["name"]}',
           subtitle=f'you will be {position} for 90 minutes',
           identity_image='icons/house.png')
    sleep(60)
    while(tracking):
        time_diff = int((datetime.now() - start_time).seconds/60)
        break_time = check_for_break(time_diff)
        transition_time = check_for_transition(time_diff)
        if transition_time:
            position = transition(position)
        elif break_time:
            take_a_break()
        sleep(60)

if __name__ == "__main__":
    try:
        with open(expanduser('~') + '/.wfh-health', 'r') as f:
            config = json.loads(f.readline())
            print(f'Config loaded, welcome back {config["name"]}')
    except Exception as e:
        print(e)
        config = {}
        setup(config)

    main_loop(config)
