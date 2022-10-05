import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Tribble Farm")
clock = pygame.time.Clock()

Traits = ("sex", "fur_color", "spottiness", "spot_color", "eye_color", "longevity", "sturdiness", "appetite", "alopecia")


def dominant_allele(alleles):
    for allele in alleles:
        if allele.isupper():
            return allele
    return alleles[0]


class Tribble:
    def __init__(self, genecode, name):
        self.genecode = genecode
        self.name = name
        self.phenotypes = {}
        self.age = 0

        for gene in self.genecode:
            if gene not in Traits:
                print(f"Houston, we have a problem. {self.name} has an unlisted gene named {gene}")
            alleles = genecode[gene]
            if alleles[0] == alleles[1] and alleles[0].isupper():
                self.zygousy = "Homozygous_Dominant"
            elif alleles[0] == alleles[1]:
                self.zygousy = "Homozygous recessive"
            elif alleles[0] != alleles[1]:
                self.zygousy = "Heterozygous"
            else:
                print(f"Houston, we have a problem. Logic is broken.")

            match gene:
                case "eye_color":
                    match dominant_allele(alleles):
                        case "B":
                            self.eye_color = "brown"
                        case "u":
                            self.eye_color = "blue"
                case "sex":
                    match dominant_allele(alleles):
                        case "x":
                            self.sex = "Female"
                        case "Y":
                            self.sex = "Male"

    def breed(self, partner):
        if partner.sex == self.sex:
            return "breed_fail:same_sex"
        for trait in self.genecode:
            partnergene = partner.genecode[trait]
            selfgene = self.genecode[trait]

    def description(self):
        return f"This is {self.name}. {self.name} is a {self.sex} tribble with {self.eye_color} eyes"


Tribbles = {"Adam": eval("Tribble")({"sex": ["x", "Y"], "eye_color": ["B", "u"]}, "Adam")}

surface1 = pygame.Surface((100, 100))
surface1.fill("cadet blue")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(surface1, (200, 100))
    pygame.display.update()
    clock.tick(60)
