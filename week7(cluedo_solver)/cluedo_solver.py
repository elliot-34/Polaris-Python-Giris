"""Sometimes i wonder what im doing with my life"""

import sympy as sp

class Elements:
    def __init__(self,*args):
        self._elements=args
        self._check_elements=list(self._elements)
        self._symbols=[]
        for s in args:
            self._symbols.append(sp.symbols(s))
        self._match=dict(zip(self._elements,self._symbols))
    def delete(self,name):
        if len(self._check_elements)>1 and (name in self._check_elements):
            self._check_elements.remove(name)
            return True
        return False

class People(Elements):
    @property
    def ppl(self):
        return self._elements
    
class Rooms(Elements):
    @property
    def rooms(self):
        return self._elements
    
class Weapons(Elements):
    @property
    def wpn(self):
        return self._elements
    
class Play:
    def __init__(self,p:People,r:Rooms,w:Weapons):
        self.p=p
        self.r=r
        self.w=w
        self.expr=[]
        """Rules"""
        self.expr.append(sp.Or(*self.p._symbols))
        self.expr.append(sp.Or(*self.r._symbols))
        self.expr.append(sp.Or(*self.w._symbols))
        self._exactly_one(self.p._symbols)
        self._exactly_one(self.r._symbols)
        self._exactly_one(self.w._symbols)

    def _exactly_one(self,symbols):
        self.expr.append(sp.Or(*symbols))
        for i in range(len(symbols)):
            for j in range(i + 1, len(symbols)):
                self.expr.append(sp.Not(sp.And(symbols[i], symbols[j])))

    def check(self):
        kb=sp.And(*self.expr)
        result={"Person":None,"Room":None,"Weapon":None}
        for k,person in self.p._match.items():
            if not sp.satisfiable(kb & ~person): #checking if person is killer
                result["Person"]=k
        for k,room in self.r._match.items():
            if not sp.satisfiable(kb & ~room): #checking room
                result["Room"]=k #the room of the murder
        for k,wep in self.w._match.items():
            if not sp.satisfiable(kb & ~wep): #checking if wep is weapon
                result["Weapon"]=k #wep is the weapon of the murder
        print("\nCurrent Guess: ",result)
        return game_end(**result)
         
    def add(self,man,room,weapon):
        self.expr.append(sp.Or(self.p._match[man],self.r._match[room],self.w._match[weapon]))
    def add_card(self,card):
        self.expr.append(sp.Not(card))

    
def main():
    startmenu()
    gameplay()

def startmenu():
    print("====== Cluedo Solver for Harvard CS50 Int. To AI ======")
    print("Game Solver: In order to get the answer of the game, you must enter a card that you hold.")
    print("Check game rules for further info.")
    
def print_items():
    print("People: Mustard, Plum, Scarlet")
    print("Rooms: Ballroom, Kitchen, Library")
    print("Weapons: Knife, Revolver, Wrench")

def gameplay():
    p=People("mustard","plum","scarlet")
    r=Rooms("ballroom","kitchen","library")
    w=Weapons("knife","revolver","wrench")
    g=Play(p,r,w)
    while not g.check():
        print_items()
        ask(g)

def game_end(Person=None,Room=None,Weapon=None):
    if (Person!=None) and (Room!=None) and (Weapon!=None):
        print(f"Game ended.\nKiller:{Person}\nRoom:{Room}\nWeapon:{Weapon}")
        return True
    return False

def ask(g:Play):
    while True:
        t=str(input("Sentence or card:").lower().strip())
        match t:
            case "sentence":
                sentence_ask(g)
                return None
            case "card":
                card_ask(g)
                return None
            case _:
                print("Try again.")
def sentence_ask(g:Play):
    while True:
        parts=input("Who Where Weapon (At least one is true. If two elements are false then the other one becomes true automatically):").lower().strip().split()
        if (parts[0] not in g.p.ppl) or (parts[1] not in g.r.rooms) or (parts[2] not in g.w.wpn):
            print("Wrong names. Try again.")
        else:
            g.add(parts[0],parts[1],parts[2])
            return None  
def card_ask(g:Play):
    while True:
        card=str(input("Card:").lower().strip())
        if (card not in g.p.ppl):
            if (card not in g.r.rooms):
                if (card not in g.w.wpn):
                    print("Wrong name. Try again.")
                else:
                    if g.w.delete(card):
                        g.add_card(g.w._match[card])
                    return None
            else:
                if g.r.delete(card):
                    g.add_card(g.r._match[card])
                return None
        else:
            if g.p.delete(card):
                g.add_card(g.p._match[card])
            return None      




        
if __name__=="__main__":
    main()