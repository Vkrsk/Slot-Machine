import random 


MAX_LINES=5
MAX_BET=500
MIN_BET=5
#using these as constants so we can use them anywhere in our code.

ROWS = 4
COLS = 4
#Now we will be adding symbols for the slot machine:
symbol_count={
      "S":3,   
      "A":6,   
      "B":9,   
      "C":12,   
}
symbol_value={
      "S":6,   
      "A":4,   
      "B":2,   
      "C":1,   
}
def check_winnings(columns,lines,bet,values):
    winnings = 0
    winning_lines=[]
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet   
            winning_lines.append(line + 1)


    return winnings, winning_lines        

     



def get_slot_machine_spin(rows,cols,symbols):
    all_symbols=[]
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol) 



    columns=[]
    for col in range(cols):
        column=[]
        current_symbols= all_symbols[:]
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i , column in enumerate(columns):
            if i !=len(columns)-1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")   

        print()         


def deposit():
    while True:
        amount= input ("Please enter the deposit amount :  ")
        if  amount.isdigit():
             amount=int(amount)
             if amount > 0:
                return amount
             else:
                print("the deposit should be greater than 0.")
        else:
             print("Enter a valid digit")

        
    
def get_number_of_lines():
    while True:
        lines=input("enter the number of lines to bet on (1-"+str(MAX_LINES)+")? ")
        if lines.isdigit():
                lines=int(lines)
                if 1<=lines <= MAX_LINES:
                    return lines
                    
                else:
                    print("Enter a number.")
        else:
               print(" enter a number.")
                
    return lines 
def get_bet():
     while True:
        bet= input ("Please enter the amount you want to bet on each line")
        if  bet.isdigit():
             bet= int(bet)
             if MIN_BET<= bet <=MAX_BET:
                return bet
                
             else:
                print(f"Amount must be in between ${MIN_BET}-${MAX_BET}.")
        else:
             print("Enter a Number ")

        
       



def game(balance):
    lines = get_number_of_lines() 
    while True:
      bet = get_bet()
      total_bet = bet * lines
      if total_bet > balance:
         print("You don't have enough balance.")
      else:
          break

    print(f"You are betting ${bet} on {lines} lines . Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots) 
    winnings, winnig_lines= check_winnings(slots,lines,bet,symbol_value)
    print(f"You won ${winnings} ")
    print(f"You won on ", *winnig_lines)
    return winnings -total_bet

def main():
    balance=deposit()
    while True:
        print(f"cureent balance is ${balance}")
        spin = input("press to play(f to quit)")
        if spin ==  "f":
            break
        balance +=game(balance)

main()
        
    