import pyshacl
import rdflib
import argparse

data_dir = 'kg-metadata/data'

parser = argparse.ArgumentParser(description='Validate a KG file.')
parser.add_argument('-i', '--input', help='file to validate', default=f'{data_dir}/metadata/wikidata.ttl')
parser.add_argument('-s', '--shacl', help='shacl file to validate against', default=f'{data_dir}/shacl/kg-full.shacl.ttl')

args = parser.parse_args()


try: 
    rdf_file_path = f'{data_dir}/metadata/wikidata.ttl'
    shacl_file_path =  f'{data_dir}/shacl/kg-full.shacl.ttl'
    if args.input:
        rdf_file_path = args.input
    if args.shacl:
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
        debug=True,
        serialize_report_graph="ttl",
    )

    conforms, report_graph, report_text = results
    
    print("Conforms:", conforms)
    print("Results Text:", report_text)
    
except Exception as e:
    print("An error occurred:")
    print(e)