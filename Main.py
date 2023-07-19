from neo4j import GraphDatabase
from Nody import create_nodes_if_not_exists

# Sono le credenziali del server neo4j
uri = "neo4j+s://ece1266a.databases.neo4j.io"
user = "neo4j"
password = "qPxdTyg5M_3K68J_fCWvrm6DAwxMZS8hHVxTbVGSJ94"

driver = GraphDatabase.driver(uri, auth=(user, password))

# Controlla la connessione al server di neo4j
def check_connection():
    session = driver.session()

    result = session.run("RETURN 1")
    record = result.single()

    if record:
        print("Connesso al server di Neo4j.")
    else:
        print("Connessione fallita al server di Neo4j.")

    session.close()

check_connection()

# Richima la funzione di creazione dei nodi se non esistono
if __name__ == '__main__':
    create_nodes_if_not_exists()

# Funzione che chrea le relazioni tra i nodi
def create_relationships():
    session = driver.session()

    query_create_relationships = """
    MATCH (s1:start {name: 'partenza 1'}),
          (l:lake {name: 'lago'})
    CREATE (s1)-[:facile{distanza:'2km', percorribilità_in_bici: 'si', tempo: '1h 30m'}]->(l)
    """

    session.run(query_create_relationships)
    print("Collegamento 'facile' tra partenza 1 e lago creato con informazioni aggiuntive.")

    query_create_relationships = """
    MATCH (s1:start {name: 'partenza 1'}),
          (p1:peak {name: 'picco 1'})
    CREATE (s1)-[:difficile{distanza:'4km', percorribilità_in_bici: 'no', tempo: '2h'}]->(p1)
    """

    session.run(query_create_relationships)
    print("Collegamento 'difficile' tra partenza 1 e picco 1 creato con informazioni aggiuntive.")

    query_create_relationships = """
    MATCH (p1:peak {name: 'picco 1'}),
          (l:lake {name: 'lago'})
    CREATE (p1)-[:facile{distanza:'2km', percorribilità_in_bici: 'no', tempo: '1h 30m'}]->(l)
    """

    session.run(query_create_relationships)
    print("Collegamento 'facile' tra picco 1 e lago creato con informazioni aggiuntive.")

    query_create_relationships = """
    MATCH (l:lake {name: 'lago'}),
          (r1:shelter {name: 'rifugio 1'})
    CREATE (l)-[:facile{distanza:'3km', percorribilità_in_bici: 'si', tempo: '2h 30m'}]->(r1)
    """

    session.run(query_create_relationships)
    print("Collegamento 'facile' tra lago e rifugio 1 creato con informazioni aggiuntive.")

    query_create_relationships = """
    MATCH (p1:peak {name: 'picco 1'}),
          (r1:shelter {name: 'rifugio 1'})
    CREATE (p1)-[:difficile{distanza:'3km', percorribilità_in_bici: 'si', tempo: '2h'}]->(r1)
    """

    session.run(query_create_relationships)
    print("Collegamento 'difficile' tra picco 1 e rifugio 1 creato con informazioni aggiuntive.")

    query_create_relationships = """
    MATCH (p1:peak {name: 'picco 1'}),
          (p2:peak {name: 'picco 2'})
    CREATE (p1)-[:facile{distanza:'6km', percorribilità_in_bici: 'no', tempo: '3h'}]->(p2)
    """

    session.run(query_create_relationships)
    print("Collegamento 'facile' tra picco 1 e picco 2 creato con informazioni aggiuntive.")

    query_create_relationships = """
    MATCH (r1:shelter {name: 'rifugio 1'}),
          (p2:peak {name: 'picco 2'})
    CREATE (r1)-[:difficile{distanza:'3km', percorribilità_in_bici: 'no', tempo: '1h 30m'}]->(p2)
    """

    session.run(query_create_relationships)
    print("Collegamento 'difficile' tra rifugio 1 e picco 2 creato con informazioni aggiuntive.")

    query_create_relationships = """
    MATCH (r1:shelter {name: 'rifugio 1'}),
          (s:trail {name: 'sentiero'})
    CREATE (r1)-[:facile{distanza:'3km', percorribilità_in_bici: 'si', tempo: '2h 30m'}]->(s)
    """

    session.run(query_create_relationships)
    print("Collegamento 'facile' tra rifugio 1 e sentiero creato con informazioni aggiuntive.")

    query_create_relationships = """
    MATCH (p2:peak {name: 'picco 2'}),
          (s:trail {name: 'sentiero'})
    CREATE (p2)-[:difficile{distanza:'2km', percorribilità_in_bici: 'no', tempo: '1h 30m'}]->(s)
    """

    session.run(query_create_relationships)
    print("Collegamento 'difficile' tra picco 2 e sentiero creato con informazioni aggiuntive.")

    query_create_relationships = """
    MATCH (s:trail {name: 'sentiero'}),
          (r2:shelter {name: 'rifugio 2'})
    CREATE (s)-[:facile{distanza:'2km', percorribilità_in_bici: 'si', tempo: '2h'}]->(r2)
    """

    session.run(query_create_relationships)
    print("Collegamento 'facile' tra sentiero e rifugio 2 creato con informazioni aggiuntive.")

    query_create_relationships = """
    MATCH (s:trail {name: 'sentiero'}),
          (s2:start {name: 'partenza 2'})
    CREATE (s)-[:facile{distanza:'1km', percorribilità_in_bici: 'si', tempo: '1h 30m'}]->(s2)
    """

    session.run(query_create_relationships)
    print("Collegamento 'facile' tra sentiero e partenza 2 creato con informazioni aggiuntive.")

    query_create_relationships = """
    MATCH (s2:start {name: 'partenza 2'}),
          (r2:shelter {name: 'rifugio 2'})
    CREATE (s2)-[:difficile{distanza:'4km', percorribilità_in_bici: 'no', tempo: '2h'}]->(r2)
    """

    session.run(query_create_relationships)
    print("Collegamento 'difficile' tra partenza 2 e picco 2 creato con informazioni aggiuntive.")

    
# Funzione che seleziona il nodo di partenza 
def select_start_node():
    while True:

        # Permette all'utente di segliere la partenza 
        choice = input("Seleziona il nodo di partenza (1 per partenza 1 o 2 per partenza 2): ")
        if choice == "1" or choice == "2":
            if choice == "1":
                return {"name": "partenza 1", "label": "start"}
            else:
                return {"name": "partenza 2", "label": "start"}
        else:
            print("Scelta non valida. Riprova.")

# Funzone che permette la scelta della destiazione 
def select_destination_node():
    session = driver.session()

    # Prende i nodi 
    query_get_nodes = """
    MATCH (n)
    RETURN DISTINCT labels(n) AS label, n.name AS name
    """

    result = session.run(query_get_nodes)

    nodes = []
    for record in result:
        nodes.append(record)

    session.close()

    if not nodes:
        print("Nessun nodo disponibile nel database.")
        exit(1)

    # Stampa i nodi selezionati
    print("Nodi disponibili:")
    for i, node in enumerate(nodes):
        print(f"{i+1}. {node['name']} ({', '.join(node['label'])})")

    while True:

        # Permette all'utente di selezionare la destinazione
        choice = input("Seleziona il numero del nodo di destinazione: ")

        if choice.isdigit() and 1 <= int(choice) <= len(nodes):
            selected_node = nodes[int(choice) - 1]
            return {"name": selected_node["name"], "label": selected_node["label"][0]}
        
        else:
            print("Scelta non valida. Riprova.")

# Funzione che seleziona i percorsi in base alla partenza e la destinazione selezionata
def find_paths(start_node, destination_node):
    session = driver.session()

    query_find_paths = """
    MATCH path = (start {name: $start_node_name})-[:facile|difficile*]->(destination {name: $destination_node_name})
    RETURN path
    """

    result = session.run(
        query_find_paths,
        start_node_name=start_node["name"],
        destination_node_name=destination_node["name"]
    )

    paths = []
    
    for record in result:
        path = record["path"]
        paths.append(path)

    session.close()

    return paths

if __name__ == '__main__':

    if not check_connection():
        print("Connessione fallita al server di Neo4j.")
        

    create_relationships()

    start_node = select_start_node()
    destination_node = select_destination_node()

    paths = find_paths(start_node, destination_node)

    if paths:
        print("Percorsi disponibili da", start_node["name"], "a", destination_node["name"] + ":")
        for i, path in enumerate(paths):
            relationships = [rel.type for rel in path.relationships]
            print("Percorso", i + 1, ":", " -> ".join(relationships))
    else:
        print("Nessun percorso trovato da", start_node["name"], "a", destination_node["name"])

    driver.close()
