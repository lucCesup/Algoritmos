from typing import Dict, List, Set, Optional

class Grafo:
    def __init__(self):
        self.adj: Dict[str, List[str]] = {}

    def adicionar_vertice(self, v: str) -> None:
        if v not in self.adj:
            self.adj[v] = []

    def adicionar_aresta(self, u: str, v: str, bidirecional: bool = True) -> None:
        self.adicionar_vertice(u)
        self.adicionar_vertice(v)
        if v not in self.adj[u]:
            self.adj[u].append(v)
        if bidirecional and u not in self.adj[v]:
            self.adj[v].append(u)

    def dfs_recursiva(self, inicio: str) -> List[str]:
        if inicio not in self.adj:
            raise ValueError(f"Vértice de início '{inicio}' não existe no grafo.")
        visitados: Set[str] = set()
        ordem: List[str] = []

        def dfs(v: str) -> None:
            visitados.add(v)
            ordem.append(v)
            for vizinho in self.adj.get(v, []):
                if vizinho not in visitados:
                    dfs(vizinho)

        dfs(inicio)
        return ordem

    def dfs_iterativa(self, inicio: str) -> List[str]:
        if inicio not in self.adj:
            raise ValueError(f"Vértice de início '{inicio}' não existe no grafo.")
        visitados: Set[str] = set()
        ordem: List[str] = []
        pilha: List[str] = [inicio]

        while pilha:
            v = pilha.pop()
            if v not in visitados:
                visitados.add(v)
                ordem.append(v)
                for vizinho in reversed(self.adj.get(v, [])):
                    if vizinho not in visitados:
                        pilha.append(vizinho)

        return ordem

    def dfs_caminho(self, origem: str, destino: str) -> Optional[List[str]]:
        if origem not in self.adj or destino not in self.adj:
            raise ValueError("Origem ou destino não existem no grafo.")

        visitados: Set[str] = set()
        pai: Dict[str, Optional[str]] = {origem: None}
        caminho_encontrado = False

        def dfs(v: str) -> None:
            nonlocal caminho_encontrado
            if caminho_encontrado:
                return
            visitados.add(v)
            if v == destino:
                caminho_encontrado = True
                return
            for vizinho in self.adj.get(v, []):
                if vizinho not in visitados:
                    pai[vizinho] = v
                    dfs(vizinho)

        dfs(origem)

        if not caminho_encontrado:
            return None

        caminho: List[str] = []
        atual: Optional[str] = destino
        while atual is not None:
            caminho.append(atual)
            atual = pai.get(atual)
        caminho.reverse()
        return caminho


def construir_grafo_rede_social() -> Grafo:
    g = Grafo()

    g.adicionar_aresta('A', 'B')
    g.adicionar_aresta('A', 'C')

    g.adicionar_aresta('B', 'D')
    g.adicionar_aresta('B', 'E')

    g.adicionar_aresta('C', 'F')
    g.adicionar_aresta('C', 'G')

    g.adicionar_aresta('D', 'H')

    g.adicionar_aresta('E', 'I')
    g.adicionar_aresta('E', 'J')

    g.adicionar_aresta('F', 'K')

    g.adicionar_aresta('G', 'L')
    g.adicionar_aresta('G', 'M')

    g.adicionar_aresta('H', 'N')

    g.adicionar_aresta('I', 'O')

    g.adicionar_aresta('J', 'P')

    g.adicionar_aresta('K', 'L')
    g.adicionar_aresta('M', 'N')
    g.adicionar_aresta('O', 'P')

    return g


def exibir_mapa_pessoas():
    print("Mapa da rede social (vértices do grafo):")
    print(" A - Ana")
    print(" B - Bruno")
    print(" C - Carla")
    print(" D - Diego")
    print(" E - Elisa")
    print(" F - Felipe")
    print(" G - Gabriela")
    print(" H - Henrique")
    print(" I - Isabel")
    print(" J - João")
    print(" K - Karina")
    print(" L - Lucas")
    print(" M - Marina")
    print(" N - Natália")
    print(" O - Otávio")
    print(" P - Paulo")
    print()


def menu():
    grafo = construir_grafo_rede_social()

    while True:
        print("=" * 60)
        print("   SIMULAÇÃO DE DFS (BUSCA EM PROFUNDIDADE) NA REDE SOCIAL")
        print("=" * 60)
        print("1 - Ver mapa das pessoas (vértices)")
        print("2 - Executar DFS recursiva a partir de uma pessoa")
        print("3 - Executar DFS iterativa a partir de uma pessoa")
        print("4 - Buscar caminho de amizade entre duas pessoas (DFS)")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            exibir_mapa_pessoas()

        elif opcao == '2':
            inicio = input("Digite a pessoa de início (A-P): ").strip().upper()
            try:
                ordem = grafo.dfs_recursiva(inicio)
                print(f"Ordem de visita (DFS recursiva) a partir de {inicio}:")
                print(" -> ".join(ordem))
            except ValueError as e:
                print(f"Erro: {e}")

        elif opcao == '3':
            inicio = input("Digite a pessoa de início (A-P): ").strip().upper()
            try:
                ordem = grafo.dfs_iterativa(inicio)
                print(f"Ordem de visita (DFS iterativa) a partir de {inicio}:")
                print(" -> ".join(ordem))
            except ValueError as e:
                print(f"Erro: {e}")

        elif opcao == '4':
            origem = input("Digite a pessoa de origem (A-P): ").strip().upper()
            destino = input("Digite a pessoa de destino (A-P): ").strip().upper()
            try:
                caminho = grafo.dfs_caminho(origem, destino)
                if caminho is None:
                    print(f"Não existe caminho de amizade entre {origem} e {destino}.")
                else:
                    print(f"Caminho de amizade de {origem} até {destino}:")
                    print(" -> ".join(caminho))
            except ValueError as e:
                print(f"Erro: {e}")

        elif opcao == '0':
            print("Encerrando a simulação. Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
