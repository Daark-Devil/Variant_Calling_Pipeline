# Figures Directory Guide

The repository contains both publication figures and supporting visualizations.

```text
main_figures/
supporting_figures/
```

---

# main_figures/

Contains the primary figures required to understand the major findings of the somatic variant calling analysis.

These figures summarize the biological conclusions and should be viewed first.

---

## Figure 1 — Driver Mutation Summary

**File:** `11871_driver_mutations.png`

Displays the highest-priority candidate driver mutations identified in the tumor sample.

### Key Findings

Candidate driver genes include:

* PIK3CA
* CDH1
* ATM

### Biological Interpretation

These genes are well-established contributors to breast cancer development and progression.

---

## Figure 2 — Driver Candidate Table

**File:** `11871_driver_candidate_table.png`

Publication-style summary table of prioritized mutations.

### Displays

* Gene
* Mutation
* Functional effect
* Impact category
* TLOD score

### Key Conclusion

Provides a concise overview of the strongest mutation candidates identified by the pipeline.

---

## Figure 3 — Variant Consequence Distribution

**File:** `11871_top_variant_effects.png`

Displays the most common mutation consequences identified after annotation.

### Examples

* Missense variants
* Stop gained variants
* Synonymous variants
* Frameshift variants

### Key Conclusion

Characterizes the functional composition of the tumor mutation landscape.

---

## Figure 4 — SnpEff Impact Categories

**File:** `11871_snpeff_impact_counts.png`

Summarizes variants by predicted impact category.

### Categories

* HIGH
* MODERATE
* LOW
* MODIFIER

### Key Findings

* 313 HIGH impact variants
* 2468 MODERATE impact variants

### Biological Interpretation

A substantial fraction of mutations are predicted to alter protein structure or function.

---

## Figure 5 — Top Mutated Genes

**File:** `11871_top_mutated_genes.png`

Displays genes containing the highest number of detected mutations.

### Key Conclusion

Highlights recurrently altered genes that may contribute to tumor biology.

### Biological Relevance

Frequently mutated genes often indicate dysregulated signaling pathways and potential therapeutic targets.

---

# supporting_figures/

Contains supplementary analyses supporting the main findings.

These figures provide additional context and validation for the mutation prioritization workflow.

---

## Quality Control Figures

Generated from:

* FastQC
* MultiQC

Includes:

* Read quality distributions
* GC-content profiles
* Sequence duplication metrics
* Adapter contamination assessment

### Purpose

Demonstrates sequencing quality prior to downstream analysis.

---

## Alignment Metrics

Generated from:

* BWA-MEM
* Picard
* Samtools

Includes:

* Mapping statistics
* Duplicate rates
* Coverage summaries

### Purpose

Validates successful alignment of tumor and normal sequencing reads.

---

## Functional Annotation Results

Generated from:

* SnpEff

Includes:

* Variant classifications
* Gene annotations
* Protein consequences

### Purpose

Provides biological interpretation of detected mutations.

---

## Cancer Gene Prioritization

Includes:

* Cancer-gene mutation summaries
* Driver candidate rankings
* Mutation significance tables

### Purpose

Supports identification of clinically relevant genomic alterations.

---

## Summary

Together, the main and supporting figures provide a complete visual representation of:

* Somatic mutation discovery
* Functional variant annotation
* Mutation impact assessment
* Cancer-gene prioritization
* Driver mutation identification
* Biological interpretation of tumor-associated variants

The final prioritized mutation set highlights candidate genomic events potentially involved in breast cancer development and progression.
