from math import inf


class Graph:

    def __init__(self):
       
        self.vertices = set()
       
        self.edges = []

    def add_edge(self, u, v, w):
        
        self.vertices.add(u)
        self.vertices.add(v)
        self.edges.append((u, v, w))

    def _print_state(self, dist, pred):
        
        print("Estado atual das distâncias e predecessores:")
        for v in sorted(self.vertices):
            print(f"  vértice {v}: dist = {dist[v]}, pred = {pred[v]}")
        print("-" * 50)

    def bellman_ford(self, source, verbose=False):
       
        
        dist = {v: inf for v in self.vertices}
        pred = {v: None for v in self.vertices}
        dist[source] = 0

        if verbose:
            print(f"Iniciando Bellman-Ford a partir da origem '{source}'")
            print("Passo 1: inicialização das distâncias e predecessores")
            self._print_state(dist, pred)

       
        num_vertices = len(self.vertices)
        for i in range(num_vertices - 1):
            if verbose:
                print(f"\nPasso 2: iteração de relaxamento {i + 1}/{num_vertices - 1}")

            houve_atualizacao = False

            
            for (u, v, w) in self.edges:
               
                if dist[u] != inf and dist[u] + w < dist[v]:
                    if verbose:
                        print(
                            f"Relaxando aresta {u} -> {v} (peso {w}): "
                            f"dist[{v}] era {dist[v]} e passa a ser {dist[u] + w} "
                            f"(via {u})"
                        )
                    dist[v] = dist[u] + w
                    pred[v] = u
                    houve_atualizacao = True

            if verbose:
                print("Estado após a iteração de relaxamento:")
                self._print_state(dist, pred)

           
            if not houve_atualizacao:
                if verbose:
                    print("Nenhuma atualização nesta iteração. Encerrando mais cedo.")
                break

        
        if verbose:
            print("\nPasso 3: verificação de ciclos negativos")

        for (u, v, w) in self.edges:
            if dist[u] != inf and dist[u] + w < dist[v]:
               
                raise ValueError(
                    "O grafo contém um ciclo de peso negativo alcançável da origem."
                )

        if verbose:
            print("Nenhum ciclo negativo detectado.")
            print("Resultado final do Bellman-Ford:")
            self._print_state(dist, pred)

        return dist, pred


def reconstruct_path(pred, source, target):
   
    caminho = []
    atual = target

    while atual is not None:
        caminho.append(atual)
        if atual == source:
            break
        atual = pred[atual]

    
    if atual is None:
        return None

   
    caminho.reverse()
    return caminho


def build_logistics_graph():
    
    g = Graph()

    g.add_edge("A", "B", 4)
    g.add_edge("A", "C", 2)
    g.add_edge("A", "D", 5)
 

    g.add_edge("B", "E", 3)
    g.add_edge("B", "G", 11)
    g.add_edge("C", "E", 7)
    g.add_edge("C", "F", 10)
    g.add_edge("D", "F", 3)
    g.add_edge("D", "H", 9)

   
    g.add_edge("E", "H", 4)
    g.add_edge("E", "I", 5)
    g.add_edge("F", "I", 2)
    g.add_edge("F", "J", 6)

  
    g.add_edge("G", "J", -2)  

  
    g.add_edge("H", "K", 1)
    g.add_edge("I", "K", 2)
    g.add_edge("I", "L", 4)
    g.add_edge("J", "L", 1)
    g.add_edge("J", "M", 7)
    g.add_edge("K", "N", 3)
    g.add_edge("L", "N", 2)
    g.add_edge("L", "O", 5)
    g.add_edge("M", "O", 2)
    g.add_edge("M", "P", 8)
    g.add_edge("N", "P", 4)
    g.add_edge("O", "P", 1)

  

    return g


def main():
   
    
    g = build_logistics_graph()

    
    origem = "A"

    
    dist, pred = g.bellman_ford(origem, verbose=True)

   
    print("\n===== RESULTADOS FINAIS =====")
    print(f"Origem: {origem}")
    for v in sorted(g.vertices):
        if dist[v] == inf:
            
            print(f"Não existe caminho de {origem} até {v}.")
        else:
            caminho = reconstruct_path(pred, origem, v)
            caminho_str = " -> ".join(caminho)
            print(
                f"Menor custo de {origem} até {v}: {dist[v]} "
                f"(caminho: {caminho_str})"
            )



if __name__ == "__main__":
    main()
