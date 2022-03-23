# Visualização da estrutura
# Inserção
# Remoção (maior)
# Busca (maior)


def subir(i, n):
	j = i // 2
	if j >= 1:
		if v[i] > v[j]:
			aux = v[i]
			v[i] = v[j]
			v[j] = aux
			print(v[1:])
			subir(j,n)
			
def descer(i,n):
	j = 2*i
	if j <= n:
		if j < n:
			if v[j+1] > v[j]:
				j += 1
		if v[i] < v[j]:
			aux = v[i]
			v[i] = v[j]
			v[j] = aux
			print(v[1:])
			descer(j,n)

def insercao_heaps(v,x):
	v.append(x)
	n = len(v) - 1		# Definindo a ultima posicao da heap
	i = n				# Poiscao do elemento inserido
	print("\nPassos de conserto da Heap:")
	print(v[1:])
	subir(i,n)
	
def remocao_heaps(v):
	n = len(v) - 1
	if n == 0:
		print("Não é possível remover, Heap vazia.")
	else:	
		maior = v[1]
		v[1] = v[n]
		v[n] = maior
		v.remove(v[n])
		n -= 1
		print("\nPassos de conserto da Heap:")
		print(v[1:])
		descer(1,n)
	
def busca_maior(v):
	n = len(v) - 1
	if n == 0:
		return "Heap vazia."
	return v[1]

# Vetor (Heap)
v = [0] # Por questoes, a primeira posicao da heap sera ocupada com o elemento 0 (que sera ignorado), para que o programa funcione usando 1 como primeiro indice.

while True:
		print("="*50)
		print("Visualização da Estrutura: ")
		print(v[1:])
		print('')
		print("="*50)
		print("(1) Inserir elemento")
		print("(2) Remover elemento do topo")
		print("(3) Buscar maior elemento")
		print("(0) Encerrar o programa")
		print("="*50)
		print('')

		escolha = input("Digite número da operação que deseja executar: ")
		print('')
		if escolha == '0':
			break
		elif escolha == '1':
				while True:
					valor = input("Digite o valor que deseja inserir no Heap: ")
					if valor.isdigit():
						valor = int(valor)
						insercao_heaps(v,valor)
						break
					print("Valor inválido, tente novamente.")
		elif escolha == '2':
				remocao_heaps(v)
		elif escolha == '3':
				print("Resultado da busca do maior elemento: ", busca_maior(v))
		else:
				print("Entrada inválida, tente novamente.")
		print('')