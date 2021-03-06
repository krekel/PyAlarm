#! /usr/bin/env python3
import argparse
import sys
import time
import webbrowser
import random


def main():
    try:
        parser = argparse.ArgumentParser(description='Video alarm')
        parser.add_argument('mode', choices=['alarm', 'random'],
                            help='Choose a mode. Alarm mode works only with 24hr format')
        parser.add_argument('hour', type=validate, nargs='?', default='00')
        parser.add_argument('minutes', type=validate, nargs='?', default='00')
        parser.add_argument('--span', type=int, nargs='?', const=2, help='Random Mode: Set time span in hours')
        args = parser.parse_args()
        print(args)

        if args.mode == 'random':
            if args.span is not None:
                span = int(time.strftime('%H')) + args.span
            else:
                span = int(time.strftime('%H')) + 2

            h = random.randint(int(time.strftime('%H')), int(span))
            r_minute = '{:02d}'.format(random.randint(int(time.strftime('%M')), 59))

            if h >= 24:
                r_hour = '{:02d}'.format(h - 24)
            else:
                r_hour = '{:02d}'.format(h)

            r_time = r_hour + r_minute
            print(r_time)
            open_browser(r_time)
        else:
            alarm = args.hour + args.minutes
            open_browser(alarm)
    except KeyboardInterrupt:
        print()


def open_browser(input_time):
    curr_time = time.strftime('%H%M')
    with open('/home/krekel/PycharmProjects/PyAlarm/videos', 'r') as f:
        video = random.choice(f.readlines())

    while input_time != curr_time:
        curr_time = time.strftime('%H%M')
        time.sleep(1)

    if input_time == curr_time:
        webbrowser.open(video)


def validate(value):
    if 0 <= int(value) <= 23 or 0 <= int(value) <= 59:
        return '{:02d}'.format(int(value))
    else:
        raise argparse.ArgumentError


if __name__ == '__main__':
    main()
    sys.exit(0)
