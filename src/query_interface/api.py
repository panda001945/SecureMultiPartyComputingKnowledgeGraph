from flask import Flask, request, jsonify
from neo4j import GraphDatabase

app = Flask(__name__)


class GraphQuery:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def run_query(self, query):
        with self.driver.session() as session:
            result = session.run(query)
            return [record.data() for record in result]


db = GraphQuery("bolt://localhost:7687", "neo4j", "password")


@app.route("/query", methods=["GET"])
def query():
    keyword = request.args.get("keyword")
    query = f"MATCH (n) WHERE n.name CONTAINS '{keyword}' RETURN n"
    result = db.run_query(query)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
