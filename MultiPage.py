#!/usr/bin/env python2

import sys, subprocess as sub

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: Multipage.py <# of pages> [add|sub|mul|div]')
        exit(0)
    type = sys.argv[2]
    limit = min(int(sys.argv[1]),100)
    output = open('Worksheet.log','w+')
    bufsize = 10000
    for i in xrange(limit):
        cmd1 = './Worksheet.py %s > Worksheet%02d.tex' %(type,i)
        p1 = sub.Popen(['/bin/bash', '-c', cmd1], stdout=sub.PIPE)
        output.write(p1.stdout.read())
        cmd2 = 'pdflatex Worksheet%02d.tex' %(i)
        p2 = sub.Popen(['/bin/bash', '-c', cmd2], stdout=sub.PIPE)
        output.write(p2.stdout.read())
    cmd3 = '/usr/bin/pdftk Worksheet*.pdf cat output Worksheet.pdf'
    p3 = sub.Popen(['/bin/bash', '-c', cmd3], stdout=sub.PIPE)
    output.write(p3.stdout.read())
