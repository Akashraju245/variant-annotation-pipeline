import pandas as pd
import os

vcf_file = "sample.vcf"
output_file = "annotated_output.csv"

# Read VCF
try:
    data = pd.read_csv(
        vcf_file,
        comment="#",
        sep="\t",
        header=None,
        names=["CHROM", "POS", "ID", "REF", "ALT", "QUAL", "FILTER", "INFO"]
    )
except FileNotFoundError:
    print(f"Error: File not found: {vcf_file}")
    exit()

# Add simple annotation
def variant_type(row):
    if len(str(row['REF'])) == 1 and len(str(row['ALT'])) == 1:
        return "SNP"
    else:
        return "INDEL"

data["Variant_Type"] = data.apply(variant_type, axis=1)
data["Gene"] = ["GENE1", "GENE2", "GENE3"][:len(data)]

# Save output
data.to_csv(output_file, index=False)

print("VCF loaded successfully!")
print(data)
print(f"Annotated CSV saved to: {output_file}")
