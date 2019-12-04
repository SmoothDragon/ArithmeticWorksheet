#!/usr/bin/env python2

import random, sys


class addition:
    def __init__(self,limit=10):
        self.Title = 'Addition Facts'
        self.x = 8
        self.y = 10
        self.limit = min(limit,1000)
        
    def random(self):
        self.a = random.randrange(self.limit)
        self.b = random.randrange(self.limit)
    
    def __str__(self):
        s = '%d + %d = __' %(self.a,self.b)
        return s

    def _latex_(self):
        s = r'$\begin{array}{l@{}r}'+'\n'
        s += r'& %d\\'%(self.a)+'\n'
        s += r'+ & %d\\'%(self.b)+'\n'
        s += r'\hline'+'\n'
        s += r'\end{array}$'+'\n'
        return s

class subtraction:
    def __init__(self,limit=10):
        self.Title = 'Subtraction Facts'
        self.x = 8
        self.y = 10
        self.limit = min(limit,1000)
        
    def random(self):
        self.a = random.randrange(self.limit)
        self.b = random.randrange(self.limit)
        if self.a < self.b:
            (self.a,self.b) = (self.b,self.a)
    
    def __str__(self):
        s = '%d - %d = __' %(self.a,self.b)
        return s

    def _latex_(self):
        s = r'$\begin{array}{l@{}r}'+'\n'
        s += r'& %d\\'%(self.a)+'\n'
        s += r'- & %d\\'%(self.b)+'\n'
        s += r'\hline'+'\n'
        s += r'\end{array}$'+'\n'
        return s


class multiplication:
    def __init__(self,limit=10):
        self.Title = 'Multiplication Facts'
        self.x = 8
        self.y = 10
        self.limit = min(limit,1000)

    def random(self):
        self.a = random.randrange(self.limit)
        self.b = random.randrange(self.limit)
        if self.a < self.b:
            self.a,self.b = self.b,self.a
    
    def __str__(self):
        s = '%d * %d = __' %(self.a,self.b)
        return s

    def _latex_(self):
        s = r'$\begin{array}{l@{}r}'+'\n'
        s += r'& %d\\'%(self.a)+'\n'
        s += r'\times & %d\\'%(self.b)+'\n'
        s += r'\hline'+'\n'
        s += r'\end{array}$'+'\n'
        return s

class division:
    def __init__(self,limit=10):
        self.Title = 'Division Facts'
        self.x = 8
        self.y = 10
        self.limit = min(limit,1000)
            
    def random(self):
        self.b = random.randrange(1,self.limit)
        self.a = random.randrange(1,self.limit)*self.b
        if self.b == 0:
            self.a,self.b = self.b,self.a
    
    def __str__(self):
        s = '%d \ %d = __' %(self.a,self.b)
        return s

    def _latex_(self):
        s = r'$\begin{array}{l@{}r}'+'\n'
        s += r'& %d\\'%(self.a)+'\n'
        s += r'\div & %d\\'%(self.b)+'\n'
        s += r'\hline'+'\n'
        s += r'\end{array}$'+'\n'
        return s

class Beth:
    def __init__(self,limit=10):
        self.Title = 'Multiplication Facts'
        self.x = 8
        self.y = 10
        self.limit = min(limit,1000)

    def random(self):
        self.a = random.randrange(self.limit)
        self.b = random.randrange(6,10)
        if random.randrange(2) == 0:
            self.a,self.b = self.b,self.a

    def __str__(self):
        s = '%d * %d = __' %(self.a,self.b)
        return s

    def _latex_(self):
        s = r'$\begin{array}{l@{}r}'+'\n'
        s += r'& %d\\'%(self.a)+'\n'
        s += r'\times & %d\\'%(self.b)+'\n'
        s += r'\hline'+'\n'
        s += r'\end{array}$'+'\n'
        return s

bstr_pos = lambda n: n>0 and bstr_pos(n>>1)+str(n&1) or ''
def bin(i,n=0):
    return bstr_pos(i).rjust(n,'0')
    
class binary:
    def __init__(self,limit=4):
        self.Title = 'Binary Operations'
        self.x = 6
        self.y = 10
        self.limit = min(limit,8)
        self.ops = (r'\wedge',r'\vee',r'\oplus')

    def random(self,limit=4):
        self.a = random.randrange(2**limit)
        self.b = random.randrange(2**limit)
        self.op = self.ops[random.randrange(len(self.ops))]
    
    def __str__(self):
        limit = 4
        s = '%s %s %s = ' %(bin(self.a,self.limit),self.op,bin(self.b,self.limit))
        return s

    def _latex_(self):
        s = r'$\begin{array}{l@{}r}'+'\n'
        s += r'& %s\\'%(bin(self.a,self.limit))+'\n'
        s += self.op
        s += r' & %s\\'%(bin(self.b,self.limit))+'\n'
        s += r'\hline'+'\n'
        s += r'\end{array}$'+'\n'
        return s

class axb:
    def __init__(self,limit=10):
        self.Title = 'Solve for $x$'
        self.x = 4
        self.y = 14
        self.limit = min(limit,100)

    def random(self):
        x = random.randrange(self.limit)
        self.a = random.randrange(1,self.limit)
        self.b = random.randrange(1,self.limit)
        self.c = self.a*x+self.b
    
    def __str__(self):
        if self.a == 1:
            t = '  '
        else:
            t = '%2d' %(self.a)
        s = '%sx + %2d = %2d' %(t,self.b,self.c)
        return s

    def _latex_(self):
        if self.a == 1:
            t = '  '
        else:
            t = '%2d' %(self.a)
        s = '$%sx + %2d = %2d$' %(t,self.b,self.c)
        return s


class Algebra1:
    def __init__(self,limit=10):
        self.Title = 'Multiply out'
        self.x = 3
        self.y = 14
        self.limit = min(limit,100)

    def random(self):
        x = random.randrange(self.limit)
        self.a = random.randrange(2,self.limit)
        self.b = random.randrange(1,self.limit)
    
    def __str__(self):
        s = '(x + %d)(x + %d)=' %(self.a,self.b)
        return s

    def _latex_(self):
        s = '$%d(x + %d)=$'%(self.a,self.b)
        return s

class Algebra2:
    def __init__(self,limit=10):
        self.Title = 'Multiply out'
        self.x = 3
        self.y = 14
        self.limit = min(limit,100)

    def random(self):
        self.a = random.randrange(1,self.limit)
        self.b = random.randrange(1,self.limit)
    
    def __str__(self):
        s = '(x + %d)(x + %d)=' %(self.a,self.b)
        return s

    def _latex_(self):
        s = '$(x + %d)(x + %d)=$' %(self.a,self.b)
        return s

class Algebra3:
    def __init__(self,limit=10):
        self.Title = 'Multiply out'
        self.x = 3
        self.y = 14
        self.limit = min(limit,100)

    def random(self):
        self.a = random.randrange(2,self.limit)
        self.b = random.randrange(1,self.limit)
        self.c = random.randrange(2,self.limit)
        self.d = random.randrange(1,self.limit)
    
    def __str__(self):
        s = '(%dx + %d)(%dx + %d)=' %(self.a,self.b,self.c,self.d)
        return s

    def _latex_(self):
        s = '$(%dx + %d)(%dx + %d)=$' %(self.a,self.b,self.c,self.d)
        return s

class Algebra4:
    def __init__(self,limit=10):
        self.Title = 'Multiply out'
        self.x = 3
        self.y = 14
        self.limit = min(limit,100)
        self.ops = ('+','-')

    def random(self):
        self.a = random.randrange(1,self.limit)
        self.b = random.randrange(1,self.limit)
        self.As = self.ops[random.randrange(len(self.ops))]
        self.bs = self.ops[random.randrange(len(self.ops))]
    
    def __str__(self):
        s = '(x %s %d)(x %s %d)=' %(self.As,self.a,self.bs,self.b)
        return s

    def _latex_(self):
        s = '$(x %s %d)(x %s %d)=$' %(self.As,self.a,self.bs,self.b)
        return s

class ModularAddition:
    def __init__(self,limit=10):
        self.Title = 'Modular Addition'
        self.x = 3
        self.y = 14
        self.limit = min(limit,100)

    def random(self):
        self.m = random.randrange(2,self.limit)
        self.a = random.randrange(1,self.m)
        self.b = random.randrange(0,self.m)
    
    def __str__(self):
        s = '%d + %d (mod %d)' %(self.a,self.b,self.m)
        return s

    def _latex_(self):
        s = '$%d + %d \equiv \underline{\hspace{1cm}} \pmod{%d}$' %(self.a,self.b,self.m)
        return s

class ModularMultiplication:
    def __init__(self,limit=10):
        self.Title = 'Modular Multiplication'
        self.x = 3
        self.y = 14
        self.limit = min(limit,100)

    def random(self):
        self.m = random.randrange(2,self.limit)
        self.a = random.randrange(1,self.m)
        self.b = random.randrange(1,self.m)
    
    def __str__(self):
        s = '%d * %d (mod %d)' %(self.a,self.b,self.m)
        return s

    def _latex_(self):
        s = r'$%d \times %d \equiv \underline{\hspace{1cm}} \pmod{%d}$' %(self.a,self.b,self.m)
        return s

class ProblemPage:
    def random(self,eq):
        s = r'\documentclass[12pt]{article}'+'\n'
        s += r'\pagestyle{empty}'+'\n'
        s += r'\usepackage{sfmath}'+'\n'
        s += r'\oddsidemargin -0.5in'+'\n'
        s += r'\textwidth 7.5in'+'\n'
        s += r'\headheight 0.0in'+'\n'
        s += r'\topmargin -0.5in'+'\n'
        s += r'\textheight 10.0in'+'\n'
        s += r'\begin{document}'+'\n'
        s += r'\textsf{\Huge '
        s += '%s'%eq.Title
        s += r'} \hfill'
        s += r'\textsc{\large Name \underline{\hspace{3in}}\hspace{0.5in}}'+'\n'
        s += r'\centering'+'\n'

        s += r'\vfill'+'\n'
        s += r'\large'+'\n'
        s += r'\begin{tabular*}{7.5in}{r*{'
        s += '%d'%(eq.x+1)
        s += r'}{@{\extracolsep{\fill}}c}}'+'\n'
        s += r'\vspace{.5cm}'+'\n'
        letters = 'abcdefghijklmnopqrstuvwxyz'
        for j in letters[:eq.x]:
            s += '&\\it{%s}'%(j)
        s += r'\\'
        for i in range(eq.y):
            s += r'\vspace{1cm}'+'\n'
            s += '\\bf{%d.}'%(i+1)
            for j in range(eq.x):
                s += '&\n'
                eq.random()
                s += eq._latex_()
            s += r'\\'+'\n'
        s += r'\end{tabular*}'+'\n'
        s += r'\end{document}'+'\n'

        return s

if __name__ == '__main__':

    if len(sys.argv) > 1:
        v = sys.argv[1]
    else:
        v = None
    if v == 'add':
        eq = addition()
    elif v == 'sub':
        eq = subtraction()
    elif v == 'mul':
        eq = multiplication()
    elif v == 'beth':
        eq = Beth()
    elif v == 'div':
        eq = division()
    elif v == 'axb':
        eq = axb()
    elif v == 'quad':
        eq = Algebra2()
    elif v == 'quad2':
        eq = Algebra3()
    elif v == 'quad3':
        eq = Algebra4()
    elif v == 'bin':
        eq = binary()
    elif v == 'mod1':
        eq = ModularAddition()
    elif v == 'mod2':
        eq = ModularMultiplication()
    else:
        eq = addition()
    #eq = CreateQuadratics()
    #eq = Algebra1()
    #eq = binary()
    #eq = multiplication()
    #eq = division()
    #eq = subtraction(1000)
    #eq = subtraction(100)
    page = ProblemPage()
    print page.random(eq)
