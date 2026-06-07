import pandas as pd

inp = "results/11871_somatic_PASS_snpeff_table.tsv"

df = pd.read_csv(inp, sep="\t")

cancer_genes = {
    "TP53","PIK3CA","GATA3","MAP3K1","CDH1","AKT1","PTEN","RB1",
    "BRCA1","BRCA2","ERBB2","ESR1","NF1","KMT2C","KMT2D","ARID1A",
    "MYC","CCND1","FGFR1","FGFR2","FGFR3","MDM2","CHEK2","ATM",
    "PALB2","BARD1","RAD51C","RAD51D","KRAS","NRAS","HRAS","BRAF"
}

high = df[df["impact"] == "HIGH"].copy()

moderate = df[df["impact"] == "MODERATE"].copy()

cancer = df[df["gene"].isin(cancer_genes)].copy()

high.to_csv("results/11871_HIGH_impact_variants.tsv", sep="\t", index=False)
moderate.to_csv("results/11871_MODERATE_variants.tsv", sep="\t", index=False)
cancer.to_csv("results/11871_cancer_gene_variants.tsv", sep="\t", index=False)

summary = pd.DataFrame({
    "category": ["HIGH", "MODERATE", "Cancer_gene"],
    "count": [len(high), len(moderate), len(cancer)]
})

summary.to_csv("results/11871_variant_priority_summary.tsv", sep="\t", index=False)

print(summary.to_string(index=False))

print("\nTop HIGH genes:")
print(high["gene"].value_counts().head(30).to_string())

print("\nCancer gene variants:")
if len(cancer) > 0:
    print(cancer[["chrom","pos","ref","alt","effect","impact","gene","hgvs_c","hgvs_p","tlod"]].to_string(index=False))
else:
    print("No known breast cancer genes found in this list.")
