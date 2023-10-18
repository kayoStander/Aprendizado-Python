def new_game():
    guesses = []
    correct_guesses = 0
    current_question_number = 1

    for k in questions:
        print('-------------------')
        print(k)
        for i in options[current_question_number-1]:
            print(i)

        guess = input('enter (A,B,C,D): ').upper()
        guesses.append(guess)
        correct_guesses = check(questions.get(k),guess)

        current_question_number += 1

    Display_Score(correct_guesses, guesses)

def check(answr,guess):
    if answr == guess:
        print('Certo ! +1 ')
        return 1
    else:
        print('Errado... + 0')
        return 0

def Display_Score(correct,list):
    print('*********************')
    print('RESULTADOS: ')
    print('*********************')
    print('Respostas: ', end='')
    for i in questions:
        print(questions.get(i), end=' ')
    print()

    print('Chutes: ', end='')
    for i in list:
        print(i, end=' ')
    print()

    score = int((correct/len(questions))*100)
    print('SCORE FINAL:', score, " !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


def Play_Again():
    resposta = input(' quer jogar dnv fdp? (S/N)').lower()

    if resposta == 'Y':
        return True
    else:
        return False

questions = {
    'Quanto pesa a carollokinha?: ' : "C",
    'Quantos creditos sociais o enzo husti tem no governo lula?: ' : "A",
    'Navio de guerra com o nome mais foda: ' : 'C',
    'Lorenzo ja cagou em quantos lençois?: ' : 'A'
}

options = [['A. 46kg ', 'B. 140kg ', 'C. 3 toneladas e meia', 'D. sim '],
           ['A. -1000 ', 'B. 1326 ', 'C. 100,000', 'D. 1.2'],
           ['A. HMS Vitória. Théodore Gudin', 'B. USS Missouri', 'C. Destruidores da Classe Zumwalt', 'D. HMS Dreadnought.'],
           ['A. 1', 'Historia mentirada', 'B. IP: 11.221.544.261', 'C. Viviane namora comigo', 'D. Talvez. ']]


new_game()
