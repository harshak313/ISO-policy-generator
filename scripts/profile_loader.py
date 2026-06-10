import json


def get_document_profile(document_id):

    with open(
        "../config/document_profiles.json",
        "r",
        encoding="utf-8"
    ) as f:

        profiles = json.load(f)

    return profiles.get(document_id)