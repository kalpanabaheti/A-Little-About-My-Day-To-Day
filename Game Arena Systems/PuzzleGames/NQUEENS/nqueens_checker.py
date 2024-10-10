import copy
import random

class NQueens_Checker:

    def __init__(self, board_width, color_map):

        self.color_map = color_map
        self.board_width = board_width
        self.cross = dict()
        for i in range(self.board_width):
            for j in range(self.board_width):
                self.cross[(i,j)] = 0


    def get_surrounding_indices(self, x, y):

        indices = {(x-1, y), (x-1, y+1), (x, y+1), (x+1, y+1), (x+1, y), (x+1, y-1), (x, y-1), (x-1, y-1)}
        updated_indices = set()
        for loc in indices:
            if loc[0]>=0 and loc[0]<self.board_width and loc[1]>=0 and loc[1]<self.board_width:
                updated_indices.add(loc)

        return updated_indices
        

    def get_color_house(self, x, y):

        for key, val in self.color_map.items():
            if (x,y) in val or (x,y)==key:
                return key
                

    def check_conflicts(self, current_occupancies): #current_occupancies is a list, with new queens added at the start

        #horizontal_check = True
        #vertical_check = True
        #surrounding_check = True
        #color_check = True

        for ind1 in range(len(current_occupancies)-1):
            for ind2 in range(ind1+1, len(current_occupancies)):

                loc1 = current_occupancies[ind1]
                loc2 = current_occupancies[ind2]
                
                if loc1[0] == loc2[0]:
                    #horizontal_check = False
                    return loc1, loc2, 1

                elif loc1[1] == loc2[1]:
                    #vertical_check = False
                    return loc1, loc2, 2

                elif loc1 in self.get_surrounding_indices(loc2[0], loc2[1]):
                    #surrounding_check = False
                    return loc1, loc2, 3

                elif self.get_color_house(loc1[0], loc1[1]) == self.get_color_house(loc2[0], loc2[1]):
                    #color_check = False
                    return loc1, loc2, 4

        return 0


    def add_cross_set(self, x, y, current_occupancies):

        current_occupancies_set = set(current_occupancies)
        horizontal_subset = {(x, j) for j in range(self.board_width)} - current_occupancies_set
        vertical_subset = {(i, y) for i in range(self.board_width)} - current_occupancies_set
        surround_subset = self.get_surrounding_indices(x, y) - current_occupancies_set
        
        color_key = self.get_color_house(x, y)
        color_subset = (self.color_map[color_key] | {color_key}) - current_occupancies_set

        cross_set = horizontal_subset | vertical_subset | surround_subset | color_subset
        cross_set = cross_set - {(x,y)}
        
        for loc in cross_set:
            if loc not in current_occupancies:
                self.cross[loc] += 1

        return cross_set
        

    def remove_cross_set(self, x, y, current_occupancies):

        current_occupancies_set = set(current_occupancies)
        horizontal_subset = {(x, j) for j in range(self.board_width)} - current_occupancies_set
        vertical_subset = {(i, y) for i in range(self.board_width)} - current_occupancies_set
        surround_subset = self.get_surrounding_indices(x, y) - current_occupancies_set
        
        color_key = self.get_color_house(x, y)
        color_subset = (self.color_map[color_key] | {color_key}) - current_occupancies_set

        cross_set = horizontal_subset | vertical_subset | surround_subset | color_subset
        cross_set = cross_set - {(x,y)}
        
        updated_cross_set = set()
        for loc in cross_set:
            if loc not in current_occupancies:
                if self.cross[loc]==1:
                    updated_cross_set.add(loc)
                self.cross[loc] -= 1

        return updated_cross_set
        