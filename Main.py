from neo4j import GraphDatabase

# Connection to the Neo4j database
uri = "neo4j+s://ece1266a.databases.neo4j.io"
user = "neo4j"
password = "qPxdTyg5M_3K68J_fCWvrm6DAwxMZS8hHVxTbVGSJ94"

driver = GraphDatabase.driver(uri, auth=(user, password))

def check_connection():
    session = driver.session()
    
    # Execute a simple query to check the connection
    result = session.run("RETURN 1")
    record = result.single()
    
    if record:
        print("Connected to Neo4j server.")
    else:
        print("Failed to connect to Neo4j server.")
    
    session.close()
    driver.close()

# Call the function to check the connection
check_connection()
