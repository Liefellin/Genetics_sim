import random

print("Hello, World!")

# Traits are as follows:
# Fur Color:
# -blUe, Red, White, Black
# Fur Spots: None(n),spots(s)
# spot colors are fur colors(u, r, w, b)
# Fur Length: Long, Short
# Eye Color: brown, blue, Cloudy brown, Cloudy blue
# Sex: Male, Female

# Fur length will be basic mendelian: short dominant, long recessive.
# Eye color: Brown dominant, blue recessive. Cloudiness X-linked dominant.
# Fur color: Dominants are blue, red. black and white are recessive.
# dominant/recessive expresses dominant.
# dom/dom or rec/rec expresses intermediate color (purple or grey)
# Fur spots: none is dominant, spot potential is recessive
# only male tribbles have spots. if a female tribble would have spots it is suppressed
# spot color: black and white are dominant, blue and red are recessive.
# dom/dom or rec/rec results in spots of both colors.
# if spots match fur, they are not described.
# only expressed if spot potential is positive
# only male/female can breed. sex of child is random 50/50.

phenotypes = dict(FCU="blue", FCR="red", fcb="black", fcw="white", eyu="blue", EYN="brown", sps="spotted", spN="spotless", SCB="black", SCW="white", scr="red", scu="blue", fll="long", FLS="short", CDC="cloudy-eyed", sxx="female", SXY="male")


# 3-letter codes are decided by a two-letter category identifier
# sx for sex or cd for cloudiness
# final letter marks which trait is expressed within that category
# Y for male or C for cloudy
# dominant traits are capitalized

pheno_list = {"sex": "", "fur_color": "", "fur_length": "", "spots": "", "spot_color": "", "eye_color": ""}

codom_scenarios = {"sex": None, "fur_color": "intermediate", "fur_length": None, "spots": None, "spot_color": "equal", "eye_color": None}

partial_codom = {("red", "blue") or ("blue", "red"): "purple", ("white", "black") or ("black", "white"): "grey"}


def removebefore(txt, target):
    txt = txt.split(target)
    return txt[1]


def removeafter(txt, target):
    txt = txt.split(target)
    return txt[0]


def heritage(code_a, code_b):
    result = [random.choice(code_a), random.choice(code_b)]
    return result
# example codes: ["U",w"],["w","w"]


def expression(gene_code):
    other_attributes = []

    for item in gene_code:
        # category like sex or fur color
        potential_codom = ""
        for gene in gene_code[item]:
            print(gene_code[item])
            # specific expression within that category, like male or red
            if "/" in gene:
                for i in removebefore(gene, "/").split(","):
                    other_attributes.append(phenotypes[i])
                gene = removeafter(gene, "/")
                print(gene[-1])
            if gene[-1].isupper():
                gene=gene.upper()
            if potential_codom != "":
                if potential_codom == gene:
                    pheno_list[item] = phenotypes[gene]
                elif potential_codom.isupper() and gene.islower():
                    pheno_list[item] = phenotypes[potential_codom]
                elif potential_codom.islower() and gene.isupper():
                    pheno_list[item] = phenotypes[gene]
                else:
                    if codom_scenarios[item] == "equal":
                        pheno_list[item] = f"{gene} and {potential_codom}"
                    elif codom_scenarios[item] == "partial":
                        pheno_list[item] = partial_codom[(gene, potential_codom)]
                    else:
                        print("Error: p_codom lookup failed")
                        break
                        # This is meant to be an unreachable state. If this occurs, then the genecode is most likely invalid.
            potential_codom = gene
        if pheno_list[item] == "":
            pheno_list[item] = phenotypes[gene_code[item][0]]
        for thing in other_attributes:
            pheno_list[thing] = True
    return pheno_list
# example gene_code:
# {
# "sex":["x/C","Y"],
# "fur_color":["U","w"],
# "fur_length":["l","l"],
# "spots":["s","s"],
# "spot_color":["u","B"],
# "eye_color":["R","R"]
# }
# a longhair blue male tribble with cloudy brown eyes and black spots.

# Next objective: implement breeding.


def create_child():

    pass


Tribbles = {}

Adam = {"sex": ["sxx/CDC", "SXY"], "fur_color": ["FCU", "fcw"], "fur_length": ["fll", "fll"], "spots": ["sps", "sps"], "spot_color": ["scu", "SCB"], "eye_color": ["EYN", "EYN"]}
# Adam is a longhair blue male tribble with cloudy brown eyes and black spots.

Eve = {"sex": ["sxx", "sxx"], "fur_color": ["FCU", "fcw"], "fur_length": ["FLS", "fll"], "spots": ["SPN", "sps"], "spot_color": ["scu", "SCB"], "eye_color": ["EYN", "EYN"]}
# Eve is a shorthair red female tribble with blue eyes.

Ctu = {"sex": ["sxx", "SXY"], "fur_color": ["FCU", "FCU"], "fur_length": ["fll", "fll"], "spots": ["SPN", "SPN"], "spot_color": ["scu", "scu"], "eye_color": ["eyu", "eyu"]}

print(expression(Adam))

