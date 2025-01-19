import csv
from neo4j import GraphDatabase


class GraphLoader:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def load_nodes(self, file_path):
        with open(file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            with self.driver.session() as session:
                for row in csv_reader:
                    query = f"CREATE (n:{row['label']} {{name: $name}})"
                    session.run(query, {"name": row["name"]})

    def load_edges(self, file_path):
        with open(file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            with self.driver.session() as session:
                for row in csv_reader:
                    query = (
                        "MATCH (a {name: $from}), (b {name: $to}) "
                        "CREATE (a)-[r:{rel_type}]->(b)"
                    )
                    session.run(query, {"from": row["from"], "to": row["to"], "rel_type": row["type"]})


if __name__ == "__main__":
    loader = GraphLoader("bolt://localhost:7687", "neo4j", "password")
    loader.load_nodes("data/processed/entities.csv")
    loader.load_edges("data/processed/edges.csv")
    loader.close()
