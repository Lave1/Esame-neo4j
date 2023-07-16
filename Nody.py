from neo4j import GraphDatabase

def create_nodes_if_not_exists():

    session = driver.session()

    # Controlla che esista il nodo 1
    query_check_start_node = "MATCH (s1:start {name: 'partenza 1'}) RETURN s1"
    result_start_node = session.run(query_check_start_node)
    existing_start_node = result_start_node.single()

    if existing_start_node:
        start_node = existing_start_node["s1"]
        print("il nodo partenza 1 esiste gia:", start_node)
    else:  
        # Crea il nodo 1
        query_create_start_node = "CREATE (s1:start {name: 'partena 1'}) RETURN s1"
        result_create_start_node = session.run(query_create_start_node)
        start_node = result_create_start_node.single()["s1"]
        print("nodo partenza 1 creato:", start_node)

    # controlla che esista il nodo 2
    query_check_shelter_node = "MATCH (m:shelter {name: 'rifugio 1'}) RETURN m1"
    result_shelter_node = session.run(query_check_shelter_node)
    existing_shelter_node = result_shelter_node.single()

    if existing_shelter_node:
        shelter_node = existing_shelter_node["r1"]
        print("", shelter_node)
    else:
        # Crea il nodo 2
        query_create_shelter_node = "CREATE (r1:shelter {name: 'rifugio 1'}) RETURN r1"
        result_create_shelter_node = session.run(query_create_shelter_node)
        shelter_node = result_create_shelter_node.single()["m1"]
        print("il nodo rifugio 1 creato:", shelter_node)

 # Controlla che esista il nodo 3
    query_check_start_node = "MATCH (s2:start {name: 'partenza 2'}) RETURN s2"
    result_start_node = session.run(query_check_start_node)
    existing_start_node = result_start_node.single()

    if existing_start_node:
        start_node = existing_start_node["s2"]
        print("il nodo partenza 2 esiste gia:", start_node)
    else:  
        # Crea il nodo 3
        query_create_start_node = "CREATE (s2:start {name: 'partenza 2'}) RETURN s2"
        result_create_start_node = session.run(query_create_start_node)
        start_node = result_create_start_node.single()["s2"]
        print("nodo partenza 2 creato:", start_node)

    # controlla che esista il nodo 4
    query_check_shelter_node = "MATCH (s2:shelter {name: 'rifugio 2'}) RETURN s2"
    result_shelter_node = session.run(query_check_shelter_node)
    existing_shelter_node = result_shelter_node.single()

    if existing_shelter_node:
        shelter_node = existing_shelter_node["r2"]
        print("il nodo fifugio 2 esite gia:", shelter_node)
    else:
        # Crea il nodo 4
        query_create_shelter_node = "CREATE (r2:shelter {name: 'rifugio 2'}) RETURN r2"
        result_create_shelter_node = session.run(query_create_shelter_node)
        shelter_node = result_create_shelter_node.single()["r2"]
        print("il nodo rifugio 2 creato:", shelter_node)

# Controlla che esista il nodo 5
    query_check_peak_node = "MATCH (p1:start {name: 'picco 1'}) RETURN p1"
    result_peak_node = session.run(query_check_peak_node)
    existing_peak_node = result_peak_node.single()

    if existing_peak_node:
        peak_node = existing_peak_node["p1"]
        print("il nodo picco 1 esiste gia:", peak_node)
    else:  
        # Crea il nodo 5
        query_create_peak_node = "CREATE (p1:start {name: 'peak 1'}) RETURN p1"
        result_create_peak_node = session.run(query_create_peak_node)
        peak_node = result_create_peak_node.single()["p1"]
        print("nodo picco 1 creato:", peak_node)

    # controlla che esista il nodo 6
    query_check_lake_node = "MATCH (l:shelter {name: 'lago'}) RETURN l"
    result_lake_node = session.run(query_check_lake_node)
    existing_lake_node = result_lake_node.single()

    if existing_lake_node:
        lake_node = existing_lake_node["l"]
        print("il nodo lago esiste gia", lake_node)
    else:
        # Crea il nodo 6
        query_create_lake_node = "CREATE (l:shelter {name: 'lago'}) RETURN l"
        result_create_lake_node = session.run(query_create_lake_node)
        lake_node = result_create_lake_node.single()["l"]
        print("il nodo lago creato:", lake_node)

 # Controlla che esista il nodo 7
    query_check_peak_node = "MATCH (p2:start {name: 'picco 2'}) RETURN p2"
    result_peak_node = session.run(query_check_peak_node)
    existing_peak_node = result_peak_node.single()

    if existing_peak_node:
        peak_node = existing_peak_node["p2"]
        print("il nodo picco 2 esiste gia:", peak_node)
    else:  
        # Crea il nodo 7
        query_create_peak_node = "CREATE (p2:start {name: 'picco 2'}) RETURN p2"
        result_create_peak_node = session.run(query_create_peak_node)
        peak_node = result_create_peak_node.single()["p2"]
        print("nodo partenza 2 creato:", peak_node)

    # controlla che esista il nodo 8
    query_check_path_node = "MATCH (s:shelter {name: 'sentiero'}) RETURN s"
    result_path_node = session.run(query_check_path_node)
    existing_path_node = result_path_node.single()

    if existing_path_node:
        path_node = existing_path_node["s"]
        print("il nodo sentiero esite gia:", path_node)
    else:
        # Crea il nodo 8
        query_create_path_node = "CREATE (s:shelter {name: 'sentiero'}) RETURN s"
        result_create_path_node = session.run(query_create_path_node)
        path_node = result_create_path_node.single()["s"]
        print("il nodo rifugio 2 creato:", path_node)


    session.close()

# Richiamo la funzione per creare i nodi se non esistono gia 
create_nodes_if_not_exists()

# Close the driver at the end of your program
driver.close()