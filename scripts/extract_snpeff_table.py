import gzip
import pandas as pd

vcf = "results/11871_somatic_PASS_snpeff.vcf"
out = "results/11871_somatic_PASS_snpeff_table.tsv"

rows = []

with open(vcf) as f:
    for line in f:
        if line.startswith("#"):
            continue

        parts = line.rstrip("\n").split("\t")
        chrom, pos, vid, ref, alt, qual, filt, info = parts[:8]

        info_dict = {}
        for item in info.split(";"):
            if "=" in item:
                k, v = item.split("=", 1)
                info_dict[k] = v

        ann = info_dict.get("ANN", "")
        if ann == "":
            continue

        first = ann.split(",")[0].split("|")

        rows.append({
            "chrom": chrom,
            "pos": pos,
            "ref": ref,
            "alt": alt,
            "filter": filt,
            "tlod": info_dict.get("TLOD", ""),
            "effect": first[1] if len(first) > 1 else "",
            "impact": first[2] if len(first) > 2 else "",
            "gene": first[3] if len(first) > 3 else "",
            "gene_id": first[4] if len(first) > 4 else "",
            "feature_type": first[5] if len(first) > 5 else "",
            "transcript": first[6] if len(first) > 6 else "",
            "biotype": first[7] if len(first) > 7 else "",
            "hgvs_c": first[9] if len(first) > 9 else "",
            "hgvs_p": first[10] if len(first) > 10 else ""
        })

df = pd.DataFrame(rows)
df.to_csv(out, sep="\t", index=False)

print("Saved:", out)
print("Variants:", len(df))
print("\nImpact counts:")
print(df["impact"].value_counts())
print("\nTop effects:")
print(df["effect"].value_counts().head(20))
print("\nTop genes:")
print(df["gene"].value_counts().head(20))
