[![Metadata Validation](https://github.com/marmhm/kg-metadata/actions/workflows/validate-metadata.yml/badge.svg)](https://github.com/marmhm/kg-metadata/actions/workflows/validate-metadata.yml)
[![SHACL Syntax Check](https://github.com/marmhm/kg-metadata/actions/workflows/shacl-syntax-check.yml/badge.svg)](https://github.com/marmhm/kg-metadata/actions/workflows/shacl-syntax-check.yml)
[![HTML+JSON-LD Validation](https://github.com/marmhm/kg-metadata/actions/workflows/validate-html.yml/badge.svg)](https://github.com/marmhm/kg-metadata/actions/workflows/validate-html.yml)


# Knowledge Graph Metadata Specification and Validation

This project proposes a specification for the description of Knowledge Graphs (KGs). The KG publisher can use the specification to generate metadata for the KG and then validate the generated metadta by shacl shapes we provide. The KG metadata specification [SHACL](shacl/full-hcls_shacl.ttl) was developed using [SHACL](https://www.w3.org/TR/shacl/) from a [community spreadsheet](https://docs.google.com/spreadsheets/d/1g6ypMzaRt6Z6rhNu4MMwgVdFJO0W47astvhXcxx66N4/edit?gid=1015207925#gid=1015207925)

# setup the environment
prepare the local environment
        
        python -m venv .venv

activate the local environment
        
        source .venv/bin/activate

install the python packages

        python -m pip install -r requirements.txt

# run the test
The file "wikidata_hcls_metadata.ttl" in this repo is an example of specification conformance metadata generated for Wikidata KG. run the shape validation with KG metadata and the KG shacl specification.

        python validate.py -i wikidata_hcls_metadata.ttl -s shacl/full-hcls_shacl.ttl


## ✅ Validate LOD Metadata

As a use case, we validate LOD metadata against SHACL-based metadata specifications. The 2025 LOD cloud contains 1,573 datasets and includes 17 metadata fields in its catalog. As described in the paper, we map elements of the LOD metadata schema to the vocabularies defined in our specification and generate a Turtle file compatible with the validation framework. To generate LOD metadata compatible to dpecification and validate it, you can run LOD/lod_ttl_gen.ipynb notebook. The output will be a report of violations.


## 🌐 Publish FAIR Metadata with JSON-LD on GitHub Pages

Easily make your dataset discoverable via [Google Dataset Search](https://datasetsearch.research.google.com/) using the steps below.

---

### 📝 1. Create Metadata

Use the provided JSON-LD context to define your KG metadata. This context includes terms such as name, description, keywords, license, creator, distribution, identifier, termCode, relatedLink, and inLanguage, which are defined as part of a curated subset of the schema.org vocabulary used in this specification.

📄 **Context URL**:  
`https://raw.githubusercontent.com/MaastrichtU-IDS/food-claims-kg/main/context/kg-schema.jsonld`


### 💾 2. Generate `index.html`

Embed your metadata in JSON-LD format inside a `<script>` block:

```html
<!DOCTYPE html>
<html>
<head>
  <script type="application/ld+json">
{
    "@context": "https://raw.githubusercontent.com/MaastrichtU-IDS/food-claims-kg/main/context/kg-schema.jsonld",
    "@type": "Dataset",
	"identifier": "Food Health Claims Knowledge Graph identifier",
    "name": "Food Health Claims Knowledge Graph",
    "alternateName": "Food Claims KG",
	"termCode": "Food Claims KG acronym",
    "description": "A FAIR RDF knowledge graph based on 260 EU-authorized health claims, structured across food, health effect, target group, and supporting scientific evidence.",
    "url": "https://maastrichtu-ids.github.io/food-claims-kg/",
	"relatedLink":"https://github.com/MaastrichtU-IDS/food-claims-kg",
    "creator": {
      "@type": "Organization",
      "name": "Maastricht University Institute of Data Science",
      "url": "https://www.maastrichtuniversity.nl/research/institute-data-science"
    },
	"publisher": {
      "@type": "Organization",
      "name": "Maastricht University"
    },
	"dateCreated": "2024-01-01",
	"datePublished": "2024-02-26",
    "dateModified": "2024-06-01",
	"subjectOf": "https://github.com/MaastrichtU-IDS/food-claims-kg",
	"image": "https://github.com/MaastrichtU-IDS/food-claims-kg/blob/master/food-claims-kg.jpg",
	"distribution": {
        "@type": "DataDownload",
        "encodingFormat": "text/turtle",
        "contentUrl": "https://raw.githubusercontent.com/MaastrichtU-IDS/food-claims-kg/main/data/food-claims.ttl"
      },
	"mainEntityOfPage": "http://grlc.io/api-git/MaastrichtU-IDS/food-claims-kg",
	"contentURL": "https://graphdb.dumontierlab.com/repositories/FoodHealthClaimsKG",
	"version": "1.0",
    "license": "https://opensource.org/licenses/MIT",
	"keywords": ["personalised nutrition", "food health claim", "knowledge graph", "FAIR data", "RDF", "EFSA"],
	"publication": "https://github.com/MaastrichtU-IDS/food-claims-kg",
	"language": "English"
  }
  </script>
</head>
<body></body>
</html>
```

---

### 🚀 3. Deploy via GitHub Pages

1. Place `index.html` in your GitHub repository.
2. Go to **Settings → Pages**.
3. Under **Source**, choose:
   - **Branch**: `main`

4. Visit your public page at:  
   `https://<username>.github.io/<repo-name>/`

---

### ✅ 4. Validate

Test your page using [Google Rich Results Test](https://search.google.com/test/rich-results) to ensure your metadata is correctly indexed.

---

Your dataset will now be Discoverable via Google Dataset Search.




        
