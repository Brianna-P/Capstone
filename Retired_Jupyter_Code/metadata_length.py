import pandas as pd
import re
import json

#PRINTS ALL QUERIES' METADATA LENGTHS 
def load_metadata(json_file):
    metadata_lookup = {}
    with open(json_file, "r", encoding="utf-8") as f:
        raw_metadata = json.load(f)

    for entry in raw_metadata:
        code = entry["code"].strip()
        name = entry.get("name", "").strip()
        description = entry.get("description", "").strip()
        metadata_lookup[code.upper()] = {
            "name": name,
            "description": description
        }

    return metadata_lookup

def generate_metadata_report(excel_file, metadata_file, min_length=0, max_length=float('inf')):
    metadata_lookup = load_metadata(metadata_file)
    df = pd.read_excel(excel_file, usecols=[0]) 

    output_lines = []
    total_lengths = []
    total_num_queries = 0

    for i, value in enumerate(df.iloc[:, 0], start=1):
        line = str(value).strip()
        codes = re.findall(r"\[(.*?)\]", line)

        if not codes:
            continue

        query_output = [f"Query {i}:"]
        query_total = 0

        for code in codes:
            code_key = code.strip().upper()
            metadata = metadata_lookup.get(code_key)

            if metadata:
                name = metadata["name"]
                description = metadata["description"]
            else:
                name = f"Unknown name for {code}"
                description = "No description found."

            name_length = len(name)
            description_length = len(description)
            total = name_length + description_length
            query_total += total

            query_output.append(f"[{code}] = name: {name_length}, description: {description_length}")

        if min_length <= query_total <= max_length:
            query_output.append(f"Total: {query_total}\n")
            output_lines.extend(query_output)
            total_lengths.append(query_total)
            total_num_queries += 1

    avg_length = sum(total_lengths) / len(total_lengths) if total_lengths else 0
    output_lines.append(f"Average length of each row (names + descriptions): {avg_length:.2f}")
    output_lines.append(f"Total number of queries within length range: {total_num_queries}")

    with open("metadata_report.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(output_lines))

    print("Metadata report written to metadata_report.txt")

def main():
    excel_file = "esgish.xlsx"
    metadata_file = "metadata.json"
    
    min_length = 350
    max_length = 500

    generate_metadata_report(excel_file, metadata_file, min_length, max_length)

if __name__ == "__main__":
    main()
