import numpy as np
import argparse

# read the dictionary and strip potential whitespace
with open('gr_dict') as f:
    dictionary = f.readlines()

dictionary = [x.strip() for x in dictionary]

# Represents the full boggle puzzle
# boggle_string is the letters as a single string (left to right, top to bottom)
class Boggle:
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('boggle_string', metavar='boggle_string', type=str,
            help='The boggle puzzle as single string from left to right, top to bottom')
        self.args = parser.parse_args()
        print("Args are: {0}".format(self.args))
        self.n = int(len(self.args.boggle_string)**0.5)
        self.boggle_arr = np.reshape([c for c in self.args.boggle_string.upper()],(self.n,self.n))
        self.neighbors = {}
        self.boggle_words = []
        # Create the neighbours lists
        for i in range(self.n):
            for j in range(self.n):
                cur_neighbors = []
                for k in range(i-1,i+2):
                    for l in range(j-1,j+2):
                        # If we have valid coordinates that don't point to ourself, add them to the neighbors.
                        if k>=0 and k<self.n and l>=0 and l<self.n and not (i == k and j == l):
                            cur_neighbors.append((k,l))
                self.neighbors[i,j] = cur_neighbors
        print("Boggle array and neighbors are ready.")

    def word_search(self,i,j,visited,word):
        to_visit = [x for x in self.neighbors[i,j] if x not in visited]
        if word != '' and str(word+self.boggle_arr[i][j]) in dictionary:
            self.boggle_words.append(str(word+self.boggle_arr[i][j]))
        word = str(word+self.boggle_arr[i][j])
        visited.append((i,j))
        # Check if we need to stop (no words in dictionary exist that start with current word)
        if any((w.startswith(word) and (len(word) < len(w))) for w in dictionary):
            for neighbor in to_visit:
                self.word_search(neighbor[0],neighbor[1],visited,word)
                visited.remove((neighbor[0],neighbor[1]))

    def solve(self):
        for i in range(self.n):
            for j in range(self.n):
                self.word_search(i,j,[],'')

        self.boggle_words = list(set(self.boggle_words))
        self.boggle_words.sort(key=len)
        for word in self.boggle_words:
            print(word)

b = Boggle()
b.solve()
