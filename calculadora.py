import math
from colorama import init, Fore, Style

# Inicializa o colorama para funcionar no Windows
init()

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: Divisão por zero!"
    return a / b

def potencia(a, b):
    return a ** b

def raiz_quadrada(a):
    if a < 0:
        return "Erro: Número negativo não possui raiz real!"
    return math.sqrt(a)

def porcentagem(a, b):
    return (a * b) / 100

def limpar_tela():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print(f"\n{Fore.CYAN}{'=' * 40}")
    print(f"{Fore.YELLOW}          CALCULADORA PYTHON")
    print(f"{Fore.CYAN}{'=' * 40}{Style.RESET_ALL}")
    print(f"\n{Fore.GREEN}Escolha a operação desejada:{Style.RESET_ALL}\n")
    
    operacoes = [
        "Adição (+)",
        "Subtração (-)",
        "Multiplicação (×)",
        "Divisão (÷)",
        "Potência (^)",
        "Raiz Quadrada (√)",
        "Porcentagem (%)",
        "Sair"
    ]
    
    for i, op in enumerate(operacoes, 1):
        print(f"{Fore.YELLOW}[{i}]{Style.RESET_ALL} {op}")

def calculadora():
    while True:
        limpar_tela()
        menu()
        try:
            opcao = input(f"\n{Fore.GREEN}Digite o número da operação desejada (1-8): {Style.RESET_ALL}")
            
            if not opcao.strip():
                continue
                
            opcao = int(opcao)
            
            if opcao == 8:
                print(f"\n{Fore.YELLOW}Obrigado por usar a calculadora! Até logo!{Style.RESET_ALL}")
                break
                
            if opcao not in range(1, 9):
                print(f"\n{Fore.RED}Erro: Opção inválida! Escolha um número entre 1 e 8.{Style.RESET_ALL}")
                input("\nPressione ENTER para continuar...")
                continue
                
            limpar_tela()
            if opcao == 6:  # Raiz quadrada
                print(f"{Fore.CYAN}=== Cálculo de Raiz Quadrada ===\n{Style.RESET_ALL}")
                a = float(input(f"{Fore.GREEN}Digite o número para calcular a raiz quadrada: {Style.RESET_ALL}"))
                resultado = raiz_quadrada(a)
            else:
                operacoes = ["Adição", "Subtração", "Multiplicação", "Divisão", "Potência", "Raiz Quadrada", "Porcentagem"]
                print(f"{Fore.CYAN}=== {operacoes[opcao-1]} ===\n{Style.RESET_ALL}")
                
                a = float(input(f"{Fore.GREEN}Digite o primeiro número: {Style.RESET_ALL}"))
                if opcao != 6:
                    b = float(input(f"{Fore.GREEN}Digite o segundo número: {Style.RESET_ALL}"))

            if opcao == 1:
                resultado = soma(a, b)
                operador = "+"
            elif opcao == 2:
                resultado = subtracao(a, b)
                operador = "-"
            elif opcao == 3:
                resultado = multiplicacao(a, b)
                operador = "×"
            elif opcao == 4:
                resultado = divisao(a, b)
                operador = "÷"
            elif opcao == 5:
                resultado = potencia(a, b)
                operador = "^"
            elif opcao == 7:
                resultado = porcentagem(a, b)
                operador = "% de"

            # Exibição do resultado
            print(f"\n{Fore.CYAN}{'=' * 40}")
            if opcao == 6:
                print(f"{Fore.YELLOW}√{a} = {resultado}")
            else:
                print(f"{Fore.YELLOW}{a} {operador} {b} = {resultado}")
            print(f"{Fore.CYAN}{'=' * 40}{Style.RESET_ALL}")
            
            input(f"\n{Fore.GREEN}Pressione ENTER para continuar...{Style.RESET_ALL}")
            
        except ValueError:
            print(f"\n{Fore.RED}Erro: Por favor, digite apenas números válidos!{Style.RESET_ALL}")
            input(f"\n{Fore.GREEN}Pressione ENTER para continuar...{Style.RESET_ALL}")
        except Exception as e:
            print(f"\n{Fore.RED}Erro: {str(e)}{Style.RESET_ALL}")
            input(f"\n{Fore.GREEN}Pressione ENTER para continuar...{Style.RESET_ALL}")

if __name__ == "__main__":
    calculadora()