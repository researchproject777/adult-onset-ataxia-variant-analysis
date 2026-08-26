def classify_consequence_v4(row):
    name = str(row['Name']).lower()

    # Loss-of-function candidates:
    # frameshift, stop-gain, canonical splice-site
    if (
        'fs' in name
        or 'ter' in name
        or '*' in name
        or any(splice in name for splice in ['+1', '+2', '-1', '-2'])
    ):
        return 'Loss-of-Function (LoF)'

    # Missense:
    # protein change that is not synonymous
    elif 'p.' in name and '=' not in name:
        return 'Missense'

    else:
        return 'Other'
