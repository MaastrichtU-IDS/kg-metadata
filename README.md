# kg-metadata

Knowledge Graph (KG) Metadata Specification and Validation

This project aims to create a specification for the description of knowledge graphs.

The KG specification [html](https://maastrichtu-ids.github.io/kg-metadata/) & [SHACL](data/shacl/kg-full.shacl.ttl) was developed using [SHACL](https://www.w3.org/TR/shacl/) from a [community spreadsheet](https://docs.google.com/spreadsheets/d/1QkTqLE2pjZHoC6Ly08Zs7bXbgSh-e5p0cy3QJRaX-L8/edit?usp=sharing)


# setup the environment
prepare the local environment
        
        python -m venv .venv

activate the local environment
        
        source .venv/bin/activate

install the python packages

        python -m pip install -r requirements.txt

# run the test
run the shape validation with kg metadata and the KG shacl specification.

        python src/validate.py -i data/metadata/wikidata.ttl -s data/shacl/kg-full.shacl.ttl
        
