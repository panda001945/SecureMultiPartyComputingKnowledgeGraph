import unittest
from graph_construction.build_graph import KnowledgeGraph


class TestGraphConstruction(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.graph = KnowledgeGraph("bolt://localhost:7687", "neo4j", "password")

    @classmethod
    def tearDownClass(cls):
        cls.graph.close()

    def test_create_node(self):
        self.graph.create_node("TestLabel", {"name": "TestNode"})
        result = self.graph.run_query("MATCH (n:TestLabel {name: 'TestNode'}) RETURN n")
        self.assertTrue(result)

    def test_create_relationship(self):
        self.graph.create_node("TestNode1", {"name": "Node1"})
        self.graph.create_node("TestNode2", {"name": "Node2"})
        self.graph.create_relationship("Node1", "Node2", "CONNECTED_TO")
        result = self.graph.run_query(
            "MATCH (a)-[r:CONNECTED_TO]->(b) WHERE a.name = 'Node1' AND b.name = 'Node2' RETURN r"
        )
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
