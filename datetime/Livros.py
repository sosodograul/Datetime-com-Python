from datetime import datetime, date

def sistema_emprestimo():
    data_str = input("Digite a data de devolução do livro (dd/mm/aaaa): ")
    
    try:
        data_devolucao = datetime.strptime(data_str, "%d/%m/%Y").date()
        hoje = date.today()
        
        diferenca = (data_devolucao - hoje).days
        
        if diferenca > 0:
            print(f"Você tem {diferenca} dias para devolver.")
        elif diferenca < 0:
            print(f"O livro está atrasado em {-diferenca} dias!")
        else:
            print("O livro vence hoje!")
            
    except ValueError:
        print("Data inválida. Por favor, use o formato dd/mm/aaaa.")

if __name__ == "__main__":
    sistema_emprestimo()
