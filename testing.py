from button import Button
import pygame
import operator
import card_deck
import random
import numpy as np
pygame.init()
screen = pygame.display.set_mode((500,500))
fps = 60
timer = pygame.time.Clock()
font = pygame.font.Font('data/fonts/pong.ttf',48)
exit = False
button_1 = Button("row",100,100,'gray','black',4,screen,font)
button_2 = Button("column",200,100,'gray','black',4,screen,font)

def main():
    def choosing_superpos():
        x = [(0, 0), (3, 0), (0, 1), (3, 1), (0, 6), (3, 6), (0, 7), (3, 7)]
        #[[(0,0),(0,1),(0,6),(0,7)],
        #        [(3,0),(3,1),(3,6),(3,7)]]
        #y = sorted(x, key= operator.itemgetter(0))
        z = sorted(x, key = lambda x: x[0])
        tmp = z[0][0]
        matrix = [[]]
        k = 0
        for (i,j) in z:
            if i == tmp:
                matrix[k].append((i,j))
            else:
                matrix.append([])
                k+=1
                matrix[k].append((i,j))
                tmp = i
        matrix1 = [[(0,1),(0,6),(0,7)],
                    [(3,0),(3,1),(3,6)]]
        super_prob_2 = [(0.4999999999999999), (0.4999999999999999)]
        super_prob_3 = [(0.2499999999999999), (0.2499999999999999), (0.2499999999999999), (0.2499999999999999)]
        
        row_measurement = random.choices(matrix1,weights= super_prob_2, k = 1)
        print(row_measurement)
        col_measurement = random.choices(list(row_measurement[0]), weights = super_prob_3, k = 1)
        print(col_measurement)

    def entanglement_check(state_vector):
        # Initialize an 8x8 matrix filled with zeros
        density_matrix = np.zeros((8, 8), dtype=complex)
        # Initialize a flag to check for entanglement
        entangled = False
        # Calculate the density matrix
        print(state_vector)
        for i in range(8):
            for j in range(8):
                density_matrix[i][j] = np.vdot(state_vector[i][1], state_vector[j][1])

        print(density_matrix)

        # Check for non-zero off-diagonal elements
        for i in range(8):
            for j in range(8):
                if i != j and density_matrix[i][j] != 0:
                    entangled = True
                    break

        # Determine if the state is entangled
        if entangled:
            print("The state is entangled.")
        else:
            print("The state is separable.")
                # Print the density matrix
        
        # Assuming you have the density matrix calculated and stored in 'density_matrix'

        # Initialize a list to store entangled states
        entangled_states = []

        # Iterate through the density matrix to find non-zero off-diagonal elements
        for i in range(8):
            for j in range(8):
                if i != j and density_matrix[i][j] != 0:
                    entangled_states.append((i, j))

        # Print the list of entangled states
        print("Entangled states:")
        for state_pair in entangled_states:
            print(f"|{state_pair[0]}> is entangled with |{state_pair[1]}>")

    entanglement_check([(0, (0.4999999999999999+0j)), (1, 0j), (2, 0j), (3, (0.4999999999999999+0j)), (4, 0j), (5, (0.4999999999999999+0j)), (6, (0.4999999999999999+0j)), (7, 0j)])
    """
    |0> is entangled with |3>
    |0> is entangled with |5>
    |0> is entangled with |6>
    |3> is entangled with |5>
    |3> is entangled with |6>
    |5> is entangled with |6>
    """
    """
    [
    ["0.25+0.j" 0.  +0.j 0.  +0.j 0.25+0.j 0.  +0.j 0.25+0.j 0.25+0.j 0.  +0.j]
    [0.  +0.j "0.  +0.j" 0.  +0.j 0.  +0.j 0.  +0.j 0.  +0.j 0.  +0.j 0.  +0.j]
    [0.  +0.j 0.  +0.j "0.  +0.j" 0.  +0.j 0.  +0.j 0.  +0.j 0.  +0.j 0.  +0.j]
    [0.25+0.j 0.  +0.j 0.  +0.j "0.25+0.j" 0.  +0.j 0.25+0.j 0.25+0.j 0.  +0.j]
    [0.  +0.j 0.  +0.j 0.  +0.j 0.  +0.j "0.  +0.j" 0.  +0.j 0.  +0.j 0.  +0.j]
    [0.25+0.j 0.  +0.j 0.  +0.j 0.25+0.j 0.  +0.j "0.25+0.j" 0.25+0.j 0.  +0.j]
    [0.25+0.j 0.  +0.j 0.  +0.j 0.25+0.j 0.  +0.j 0.25+0.j "0.25+0.j": 0.  +0.j]
    [0.  +0.j 0.  +0.j 0.  +0.j 0.  +0.j 0.  +0.j 0.  +0.j 0.  +0.j "0.  +0.j"]
    ]
    """
if __name__ == '__main__':
    main()
"""          
while not exit:
    screen.fill((255,255,255))
    button_1.add_button(10,10)
    button_2.add_button(10,125)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                exit = True
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r] and keys[pygame.K_LSHIFT]:
                  button_2.un_press()
                  button_1.press()
            if keys[pygame.K_c] and keys[pygame.K_LSHIFT]:
                  button_1.un_press()
                  button_2.press()

    timer.tick(60)
    pygame.display.flip()
"""