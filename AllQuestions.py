import random


LADDERS = {3: 16, 5: 7, 15: 25, 18: 20, 21: 32}
SNAKES = {12: 2, 14: 11, 17: 4, 31: 19, 35: 22}
WINNING_SQUARE = 36
NUM_SIMULATIONS = 10000

def roll_dice():
    return random.randint(1, 6)

def simulate_q1():
    p1_wins = 0

    for _ in range(NUM_SIMULATIONS):
        pos = [1, 1]
        turn = 0

        while True:
            roll = roll_dice()
            pos[turn] += roll

            
            if pos[turn] in LADDERS:
                pos[turn] = LADDERS[pos[turn]]
            elif pos[turn] in SNAKES:
                pos[turn] = SNAKES[pos[turn]]

            
            if pos[turn] >= WINNING_SQUARE:
                if turn == 0:
                    p1_wins += 1
                break

            
            turn = 1 - turn

    return p1_wins / NUM_SIMULATIONS

def simulate_q2():
    total_snakes_hit = 0
    for _ in range(NUM_SIMULATIONS):
        pos = [1, 1]
        turn = 0
        
        while True:
            pos[turn] += roll_dice()
            
            if pos[turn] in LADDERS:
                pos[turn] = LADDERS[pos[turn]]
            elif pos[turn] in SNAKES:
                total_snakes_hit += 1
                pos[turn] = SNAKES[pos[turn]]
                
            if pos[turn] >= WINNING_SQUARE:
                break
            turn = 1 - turn
            
    return total_snakes_hit / NUM_SIMULATIONS

def simulate_q3():
    total_rolls = 0
    for _ in range(NUM_SIMULATIONS):
        pos = [1, 1]  
        turn = 0      
        match_rolls = 0
        
        while True:
            match_rolls += 1
            pos[turn] += roll_dice()
            
            if pos[turn] in LADDERS:
                
                if random.random() < 0.5:
                    pos[turn] = LADDERS[pos[turn]]
            elif pos[turn] in SNAKES:
                pos[turn] = SNAKES[pos[turn]]
                
            
            if pos[turn] >= WINNING_SQUARE:
                break
                
            turn = 1 - turn  
            
        total_rolls += match_rolls
        
    return total_rolls / NUM_SIMULATIONS

def simulate_q4():
    best_start = 1
    closest_to_50 = 1.0 
    
    for start_pos in range(2, WINNING_SQUARE):
        p1_wins = 0
        for _ in range(NUM_SIMULATIONS):
            pos = [1, start_pos]
            turn = 0
            
            while True:
                pos[turn] += roll_dice()
                
                if pos[turn] in LADDERS:
                    pos[turn] = LADDERS[pos[turn]]
                elif pos[turn] in SNAKES:
                    pos[turn] = SNAKES[pos[turn]]
                    
                if pos[turn] >= WINNING_SQUARE:
                    if turn == 0:
                        p1_wins += 1
                    break
                turn = 1 - turn
                
        p1_win_rate = p1_wins / NUM_SIMULATIONS
        diff = abs(p1_win_rate - 0.5)
        
        if diff < closest_to_50:
            closest_to_50 = diff
            best_start = start_pos
            
    return best_start

def simulate_q5():
    p1_wins = 0
    for _ in range(NUM_SIMULATIONS):
        pos = [1, 1]
        turn = 0
        p2_immunity_active = True
        
        while True:
            pos[turn] += roll_dice()
            
            if pos[turn] in LADDERS:
                pos[turn] = LADDERS[pos[turn]]
            elif pos[turn] in SNAKES:
                if turn == 1 and p2_immunity_active:
                    
                    p2_immunity_active = False
                else:
                    
                    pos[turn] = SNAKES[pos[turn]]
                    
            if pos[turn] >= WINNING_SQUARE:
                if turn == 0:
                    p1_wins += 1
                break
                
            turn = 1 - turn
            
    return p1_wins / NUM_SIMULATIONS

if __name__ == "__main__":
    
    Q1 = simulate_q1()
    Q2 = simulate_q2()
    Q3 = simulate_q3()
    Q4 = simulate_q4()
    Q5 = simulate_q5()

    print("Questao 1:")
    print(f"Probabilidade de o jogador que começa a partida vencer: {(Q1 * 100):.2f}%.")
    print()
    print("Questao 2:")
    print(f"Em média, os jogadores caem em {Q2:.2f} cobras por partida.")
    print()
    print("Questao 3")
    print(f"Com 50% de chance de subir as escadas, a média de lançamentos de dados é {Q3:.2f}.")
    print()
    print("Questao 4")
    print(f"As probabilidades de vitória dos jogadores se tornam mais similares quando o jogador 2 inicia na posição {Q4}")
    print()
    print("Questao 5")
    print(f"A probabilidade que o Jogador 1 vença, quando o jogador 2 possui imunidade, é: {(Q5 * 100):.2f}%.")