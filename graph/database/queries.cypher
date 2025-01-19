// Query 1: Retrieve all nodes
MATCH (n) RETURN n;

// Query 2: Retrieve all relationships
MATCH ()-[r]->() RETURN r;

// Query 3: Find protocols and their applications
MATCH (p:Protocol)-[r:IMPLEMENTS]->(a:Application)
RETURN p.name AS Protocol, a.name AS Application;

// Query 4: Find participants and their applications
MATCH (n:Participant)-[r:PARTICIPATES_IN]->(a:Application)
RETURN n.name AS Participant, a.name AS Application;

// Query 5: Shortest path between two nodes
MATCH p=shortestPath((a {name: 'Participant A'})-[*]->(b {name: 'Privacy-preserving computations'}))
RETURN p;
