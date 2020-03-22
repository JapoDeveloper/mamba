import sys
import time

config = {
    'w_session'  :{ 'name':'Work session',  'message':'Come to work!' },
    'b_session'  :{ 'name':'Break session', 'message':'Take a short break!' },
    'lb_session' :{ 'name':'Long break session', 'message':'Take a long break!' }
}

def notify(message):
    """Print the given message n times in the console"""
    print()
    for i in range(1, 3):
        print('*' * i, f'{message}')
        time.sleep(2)

def start_session(session):
    """Execute a session and keep track of the time left to the session end"""
    notify(session.get('message'))
    min = session.get('time') - 1
    while min >= 0:
        for sec in range(59, -1, -1):
            print(f'{session.get("name")} > {min:02d}m {sec:02d}s left')
            time.sleep(1)
        min -= 1

def next_session(counter):
    """Determine what is the next session base in the number of sessions that were executed"""
    if counter % config.get('frequency') == 0:
        return config.get('lb_session')
    elif counter % 2 == 0:
        return config.get('b_session')
    else:
        return config.get('w_session')

def apply_config(wtime=25, btime=5, lbtime=15, frequency=4):
    try:
        
        if int(wtime) < 1:
            print('* Min work session time accepted is 1')
            wtime = 1
        if int(btime) < 1:
            print('* Min break session time accepted is 1')
            btime = 1
        if int(lbtime) < 1:
            print('* Min long break session time accepted is 1')
            lbtime = 1
        if int(frequency) < 2:
            print('* Min frequency accepted is 2')
            frequency = 2    
        
        config.get('w_session').setdefault('time',int(wtime))
        config.get('b_session').setdefault('time',int(btime))
        config.get('lb_session').setdefault('time',int(lbtime))
        config.setdefault('frequency',int(frequency))

        print(f'Configuration: {config}')
        return True
    except Exception as e:
        print('* Cannot config the program.')
        print('\tReason:',e)
        return False

def main(argv):
    if apply_config(*argv):
        sessions_counter = 1
        while True:
            start_session(next_session(sessions_counter))
            sessions_counter += 1

if __name__ == '__main__':
    main(sys.argv[1:])