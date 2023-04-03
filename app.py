_S='health'
_R='inf'
_Q='move'
_P='-inf'
_O='snakes'
_N='height'
_M='width'
_L='id'
_K=None
_J='length'
_I='body'
_H='up'
_G='down'
_F='right'
_E='board'
_D='left'
_C='you'
_B='y'
_A='x'
import random,typing,numpy
MIN_SCORE=float(_P)
DEFAULT_SCORE=0
LARGER_SNAKE_DANGER=3
SAME_SNAKE_DANGER=1
SMALLER_SNAKE_REWARD=0.5
EDGE_KILL_WEIGHT=2
HP_THRESH=30
LENGTH_AIM=2
AREA_AIM=20
len_you=0
def info():A='pixel';print('INFO');return{'apiversion':'1','author':'','color':'#3399FF','head':A,'tail':A}
def start(game_state):print('GAME START')
def end(game_state):print('GAME OVER\n')
def move(game_state):
        N='turn';B=game_state;A={_H:DEFAULT_SCORE,_G:DEFAULT_SCORE,_D:DEFAULT_SCORE,_F:DEFAULT_SCORE};C=B[_C][_I][0];O=B[_C][_I][1];L=B[_C][_I];G=B[_E][_O];P=B[_E]['food'];Q=B[_C][_J];D=B[_E][_M];H=B[_E][_N];print(Q);map=[[0 for A in range(D)]for A in range(H)];E=[[0 for A in range(D)]for A in range(H)];map,E=setBound(map,E,G,B);A=prevent_back(B,A,C,O);A=out_of_bounds(B,A,C);A=self_collision(A,C,L);A=opp_collision(B,A,C,L,G);M=[]
        for (I,R) in A.items():
                if R>MIN_SCORE:M.append(I)
        if len(M)==0:print(f"MOVE {B[N]}: No safe moves detected! Moving down");return{_Q:_G}
        J=floodFill(map,D,H,C[_A],C[_B]);print(f"spaces: {J}");S=max([A for(B,A)in J.items()]);T=[A for(A,B)in J.items()if B==S]
        for I in T:A[I]+=1
        if should_find_food(B,G):A=find_food(B,A,C,P,E);print('find food')       
        A=can_edge_kill(B,A);A=score(B,C,A,map,E);print(f"scores: {A}");U=max([A for(B,A)in A.items()]);K=[A for(A,B)in A.items()if B==U];F=K[0]
        if K==[_D,_F]or K==['rigth',_D]:
                if C[_A]<D//2:F=_F
                else:F=_D
        print(f"MOVE {B[N]}: {F}");return{_Q:F}
def out_of_bounds(game_state,moves,head):
        C=game_state;B=head;A=moves;D=C[_E][_M];E=C[_E][_N]
        if B[_A]>=D-1:A[_F]=MIN_SCORE
        if B[_A]<=0:A[_D]=MIN_SCORE
        if B[_B]<=0:A[_G]=MIN_SCORE
        if B[_B]>=E-1:A[_H]=MIN_SCORE
        return A
def prevent_back(game_state,moves,head,neck):
        C=neck;B=head;A=moves
        if C[_A]<B[_A]:A[_D]=MIN_SCORE
        elif C[_A]>B[_A]:A[_F]=MIN_SCORE
        elif C[_B]<B[_B]:A[_G]=MIN_SCORE
        elif C[_B]>B[_B]:A[_H]=MIN_SCORE
        return A
def self_collision(moves,head,body):
        E=body;B=moves;A=head
        for C in range(len(E)):
                D=MIN_SCORE
                if C==0 or C==1:continue
                F=E[C][_A];G=E[C][_B]
                if C==len(E)-1:D=-0.5
                if A[_B]==G:
                        if A[_A]+1!=_K and A[_A]+1==F:B[_F]+=D
                        elif A[_A]-1!=_K and A[_A]-1==F:B[_D]+=D
                elif A[_A]==F:
                        if A[_B]+1!=_K and A[_B]+1==G:B[_H]+=D
                        elif A[_B]-1!=_K and A[_B]-1==G:B[_G]+=D
        return B
def opp_collision(game_state,moves,head,body,opp):
        D=opp;C=moves;A=head
        for E in range(len(D)):
                if game_state[_C][_L]==D[E][_L]:continue
                for F in range(len(D[E][_I])):
                        B=D[E][_I][F]
                        if A[_A]==B[_A]:
                                if A[_B]+1!=_K and A[_B]+1==B[_B]:C[_H]+=MIN_SCORE
                                elif A[_B]-1!=_K and A[_B]-1==B[_B]:C[_G]+=MIN_SCORE
                        elif A[_B]==B[_B]:
                                if A[_A]+1!=_K and A[_A]+1==B[_A]:C[_F]+=MIN_SCORE
                                elif A[_A]-1!=_K and A[_A]-1==B[_A]:C[_D]+=MIN_SCORE
        return C
def dist(a,b):return abs(a[_A]-b[_A])+abs(a[_B]-b[_B])
def should_find_food(game_state,opp):
        D=False;C=game_state;A=C[_E][_O][:];B=C[_C];A.remove(B)
        if B[_S]<HP_THRESH:return True
        if len(A)==0:return D
        E=[A[_J]for A in A]
        if B[_J]-max(E)<=LENGTH_AIM:return True
        return D
def find_food(game_state,moves,head,foods,length_map):
        C=head;A=moves;E=float(_R);B={};D=HP_THRESH/game_state[_C][_S]
        for F in foods:
                G=dist(C,F)
                if G<E:B=F;E=G
        if B=={}:return A
        if B[_A]>C[_A]:A[_F]+=D
        if B[_A]<C[_A]:A[_D]+=D
        if B[_B]>C[_B]:A[_H]+=D
        if B[_B]<C[_B]:A[_G]+=D
        return A
def can_edge_kill(game_state,moves):
        D=game_state;C=moves;G=D[_E][_O];M=D[_C][_L];A=D[_C][_I][0];J=D[_C][_I][1];H=A[_A]-J[_A],A[_B]-J[_B];E=D[_E][_N];F=D[_E][_M]
        if len(G)==2:
                K=G[0]if G[0][_L]!=M else G[1];B=K[_I][0];L=K[_I][1];I=B[_A]-L[_A],B[_B]-L[_B]
                if(A[_B]==1 and B[_B]==0)and A[_A]>B[_A]:C[_F]+=EDGE_KILL_WEIGHT 
                elif(A[_B]==1 and B[_B]==0)and A[_A]<B[_A]:C[_D]+=EDGE_KILL_WEIGHT
                elif(A[_B]==1 and B[_B]==0)and A[_A]==B[_A]and I==H:C[_D]+=EDGE_KILL_WEIGHT;C[_F]+=EDGE_KILL_WEIGHT
                elif(A[_A]==1 and B[_A]==0)and A[_B]>B[_B]:C[_H]+=EDGE_KILL_WEIGHT
                elif(A[_A]==1 and B[_A]==0)and A[_B]<B[_B]:C[_G]+=EDGE_KILL_WEIGHT
                elif(A[_A]==1 and B[_A]==0)and A[_B]==B[_B]and I==H:C[_G]+=EDGE_KILL_WEIGHT;C[_H]+=EDGE_KILL_WEIGHT
                elif(A[_B]==E-2 and B[_B]==E-1)and A[_A]>B[_A]:C[_F]+=EDGE_KILL_WEIGHT
                elif(A[_B]==E-2 and B[_B]==E-1)and A[_A]<B[_A]:C[_D]+=EDGE_KILL_WEIGHT
                elif(A[_B]==E-2 and B[_B]==E-1)and A[_A]==B[_A]and I==H:C[_D]+=EDGE_KILL_WEIGHT;C[_F]+=EDGE_KILL_WEIGHT
                elif(A[_A]==F-2 and B[_A]==F-1)and A[_B]<B[_B]:C[_H]+=EDGE_KILL_WEIGHT
                elif(A[_A]==F-2 and B[_A]==F-1)and A[_B]>B[_B]:C[_G]+=EDGE_KILL_WEIGHT
                elif(A[_A]==F-2 and B[_A]==F-1)and A[_B]==B[_B]and I==H:C[_G]+=EDGE_KILL_WEIGHT;C[_H]+=EDGE_KILL_WEIGHT
        return C
def floodFill(map,width,height,x,y):
        D=height;C=width;dir=[[0,1],[0,-1],[-1,0],[1,0]];E={_H:0,_G:0,_F:0,_D:0} 
        for F in dir:
                A=x+F[0];B=y+F[1]
                if A<0 or B<0 or A>=C or B>=D:continue
                G=[A[:]for A in map]
                if map[A][B]==1:continue
                if F==[1,0]:E[_F]=fill(G,C,D,A,B)
                elif F==[-1,0]:E[_D]=fill(G,C,D,A,B)
                elif F==[0,1]:E[_H]=fill(G,C,D,A,B)
                else:E[_G]=fill(G,C,D,A,B)
        return E
def fill(map,width,height,x,y):
        B=height;A=width
        if x<0 or y<0 or x>=A or y>=B or map[x][y]>=1:return 0
        map[x][y]=2;C=1;C+=fill(map,A,B,x+1,y);C+=fill(map,A,B,x-1,y);C+=fill(map,A,B,x,y+1);C+=fill(map,A,B,x,y-1);return C
def setBound(map,length_map,opp,game_state):
        C=length_map;A=opp;G=game_state[_C]
        for B in range(len(A)):
                H=A[B][_I]
                for D in H:
                        E=D[_A];F=D[_B];map[E][F]=1
                        if A[B][_L]!=G[_L]:C[E][F]=A[B][_J]
        return map,C
def score(game_state,head,moves,map,length_map):
        D=head;C=moves;B=game_state;G={_H:0,_G:0,_D:0,_F:0}
        for (A,N) in C.items():
                if N>MIN_SCORE:
                        if A==_H:E=D[_A];F=D[_B]+1;H=[[1,0],[-1,0],[0,1]]        
                        if A==_G:E=D[_A];F=D[_B]-1;H=[[1,0],[-1,0],[0,-1]]       
                        if A==_D:E=D[_A]-1;F=D[_B];H=[[0,1],[0,-1],[-1,0]]       
                        if A==_F:E=D[_A]+1;F=D[_B];H=[[0,1],[0,-1],[1,0]]        
                        I=numpy.asarray(length_map)
                        if E==0 and numpy.any(I[1]):C[A]-=0.7
                        if E==B[_E][_M]-1 and numpy.any(I[B[_E][_M]-2]):C[A]-=0.7
                        if F==0 and numpy.any(I[:,1]):C[A]-=0.7
                        if F==B[_E][_N]-1 and numpy.any(I[:,B[_E][_N]-2]):C[A]-=0.7
                        for J in B[_E][_O]:
                                if J[_L]==B[_C][_L]:continue
                                L=J['head']
                                for M in H:
                                        O=M[0]+E;P=M[1]+F
                                        if L[_A]==O and L[_B]==P:
                                                if J[_J]>B[_C][_J]:C[A]-=LARGER_SNAKE_DANGER
                                                elif J[_J]==B[_C][_J]:C[A]-=SAME_SNAKE_DANGER
                                                else:C[A]+=SMALLER_SNAKE_REWARD  
                        K=[A[:]for A in map];K[E][F]=1;K[B[_C][_I][-1][_A]][B[_C][_I][-1][_B]]=0;Q=floodFill(K,B[_E][_M],B[_E][_N],E,F);G[A]=max([A for(B,A)in Q.items()])
        print(f"average spaces {G}");R=max([A for(B,A)in G.items()]);S=[A for(A,B)in G.items()if B==R]
        for A in S:C[A]+=1
        return C
def area(game_state,body):
        G=game_state
        if G[_C][_J]<8:return 0
        C=float(_P);D=float(_P);E=float(_R);F=float(_R)
        for H in body:
                A=H[_A];B=H[_B]
                if C<A:C=A
                if D<B:D=B
                if E>A:E=A
                if F>B:F=B
        I=(C-E+1)*(D-F+1)-G[_C][_J];return I
if __name__=='__main__':from server import run_server;run_server({'info':info,'start':start,_Q:move,'end':end})