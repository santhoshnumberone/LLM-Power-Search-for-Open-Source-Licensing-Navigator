### Step 1: Documents collection
##### Two documents are needed
1. `*.txt` -> Inside `full_text` directory 
2. `*.json` -> Inside `summaries` directory

```
docs/
├── licenses/
│   ├── full_text/         ← Plain `.txt` versions of full licenses
│   ├── summaries/         ← JSON summaries for each license
│   └── index.csv          ← Overview table linking it all
├── LICENSES_README.md     ← Explanation and attributions
└── license_schema.json    ← (Optional) Defines the JSON schema format
```

##### Here we focus on [OSI Approved Licenses](https://opensource.org/licenses)
You can selected which ever licenses
###### `full_text` contain `*.txt` files which contain
	- `# Source:url`
	- `<complete raw text from the link>`
###### `summaries` directory contain `*.json` which contain
```
- `license_name`
- `version` (if available)
- `approved_by` (OSI, EU, etc., or `null` if not found)
- `permissions` (array of allowed actions)
- `conditions` (array of requirements)
- `limitations` (array of legal limitations)
- `canonical_language` (e.g., "English", "German", etc.)
- `english_translation` (true/false)
- `url` (link to the license source)
```
Example 
`LICENSE_ADAPTIVE_PUBLIC-1.0.txt`
`LICENSE_ADAPTIVE_PUBLIC-1.0.json`

Here to generate `json` we have used `template prompt` structure using LLM
```
I will give you a license text block inside triple backticks.

Your task: 
- Extract a structured JSON summary from the license content. 
- Follow this schema exactly: 
- license_name - version (if available) 
- approved_by (e.g., "OSI", "EU", or null) 
- permissions (array of allowed actions) 
- conditions (array of usage requirements) 
- limitations (array of legal limitations) 
- canonical_language (e.g., "English", "German", etc.) 
- english_translation (true or false) 
- url (the source link I provide separately) 

Display only the JSON output inside a markdown code block. Don’t explain anything unless I ask. 

Input Format: 
INFO: ```<license full text here>``` 
LINK: ```<source URL>```
```

##### Note: ChatGPT ✅ **Max characters you can send in one message:**

**~25,000 characters** (including spaces and formatting)

- This equals around **4,000–4,500 words** of plain text.
- Markdown/code blocks and long URLs count toward this limit.
#####  🔁 If your license text is longer:

You can **split it into multiple parts** (e.g., `Part 1/3`, `Part 2/3`, `Part 3/3`) and clearly label them. I can then **reconstruct the full license** before extracting the summary.
Just send:
1. First part like:
    `INFO Part 1/3:`
2. Follow up with:
    `INFO Part 2/3:`
3. And so on, then finally provide:
    `LINK:`

### Step 2: Generate `Index.csv`

After collecting the licenses with its `*.txt` and `*.json` run `python step1_generate_index.py`  to generate`index.csv`

- **You already have a functioning `generate_index.py` script** that:
    - Scans the `summaries/` directory for JSON files.
    - Validates matching `.txt` file in `full_text/`.
    - Extracts metadata such as `license_name`, `SPDX_code`, `approved_by`, `category`.
    - Generates a clean and structured `index.csv`.
        
- **Output verified**: Your generated `index.csv` contains:
    - Correct column headers (`license_id`, `license_name`, etc.).
    - Clean file paths and tags for filtering (`Permissive`, `OSI`).
    - Summary and full text associations are validated during generation.
#### OUPUT:
```
docs_dir docs/licenses

Generated: docs/licenses/index.csv
```
