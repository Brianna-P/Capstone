import pandas as pd
import re

def generate_metadata_report(filename):
    df = pd.read_excel(filename, usecols=[0]) 

    output_lines = []
    total_lengths = []
    
    for i, value in enumerate(df.iloc[:, 0], start=1):
        line = str(value).strip()
        codes = re.findall(r"\[(.*?)\]", line)

        if not codes:
            continue

        output_lines.append(f"Query {i}:")

        query_total = 0
        for code in codes:
            name = f"Name for {code}"
            description = f"Description for {code}"

            name_length = len(name)
            description_length = len(description)
            total = name_length + description_length
            query_total += total

            output_lines.append(f"[{code}] = name: {name_length}, description: {description_length}")

        output_lines.append(f"Total: {query_total}\n")
        total_lengths.append(query_total)

    avg_length = sum(total_lengths) / len(total_lengths) if total_lengths else 0
    output_lines.append(f"Average length of each row (names + descriptions): {avg_length:.2f}")

    with open("metadata_report.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(output_lines))

    print("Metadata report written to metadata_report.txt")
