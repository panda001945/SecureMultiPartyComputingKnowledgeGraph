from neo4j import GraphDatabase


class KnowledgeGraph:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def create_node(self, label, properties):
        query = f"CREATE (n:{label} {{ {', '.join([f'{k}: ${k}' for k in properties.keys()])} }})"
        with self.driver.session() as session:
            session.run(query, properties)

    def create_relationship(self, from_node, to_node, rel_type):
        query = (
            f"MATCH (a), (b) "
            f"WHERE a.name = $from_name AND b.name = $to_name "
            f"CREATE (a)-[r:{rel_type}]->(b)"
        )
        with self.driver.session() as session:
            session.run(query, {"from_name": from_node, "to_name": to_node})


if __name__ == "__main__":
    graph = KnowledgeGraph("bolt://localhost:7687", "neo4j", "password")
    graph.create_node("Protocol", {"name": "Yao's Garbled Circuits"})
    graph.create_node("Application", {"name": "Privacy-preserving computations"})
    graph.create_relationship("Yao's Garbled Circuits", "Privacy-preserving computations", "IMPLEMENTS")
    graph.close()
