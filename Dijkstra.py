import heapq  


GRAFO_CIDADE = {
    "Centro":     {"Mercado": 4, "Hospital": 3, "Estacao": 6, "Parque": 5},
    "Mercado":    {"Centro": 4, "Shopping": 2, "BairroA": 7},
    "Hospital":   {"Centro": 3, "Universidade": 4, "BairroB": 6},
    "Universidade": {"Hospital": 4, "BairroC": 5, "Terminal": 9},
    "Aeroporto":  {"Parque": 4, "Terminal": 3, "BairroD": 8},
    "Estacao":    {"Centro": 6, "Shopping": 3, "BairroE": 4},
    "Shopping":   {"Mercado": 2, "Estacao": 3, "BairroF": 6},
    "Parque":     {"Centro": 5, "Aeroporto": 4, "BairroG": 3},
    "BairroA":    {"Mercado": 7, "BairroB": 4},
    "BairroB":    {"Hospital": 6, "BairroA": 4, "BairroC": 3},
    "BairroC":    {"Universidade": 5, "BairroB": 3},
    "BairroD":    {"Aeroporto": 8, "BairroE": 5},
    "BairroE":    {"Estacao": 4, "BairroD": 5},
    "BairroF":    {"Shopping": 6, "Terminal": 4},
    "BairroG":    {"Parque": 3, "Terminal": 7},
    "Terminal":   {"Universidade": 9, "Aeroporto": 3, "BairroF": 4, "BairroG": 7},
}


assert len(GRAFO_CIDADE) >= 16, "O grafo deve ter no mínimo 16 vértices."



def dijkstra(grafo: dict, origem: str, debug: bool = False):
    

    
    dist = {v: float("inf") for v in grafo}
   
    anterior = {v: None for v in grafo}

    
    dist[origem] = 0

    
    visitados = set()

   
    fila = [(0, origem)]

    passo = 0  

  
    while fila:
       
        dist_atual, u = heapq.heappop(fila)

        
        if u in visitados:
            continue

        visitados.add(u)

        if debug:
            print(f"Passo {passo}: visitando '{u}' com distância atual {dist_atual}")
            passo += 1

        
        for v, peso in grafo[u].items():
            if v in visitados:
                continue  

           
            nova_dist = dist_atual + peso

            if nova_dist < dist[v]:
                dist[v] = nova_dist
                anterior[v] = u  
                heapq.heappush(fila, (nova_dist, v))

                if debug:
                    print(
                        f"  Atualizando '{v}': nova distância = {nova_dist} (via '{u}')"
                    )

    return dist, anterior



def reconstruir_caminho(anterior: dict, origem: str, destino: str):
    
    caminho = []
    atual = destino

    
    while atual is not None:
        caminho.append(atual)
        atual = anterior[atual]

    
    if caminho[-1] != origem:
        return None  

   
    caminho.reverse()
    return caminho



def caminho_mais_curto(grafo: dict, origem: str, destino: str, debug: bool = False):
    
    if origem not in grafo:
        raise ValueError(f"Origem '{origem}' não existe no grafo.")
    if destino not in grafo:
        raise ValueError(f"Destino '{destino}' não existe no grafo.")

    dist, anterior = dijkstra(grafo, origem, debug=debug)
    if dist[destino] == float("inf"):
        return None, float("inf")

    caminho = reconstruir_caminho(anterior, origem, destino)
    return caminho, dist[destino]



def mostrar_vertices(grafo: dict):
    
    print("Locais disponíveis no mapa:\n")
    for i, v in enumerate(grafo.keys(), start=1):
        print(f"{i:2d}. {v}")
    print()  # linha em branco


def main():
    print("==== SIMULAÇÃO DE CAMINHOS EM UMA CIDADE (DIJKSTRA) ====\n")

    grafo = GRAFO_CIDADE
    mostrar_vertices(grafo)

    origem = input("Digite o NOME EXATO do local de ORIGEM: ").strip()
    destino = input("Digite o NOME EXATO do local de DESTINO: ").strip()

    ver_passos = input("Deseja ver o passo a passo do algoritmo? (s/n): ").strip().lower()
    debug = ver_passos == "s"

    try:
        caminho, custo = caminho_mais_curto(grafo, origem, destino, debug=debug)
    except ValueError as e:
        print("\nErro:", e)
        return

    print("\n===== RESULTADO =====")
    if caminho is None:
        print(f"Não existe caminho de '{origem}' até '{destino}' no grafo.")
    else:
        print("Caminho mais curto encontrado:")
        print(" -> ".join(caminho))
        print(f"Custo total (tempo estimado de viagem): {custo} minutos")


if __name__ == "__main__":
    main()
