# Adult-Onset Hereditary Ataxia Variant Analysis

This repository contains the Python code used for a computational study examining the association between predicted molecular variant consequence and clinical pathogenicity classification in genes associated with adult-onset hereditary ataxia.

## Data Sources

Gene-disease associations were obtained from the Genomics England PanelApp Adult-Onset Hereditary Ataxia panel (Panel 466). Only Green-rated genes were included.

Clinical variant data were obtained from the NCBI ClinVar Variant Summary dataset. The analysis used a fixed ClinVar data snapshot obtained in July 2026 and restricted variants to the GRCh38 human genome assembly.

## Analysis

The notebook performs the following steps:

1. Loads the selected PanelApp genes.
2. Loads the ClinVar Variant Summary dataset.
3. Filters variants to the selected genes and GRCh38.
4. Deduplicates variants using ClinVar VariationID.
5. Classifies variants as predicted loss-of-function (LoF), missense, or Other using an HGVS-based classification rule.
6. Compares predicted LoF and missense variants according to ClinVar pathogenic/likely pathogenic classification.
7. Performs a chi-square test of independence.
8. Calculates the odds ratio and 95% confidence interval.
9. Performs a secondary analysis of broader ClinVar clinical significance categories.

## Reproducibility

The code is provided to document the data-processing and statistical procedures used in the associated manuscript.

Because ClinVar is updated over time, the analysis was based on a fixed July 2026 data snapshot rather than the current ClinVar release.

## Software

The analysis was performed in Python 3 using:

- pandas
- SciPy
