import numpy as np
import copy
import random


class NQueens_Generator:

    def __init__(self, board_width):

        self.board_width = board_width
        self.board = np.zeros((self.board_width, self.board_width)).astype(int)
        self.colored_board = np.empty((self.board_width, self.board_width)).astype(str)
        self.initial_places = {(i,j) for j in range(self.board_width) for i in range(self.board_width)}
        self.color_map = dict()
        self.colors = []
        
        for i in range(self.board_width):
            num_str = str(i)
            if i<10:
                num_str = '0' + num_str
            full_str = 'C' + num_str
            self.colors.append(full_str)
        
    
    def adjusted_surrounding_indices(self, x, y):

        indices = {(x-1, y), (x-1, y+1), (x, y+1), (x+1, y+1), (x+1, y), (x+1, y-1), (x, y-1), (x-1, y-1)}
        updated_indices = set()
        for loc in indices:
            if loc[0]>=0 and loc[0]<self.board_width and loc[1]>=0 and loc[1]<self.board_width:
                updated_indices.add(loc)

        return updated_indices
        

    def block_locations(self, x, y, possible_places):

        adjusted_indices = self.adjusted_surrounding_indices(x, y)
        set_row = {(x, i) for i in range(self.board_width)}
        set_col = {(i, y) for i in range(self.board_width)}
        #set_surround = {tuple(loc) for loc in adjusted_indices}
        set_to_remove = set_row | set_col | adjusted_indices | {(x, y)}
        new_possible_places = possible_places - set_to_remove
        
        return new_possible_places
        

    def place_queen(self, current_occupancies=set(), possible_places=None, place_loc=None):

        if possible_places == None:
            possible_places = self.initial_places

        if place_loc == None:
            x = np.random.randint(0, self.board_width)
            y = np.random.randint(0, self.board_width)
            
        else:
            x, y = place_loc[0], place_loc[1]

        new_possible_places = self.block_locations(x, y, possible_places)
        current_occupancies.add((x,y))
        return new_possible_places, current_occupancies
        

    def check_moves_and_remnants(self, moves_and_remnants):

        flag_none_left = True
        for i in moves_and_remnants:

            if len(i[0]) == self.board_width:
                return True, i[0] 

            if len(i[1]) != 0:
                flag_none_left = False

        return flag_none_left, -1

    def search_solver_dynamic(self, moves_and_remnants):

        result = False, _
        count = 0
        #print('Initial: ',moves_and_remnants, len(moves_and_remnants[0][1]))
        #print('\n')

        while result[0] != True:

            new_check_moves_remnants = []
            for track in moves_and_remnants:

                subtrack = []
                current_occupancies = track[0]
                current_availabilities = track[1]
                for next_step in current_availabilities:
                    copy_occ, copy_avail = copy.deepcopy(current_occupancies), copy.deepcopy(current_availabilities)
                    new_availabilities, new_occupancies = self.place_queen(copy_occ, copy_avail, next_step)
                    subtrack.append([new_occupancies, new_availabilities])

                    '''
                    if count == 3:
                        print(next_step, [new_occupancies, new_availabilities], len(new_availabilities))
                        print('\n')
                    '''

                new_check_moves_remnants.extend(subtrack)

            moves_and_remnants = new_check_moves_remnants
            result = self.check_moves_and_remnants(moves_and_remnants)

        return result
        

    def get_solved_board(self):

        first_iter_places, first_occupancies = self.place_queen(place_loc = (4,3))
        moves_and_remnants = [[first_occupancies, first_iter_places]]
        result = self.search_solver_dynamic(moves_and_remnants)

        return result
            

    def select_color_sizes(self):

        sample_size = self.board_width  
        n = self.board_width**2        
        
        sample = np.random.randint(0, 101, size=sample_size)
        normalized_sample = (sample / sample.sum()) * n
        normalized_sample_rounded = np.round(normalized_sample).astype(int)
        
        difference = n - normalized_sample_rounded.sum()
        for i in range(abs(difference)):
            normalized_sample_rounded[i % sample_size] += int(np.sign(difference))

        #print("Normalized Sample:", normalized_sample_rounded)

        sample_list = normalized_sample_rounded.tolist()
       
        larger_samples = [i for i in range(len(sample_list)) if sample_list[i]>2]
        zero_samples = [i for i in range(len(sample_list)) if sample_list[i]==0]

        for z in zero_samples:
                
            sample_list[larger_samples[0]] -= 1
            sample_list[z] += 1
            larger_np = np.array([i for i in range(len(sample_list)) if sample_list[i]>2])
            np.random.shuffle(larger_np)
            larger_samples = larger_np.tolist()

        
        larger_samples = [i for i in range(len(sample_list)) if sample_list[i]>3]
        one_samples = [i for i in range(len(sample_list)) if sample_list[i]==1]
        
        if one_samples != []:
            one_samples.pop(0)

        for o in one_samples: 

            sample_list[larger_samples[0]] -= 2
            sample_list[o] += 2
            larger_np = np.array([i for i in range(len(sample_list)) if sample_list[i]>3])
            np.random.shuffle(larger_np)
            larger_samples = larger_np.tolist()

        #print("Fully Adjusted Sample: ", sample_list)
        return sample_list
        

    def assign_color(self, loc, availabilities, color_size):

        assignments = set()
        count = 0

        frontier = self.adjusted_surrounding_indices(loc[0], loc[1])
        while frontier!=set():

            new_frontier = set()
            compulsory_pick = random.choice(list(frontier))
            
            if compulsory_pick in availabilities:
                assignments.add(compulsory_pick)
                frontier = frontier - {compulsory_pick}
                new_frontier = new_frontier | self.adjusted_surrounding_indices(compulsory_pick[0], compulsory_pick[1])
                availabilities = availabilities - {compulsory_pick}
                count += 1
                if count == color_size:
                    return availabilities, assignments
                
            for surr_loc in frontier:
                
                choice = random.choice([0, 1])
                if choice == 1 and surr_loc in availabilities:
                    assignments.add(surr_loc)
                    new_frontier = new_frontier | self.adjusted_surrounding_indices(surr_loc[0], surr_loc[1])
                    availabilities = availabilities - {surr_loc}
                    count += 1
                    if count == color_size:
                        return availabilities, assignments

            frontier = new_frontier

        avail_list = list(availabilities)
        while count < color_size:

            chosen_loc = avail_list.pop()
            assignments.add(chosen_loc)
            availabilities = availabilities - {chosen_loc}
            count += 1

        return availabilities, assignments
    

    def color_board(self, solver, color_sizes):

        availabilities = self.initial_places - solver
        color_map = {loc:set() for loc in solver}

        color_itr = 0
        for loc, region in color_map.items():

            color_size = color_sizes[color_itr]-1
            if color_size != 0:
                availabilities, assignments = self.assign_color(loc, availabilities, color_size)
                color_map[loc] = assignments
            
            color_itr += 1

        self.color_map = color_map

        return color_map


    def populate_board(self, formation_set):

        for loc in formation_set:
            self.board[loc[0], loc[1]] = 1
            

    def paint_board(self, color_map):

        color_itr = 0
        for key, val in color_map.items():

            self.colored_board[key[0], key[1]] = self.colors[color_itr]
            for box in val:
                self.colored_board[box[0], box[1]] = self.colors[color_itr]

            color_itr += 1

    def get_solver(self):

        file_path = 'queens'+str(self.board_width)+'.txt'
        lists = []

        # Open the file and read it line by line
        with open(file_path, 'r') as file:
            for line in file:
                # Evaluate the line as a list and append it to the lists
                lists.append(eval(line.strip()))

        solver = random.choice(lists)
        return solver
                