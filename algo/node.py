#!/usr/bin/python2.7
# encoding: utf-8

from Tkinter import *   

class Node:
    """
    Représentation d'un noeud d'arbre. Cet element peut prendre la place de racine, de feuille ou de 
    sous-arbre. Attention, les fils ne sont pas triées.
    """    
    def __init__(self, value, *childs):
        self.value = value 
        self.father = None
        self.childs = childs
        
        for c in childs:
            c.father = self

    def __repr__(self):
        return "{Node: " + self.value + ", childs: " + str(self.childs) + "}"

    def isLeaf(self):
        return self.getChildNumber() == 0
    
    def getChilds(self):
        return self.childs
    
    def getChild(self, index):
        try:
            return self.childs[index]
        except Exception:
            return None
    
    def getChildNumber(self):
        return len(self.childs)
    
    def getValue(self):
        return self.value
    
    def next(self):
        self.iterIndex += 1
        if self.iterIndex < len(self.childs):
            return self.childs[self.iterIndex]
        else:
            raise StopIteration
        
    def __eq__(self, other):
        return isinstance(other, Node) and self.value == other.value and self.childs == other.childs
        
    def __iter__(self):
        self.iterIndex = -1;
        return self
        
class TreeWindow:
    """
    Dessiner un arbre dans une fenêtre
    """
    def __init__(self, rootNode):
        
        # l'arbre à dessiner
        self.tree = rootNode
        self.treeLineWidth = 4
        
        # taille des noeuds en pixels
        self.nodeSize = 30
        self.textSize = 14
        
        # espace entre les différents niveaux de noeuds
        self.spaceBetweenLevels = self.nodeSize * 2
        self.spaceBetweenBrothers = self.nodeSize * 3
        
        # dimensions du canvas
        self.canvasHeight = 2000
        self.canvasWidth = 2000
        
        # Couleurs
        self.nodeBgColor = "#DDDDFF"
        self.nodeStrokeColor = "blue"
        self.leafStrokeColor = "red"
        
    def show(self):
        """
        Afficher la fenêtre avec l'arbre
        """
        # creer une fenetre
        frame = Tk()
        
        # barres de scroll
        xscrollbar = Scrollbar(frame, orient=HORIZONTAL)
        xscrollbar.grid(row=1, column=0, sticky=E + W)
        
        yscrollbar = Scrollbar(frame)
        yscrollbar.grid(row=0, column=1, sticky=N + S)
        
        # canvas ou dessiner l'arbre
        canvas = Canvas(frame, bd=0, bg="white", height=600, width=600,
                        xscrollcommand=xscrollbar.set,
                        yscrollcommand=yscrollbar.set,
                        scrollregion=(0, 0, self.canvasHeight, self.canvasWidth))
        
        canvas.grid(row=0, column=0, sticky=N + S + E + W)
        
        xscrollbar.config(command=canvas.xview)
        yscrollbar.config(command=canvas.yview)
        
        canvas.xview_moveto(0.35)
        
        # dessiner l'arbre
        self._drawTree(canvas, self.tree, 1, self.canvasWidth / 2)
        self._drawNodes(canvas, self.tree, 1, self.canvasWidth / 2)
        
        frame.mainloop()
        
    def _drawTree(self, canvas, node, treeLevel, baseX, startPoint=None):
        """
        Dessiner les liens d'un arbre sur un canevas
        """
        
        # position y des noeuds en fonction de la position verticale dans l'arbre
        y = self._getYFromLevel(treeLevel) 
        
        # dessiner le lien entre les noeuds
        if startPoint != None:
            canvas.create_line(baseX, y, startPoint[0], startPoint[1], width=self.treeLineWidth)

        x = self._getXFromNodeNumber(baseX, node.getChildNumber())
        
        # iterer les noeuds fils si présents
        for n in node:
            
            self._drawTree(canvas, n, treeLevel + 1, x, [baseX, y])
                
            # avancer sur l'axe des x
            x = x + self.nodeSize + self.spaceBetweenBrothers
            
    def _drawNodes(self, canvas, node, treeLevel, baseX):
        """
        Dessiner les noeuds d'un arbre sur un canevas
        """
        
        # position y des noeuds en fonction de la position verticale dans l'arbre
        y = self._getYFromLevel(treeLevel)
        
        # dessiner la racine de l'arbre
        self._drawNode(canvas, node, baseX, y)

        x = self._getXFromNodeNumber(baseX, node.getChildNumber())
        
        # iterer les noeuds fils si présents
        for n in node:
            
            self._drawNodes(canvas, n, treeLevel + 1, x)
                
            # avancer sur l'axe des x
            x = x + self.nodeSize + self.spaceBetweenBrothers
    
    def _getXFromNodeNumber(self, baseX, cn):
        """
        Calculer la position x de départ des enfants, en fonction de leur nombre
         et de la position de départ
        """
        # largeur totale de tous les enfants avec les espaces intermédiaires
        tcw = cn * self.nodeSize + (cn - 1) * self.spaceBetweenBrothers 
        return baseX - (tcw / 2) + self.nodeSize / 2
    
    def _getYFromLevel(self, level):
        return level * self.spaceBetweenLevels
            
    def _drawNode(self, canvas, node, x, y):
        """
        Dessiner un noeud sur le canvas a la position x y passée en paramètre
        """

        # dessiner un rond        
        hs = self.nodeSize / 2
        canvas.create_oval(x - hs, y - hs, x + self.nodeSize, y + self.nodeSize, fill=self.nodeBgColor)
        
        # dessiner la valeur 
        ht = self.textSize / 2
        color = self.leafStrokeColor if node.isLeaf() else self.nodeStrokeColor
        canvas.create_text(x + ht, y + ht, text=str(node.getValue()), font=("Arial", self.textSize), fill=color)
    

if __name__ == "__main__":
    
    # Test de a méthode feuille
    assert(Node("test").isLeaf() == True)
    
    print "Arbre du TD 17 d'algo, exercice 2"
    tree1 = Node("*", 
                Node("-", 
                     Node("u"), Node("^", 
                                     Node("+", 
                                        Node("x"), Node("*", 
                                                        Node("y"), Node("log", 
                                                                        Node("-", 
                                                                             Node("z"), Node("5"))))), 
                                     Node("3"))), 
                 Node("2"))
 
    TreeWindow(tree1).show()
    print tree1
    
    
