"""Request Body Schemas for API Tools

DO NOT EDIT THIS MODULE DIRECTLY.

THIS MODULE WAS AUTO-GENERATED AND CONTAINS OpenAPI REQUEST BODY SCHEMAS
FOR TOOLS WITH COMPLEX REQUEST BODIES. ANY CHANGES TO THIS MODULE WILL
BE OVERWRITTEN BY THE TRANSPILER.
"""

from typing import Any

REQUEST_BODY_SCHEMAS: dict[str, Any] = {
    "SEARCHDRUGADVERSEEVENTS": '{"oneOf": [{"type": "object", "description": "Query parameters for searching drug adverse event reports. Use Elasticsearch query syntax to construct the search field.", "x-searchable-fields": {"$ref": "#/components/schemas/DrugAdverseEventFields"}, "properties": {"search": {"type": "string", "description": "Elasticsearch query string to filter adverse event records. Use the format \'field:term\' for exact matches, \'field:term+AND+field:term\' for AND logic, or \'field:term+field:term\' for OR logic. Use brackets [a TO b] for ranges. Wrap phrases in quotes and replace spaces with + signs.\n\nExamples:\n- Search for headache reactions: patient.reaction.reactionmeddrapt:"headache"\n- Date range: receivedate:[20040101 TO 20081231]\n- Pharmacologic class: patient.drug.openfda.pharm_class_epc:"nonsteroidal+anti-inflammatory+drug"\n- Multiple conditions: patient.reaction.reactionmeddrapt:"fatigue"+AND+occurcountry:"CA"\n- Serious events only: serious:1\n- Deaths: seriousnessdeath:1\n\nRefer to the x-searchable-fields schema for all available fields, their types, and descriptions."}, "sort": {"type": "string", "description": "Sort results by field. Format: \'field:asc\' or \'field:desc\'. Example: \'receivedate:desc\' to get newest reports first."}, "count": {"type": "string", "description": "Count unique values in a field across matching records. Returns the 1000 most frequent values. Use \'.exact\' suffix for exact phrase counting (e.g., \'patient.reaction.reactionmeddrapt.exact\'). Cannot be used with \'limit\' or \'skip\'. Examples: \'patient.reaction.reactionmeddrapt.exact\', \'patient.drug.openfda.pharm_class_epc.exact\', \'occurcountry\'."}, "limit": {"type": "integer", "minimum": 1, "maximum": 1000, "default": 1, "description": "Maximum number of records to return (1-1000). Default is 1 if not specified. Cannot be used with \'count\'."}, "skip": {"type": "integer", "minimum": 0, "maximum": 25000, "default": 0, "description": "Number of records to skip for pagination (0-25000). Use with \'limit\' for pagination. Cannot be used with \'count\'. Note: For datasets exceeding 25,000 records, use the search_after parameter with Link headers instead."}}}], "description": "Query parameters for searching adverse events. Use schema mode: first call get_request_schema to retrieve searchable fields and query syntax, then construct your query based on the user\'s requirements."}',  # noqa: E501
}
