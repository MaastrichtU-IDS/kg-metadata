[![Wikidata Metadata Validation](https://github.com/marmhm/kg-metadata/actions/workflows/validate-metadata.yml/badge.svg)](https://github.com/marmhm/kg-metadata/actions/workflows/validate-metadata.yml)
[![SHACL Syntax Validation](https://github.com/marmhm/kg-metadata/actions/workflows/shacl-syntax-check.yml/badge.svg)](https://github.com/marmhm/kg-metadata/actions/workflows/shacl-syntax-check.yml)


# Knowledge Graph Metadata Specification and Validation

This project helps you:

- Describe your Knowledge Graph (KG) using [our metadata schema] (docs/KG_Metadata_schema_V1.0.xlsx) 
- Validate your KG metadata using [our SHACL shapes] (schacl/full-hcls_shacl.ttl) 
- Publish your KG and make it discoverable by Google (instructions below)

## Example Usage 

The file "data/wikidata_hcls_metadata.ttl" in this repo is an example of specification conformance metadata generated for Wikidata KG. run the SHACL validation to check conformance of Wikidata metadata to proposed specification.

### setup the environment
prepare the local environment
        
        python -m venv .venv

activate the local environment
        
        source .venv/bin/activate

install the python packages

        python -m pip install -r requirements.txt

### run the test

        python validate.py -i data/wikidata_hcls_metadata.ttl -s shacl/full-hcls_shacl.ttl



## Publish KG Metadata 

Make your dataset discoverable via [Google Dataset Search](https://datasetsearch.research.google.com/) using the steps below.

---

###  1. Create Metadata

Use the provided JSON-LD context/KG specification to define your KG metadata. 


###  2. Generate `index.html`

Embed your metadata in JSON-LD format inside a `<script>` block, see example index.hml for food health claim kg here https://github.com/MaastrichtU-IDS/food-claims-kg/blob/gh-pages/index.html 


###  3. Deploy via GitHub Pages

1. Place `index.html` in your KG's GitHub repository.
2. Go to **Settings → Pages**.
3. Under **Source**, choose:
   - **Branch**: `gh-pages`

4. Visit your public page at:  
   `https://<username>.github.io/<repo-name>/`
Example:  
\url{https://maastrichtu-ids.github.io/food-claims-kg/}

###  4. Validate with Google Rich Results Test

Visit  [Google Rich Results Test](https://search.google.com/test/rich-results), enter the published URL, and verify structured data compatibility.


### 5. Verify Site Ownership (Google Search Console)

- Go to [https://search.google.com/search-console](https://search.google.com/search-console)
- Add the URL as a new property.
- Choose one of the following verification methods:
  - Add a meta tag to the `<head>` of the HTML file.
  - Upload a provided HTML verification file to the root directory.
- Complete the verification process.

### Step 7: Submit for Indexing

Use the URL Inspection Tool in Google Search Console to request indexing.  
Optionally, submit a `sitemap.xml` file to improve crawlability.





        
