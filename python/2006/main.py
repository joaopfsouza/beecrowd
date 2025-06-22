# def read_file_input(file_path):

#     lines = ""
#     with open(file_path, 'r') as file:
#         lines = file.readlines()

#     return [line.strip() for line in lines if line.strip()]

# if __name__ == "__main__":
#     input_file_path = 'input.txt'
#     expected_answer, player_guesses = read_file_input(input_file_path)
#     print(f"Expected Answer: {expected_answer}")
#     print(f"Player Guesses: {player_guesses}")
#     correct_answer = [1 for guess in player_guesses if guess == expected_answer].count(1)
#     print(f"Correct Answers: {correct_answer}")    

def main():
    expected_answer = int(input()) 
    player_guesses = input().split('')

    print([1 for guess in player_guesses if expected_answer == int(guess)].count(1))
    
main()