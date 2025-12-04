from collections import deque


class Grafo:
    

    def __init__(self):
       
        self.adj = {
            'A': ['B', 'E'],
            'B': ['A', 'C', 'F'],
            'C': ['B', 'D', 'G'],
            'D': ['C', 'H'],
            'E': ['F', 'A', 'I'],
            'F': ['E', 'G', 'B', 'J'],
            'G': ['F', 'H', 'C', 'K'],
            'H': ['G', 'D', 'L'],
            'I': ['J', 'E', 'M'],
            'J': ['I', 'K', 'F', 'N'],
            'K': ['J', 'L', 'G', 'O'],
            'L': ['K', 'H', 'P'],
            'M': ['N', 'I'],
            'N': ['M', 'O', 'J'],
            'O': ['N', 'P', 'K'],
            'P': ['O', 'L']
        }

    
    def bfs_caminhamento(self, origem: str, verbose: bool = False):
       

       
        visitados = set()

        
        fila = deque()

   
        ordem_visita = []

        visitados.add(origem)
        fila.append(origem)

        if verbose:
            print(f"Inicializando BFS a partir de {origem}")
            print(f"Fila inicial: {list(fila)}")
            print(f"Visitados inicialmente: {visitados}")
            print("-" * 40)

        passo = 0  
        

        while fila:
            passo += 1
            
            atual = fila.popleft()
            ordem_visita.append(atual)

            if verbose:
                print(f"Passo {passo}: removendo '{atual}' da fila")
                print(f"Fila após remoção: {list(fila)}")
                print(f"Visitados até agora: {visitados}")

            
            for vizinho in self.adj[atual]:
                
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    fila.append(vizinho)

                    if verbose:
                        print(f"  Descoberto vizinho '{vizinho}' de '{atual}'")
                        print(f"  Fila agora: {list(fila)}")
                        print(f"  Visitados agora: {visitados}")

            if verbose:
                print("-" * 40)

        return ordem_visita

   
    def bfs_caminho_minimo(self, origem: str, destino: str, verbose: bool = False):
        

       
        if origem == destino:
            return [origem], 0

        visitados = set()
        fila = deque()
       
        pai = {}

        visitados.add(origem)
        fila.append(origem)
        pai[origem] = None  

        if verbose:
            print(f"Buscando caminho mínimo de '{origem}' até '{destino}'")
            print(f"Fila inicial: {list(fila)}")
            print(f"Visitados inicialmente: {visitados}")
            print("-" * 40)

        passo = 0

        
        while fila:
            passo += 1
            atual = fila.popleft()

            if verbose:
                print(f"Passo {passo}: removendo '{atual}' da fila")
                print(f"Fila após remoção: {list(fila)}")
                print(f"Visitados até agora: {visitados}")

           
            if atual == destino:
                if verbose:
                    print(f"Destino '{destino}' encontrado! Encerrando BFS.")
                break

            for vizinho in self.adj[atual]:
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    fila.append(vizinho)
                    pai[vizinho] = atual  

                    if verbose:
                        print(f"  Descoberto vizinho '{vizinho}' de '{atual}'")
                        print(f"  Fila agora: {list(fila)}")
                        print(f"  Visitados agora: {visitados}")

            if verbose:
                print("-" * 40)

       
        if destino not in pai:
            if verbose:
                print(f"Não existe caminho de '{origem}' até '{destino}'.")
            return None, float("inf")

        
        caminho = []
        atual = destino
        while atual is not None:
            caminho.append(atual)
            atual = pai[atual]

      
        caminho.reverse()
        distancia = len(caminho) - 1

        if verbose:
            print(f"Caminho encontrado: {caminho}")
            print(f"Distância (número de arestas): {distancia}")

        return caminho, distancia



if __name__ == "__main__":
    grafo = Grafo()

    print("=== CAMINHAMENTO BFS A PARTIR DE 'A' ===")
    ordem = grafo.bfs_caminhamento('A', verbose=True)
    print("\nOrdem final de visita (caminhamento):")
    print(" -> ".join(ordem))

    print("\n\n=== CAMINHO MÍNIMO (BFS) DE 'A' ATÉ 'P' ===")
    caminho, distancia = grafo.bfs_caminho_minimo('A', 'P', verbose=True)
    print("\nCaminho mínimo de 'A' até 'P':")
    print(" -> ".join(caminho))
    print(f"Número de arestas (distância): {distancia}")
