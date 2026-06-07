import os
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("results/final_figures", exist_ok=True)

df = pd.read_csv("results/11871_driver_candidate_variants.tsv", sep="\t")

table = df[["gene","effect","impact","hgvs_p","tlod"]].copy()
table["tlod"] = table["tlod"].round(2)

fig, ax = plt.subplots(figsize=(12, 3.5))
ax.axis("off")

tbl = ax.table(
    cellText=table.values,
    colLabels=table.columns,
    loc="center",
    cellLoc="center"
)

tbl.auto_set_font_size(False)
tbl.set_fontsize(9)
tbl.scale(1, 1.6)

plt.title("Prioritized Somatic Driver Candidates", pad=20)
plt.tight_layout()
plt.savefig("results/final_figures/11871_driver_candidate_table.png", dpi=300)
plt.close()

print("Saved driver candidate table figure")
