from neo4j import GraphDatabase

#connessione al batabase neo4j
uri = "neo4j+s://ece1266a.databases.neo4j.io"
user = "neo4j"
password = "qPxdTyg5M_3K68J_fCWvrm6DAwxMZS8hHVxTbVGSJ94"

driver = GraphDatabase.driver(uri, auth=(user, password))


def creazione_nodi():
    session = driver.session()
    
    
    
    
    result = session.run(#query)
                         
      #questi servono per chiudere il collegamento al server neo4j                   
    # session.close()
    # driver.close()