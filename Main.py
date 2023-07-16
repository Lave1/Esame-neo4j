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

# Call the function to check the connection 
check_connection()


def create_nodes_if_not_exists():
    session = driver.session()

    # Check if the start node already exists
    query_check_start_node = "MATCH (s:start {name: 'parcheggio'}) RETURN s"
    result_start_node = session.run(query_check_start_node)
    existing_start_node = result_start_node.single()

    if existing_start_node:
        start_node = existing_start_node["s"]
        print("Start node already exists:", start_node)
    else:
        # Create the start node
        query_create_start_node = "CREATE (s:start {name: 'parcheggio'}) RETURN s"
        result_create_start_node = session.run(query_create_start_node)
        start_node = result_create_start_node.single()["s"]
        print("Created start node:", start_node)

    # Check if the middle node already exists
    query_check_middle_node = "MATCH (m:middle {name: 'valle'}) RETURN m"
    result_middle_node = session.run(query_check_middle_node)
    existing_middle_node = result_middle_node.single()

    if existing_middle_node:
        middle_node = existing_middle_node["m"]
        print("Middle node already exists:", middle_node)
    else:
        # Create the middle node
        query_create_middle_node = "CREATE (m:middle {name: 'valle'}) RETURN m"
        result_create_middle_node = session.run(query_create_middle_node)
        middle_node = result_create_middle_node.single()["m"]
        print("Created middle node:", middle_node)

    session.close()

# Call the function to create nodes if they don't exist
create_nodes_if_not_exists()

# Close the driver at the end of your program
driver.close()
