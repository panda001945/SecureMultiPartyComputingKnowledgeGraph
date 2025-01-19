import json
import csv


def validate_node(node, schema):
    """
    Validate a node against the schema.
    """
    label = node.get("label")
    if label not in schema:
        return False, f"Label '{label}' not defined in schema."

    schema_props = schema[label]
    for field in schema_props["required"]:
        if field not in node or node[field] == "":
            return False, f"Missing required field '{field}' for label '{label}'."

    return True, "Valid"


def validate_edge(edge, schema):
    """
    Validate an edge against the schema.
    """
    rel_type = edge.get("type")
    if rel_type not in schema:
        return False, f"Relationship type '{rel_type}' not defined in schema."

    schema_props = schema[rel_type]
    # Check for required fields
    missing_fields = [
        field for field in schema_props["required"]
        if field not in edge or edge[field] == ""
    ]

    # Adjust to map 'from' and 'to' to expected schema
    if 'source' in schema_props["required"] and 'from' not in edge:
        missing_fields.append('source')
    if 'target' in schema_props["required"] and 'to' not in edge:
        missing_fields.append('target')

    if missing_fields:
        return False, f"Missing required fields {missing_fields} for relationship '{rel_type}'."

    return True, "Valid"


if __name__ == "__main__":
    # Load schemas
    with open("../schema/node_schema.json", "r") as f:
        node_schema = json.load(f)
    with open("../schema/edge_schema.json", "r") as f:
        edge_schema = json.load(f)

    # Validate nodes
    with open("../database/nodes.csv", mode="r", encoding="utf-8") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            is_valid, message = validate_node(row, node_schema)
            if not is_valid:
                print(f"Node validation failed: {message}")

    # Validate edges
with open("../database/edges.csv", mode="r", encoding="utf-8") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        # Map 'from' and 'to' to expected 'source' and 'target'
        row['source'] = row.get('from', '')
        row['target'] = row.get('to', '')
        is_valid, message = validate_edge(row, edge_schema)
        if not is_valid:
            print(f"Edge validation failed: {message}")
            print(f"Problematic row: {row}")

