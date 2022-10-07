import pygame
from sys import exit
import random

pygame.init()
screen = pygame.display.set_mode((1920, 1080), pygame.RESIZABLE)
pygame.display.set_caption("Tribble Farm")
clock = pygame.time.Clock()

Traits = ("sex", "fur_color", "spottiness", "spot_color", "eye_color", "longevity", "sturdiness", "fertility", "alopecia")

images = {
    "Blue_spots": pygame.image.load("Art/Tribbles/Tribble Parts/Spots/Blue_Spots.png"),
    "Green_spots": pygame.image.load("Art/Tribbles/Tribble Parts/Spots/Green_Spots.png"),
    "Orange_spots": pygame.image.load("Art/Tribbles/Tribble Parts/Spots/Orange_Spots.png"),
    "Purple_spots": pygame.image.load("Art/Tribbles/Tribble Parts/Spots/Purple_Spots.png"),
    "Red_spots": pygame.image.load("Art/Tribbles/Tribble Parts/Spots/Red_Spots.png"),
    "Yellow_spots": pygame.image.load("Art/Tribbles/Tribble Parts/Spots/Yellow_Spots.png"),
    "White_spots": pygame.image.load("Art/Tribbles/Tribble Parts/Spots/White_Spots.png"),
    "Black_spots": pygame.image.load("Art/Tribbles/Tribble Parts/Spots/Black_Spots.png"),
    "Blue_fur": pygame.image.load("Art/Tribbles/Tribble Parts/Body Fur/Blue_Fur.png"),
    "Green_fur": pygame.image.load("Art/Tribbles/Tribble Parts/Body Fur/Green_Fur.png"),
    "Orange_fur": pygame.image.load("Art/Tribbles/Tribble Parts/Body Fur/Orange_Fur.png"),
    "Purple_fur": pygame.image.load("Art/Tribbles/Tribble Parts/Body Fur/Purple_Fur.png"),
    "Red_fur": pygame.image.load("Art/Tribbles/Tribble Parts/Body Fur/Red_Fur.png"),
    "Yellow_fur": pygame.image.load("Art/Tribbles/Tribble Parts/Body Fur/Yellow_Fur.png"),
    "White_fur": pygame.image.load("Art/Tribbles/Tribble Parts/Body Fur/White_Fur.png"),
    "Black_fur": pygame.image.load("Art/Tribbles/Tribble Parts/Body Fur/Black_Fur.png"),
    "Blue_eyes_left": pygame.image.load("Art/Tribbles/Tribble Parts/Eye colors/Sky_Blue_Irises_Looking_left.png"),
    "Blue_eyes_right": pygame.image.load("Art/Tribbles/Tribble Parts/Eye colors/Sky_Blue_Irises_Looking_right.png"),
    "Blue_eyes_forward": pygame.image.load("Art/Tribbles/Tribble Parts/Eye colors/Sky_Blue_Irises_Looking_forward.png"),
    "Brown_eyes_forward": pygame.image.load("Art/Tribbles/Tribble Parts/Eye colors/Brown_Irises_Looking_forward.png"),
    "Brown_eyes_left": pygame.image.load("Art/Tribbles/Tribble Parts/Eye colors/Brown_Irises_Looking_left.png"),
    "Brown_eyes_right": pygame.image.load("Art/Tribbles/Tribble Parts/Eye colors/Brown_Irises_Looking_right.png"),
    "Red_eyes_right": pygame.image.load("Art/Tribbles/Tribble Parts/Eye colors/Red_Irises_Looking_right.png"),
    "Red_eyes_left": pygame.image.load("Art/Tribbles/Tribble Parts/Eye colors/Red_Irises_Looking_left.png"),
    "Red_eyes_forward": pygame.image.load("Art/Tribbles/Tribble Parts/Eye colors/Red_Irises_Looking_forward.png"),
    "Eyes_look_forward": pygame.image.load("Art/Tribbles/Tribble Parts/Gaze Direction/Eyes_Looking_Forward.png"),
    "Eyes_look_left": pygame.image.load("Art/Tribbles/Tribble Parts/Gaze Direction/Eyes_Looking_Left.png"),
    "Eyes_look_right": pygame.image.load("Art/Tribbles/Tribble Parts/Gaze Direction/Eyes_Looking_Right.png"),
    "Tribble_skeleton": pygame.image.load("Art/Tribbles/Tribble Parts/Skeletons/Tribble_Skeleton.png")
}

field = pygame.image.load("Art/field.png")


def domrec_alleles(alleles2):
    x = []
    y = []
    for a in alleles2:
        y.append(a)
    for allele in alleles2:
        if allele.isupper():
            x.append(allele)
            y.remove(allele)
    return [x, y]


colors = {"R": "red", "Y": "yellow", "U": "blue", "B": "black", "W": "white"}
partials = {("blue", "red"): "purple", ("blue", "yellow"): "green", ("red", "yellow"): "orange", ("black", "white"): "grey"}


def name_babies(babies):
    pass


class Tribble:
    def __init__(self, genecode, name):
        if len(genecode) != len(Traits):
            pass
        self.genecode = genecode
        self.name = name
        self.phenotypes = {}
        self.age = 0
        self.looking = "forward"

        for gene in self.genecode:
            if gene not in Traits:
                print(f"Houston, we have a problem. {self.name} has an unlisted gene named {gene}")
            alleles = genecode[gene]
            allele_count = len(alleles)
            if allele_count != 2:
                print(f"Houston, we have a problem. {self.name} does not have the correct amount of alleles. They have {allele_count} alleles.")
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
                    print (domrec_alleles(alleles))
                    if len(domrec_alleles(alleles)[0]) == 0:
                        match domrec_alleles(alleles)[1][0]:
                            case "u":
                                self.eye_color = "sky blue"
                    else:
                        print(domrec_alleles(alleles)[0][0])
                        match domrec_alleles(alleles)[0][0]:
                            case "B":
                                self.eye_color = "Brown"
                case "sex":
                    if len(domrec_alleles(alleles)[0]) == 0:
                        match domrec_alleles(alleles)[1][0]:
                            case "Y":
                                self.sex = "male"
                    else:
                        match domrec_alleles(alleles)[0][0]:
                            case "x":
                                self.sex = "female"
                case "fur_color":
                    if len(domrec_alleles(alleles)[0]) == 2 and (domrec_alleles(alleles)[0][0]) != (domrec_alleles(alleles)[0][1]) or (len(domrec_alleles(alleles)[1]) == 2 and (domrec_alleles(alleles)[1][0]) != (domrec_alleles(alleles)[1][1])):
                        mixer = []
                        for color in alleles:
                            color = colors[color]
                            mixer.append(color)
                        self.furcolor = partials[tuple(sorted(mixer))]
                    elif len(domrec_alleles(alleles)[0]) == 0:
                        self.fur_color = colors[domrec_alleles(alleles)[1][0]]
                    else:
                        self.fur_color = colors[domrec_alleles(alleles)[0][0]]
                case "spottiness":
                    print(domrec_alleles(alleles))
                    if len(domrec_alleles(alleles)[0]) == 0:
                        match domrec_alleles(alleles)[1][0]:
                            case "p":
                                self.spots = "plain"
                    else:
                        print("f", domrec_alleles(alleles)[0][0])
                        match domrec_alleles(alleles)[0][0]:
                            case "S":
                                self.spots = "spotted"
                case "spot_color":
                    if len(domrec_alleles(alleles)[0]) == 2 and (domrec_alleles(alleles)[0][0]) != (domrec_alleles(alleles)[0][1]) or (len(domrec_alleles(alleles)[1]) == 2 and (domrec_alleles(alleles)[1][0]) != (domrec_alleles(alleles)[1][1])):
                        mixer = []
                        for color in alleles:
                            color = colors[color.upper()]
                            mixer.append(color)
                        self.spot_color = partials[tuple(sorted(mixer))]
                    elif len(domrec_alleles(alleles)[0]) == 0:
                        self.spot_color = colors[domrec_alleles(alleles)[1][0].upper()]
                    else:
                        self.spot_color = colors[domrec_alleles(alleles)[0][0]]
                case "fertility":
                    self.fertility = 0
                    for dom in domrec_alleles(alleles)[0]:
                        self.fertility += 1
                    for rec in domrec_alleles(alleles)[1]:
                        if self.fertility > 0:
                            self.fertility -= 1


    def breed(self, partner):
        if partner.sex == self.sex:
            return "breed_fail:same_sex"
        childcode = []
        babies = []
        fertbonus = max(self.fertility, partner.fertility)
        broodsize = random.randint(1, 5+fertbonus)
        for i in range(broodsize):
            for trait in self.genecode:
                partnergene = partner.genecode[trait]
                selfgene = self.genecode[trait]
                childcode[trait] = [random.choice(selfgene), random.choice(partnergene)]
            babies.append(eval("Tribble")(childcode, "placeholder"))
        name_babies(babies)

    def description(self):
        return f"This is {self.name}. {self.name} is a {self.sex} tribble with {self.eye_color} eyes"


    def draw(self, location):
        screen.blit(images["Tribble_skeleton"], location)
        match self.eye_color:
            case "Brown":
                match self.looking:
                    case "forward":
                        screen.blit(images["Eyes_look_forward"], location)
                        screen.blit(images["Brown_eyes_forward"], location)
                    case "left":
                        screen.blit(images["Eyes_look_left"], location)
                        screen.blit(images["Brown_eyes_left"], location)
                    case "right":
                        screen.blit(images["Eyes_look_right"], location)
                        screen.blit(images["Brown_eyes_right"], location)
            case "sky blue":
                match self.looking:
                    case "forward":
                        screen.blit(images["Eyes_look_forward"], location)
                        screen.blit(images["Blue_eyes_forward"], location)
                    case "left":
                        screen.blit(images["Eyes_look_left"], location)
                        screen.blit(images["Blue_eyes_left"], location)
                    case "right":
                        screen.blit(images["Eyes_look_right"], location)
                        screen.blit(images["Blue_eyes_right"], location)


            case "red":
                match self.looking:
                    case "forward":
                        screen.blit(images["Eyes_look_forward"], location)
                        screen.blit(images["Red_eyes_forward"], location)
                    case "left":
                        screen.blit(images["Eyes_look_left"], location)
                        screen.blit(images["Red_eyes_left"], location)
                    case "right":
                        screen.blit(images["Eyes_look_right"], location)
                        screen.blit(images["Red_eyes_right"], location)
        match self.fur_color:
            case "red":
                screen.blit(images["Red_fur"], location)
            case "orange":
                screen.blit(images["Orange_fur"], location)
            case "yellow":
                screen.blit(images["Yellow_fur"], location)
            case "green":
                screen.blit(images["Green_fur"], location)
            case "blue":
                screen.blit(images["Blue_fur"], location)
            case "purple":
                screen.blit(images["Purple_fur"], location)
            case "white":
                screen.blit(images["White_fur"], location)
            case "black":
                screen.blit(images["Black_fur"])
        if self.spots == "spotted":
            match self.spot_color:
                case "red":
                    screen.blit(images["Red_spots"], location)
                case "orange":
                    screen.blit(images["Orange_spots"], location)
                case "yellow":
                    screen.blit(images["Yellow_spots"], location)
                case "green":
                    screen.blit(images["Green_spots"], location)
                case "blue":
                    screen.blit(images["Blue_spots"], location)
                case "purple":
                    screen.blit(images["Purple_spots"], location)
                case "white":
                    screen.blit(images["White_spots"], location)
                case "black":
                    screen.blit(images["Black_spots"], location)



Tribble_list = {
    "Joe": eval("Tribble")({"sex": ["x", "Y"], "eye_color": ["B", "u"], "spottiness": ["S", "p"], "fur_color": ["R", "U"], "spot_color": ["R", "U"], "fertility": ["F", "f"]}, "Joe"),
    "Eve": eval("Tribble")({"sex": ["x", "x"], "eye_color": ["u", "u"], "spottiness": ["p", "p"], "fur_color": ["R", "w"], "spot_color": ["b", "b"], "fertility": ["F", "F"]}, "Eve")
}




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            exit()
        elif event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode(
                event.dict['size'], pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE)
            screen.blit(pygame.transform.scale(field, event.dict['size']), (0, 0))
            pygame.display.flip()


    screen.blit(field, (0, 0))
    Tribble_list["Eve"].draw((200, 200))
    pygame.display.update()
    clock.tick(60)
