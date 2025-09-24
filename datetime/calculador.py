from datetime import date

def calculadora_idade():
    data_str = input("Digite sua data de nascimento (dd/mm/aaaa): ")
    
    try:
        nascimento = datetime.strptime(data_str, "%d/%m/%Y").date()
        ano_atual = date.today().year
        idade = ano_atual - nascimento.year
        
        print(f"Você tem {idade} anos.")
        
    except ValueError:
        print("Data inválida. Por favor, use o formato dd/mm/aaaa.")

if __name__ == "__main__":
    from datetime import datetime
    calculadora_idade()
