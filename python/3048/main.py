def main():
    amount_numbers = int(input("Digite a quantidade de números: "))
    number_list = []
    
    for _ in range(amount_numbers):
        number = int(input("Digite um número: "))
        number_list.append(number)
       
    print(f"Números: {number_list}")
    
    amount_circle = 1   
    for index in range(1,amount_numbers):
        print(f"Índice: {index}")
    
        current_number = number_list[index-1]
        
        if current_number != number_list[index]:
            amount_circle += 1
            
    print(f"Quantidade de círculos: {amount_circle}")   
    

main()