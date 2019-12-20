from fuzzywuzzy import fuzz

# Roberto Farias Dias
# Roberto F. Dias

# Similaridade da string em ordem
fuzz.ratio('Apple Inc.', 'Apple')

# Similaridade da string parcial
fuzz.ratio('Apple Inc.', 'Apple')
fuzz.partial_ratio('Apple Inc.', 'Apple')

# Ignora a ordem das palavras
fuzz.ratio('Lakers x Chicago Bulls', 'Chigado Bulls x Lakers')
fuzz.partial_ratio('Lakers x Chicago Bulls', 'Chigado Bulls x Lakers')
fuzz.token_sort_ratio('Lakers x Chicago Bulls', 'Chigado Bulls x Lakers')

# Ignora palavras duplicadas
fuzz.ratio('Today we have a great game: Lakers x Chicago Bulls', 'Chigado Bulls x Lakers')
fuzz.partial_ratio('Today we have a great game: Lakers x Chicago Bulls', 'Chigado Bulls x Lakers')
fuzz.token_sort_ratio('Today we have a great game: Lakers x Chicago Bulls', 'Chigado Bulls x Lakers')
fuzz.token_set_ratio('Today we have a great game: Lakers x Chicago Bulls', 'Chigado Bulls x Lakers')
