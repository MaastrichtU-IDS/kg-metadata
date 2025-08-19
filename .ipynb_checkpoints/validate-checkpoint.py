import pyshacl
import rdflib
import argparse

parser = argparse.ArgumentParser(description='Validate a KG file.')
parser.add_argument('-i', '--input', help='file to validate', required=True)
parser.add_argument('-s', '--shacl', help='shacl file to validate against', required=True)

args = parser.parse_args()

try: 
    rdf_file_path = args.input
    shacl_file_path = args.shacl
    
    data_graph = rdflib.Graph()
    data_graph.parse(rdf_file_path, format="turtle")

    # Create a SHACL graph
    shapes_graph = rdflib.Graph()
    shapes_graph.parse(shacl_file_path, format="turtle")

    results = pyshacl.validate(
        data_graph,
        shacl_graph=shapes_graph,
        data_graph_format="ttl",
        shacl_graph_format="ttl",
        inference="rdfs",
        debug=False,
        serialize_report_graph="ttl",
    )

    conforms, report_graph, report_text = results
    
    # Print if it conforms or not
    print("Conforms:", conforms)
    
    # Parse report graph to extract violations
    if not conforms:
        report_graph = rdflib.Graph().parse(data=report_graph, format="turtle")
        violation_count = 0
        for s in report_graph.subjects(predicate=rdflib.RDF.type, object=rdflib.URIRef("http://www.w3.org/ns/shacl#ValidationResult")):
            violation_count += 1
            focus_node = report_graph.value(subject=s, predicate=rdflib.URIRef("http://www.w3.org/ns/shacl#focusNode"))
            result_message = report_graph.value(subject=s, predicate=rdflib.URIRef("http://www.w3.org/ns/shacl#resultMessage"))
            result_path = report_graph.value(subject=s, predicate=rdflib.URIRef("http://www.w3.org/ns/shacl#resultPath"))
            print(f"Violation {violation_count}:")
            print(f"  Focus Node: {focus_node}")
            print(f"  Message: {result_message}")
            if result_path:
                print(f"  Result Path: {result_path}")
        
        print("Total Violations:", violation_count)

except Exception as e:
    print("An error occurred:")
    print(e)
