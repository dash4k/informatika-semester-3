def parse_grammar(grammar_string):
    grammar_dict = {}
    for line in grammar_string.split('\n'):
        if not line.strip():
            continue
        head, productions = line.split(' -> ')
        productions = productions.split(' | ')
        grammar_dict[head.strip()] = [production.split() for production in productions]
    return grammar_dict

grammar = """
    K -> S P | X1 Pel | X1 Ket | X1 X2 | X3 X4
    X1 -> S P
    X2 -> Pel Ket
    X3 -> S P1
    X4 -> P2 Ket
    S -> NP Noun | NP Pronoun | NP Adj | NP Det | ipune | ia | tiange | titiang | tiang | ibu | guru | matematika | anake | luh | wewantenan | ketua | muda-mudi | desan | pianakne | pak | komputer | sekolah | basa | bali | bapakne | sari | memene | timpal-timpal | kulawargan | polisi | lalu-lintas | denpasar | jero | balian | basang | sepedane | wayan | darta | bapane | carik | pasar | tuni | semeng | lanang | koperasi | badung | mahasiswa | i | putu | gede | bapakne | olahraga | sepatu | adin | pasang | kota | surabaya | motorne | padi | tuning | semengan | ketut | bagus | yogyakarta | adine | perbekel | ibi | sanja | sepeda | bapan
    P -> Adj Adv | Adv Adj | galak | jegeg | dueg | bagus | seleg | males | gedeg | becik | luung | sakti | sakit | baru | wanen | baru
    P1 -> Adj Adv | Adv Adj | galak | jegeg | dueg | bagus | seleg | males | gedeg | becik | luung | sakti | sakit | baru | wanen | baru
    P2 -> VP Noun | VP Adj | VP Verb | ngajahin | mekarya | melajah | malajah | ngatur | ngubadin | mejejaitan | anggone | ngatehin | rauh | abane | nanem | ngalihin
    Pel -> VP Noun | VP Pronoun | VP Adj | VP Verb | ngajahin | mekarya | melajah | malajah | ngatur | ngubadin | mejejaitan | anggone | ngatehin | rauh | abane | nanem | ngalihin | PP Noun | PP Pronoun | PP Num | ring | di | ajak | ka | saking | uli | ke | NP Noun | NP Pronoun | NP Adj | NP Det | ipune | ia | tiange | titiang | tiang | ibu | guru | matematika | anake | luh | wewantenan | ketua | muda-mudi | desan | pianakne | pak | komputer | sekolah | basa | bali | bapakne | sari | memene | timpal-timpal | kulawargan | polisi | lalu-lintas | denpasar | jero | balian | basang | sepedane | wayan | darta | bapane | carik | pasar | tuni | semeng | lanang | koperasi | badung | mahasiswa | i | putu | gede | bapakne | olahraga | sepatu | adin | pasang | kota | surabaya | motorne | padi | tuning | semengan | ketut | bagus | yogyakarta | adine | perbekel | ibi | sanja | sepeda | bapan | AdjP Adv | AdjP Adj | galak | jegeg | dueg | bagus | seleg | males | gedeg | becik | luung | sakti | sakit | baru | wanen | baru | NumP Noun | NumP Num | sakancan | telung | dadue
    Ket -> PP Noun | PP Pronoun | PP Num | ring | di | ajak | ka | saking | uli | ke
    NP -> NP Noun | NP Pronoun | NP Adj | NP Det | ipune | ia | tiange | titiang | tiang | ibu | guru | matematika | anake | luh | wewantenan | ketua | muda-mudi | desan | pianakne | pak | komputer | sekolah | basa | bali | bapakne | sari | memene | timpal-timpal | kulawargan | polisi | lalu-lintas | denpasar | jero | balian | basang | sepedane | wayan | darta | bapane | carik | pasar | tuni | semeng | lanang | koperasi | badung | mahasiswa | i | putu | gede | bapakne | olahraga | sepatu | adin | pasang | kota | surabaya | motorne | padi | tuning | semengan | ketut | bagus | yogyakarta | adine | perbekel | ibi | sanja | sepeda | bapan
    AdjP -> Adj Adv | Adv Adj | galak | jegeg | dueg | bagus | seleg | males | gedeg | becik | luung | sakti | sakit | baru | wanen | baru
    VP -> VP Noun | VP Pronoun | VP Adj | VP Verb | ngajahin | mekarya | melajah | malajah | ngatur | ngubadin | mejejaitan | anggone | ngatehin | rauh | abane | nanem | ngalihin
    PP -> PP Noun | PP Pronoun | PP Num | ring | di | ajak | ka | saking | uli | ke
    NumP -> NumP Noun | NumP Num | sakancan | telung | dadue
    Noun -> ibu | guru | matematika | anake | luh | wewantenan | ketua | muda-mudi | desan | pianakne | pak | komputer | sekolah | basa | bali | bapakne | sari | memene | timpal-timpal | kulawargan | polisi | lalu-lintas | denpasar | jero | balian | basang | sepedane | wayan | darta | bapane | carik | pasar | tuni | semeng | lanang | koperasi | badung | mahasiswa | i | putu | gede | bapakne | olahraga | sepatu | adin | pasang | kota | surabaya | motorne | padi | tuning | semengan | ketut | bagus | yogyakarta | adine | perbekel | ibi | sanja | sepeda | bapan
    Pronoun -> ipune | ia | tiange | titiang | tiang
    Adj -> galak | jegeg | dueg | bagus | seleg | males | gedeg | becik | luung | sakti | sakit | baru | wanen | baru
    Adv -> pisan | paling | pesan | kapah | sesai | sampun | lakar | gati
    Verb -> ngajahin | mekarya | melajah | malajah | ngatur | ngubadin | mejejaitan | anggone | ngatehin | rauh | abane | nanem | ngalihin
    Prep -> ring | di | ajak | ka | saking | uli | ke
    Num -> sekancan | telung | dadue
    Det -> punika | ento | puniki
    """

R = parse_grammar(grammar)

# Function to perform the CYK Algorithm
def cykParse(w):
    n = len(w)
    # Initialize the table
    T = [[set([]) for j in range(n)] for i in range(n)]
    # Filling in the table
    for j in range(0, n):
        # Iterate over the rules
        for lhs, rule in R.items():
            for rhs in rule:
                # If a terminal is found
                if len(rhs) == 1 and rhs[0] == w[j]:
                    T[j][j].add(lhs)
        for i in range(j, -1, -1):
            # Iterate over the range i to j-1 (inclusive)
            for k in range(i, j):
                # Iterate over the rules
                for lhs, rule in R.items():
                    for rhs in rule:
                        if len(rhs) == 2 and rhs[0] in T[i][k] and rhs[1] in T[k+1][j]:
                            T[i][j].add(lhs)

    # If word can be formed by rules
    # of given grammar
    return ('K' in T[0][n-1]), T