import networkx as nx
import dash
from dash import dcc, html
import plotly.graph_objs as go


def get_graph_data():
    """
    Returns example graph data.
    Replace with actual data fetched from Neo4j or processed files.
    """
    nodes = [{"id": "Protocol1", "label": "Yao's Garbled Circuits"},
             {"id": "Application1", "label": "Privacy-preserving computations"}]
    edges = [{"source": "Protocol1", "target": "Application1", "label": "IMPLEMENTS"}]
    return nodes, edges


def create_dash_app():
    app = dash.Dash(__name__)
    nodes, edges = get_graph_data()

    G = nx.DiGraph()
    for node in nodes:
        G.add_node(node['id'], label=node['label'])
    for edge in edges:
        G.add_edge(edge['source'], edge['target'], label=edge['label'])

    pos = nx.spring_layout(G)
    edge_trace = []
    for edge in G.edges(data=True):
        edge_trace.append(go.Scatter(
            x=[pos[edge[0]][0], pos[edge[1]][0], None],
            y=[pos[edge[0]][1], pos[edge[1]][1], None],
            line=dict(width=1, color='#888'),
            hoverinfo='none',
            mode='lines'))

    node_trace = go.Scatter(
        x=[pos[node][0] for node in G.nodes()],
        y=[pos[node][1] for node in G.nodes()],
        text=[G.nodes[node]['label'] for node in G.nodes()],
        mode='markers+text',
        marker=dict(size=10, color='blue'))

    app.layout = html.Div([
        dcc.Graph(
            id='graph',
            figure=go.Figure(data=edge_trace + [node_trace],
                             layout=go.Layout(showlegend=False))
        )
    ])

    return app


if __name__ == "__main__":
    app = create_dash_app()
    app.run_server(debug=True)
