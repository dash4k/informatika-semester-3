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
    K -> S P | X1 Ket | X1 Pel | X1 X2
    X1 -> S P
    X2 -> Pel Ket
    S -> NP Det | NP Pronoun | NP Adj | Num NP | NP Prep | Adj NP | NumP NP | buku | meja | tresna | umah | banjar | pura | gajah | bale | batu | wulan | gunung | yeh | jalan | kambing | kayu | langit | segara | karang | pasar | bunga | tukad | manuk | cicing | meong | ayam | bikul | kakul | gong | bali | kurenan | meme | bapa | anak | desa | agung | telaga | biuh | jagung | nyuh | lawang | pintu | peken | bale | pedati | sepeda | mobil | motor | lontar | pena | kertas | kopi | teh | yeh | uyah | lada | mangga | apel | surya | jaran | kerbau | bebek | kakul | lilin | bantal | selimut | udeng | sapatu | baju | celana | saput | obat | sakit | balian | guru | murid | sekolah | kelas | roti | nasi | jukut | buah | telo | be | be segara | padi | alas | daun | akar | panan | jepun | kupukupu | semut | ular | singa | jembatan | gedong | alas | pantai | pasir | surya | lukisan | patung | joged | tiang | ragane | dane | ia | ipun | ida | i | cai | ia | nika | tiang | kula | raga | nika | punika | sira | kita | side | nyane | dewek | pekak | meme | bapa | ipun | sira | nyen | anake | tusing | suba | ento | madan | ipun | ida | titiang | sameton | timpal | luh | gede | adi | ratu | ratu bagus | sampun | ngih | mbok | tusing | nenten | kantos | nyane | kadi | inggih | karang | maleh | punduk | ritat | sane | maut | bani | ditu | aeng | pisaga | dewekne | ipun | manira | ida sang | ngiring | kawis | kanti | punyan | malih | serahang | mujur | sapunapi | suang-suang | saling | keneh | sepisan | cang | panake | kantos | sidan | nyantos | tekan | sesampun | timpal | pasikian | antuk | krama | patuh | bakti | timpi | gegeden | luh | madan | pidik | ragae | inggih | ngantos | mangda
    P -> AdjP Adv | AdjP Prep | AdjP Noun | gede | ageng | jegeg | barak | bagus | alit | gedé | tiyis | panas | wates | majeng | polos | wenten | madan | bagia | rahayu | ganteng | ayu | seru | demen | meduwe | galang | lembut | keras | galak | satya | tulus | luh | meketeg | kucit | kaseng | jernih | peteng | terang | basah | kering | jangkep | katoh | jelas | suci | enu | busuk | manis | pait | masem | asin | murah | mahal | abang | barak | bungkah | lemah | kuat | lemah | tua | muda | lembrana | jebos | cingcang | dues | ertami | cantik | ngeleng | werdah | aman | setata | genjah | lambat | pegat | sambung | adi | apik | durhaka | cedas | tolo | entok | nguda | gemuk | beber | tebas | bude | lenteng | ijem | kuluk | biasa | gumi | luas | seket | kedap | enteng | cingsal | mabris | peteng | blonjo | lius | aruh | dewasa | kejem | lempeng | seling | sarwa
    Y1 -> Prep Det
    Y2 -> Prep Adj
    Y3 -> Prep Num
    Ket ->  Prep Noun | Prep Pronoun | Prep NP | Prep PP | Y1 Noun | Y2 Noun | Y3 Noun
    Y4 -> NumP Det
    Y5 -> NumP Adj
    Y6 -> Verb Prep
    Pel -> NP Det | NP Pronoun | NP Adj | Num NP | NP Prep | Adj NP | Nu~mP NP | buku | meja | tresna | umah | banjar | pura | gajah | bale | batu | wulan | gunung | yeh | jalan | kambing | kayu | langit | segara | karang | pasar | bunga | tukad | manuk | cicing | meong | ayam | bikul | kakul | gong | bali | kurenan | meme | bapa | anak | desa | agung | telaga | biuh | jagung | nyuh | lawang | pintu | peken | bale | pedati | sepeda | mobil | motor | lontar | pena | kertas | kopi | teh | yeh | uyah | lada | mangga | apel | surya | jaran | kerbau | bebek | kakul | lilin | bantal | selimut | udeng | sapatu | baju | celana | saput | obat | sakit | balian | guru | murid | sekolah | kelas | roti | nasi | jukut | buah | telo | be | be segara | padi | alas | daun | akar | panan | jepun | kupukupu | semut | ular | singa | jembatan | gedong | alas | pantai | pasir | surya | lukisan | patung | joged | tiang | ragane | dane | ia | ipun | ida | i | cai | ia | nika | tiang | kula | raga | nika | punika | sira | kita | side | nyane | dewek | pekak | meme | bapa | ipun | sira | nyen | anake | tusing | suba | ento | madan | ipun | ida | titiang | sameton | timpal | luh | gede | adi | ratu | ratu bagus | sampun | ngih | mbok | tusing | nenten | kantos | nyane | kadi | inggih | karang | maleh | punduk | ritat | sane | maut | bani | ditu | aeng | pisaga | dewekne | ipun | manira | ida sang | ngiring | kawis | kanti | punyan | malih | serahang | mujur | sapunapi | suang-suang | saling | keneh | sepisan | cang | panake | kantos | sidan | nyantos | tekan | sesampun | timpal | pasikian | antuk | krama | patuh | bakti | timpi | gegeden | luh | madan | pidik | ragae | inggih | ngantos | mangda | Prep Noun | Prep Pronoun | Prep NP | Prep PP | Y1 Noun | Y2 Noun | Y3 Noun | AdjP Adv | AdjP Prep | AdjP Noun | pisan | sesai | kapah | kaja | kelod | maut | manis | taluh | langsung | pelan | cepat | ajeg | sekali | tusing | ento | ritat | punduk | jani | kadi | ento | ider | suba | titiang | becik | sane | utama | temenan | juari | malih | puput | sadurung | madan | kapungkur | ring | jeg | lan | titi | anake | kawit | patuh | pidik | gedang | munggah | turun | pemit | maleh | malah | temenan | ngih | mbok | sing | dini | lajeng | kadi | karyane | yening | nenten | bani | pinaka | kanti | sampun | nenten | sane | wantah | gati | buka | ditu | madan | riang | kebus | karang | ngidang | sinam | kasih | kenkene | bebeletan | salawas | sadurung | suba | makejang | mandas | pesu | malih | perak | idep | cepat | lambar | alon | becik | ngawit | temen | bukak | bebas | nganti | muah | serahin | juari | adan | langsung| NumP PP | NumP Pronoun | NumP Noun | NumP Noun | Y4 Noun | Y5 Noun | dua | telu | katiga | siki | duet | tiga | empat | lima | enem | pitu | wolu | sanga | dasan | sebelas | duabelas | tigabelas | empatbelas | limabelas | enambelas | pitulas | woluolas | sangalas | dasalima | telulas | pitulas | dua | tigang | empat | lima | enem | pitu | wolu | sanga | ratus | dasa | satus | selikur | lingtang | tapel | siki dos | tiga dos | malih | sekawan | lulung | lulung iraga | gagel | kakandel | kantos | malih sadurung | tunggal | antuk | duang | wenten | titiang | sakedik | kombinasi | gede | kalih | langkung | ringkang | palu | kombongan | buka | sinyuk | gebel | angga | jujur | mandala | kayang | balang | satya | pekerja | mandiri | pantes | makaya | sawa | pakir | majeng | bentang | sankang | madu | Verb Adv | Verb O | Y6 O | Verb NP | Verb AdjP | Verb PP | manten | ngidang | mados | ngantos | nyidang | ngantosang | ngidangang | nentenang | matu | nganggo | ngemargiang | makta | jaga | laksanayang | ngemargiang | ngajeng | saring | ngidangang | krama | talang | madu | lempas | jaga | lampah | tangi | ngatur | nyakra | medalang | ngidang | bebeng | segara | nganteg | mangda | laksanayang | taler | sia | nyaman | nuntun | lungsur | akeh | ngetang | malih | laksanayang | sambung | nandur | pidang | ngidangang | serahang | ngidang | medal | pidang | saksi | jaladin | lampah | sura | kadep | carang | kembangi | nyekel | pidang | titiang | wasa | gendang | buka | hatur | seleh | panggung | njaga | sirah | mandalika | manten | mentas | adang | kenget | ture | lecengan | repat | kakandeng | aja | laksanayang | wentenang | ngumbah | ngawit | peken | gantos | patur | antosang | matur | malih | jajal | linggah | talu | kepak | manut | pramadi | maté | pindah | tamba | temba | ngetan | nyantosang | kebeng | patu | manca | wastu | sedetik | mangda | maos | tirta | polih | bangun | nawa | taman | nyen
    O -> NP Det | NP Pronoun | NP Adj | Num NP | NP Prep | Adj NP | NumP NP | buku | meja | tresna | umah | banjar | pura | gajah | bale | batu | wulan | gunung | yeh | jalan | kambing | kayu | langit | segara | karang | pasar | bunga | tukad | manuk | cicing | meong | ayam | bikul | kakul | gong | bali | kurenan | meme | bapa | anak | desa | agung | telaga | biuh | jagung | nyuh | lawang | pintu | peken | bale | pedati | sepeda | mobil | motor | lontar | pena | kertas | kopi | teh | yeh | uyah | lada | mangga | apel | surya | jaran | kerbau | bebek | kakul | lilin | bantal | selimut | udeng | sapatu | baju | celana | saput | obat | sakit | balian | guru | murid | sekolah | kelas | roti | nasi | jukut | buah | telo | be | be segara | padi | alas | daun | akar | panan | jepun | kupukupu | semut | ular | singa | jembatan | gedong | alas | pantai | pasir | surya | lukisan | patung | joged | tiang | ragane | dane | ia | ipun | ida | i | cai | ia | nika | tiang | kula | raga | nika | punika | sira | kita | side | nyane | dewek | pekak | meme | bapa | ipun | sira | nyen | anake | tusing | suba | ento | madan | ipun | ida | titiang | sameton | timpal | luh | gede | adi | ratu | ratu bagus | sampun | ngih | mbok | tusing | nenten | kantos | nyane | kadi | inggih | karang | maleh | punduk | ritat | sane | maut | bani | ditu | aeng | pisaga | dewekne | ipun | manira | ida sang | ngiring | kawis | kanti | punyan | malih | serahang | mujur | sapunapi | suang-suang | saling | keneh | sepisan | cang | panake | kantos | sidan | nyantos | tekan | sesampun | timpal | pasikian | antuk | krama | patuh | bakti | timpi | gegeden | luh | madan | pidik | ragae | inggih | ngantos | mangda
    NP -> NP Det | NP Pronoun | NP Adj | Num NP | NP Prep | Adj NP | NumP NP | buku | meja | tresna | umah | banjar | pura | gajah | bale | batu | wulan | gunung | yeh | jalan | kambing | kayu | langit | segara | karang | pasar | bunga | tukad | manuk | cicing | meong | ayam | bikul | kakul | gong | bali | kurenan | meme | bapa | anak | desa | agung | telaga | biuh | jagung | nyuh | lawang | pintu | peken | bale | pedati | sepeda | mobil | motor | lontar | pena | kertas | kopi | teh | yeh | uyah | lada | mangga | apel | surya | jaran | kerbau | bebek | kakul | lilin | bantal | selimut | udeng | sapatu | baju | celana | saput | obat | sakit | balian | guru | murid | sekolah | kelas | roti | nasi | jukut | buah | telo | be | be segara | padi | alas | daun | akar | panan | jepun | kupukupu | semut | ular | singa | jembatan | gedong | alas | pantai | pasir | surya | lukisan | patung | joged | tiang | ragane | dane | ia | ipun | ida | i | cai | ia | nika | tiang | kula | raga | nika | punika | sira | kita | side | nyane | dewek | pekak | meme | bapa | ipun | sira | nyen | anake | tusing | suba | ento | madan | ipun | ida | titiang | sameton | timpal | luh | gede | adi | ratu | ratu bagus | sampun | ngih | mbok | tusing | nenten | kantos | nyane | kadi | inggih | karang | maleh | punduk | ritat | sane | maut | bani | ditu | aeng | pisaga | dewekne | ipun | manira | ida sang | ngiring | kawis | kanti | punyan | malih | serahang | mujur | sapunapi | suang-suang | saling | keneh | sepisan | cang | panake | kantos | sidan | nyantos | tekan | sesampun | timpal | pasikian | antuk | krama | patuh | bakti | timpi | gegeden | luh | madan | pidik | ragae | inggih | ngantos | mangda
    AdjP -> AdjP Adv | AdjP Prep | AdjP Noun | gede | ageng | jegeg | barak | bagus | alit | gedé | tiyis | panas | wates | majeng | polos | wenten | madan | bagia | rahayu | ganteng | ayu | seru | demen | meduwe | galang | lembut | keras | galak | satya | tulus | luh | meketeg | kucit | kaseng | jernih | peteng | terang | basah | kering | jangkep | katoh | jelas | suci | enu | busuk | manis | pait | masem | asin | murah | mahal | abang | barak | bungkah | lemah | kuat | lemah | tua | muda | lembrana | jebos | cingcang | dues | ertami | cantik | ngeleng | werdah | aman | setata | genjah | lambat | pegat | sambung | adi | apik | durhaka | cedas | tolo | entok | nguda | gemuk | beber | tebas | bude | lenteng | ijem | kuluk | biasa | gumi | luas | seket | kedap | enteng | cingsal | mabris | peteng | blonjo | lius | aruh | dewasa | kejem | lempeng | seling | sarwa
    PP -> Prep Noun | Prep Pronoun | Y1 Noun | Y2 Noun | Y3 Noun | Prep NP | Prep PP
    NumP -> NumP Noun | Y4 Noun | Y5 Noun | NumP PP | NumP Pronoun | dua | telu | katiga | siki | duet | tiga | empat | lima | enem | pitu | wolu | sanga | dasan | sebelas | duabelas | tigabelas | empatbelas | limabelas | enambelas | pitulas | woluolas | sangalas | dasalima | telulas | pitulas | dua | tigang | empat | lima | enem | pitu | wolu | sanga | ratus | dasa | satus | selikur | lingtang | tapel | siki dos | tiga dos | malih | sekawan | lulung | lulung iraga | gagel | kakandel | kantos | malih sadurung | tunggal | antuk | duang | wenten | titiang | sakedik | kombinasi | gede | kalih | langkung | ringkang | palu | kombongan | buka | sinyuk | gebel | angga | jujur | mandala | kayang | balang | satya | pekerja | mandiri | pantes | makaya | sawa | pakir | majeng | bentang | sankang | madu
    Noun -> buku | meja | tresna | umah | banjar | pura | gajah | bale | batu | wulan | gunung | yeh | jalan | kambing | kayu | langit | segara | karang | pasar | bunga | tukad | manuk | cicing | meong | ayam | bikul | kakul | gong | bali | kurenan | meme | bapa | anak | desa | agung | telaga | biuh | jagung | nyuh | lawang | pintu | peken | bale | pedati | sepeda | mobil | motor | lontar | pena | kertas | kopi | teh | yeh | uyah | lada | mangga | apel | surya | jaran | kerbau | bebek | kakul | lilin | bantal | selimut | udeng | sapatu | baju | celana | saput | obat | sakit | balian | guru | murid | sekolah | kelas | roti | nasi | jukut | buah | telo | be | be segara | padi | alas | daun | akar | panan | jepun | kupukupu | semut | ular | singa | jembatan | gedong | alas | pantai | pasir | surya | lukisan | patung | joged
    Adj -> gede | ageng | jegeg | barak | bagus | alit | gedé | tiyis | panas | wates | majeng | polos | wenten | madan | bagia | rahayu | ganteng | ayu | seru | demen | meduwe | galang | lembut | keras | galak | satya | tulus | luh | meketeg | kucit | kaseng | jernih | peteng | terang | basah | kering | jangkep | katoh | jelas | suci | enu | busuk | manis | pait | masem | asin | murah | mahal | abang | barak | bungkah | lemah | kuat | lemah | tua | muda | lembrana | jebos | cingcang | dues | ertami | cantik | ngeleng | werdah | aman | setata | genjah | lambat | pegat | sambung | adi | apik | durhaka | cedas | tolo | entok | nguda | gemuk | beber | tebas | bude | lenteng | ijem | kuluk | biasa | gumi | luas | seket | kedap | enteng | cingsal | mabris | peteng | blonjo | lius | aruh | dewasa | kejem | lempeng | seling | sarwa
    Adv -> pisan | sesai | kapah | kaja | kelod | maut | manis | taluh | langsung | pelan | cepat | ajeg | sekali | tusing | ento | ritat | punduk | jani | kadi | ento | ider | suba | titiang | becik | sane | utama | temenan | juari | malih | puput | sadurung | madan | kapungkur | ring | jeg | lan | titi | anake | kawit | patuh | pidik | gedang | munggah | turun | pemit | maleh | malah | temenan | ngih | mbok | sing | dini | lajeng | kadi | karyane | yening | nenten | bani | pinaka | kanti | sampun | nenten | sane | wantah | gati | buka | ditu | madan | riang | kebus | karang | ngidang | sinam | kasih | kenkene | bebeletan | salawas | sadurung | suba | makejang | mandas | pesu | malih | perak | idep | cepat | lambar | alon | becik | ngawit | temen | bukak | bebas | nganti | muah | serahin | juari | adan | langsung
    Pronoun -> tiang | ragane | dane | ia | ipun | ida | i | cai | ia | nika | tiang | kula | raga | nika | punika | sira | kita | side | nyane | dewek | pekak | meme | bapa | ipun | sira | nyen | anake | tusing | suba | ento | madan | ipun | ida | titiang | sameton | timpal | luh | gede | adi | ratu | ratu bagus | sampun | ngih | mbok | tusing | nenten | kantos | nyane | kadi | inggih | karang | maleh | punduk | ritat | sane | maut | bani | ditu | aeng | pisaga | dewekne | ipun | manira | ida sang | ngiring | kawis | kanti | punyan | malih | serahang | mujur | sapunapi | suang-suang | saling | keneh | sepisan | cang | panake | kantos | sidan | nyantos | tekan | sesampun | timpal | pasikian | antuk | krama | patuh | bakti | timpi | gegeden | luh | madan | pidik | ragae | inggih | ngantos | mangda
    Num -> dua | telu | katiga | siki | duet | tiga | empat | lima | enem | pitu | wolu | sanga | dasan | sebelas | duabelas | tigabelas | empatbelas | limabelas | enambelas | pitulas | woluolas | sangalas | dasalima | telulas | pitulas | dua | tigang | empat | lima | enem | pitu | wolu | sanga | ratus | dasa | satus | selikur | lingtang | tapel | siki dos | tiga dos | malih | sekawan | lulung | lulung iraga | gagel | kakandel | kantos | malih sadurung | tunggal | antuk | duang | wenten | titiang | sakedik | kombinasi | gede | kalih | langkung | ringkang | palu | kombongan | buka | sinyuk | gebel | angga | jujur | mandala | kayang | balang | satya | pekerja | mandiri | pantes | makaya | sawa | pakir | majeng | bentang | sankang | madu
    Prep -> di | ka | ring | uli | ring | antuk | dumatang | ngidang | saking | manten | taler | malih | dados | lintang | rerainan | nenten | suda | genten | ka | peken | waras | ngelantur | lantip | patut | kaang | aras | madu | agung | jujur | ping | malih | klaksan | wenten | sisan | peteng | ringgih | sekancan | temba | luning | pajalan | ringra | mula | arah | becik | nore | kali | luwih | malih | wenten | kantos | lawa | enget | wentenang | pungkasan | tengan | udengan | pelaksana | sané | kantos | pantes | arah | medalan | wenten | luar | ngangge | makta | bentuk | wangunan | ngantos | maosang | ulung | tamiang | kuningan | kebah | mertha | antosang | semengan | pidang | wenten | sekali | malih | anyar | swentan | teman | minak | rerainan | saling | sayang | ringgih | sampun | lampah | ngidang | sareg | sikan | padahal | kawentenan | lumantar | pesar | rahina | balan | samin | langgeng | pahaman | malih | metaken | rorod
    Det -> puniki | punika | eni | ento | i | siki | nenten | wenten | lain | punika | sane | saking | sira | raga | pindah | wentenang | nyane | saking | sikiang | ring | wenten | kawis | masing | polih | sami | sangat | benten | sane | prasida | kebog | nyarengin | kantos | sangkalan | suba | dados | sekar | nentenang | ulam | pijakan | akeh | sangkan | kekecualian | tujuan | weta | jauh | sareg | bika | kawi | jamin | lalu | genten | sama | teras | alit | matu | ngidang | sing | sada | sadurung | malih | sadereng | balik | agung | magi | bajik | sini | aras | bhineka | arta | wenten | ngajeng | kanti | petak | sakiang | sakehing | beten | kadadosan | silih | ringgih | enggal | dede | madu | sane | kejang | katampi | buin | sadurung | ngidang | tentan | sami | parindikan | tengah | seken | wentenang | asta | rarasan | pitung | sameton | rantan | kerang | ngehang | simal | tengahang | sidayang | enget | waras | saring | pelem
    Verb -> manten | ngidang | mados | ngantos | nyidang | ngantosang | ngidangang | nentenang | matu | nganggo | ngemargiang | makta | jaga | laksanayang | ngemargiang | ngajeng | saring | ngidangang | krama | talang | madu | lempas | jaga | lampah | tangi | ngatur | nyakra | medalang | ngidang | bebeng | segara | nganteg | mangda | laksanayang | taler | sia | nyaman | nuntun | lungsur | akeh | ngetang | malih | laksanayang | sambung | nandur | pidang | ngidangang | serahang | ngidang | medal | pidang | saksi | jaladin | lampah | sura | kadep | carang | kembangi | nyekel | pidang | titiang | wasa | gendang | buka | hatur | seleh | panggung | njaga | sirah | mandalika | manten | mentas | adang | kenget | ture | lecengan | repat | kakandeng | aja | laksanayang | wentenang | ngumbah | ngawit | peken | gantos | patur | antosang | matur | malih | jajal | linggah | talu | kepak | manut | pramadi | maté | pindah | tamba | temba | ngetan | nyantosang | kebeng | patu | manca | wastu | sedetik | mangda | maos | tirta | polih | bangun | nawa | taman | nyen
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
    return 'K' in T[0][n-1], T