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
    CREATE (s1)-[:facile{distanza:'2km', percorribilità_in_bici: 'si'}]->(l)
    """
    session.run(query_create_relationships)
    print("Collegamento 'facile' tra partenza 1 e lago creato con informazioni aggiuntive.")

    session.close()

create_relationships()

driver.close()
