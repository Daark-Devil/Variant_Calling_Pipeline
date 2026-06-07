import os
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("results/final_figures", exist_ok=True)

df = pd.read_csv("results/11871_somatic_PASS_snpeff_table.tsv", sep="\t")

# Impact counts
impact = df["impact"].fillna("UNKNOWN").value_counts()

plt.figure(figsize=(6,4))
plt.bar(impact.index, impact.values)
plt.ylabel("Variant count")
plt.title("SnpEff Impact Categories")
plt.tight_layout()
plt.savefig("results/final_figures/11871_snpeff_impact_counts.png", dpi=300)
plt.close()

# Top effects
effects = df["effect"].fillna("UNKNOWN").value_counts().head(15)

plt.figure(figsize=(10,5))
plt.bar(effects.index, effects.values)
plt.xticks(rotation=75, ha="right")
plt.ylabel("Variant count")
plt.title("Top Variant Consequences")
plt.tight_layout()
plt.savefig("results/final_figures/11871_top_variant_effects.png", dpi=300)
plt.close()

# Top genes
genes = df[df["gene"].notna() & (df["gene"] != "")]["gene"].value_counts().head(20)

plt.figure(figsize=(10,5))
plt.bar(genes.index, genes.values)
plt.xticks(rotation=75, ha="right")
plt.ylabel("Variant count")
plt.title("Top Mutated Genes")
plt.tight_layout()
plt.savefig("results/final_figures/11871_top_mutated_genes.png", dpi=300)
plt.close()

# Driver table figure
drivers = pd.read_csv("results/11871_driver_candidate_variants.tsv", sep="\t")
drivers[["gene","effect","impact","hgvs_c","hgvs_p","tlod"]].to_csv(
    "results/11871_driver_candidate_summary_table.tsv",
    sep="\t",
    index=False
)

print("Saved full variant visual summary.")
