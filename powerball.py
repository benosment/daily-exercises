#! /usr/bin/env python3

import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='matcher')
    parser.add_argument('balls', action='store', nargs='+',
                        help='powerball balls')
    parser.add_argument('--filename', help='filename with a list of tickets',
                        action='store')
    args = parser.parse_args()
    if len(args.balls) != 6:
        print("Error: need to specify 6 balls")
    return args

def check_win(reg_count, pb_match):
    if pb_match and (reg_count == 0):
        return 4
    elif pb_match and (reg_count == 1):
        return 4
    elif pb_match and (reg_count == 2):
        return 7
    elif not pb_match and (reg_count == 3):
        return 7
    elif pb_match and (reg_count == 3):
        return 100
    elif not pb_match and (reg_count == 4):
        return 100
    elif pb_match and (reg_count == 4):
        return 50000
    elif not pb_match and (reg_count == 5):
        return 1000000
    elif pb_match and (reg_count == 5):
        return 1500000000
    else:
        return 0


def check_entry(winning_balls, regular_balls, powerball):
    winning_regular_balls = winning_balls[0:5]
    winning_powerball = winning_balls[5]
    reg_count = 0
    matches = []
    pb_match = (winning_powerball == powerball)
    for ball in winning_regular_balls:
        if ball in regular_balls:
            matches.append(ball)
            reg_count += 1
    win_amount = check_win(reg_count, pb_match)
    print("Matched: %d reg balls [%s], PB: %s won $%d" %
            (reg_count, ','.join(matches), pb_match,
            win_amount))
    return win_amount


def match(filename, winning_balls):
    entry_count = 1
    total_win = 0
    with open(filename) as f:
        for entry in f.readlines():
            balls = entry.split()
            regular_balls = balls[0:5]
            powerball = balls[5]
            print("Entry %d: regular: %s powerball: %s" %
                  (entry_count, ' '.join(regular_balls), powerball))
            total_win += check_entry(winning_balls, regular_balls, powerball)
            entry_count += 1
    print("Total winnings: $%d" % total_win)


if __name__ == '__main__':
    args = parse_args()
    match(args.filename, args.balls)
