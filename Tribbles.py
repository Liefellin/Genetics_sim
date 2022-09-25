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

phenotypes = dict(FCU="blue", FCR="red", FCY="yellow", fcb="black", fcw="white", eyu="blue", EYN="brown", sps="spotted", SPN="spotless", SCB="black", SCW="white", scr="red", scu="blue", scy="yellow", fll="long", FLS="short", CDC="cloudy-eyed", sxx="female", SXY="male")


# 3-letter codes are decided by a two-letter category identifier
# sx for sex or cd for cloudiness
# final letter marks which trait is expressed within that category
# Y for male or C for cloudy
# dominant traits are capitalized

pheno_list = {"name": "", "sex": "", "fur_color": "", "fur_length": "", "spots": "", "spot_color": "", "eye_color": ""}

codom_scenarios = {"sex": None, "fur_color": "partial", "fur_length": None, "spots": None, "spot_color": "equal", "eye_color": None}

partial_codom = {("red", "blue") or ("blue", "red"): "purple", ("yellow", "blue") or ("blue", "yellow"): "green", ("red", "yellow") or ("yellow", "red"): "orange", ("white", "black") or ("black", "white"): "grey"}


def remove_before(txt, target):
    txt = txt.split(target)
    return txt[1]


def remove_after(txt, target):
    txt = txt.split(target)
    return txt[0]


def heritage(code_a, code_b):
    result = [random.choice(code_a), random.choice(code_b)]
    return result
# example codes: ["U",w"],["w","w"]


def expression(gene_code):
    other_attributes = []
    pheno_list["name"] = gene_code["name"]
    del gene_code["name"]
    for item in gene_code:
        # category like sex or fur color
        potential_codom = ""
        for gene in gene_code[item]:
            # specific expression within that category, like male or red
            if "/" in gene:
                for i in remove_before(gene, "/").split(","):
                    other_attributes.append(phenotypes[i])
                gene = remove_after(gene, "/")
            if gene[-1].isupper():
                gene = gene.upper()
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
                        pheno_list[item] = partial_codom[(phenotypes[gene], phenotypes[potential_codom])]
                    else:
                        print("Error: p_codom lookup failed")
                        break
                        # This is meant to be an unreachable state. If this occurs, then the gene code is most likely
                        # invalid.
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


def breeding_failure():
    print("The Tribbles had a lot of fun, but no baby")


def create_child(parent1, parent2):
    if expression(parent1)["sex"] == expression(parent2)["sex"]:
        return breeding_failure
    else:

        pass


Adam = {"name": "Adam", "sex": ["sxx", "SXY"], "fur_color": ["FCU", "fcw"], "fur_length": ["fll", "fll"], "spots": ["sps", "sps"], "spot_color": ["scu", "SCB"], "eye_color": ["EYN", "EYN"]}
# Adam is a longhair blue male tribble with cloudy brown eyes and black spots.

Eve = {"name": "Eve", "sex": ["sxx", "sxx"], "fur_color": ["FCY", "FCR"], "fur_length": ["FLS", "FLS"], "spots": ["SPN", "sps"], "spot_color": ["scu", "SCB"], "eye_color": ["EYN", "EYN"]}
# Eve is a shorthair orange female tribble with blue eyes.

Skye = {"name": "Skye", "sex": ["sxx/CDC", "SXY"], "fur_color": ["FCU", "FCU"], "fur_length": ["FLS", "fll"], "spots": ["sps", "sps"], "spot_color": ["SCW", "scu"], "eye_color": ["eyu", "eyu"]}
# Skye is a shorthair blue male tribble with cloudy blue eyes and white spots.

Tribbles = {"Adam": Adam, "Eve": Eve, "Skye": Skye}
for tribble in Tribbles:
    print(expression(Tribbles[tribble]))
print(expression(Tribbles[tribble]) for tribble in Tribbles)
