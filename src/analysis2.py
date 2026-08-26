df_filtered['Refined_Consequence_v4'] = df_filtered.apply(
    classify_consequence_v4,
    axis=1
)
