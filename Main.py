from neo4j import GraphDatabase # Importa la classe GraphDatabase dalla libreria di neo4j
from Nody import create_nodes_if_not_exists # Importa la funzione crea un nodo se non esiste 

# Connessione al database di Neo4j
uri = "neo4j+s://ece1266a.databases.neo4j.io"
user = "neo4j"
password = "qPxdTyg5M_3K68J_fCWvrm6DAwxMZS8hHVxTbVGSJ94"

driver = GraphDatabase.driver(uri, auth=(user, password))

def check_connection():
    session = driver.session()
    
    # Esegue una query per controllare le connessioni
    result = session.run("RETURN 1")
    record = result.single()
    
    if record:
        print("Connected to Neo4j server.")
    else:
        print("Failed to connect to Neo4j server.")
    
    session.close()

# Richiama la funzione controlla connessioni
check_connection()

if __name__ == '__main__':

    # Richiamon la funzione crea un nodo se non esiste
    create_nodes_if_not_exists()

# Chiude la connessione con il drive
driver.close()
