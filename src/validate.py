import pyshacl
import rdflib

data_dir = 'kg-metadata/data'

try: 
    rdf_file_path = f'{data_dir}/metadata/wikidata.ttl'
    shacl_file_path =  f'{data_dir}/shacl/kg.shacl.ttl'
    service_file_path = f'{data_dir}/shacl/dataservice.shacl.ttl'
    data_graph = rdflib.Graph()
    data_graph.parse(rdf_file_path, format="turtle")

    # Create a SHACL graph
    shapes_graph = rdflib.Graph()
    shapes_graph.parse(shacl_file_path, format="turtle")
    shapes_graph.parse(service_file_path, format="turtle")

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