import os
import pandas as pd
import requests

from template_reader import read_docx
from profile_loader import get_document_profile


# ====================================
# CONFIG
# ====================================

DOCUMENT_ID = input(
    "Enter Document ID: "
).strip()

MODEL_NAME = "gemma4:31b-cloud"

MATRIX_FILE = "../documents/matrix/ISO 27001_Document_Coverage_Matrix.xlsx"

ISO_FILE = "../documents/standards/ISO_27001_2022.xlsx"

TEMPLATE_FOLDER = "../documents/templates"

OUTPUT_FOLDER = "../documents/generated_policies"

# ====================================
# READ MATRIX
# ====================================

annex_df = pd.read_excel(
    MATRIX_FILE,
    sheet_name="Annex A Coverage",
    header=2
)

control_rows = annex_df[
    annex_df["Covered By (Doc ID)"]
    == DOCUMENT_ID
]

if control_rows.empty:

    raise Exception(
        f"No controls found for {DOCUMENT_ID}"
    )

document_title = control_rows.iloc[0][
    "Document Title"
]

control_ids = (
    control_rows["Control"]
    .tolist()
)

# ====================================
# READ CLAUSE COVERAGE
# ====================================

clause_df = pd.read_excel(
    MATRIX_FILE,
    sheet_name="Clause Coverage",
    header=2
)

clause_rows = clause_df[
    clause_df[
        "Covered By (Doc ID)"
    ]
    .astype(str)
    .str.contains(
        DOCUMENT_ID,
        na=False
    )
]

clause_ids = []

for _, row in clause_rows.iterrows():

    clause = (
        str(row["Clause"])
        .replace("Cl.", "")
        .strip()
    )

    clause_ids.append(clause)

# ====================================
# READ ISO STANDARD
# ====================================

iso_clause_df = pd.read_excel(
    ISO_FILE,
    sheet_name="Clauses"
)

iso_control_df = pd.read_excel(
    ISO_FILE,
    sheet_name="Annex A Controls"
)

# ====================================
# BUILD CLAUSE TEXT
# ====================================

clause_text = ""

for clause in clause_ids:

    result = iso_clause_df[
        iso_clause_df[
            "Clause"
        ].astype(str)
        == clause
    ]

    if not result.empty:

        clause_text += f"""

Clause: {clause}

Title:
{result.iloc[0]['Clause Name']}

Description:
{result.iloc[0]['Description']}

"""

# ====================================
# BUILD CONTROL TEXT
# ====================================

control_text = ""

for control in control_ids:

    result = iso_control_df[
        iso_control_df["Control"]
        == control
    ]

    if not result.empty:

        control_text += f"""

Control: {control}

Title:
{result.iloc[0]['Control Name']}

Description:
{result.iloc[0]['Description']}

"""

# ====================================
# LOAD TARGET TEMPLATE
# ====================================

template_text = ""

for file in os.listdir(
    TEMPLATE_FOLDER
):

    if (
        DOCUMENT_ID in file
        and file.endswith(".docx")
    ):

        template_text = read_docx(
            os.path.join(
                TEMPLATE_FOLDER,
                file
            )
        )

        print(
            f"\nTemplate Found: {file}"
        )

        break

# ====================================
# LOAD DOCUMENT PROFILE
# ====================================

profile = get_document_profile(
    DOCUMENT_ID
)

section_text = ""

if profile:

    for index, section in enumerate(
        profile["sections"],
        start=1
    ):

        section_text += (
            f"{index}. {section}\n"
        )

# ====================================
# LOAD ALL REFERENCE TEMPLATES
# ====================================

reference_templates = ""

for file in os.listdir(
    TEMPLATE_FOLDER
):

    if file.endswith(".docx"):

        try:

            template_content = read_docx(
                os.path.join(
                    TEMPLATE_FOLDER,
                    file
                )
            )

            reference_templates += f"""

=========================================
TEMPLATE: {file}
=========================================

{template_content}

"""

        except:

            pass

# ====================================
# PROMPT
# ====================================

prompt = f"""
You are a Senior ISO 27001 Consultant,
Lead Auditor,
and ISMS Documentation Specialist.

Generate a professional ISO 27001 policy
or procedure document.

================================================
DOCUMENT INFORMATION
================================================

Document ID:
{DOCUMENT_ID}

Document Name:
{document_title}

================================================
MANDATORY DOCUMENT SECTIONS
================================================

{section_text}

================================================
ISO CLAUSES
================================================

{clause_text}

================================================
ISO CONTROLS
================================================

{control_text}

================================================
PRIMARY TEMPLATE
================================================

{template_text}

================================================
REFERENCE TEMPLATES
================================================

{reference_templates}

================================================
INSTRUCTIONS
================================================

1. Use EXACTLY the sections listed.

2. Do not add sections.

3. Do not remove sections.

4. Do not rename sections.

5. Do not reorder sections.

6. Follow ISO/IEC 27001:2022 requirements.

7. Follow the style,
tone,
and structure of the templates.

8. Create detailed,
professional,
audit-ready content.

9. Every supplied clause
and control must be addressed.

10. Use placeholders:

[Organization Name]

[Owner]

[Approver]

[Date]

11. Add a final section:

Appendix A - ISO 27001 Control Mapping

Map each control
to the section(s)
that implement it.

12. Return ONLY markdown content.

13. Do not use code blocks.

"""

# ====================================
# GENERATE
# ====================================

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.2,
            "num_ctx": 16384
        }
    }
)

response.raise_for_status()

policy_text = response.json()[
    "response"
]

# ====================================
# SAVE MARKDOWN
# ====================================

os.makedirs(
    OUTPUT_FOLDER,
    exist_ok=True
)

output_file = (
    f"{OUTPUT_FOLDER}/"
    f"{DOCUMENT_ID}.md"
)

with open(
    output_file,
    "w",
    encoding="utf-8"
) as f:

    f.write(policy_text)

print("\nCompleted")

print(
    f"\nMarkdown File: {output_file}"
)