#!/usr/bin/python3
# -*- coding: utf-8 -*-
    
import sys
    
import re
    
header='[SFEN "lnsgkgsnl/1r5b1/ppppppppp/9/9/9/PPPPPPPPP/1B5R1/LNSGKGSNL b - 1"]'
alpha =   list('abcdefghi')
zensuji = list('１２３４５６７８９')
kansuji = list('一二三四五六七八九')
    
zen_map = dict(zip(zensuji, range(1,10)))
kan_map = dict(zip(kansuji, alpha))
    
piece   = '歩香桂銀金角飛玉と馬龍'
piece_map   = dict(zip(list('歩香桂銀金角飛玉') + list('と馬龍'),
                       list('PLNSGBRK')+ ['+P', '+B', '+R']))
    
line_re = re.compile('( *\\d+) +([^ ]+)')


def parse_kif(f):
    move_list = []
    for i in f:
        res = line_re.match(i)
        if res:
            num = int(res.groups()[0])
            s = res.groups()[1]
            if s[0] in zensuji:
                next_position = "%d%s" % (zen_map[s[0]], kan_map[s[1]])
            elif s[0] == '同':
                pass
            elif s[0] == '反' or s[0] == '切' or s[0] == '投':
                break
            else:
                raise RuntimeError("Unknown Move", s[0])
            if s[2] in piece:
                piace_name = piece_map[s[2]]
                rest = s[3:]
            elif s[2] == '成':
                piace_name = '+' + piece_map[s[3]]
                rest = s[4:]
            else:
                raise RuntimeError("Unknown Piece", s[2])
            promote = ''
            if rest[0] == '成':
                promote = '+'
                prev_position = rest[2] + alpha[int(rest[3])-1] + '-'
            elif rest[0] == '打':
                prev_position = '*'
            elif rest[0] == '(':
                prev_position = rest[1] + alpha[int(rest[2])-1] + '-'
            else:
                raise RuntimeError("Unknown ???", rest[0])
            move_list.append("%s%s%s%s" % (piace_name, prev_position,
                                           next_position , promote))
    return move_list


def as_psn(move_list):
    s = header + '\n'
    if len(move_list) % 2 != 0:
        move_list.append("")
    move_black = move_list[0::2]
    move_white = move_list[1::2]
    pair = zip(move_black, move_white)
    for i,j in enumerate(pair):
        s += ("%d. %s %s" % (i+1, j[0], j[1])) + '\n'
    return s


def main():
    f = open(sys.argv[1])
    move_list = parse_kif(f)
    print(as_psn(header, move_list))


if __name__ == '__main__':
    main()
            
