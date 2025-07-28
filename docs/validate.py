from rdflib import Graph
from pyshacl import validate

# Load the JSON-LD metadata
g = Graph()
g.parse("metadata_complete.jsonld", format="json-ld")

# Load the SHACL shapes
shacl_graph = Graph()
shacl_graph.parse("schema_shacl.ttl", format="turtle")

# Validate it
conforms, results_graph, results_text = validate(
    data_graph=g,
    shacl_graph=shacl_graph,
    inference='rdfs',
    serialize_report_graph=True
)

print("Conforms:", conforms)
print(results_text)
