import csv
from neo4j import GraphDatabase


class Neo4jImporter:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def import_nodes(self, file_path):
        with open(file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            with self.driver.session() as session:
                for row in csv_reader:
                    query = f"CREATE (n:{row['label']} {{id: $id, name: $name}})"
                    session.run(query, {"id": int(row["id"]), "name": row["name"]})

    def import_edges(self, file_path):
        with open(file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            with self.driver.session() as session:
                for row in csv_reader:
                    query = (
                        "MATCH (a {id: $from}), (b {id: $to}) "
                        "CREATE (a)-[r:{type}]->(b)"
                    )
                    session.run(query, {"from": int(row["from"]), "to": int(row["to"]), "type": row["type"]})


if __name__ == "__main__":
    importer = Neo4jImporter("bolt://localhost:7687", "neo4j", "password")
    importer.import_nodes("database/nodes.csv")
    importer.import_edges("database/edges.csv")
    importer.close()
