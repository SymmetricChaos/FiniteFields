from Sequences import Drawing as draw
from Sequences.Combinatorics import motzkin_paths, dyck_words, catalan, pascal_triangle
from Sequences.Manipulations import segment

import numpy as np
from math import comb


def dyck_mountains(n=2):
    
    num_words = comb(2*n,n)//(n+1)
    
    size = 1
    while size*size < num_words:
        size += 1
    
    W = dyck_words(n)
    
    draw.make_blank_canvas([15,15],facecolor="lightgray")
    
    for pos,word in enumerate(W,1):
        draw.make_blank_plot(size,size,pos,[-4,4])
        x = -4
        y = -4
        
        for move in word:
            draw.connection_p((x,y),(x+(4/n),y+(4/n)*move))
            x = x+(4/n)
            y = y+(4/n)*move


def motzkin_mountains(n=2):
    
    num_words = sum([comb(n,2*k)*c for k,c in zip(range(0,n//2+1),catalan())])
    
    size = 1
    while size*size < num_words:
        size += 1
    
    W = motzkin_paths(n)
    
    draw.make_blank_canvas([15,15],facecolor="lightgray")
    
    for pos,word in enumerate(W,1):
        draw.make_blank_plot(size,size,pos,[-4,4])
        x = -4
        y = -3.95
        
        for move in word:
            draw.connection_p((x,y),(x+(8/n),y+(8/n)*move))
            x = x+(8/n)
            y = y+(8/n)*move


def pascal_triangle_art(n,circle_size=.15,text_size=8,circle_color="lavender",cavas_size=15):
    
    draw.make_blank_canvas([cavas_size,cavas_size],facecolor="lightgray")
    draw.make_blank_plot(1,1,1,[-4,4],[-4,4])
    draw.title("Pascal's Triangle",size=30)
    
    for k,row in enumerate(pascal_triangle(),0):
        y = 2.5-4*k/n
        x_space = np.linspace(-3.7*k/n,3.7*k/n,k+1)
        
        for x,val in zip(x_space,row):
            draw.circle_xy(x,y,circle_size,fc=circle_color)
            draw.text_xy(x,y,val,ha='center',va='center',size=text_size)
        if k >= n:
            break


def pascal_sierpinski_art(n,circle_size=.12,text_size=8,circle_color="cornflowerblue",cavas_size=15):
    
    draw.make_blank_canvas([cavas_size,cavas_size],facecolor="lightgray")
    draw.make_blank_plot(1,1,1,[-4,4],[-4,4])
    draw.title("Sierpinski Triangle\nBuilt From Pascal's Triangle",size=30)
    
    for k,row in enumerate(pascal_triangle(),0):
        y = 2.5-4*k/n
        x_space = np.linspace(-3.7*k/n,3.7*k/n,k+1)
        
        for x,val in zip(x_space,row):
            if val % 2 == 1:
                draw.circle_xy(x,y,circle_size,fc=circle_color)
            else:
                draw.circle_xy(x,y,circle_size,fc="white",ec="black")
            draw.text_xy(x,y,val,ha='center',va='center',size=text_size)
        if k >= n:
            break


# Each chord partitions the set of points into three sets: those on the chord, those to the "left", and those to the "right"
# We should be able to generate solutions by using this knowledge to then partition each partition
# Turns out to be some error in this implementation for n > 5
def motzkin_chords(n,cavas_size=15):
    
    draw.make_blank_canvas([cavas_size,cavas_size],facecolor="lightgray")
    
    th = np.linspace(0,2*np.pi,n+1)
    x = np.sin(th[:n])
    y = np.cos(th[:n])
    P = draw.xy_to_points(x,y)
    
    S = tuple([i for i in range(n)])
    
    def chord_recur(S):
        print(S)
        yield []
        for a in S:
            for b in S:
                if a < b:
                    for x in chord_recur(tuple([s for s in S if s > b])):
                        yield [(a,b)] + x
                    for x in chord_recur(tuple([s for s in S if s > a and s < b])):
                        if x != []:
                            yield [(a,b)] + x

    
    for ctr,i in enumerate(chord_recur(S),1):
        draw.make_blank_plot(8,8,ctr,[-1.2,1.2],[-1.2,1.2])
        draw.circle_xy(0, 0, 1, fc='white', ec='black')
        draw.circles_xy(x,y,[.1]*n)
        for pair in i:
            draw.connection_p(P[pair[0]],P[pair[1]],color='red')





# dyck_mountains(5)
# motzkin_mountains(5)
# pascal_triangle_art(14)
# pascal_sierpinski_art(15)
motzkin_chords(6)