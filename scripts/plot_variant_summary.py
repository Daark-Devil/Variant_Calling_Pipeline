import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("results/final_figures", exist_ok=True)

summary = pd.read_csv(
    "results/11871_variant_priority_summary.tsv",
    sep="\t"
)

plt.figure(figsize=(6,4))
plt.bar(summary["category"], summary["count"])
plt.ylabel("Variant count")
plt.title("11871 Somatic Variant Summary")
plt.tight_layout()
plt.savefig("results/final_figures/11871_variant_summary.png", dpi=300)
plt.close()

drivers = pd.read_csv(
    "results/11871_driver_candidate_variants.tsv",
    sep="\t"
)

drivers["label"] = drivers["gene"] + "\n" + drivers["hgvs_p"].fillna("")

plt.figure(figsize=(9,4))
plt.bar(drivers["label"], drivers["tlod"])
plt.xticks(rotation=45, ha="right")
plt.ylabel("TLOD")
plt.title("11871 Candidate Driver Mutations")
plt.tight_layout()
plt.savefig("results/final_figures/11871_driver_mutations.png", dpi=300)
plt.close()

print("Saved:")
print("results/final_figures/11871_variant_summary.png")
print("results/final_figures/11871_driver_mutations.png")
