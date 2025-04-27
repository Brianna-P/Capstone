import pandas as pd
import re
#SHOWS ALL QUERIES CONTAINING THE KEYWORDS
def filter_queries(filename):
    matches = []
    keywords = {"IN", "ANY", "NONE", ":NC", ":NA", ":ND", ":NI", ":NM"}

    df = pd.read_excel(filename, usecols=[0])

    for value in df.iloc[:, 0]:
        cell_str = str(value).strip().upper()
        if any(re.search(rf"\b{re.escape(keyword)}\b", cell_str) for keyword in keywords):
            matches.append(cell_str)

    return matches, len(matches)

def main():
    filename = "esgish.xlsx"
    output_file = "matches_output.txt"
    
    matches, count = filter_queries(filename)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"Number of matches: {count}\n\n")
        for match in matches:
            f.write(match + "\n")
    
    print(f"Results written to {output_file}")

if __name__ == "__main__":
    main()