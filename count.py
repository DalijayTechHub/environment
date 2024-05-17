

with open('preproinsulin-seq-clean.txt', 'r') as f:
    text = f.read().replace(" ", "").replace("\n", "")

ainsulin_seq_clean = text[89:110]

with open('ainsulin_seq_clean', 'w') as f:
    f.write(ainsulin_seq_clean)
