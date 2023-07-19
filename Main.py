from neo4j import GraphDatabase
from Nody import create_nodes_if_not_exists

uri = "neo4j+s://ece1266a.databases.neo4j.io"
user = "neo4j"
password = "qPxdTyg5M_3K68J_fCWvrm6DAwxMZS8hHVxTbVGSJ94"

driver = GraphDatabase.driver(uri, auth=(user, password))

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

if __name__ == '__main__':
    create_nodes_if_not_exists()

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

    session.close()

create_relationships()

driver.close()
