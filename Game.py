import pygame
from sys import exit
import random

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Tribble Farm")
clock = pygame.time.Clock()
mouse_pointer = ()
midscreen = 0
current_customer = ""

Traits = ("sex", "fur_color", "spottiness", "spot_color", "eye_color", "longevity", "sturdiness", "fertility", "alopecia")
images = {
    "Tribble_skeleton": pygame.image.load("Art/Tribbles/Tribble Parts/Skeletons/Tribble_Skeleton.png").convert_alpha(),
    "Blue_spots": pygame.image.load("Art/Tribbles/Tribble Parts/Spots/Blue_Spots.png").convert_alpha(),
    "Green_spots": pygame.image.load("Art/Tribbles/Tribble Parts/Spots/Green_Spots.png").convert_alpha(),
    "Orange_spots": pygame.image.load("Art/Tribbles/Tribble Parts/Spots/Orange_Spots.png").convert_alpha(),
    "Purple_spots": pygame.image.load("Art/Tribbles/Tribble Parts/Spots/Purple_Spots.png").convert_alpha(),
    "Red_spots": pygame.image.load("Art/Tribbles/Tribble Parts/Spots/Red_Spots.png").convert_alpha(),
    "Yellow_spots": pygame.image.load("Art/Tribbles/Tribble Parts/Spots/Yellow_Spots.png").convert_alpha(),
    "White_spots": pygame.image.load("Art/Tribbles/Tribble Parts/Spots/White_Spots.png").convert_alpha(),
    "Black_spots": pygame.image.load("Art/Tribbles/Tribble Parts/Spots/Black_Spots.png").convert_alpha(),
    "Blue_fur": pygame.image.load("Art/Tribbles/Tribble Parts/Body Fur/Blue_Fur.png").convert_alpha(),
    "Green_fur": pygame.image.load("Art/Tribbles/Tribble Parts/Body Fur/Green_Fur.png").convert_alpha(),
    "Orange_fur": pygame.image.load("Art/Tribbles/Tribble Parts/Body Fur/Orange_Fur.png").convert_alpha(),
    "Purple_fur": pygame.image.load("Art/Tribbles/Tribble Parts/Body Fur/Purple_Fur.png").convert_alpha(),
    "Red_fur": pygame.image.load("Art/Tribbles/Tribble Parts/Body Fur/Red_Fur.png").convert_alpha(),
    "Yellow_fur": pygame.image.load("Art/Tribbles/Tribble Parts/Body Fur/Yellow_Fur.png").convert_alpha(),
    "White_fur": pygame.image.load("Art/Tribbles/Tribble Parts/Body Fur/White_Fur.png").convert_alpha(),
    "Black_fur": pygame.image.load("Art/Tribbles/Tribble Parts/Body Fur/Black_Fur.png").convert_alpha(),
    "Blue_eyes_left": pygame.image.load("Art/Tribbles/Tribble Parts/Eye colors/Sky_Blue_Irises_Looking_left.png").convert_alpha(),
    "Blue_eyes_right": pygame.image.load("Art/Tribbles/Tribble Parts/Eye colors/Sky_Blue_Irises_Looking_right.png").convert_alpha(),
    "Blue_eyes_forward": pygame.image.load("Art/Tribbles/Tribble Parts/Eye colors/Sky_Blue_Irises_Looking_forward.png").convert_alpha(),
    "Brown_eyes_forward": pygame.image.load("Art/Tribbles/Tribble Parts/Eye colors/Brown_Irises_Looking_forward.png").convert_alpha(),
    "Brown_eyes_left": pygame.image.load("Art/Tribbles/Tribble Parts/Eye colors/Brown_Irises_Looking_left.png").convert_alpha(),
    "Brown_eyes_right": pygame.image.load("Art/Tribbles/Tribble Parts/Eye colors/Brown_Irises_Looking_right.png").convert_alpha(),
    "Red_eyes_right": pygame.image.load("Art/Tribbles/Tribble Parts/Eye colors/Red_Irises_Looking_right.png").convert_alpha(),
    "Red_eyes_left": pygame.image.load("Art/Tribbles/Tribble Parts/Eye colors/Red_Irises_Looking_left.png").convert_alpha(),
    "Red_eyes_forward": pygame.image.load("Art/Tribbles/Tribble Parts/Eye colors/Red_Irises_Looking_forward.png").convert_alpha(),
    "Eyes_look_forward": pygame.image.load("Art/Tribbles/Tribble Parts/Gaze Direction/Eyes_Looking_Forward.png").convert_alpha(),
    "Eyes_look_left": pygame.image.load("Art/Tribbles/Tribble Parts/Gaze Direction/Eyes_Looking_Left.png").convert_alpha(),
    "Eyes_look_right": pygame.image.load("Art/Tribbles/Tribble Parts/Gaze Direction/Eyes_Looking_Right.png").convert_alpha(),
    "Option_Button": pygame.image.load("Art/UI/Option_Button.png").convert_alpha(),
    "Left_Button": pygame.image.load("Art/UI/Side_Button_Left.png").convert_alpha(),
    "Right_Button": pygame.image.load("Art/UI/Side_Button_Right.png").convert_alpha(),
    "Text_Box": pygame.image.load("Art/UI/Text_box.png").convert_alpha(),
    "Beret_Lady": pygame.image.load("Art/Beret_Lady.png").convert_alpha(),
    "Beret_Lady's_Car": pygame.image.load("Art/Beret_Lady_Car.png").convert_alpha(),
    "Customer_walking": pygame.image.load("Art/Customer_Walking.png").convert_alpha(),
    "Field": pygame.image.load("Art/Field.png").convert_alpha(),
    "Upper_Strip": pygame.image.load("Art/Top_Screen.png").convert_alpha(),
    "Food_Bowl": pygame.image.load("Art/Food_Bowl.png").convert_alpha(),
    "Water_Bowl": pygame.image.load("Art/Water_Bowl.png").convert_alpha(),
    "Office": pygame.image.load("Art/Office.png").convert_alpha(),
    "Hill": pygame.image.load("Art/Top_Screen_Hill.png").convert_alpha()
}
colors = {"R": "red", "Y": "yellow", "U": "blue", "B": "black", "W": "white"}
partials = {("blue", "red"): "purple", ("blue", "yellow"): "green", ("red", "yellow"): "orange", ("black", "white"): "grey"}

field_rect = images["Field"].get_rect(topleft=(0, 200))


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


def name_babies(babies):
    pass


class Tribble(pygame.sprite.Sprite):
    def __init__(self, genecode, name):
        super().__init__()
        if len(genecode) != len(Traits):
            pass
        self.genecode = genecode
        self.name = name
        self.phenotypes = {}
        self.age = 0
        self.looking = "forward"
        self.goal = ()
        self.image = images["Tribble_skeleton"]
        self.rect = self.image.get_rect(topleft=(300, 300))

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
                    print(domrec_alleles(alleles))
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
                        self.fur_color = partials[tuple(sorted(mixer))]
                    elif len(domrec_alleles(alleles)[0]) == 0:
                        self.fur_color = colors[domrec_alleles(alleles)[1][0]]
                    else:
                        self.fur_color = colors[domrec_alleles(alleles)[0][0]]
                case "spottiness":
                    print(domrec_alleles(alleles))
                    if len(domrec_alleles(alleles)[0]) == 0:
                        match domrec_alleles(alleles)[1][0]:
                            case "p":
                                self.spots = False
                    else:
                        print("f", domrec_alleles(alleles)[0][0])
                        match domrec_alleles(alleles)[0][0]:
                            case "S":
                                self.spots = True
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
                    self.fertility = len(domrec_alleles(alleles)[0])
                    if self.fertility > 0:
                        self.fertility -= len(domrec_alleles(alleles)[1])

        match self.eye_color:
            case "Brown":
                match self.looking:
                    case "forward":
                        self.image.blit(images["Eyes_look_forward"], (0, 0))
                        self.image.blit(images["Brown_eyes_forward"], (0, 0))
                    case "left":
                        self.image.blit(images["Eyes_look_left"], (0, 0))
                        self.image.blit(images["Brown_eyes_left"], (0, 0))
                    case "right":
                        self.image.blit(images["Eyes_look_right"], (0, 0))
                        self.image.blit(images["Brown_eyes_right"], (0, 0))
            case "sky blue":
                match self.looking:
                    case "forward":
                        self.image.blit(images["Eyes_look_forward"], (0, 0))
                        self.image.blit(images["Blue_eyes_forward"], (0, 0))
                    case "left":
                        self.image.blit(images["Eyes_look_left"], (0, 0))
                        self.image.blit(images["Blue_eyes_left"], (0, 0))
                    case "right":
                        self.image.blit(images["Eyes_look_right"], (0, 0))
                        self.image.blit(images["Blue_eyes_right"], (0, 0))

            case "red":
                match self.looking:
                    case "forward":
                        self.image.blit(images["Eyes_look_forward"], (0, 0))
                        self.image.blit(images["Red_eyes_forward"], (0, 0))
                    case "left":
                        self.image.blit(images["Eyes_look_left"], (0, 0))
                        self.image.blit(images["Red_eyes_left"], (0, 0))
                    case "right":
                        self.image.blit(images["Eyes_look_right"], (0, 0))
                        self.image.blit(images["Red_eyes_right"], (0, 0))
        match self.fur_color:
            case "red":
                self.image.blit(images["Red_fur"], (0, 0))
            case "orange":
                self.image.blit(images["Orange_fur"], (0, 0))
            case "yellow":
                self.image.blit(images["Yellow_fur"], (0, 0))
            case "green":
                self.image.blit(images["Green_fur"], (0, 0))
            case "blue":
                self.image.blit(images["Blue_fur"], (0, 0))
            case "purple":
                self.image.blit(images["Purple_fur"], (0, 0))
            case "white":
                self.image.blit(images["White_fur"], (0, 0))
            case "black":
                self.image.blit(images["Black_fur"], (0, 0))

        if self.spots == "spotted":
            match self.spot_color:
                case "red":
                    self.image.blit(images["Red_spots"], (0, 0))
                case "orange":
                    self.image.blit(images["Orange_spots"], (0, 0))
                case "yellow":
                    self.image.blit(images["Yellow_spots"], (0, 0))
                case "green":
                    self.image.blit(images["Green_spots"], (0, 0))
                case "blue":
                    self.image.blit(images["Blue_spots"], (0, 0))
                case "purple":
                    self.image.blit(images["Purple_spots"], (0, 0))
                case "white":
                    self.image.blit(images["White_spots"], (0, 0))
                case "black":
                    self.image.blit(images["Black_spots"], (0, 0))

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
            babies.append(pygame.sprite.GroupSingle(eval("Tribble")(childcode, "placeholder")))
        name_babies(babies)

    def description(self):
        desc = f" This is {self.name}. {self.name} is a {self.fur_color} {self.sex} tribble with {self.eye_color} eyes."
        if self.spots and self.spot_color != self.fur_color:
            desc += f" {self.name} has {self.spot_color} spots."
        return desc


    def move(self, xy):
        self.rect = self.rect.move(xy[0], xy[1])


    def moveto(self, coords):
        self.rect.center = coords


    def set_eyes(self):
        if self.goal[0] < self.rect.left:
            self.looking = "left"
        elif self.goal[0] > self.rect.right:
            self.looking = "right"
        else:
            self.looking = "forward"


    def movetowards(self, goal):
        x = 0
        y = 0
        if self.rect.left >= goal[0]:
            x -= 1
        elif self.rect.right <= goal[0]:
            x += 1
        if self.rect.top >= goal[1]:
            y -= 1
        elif self.rect.bottom <= goal[1]:
            y += 1
        self.move((x, y))

    def update(self):
        if self.goal == () or self.rect.collidepoint(self.goal):
            self.goal = mouse_pointer
        elif not field_rect.contains(self.rect):
            self.goal = field_rect.center
            self.movetowards(self.goal)
            self.goal = mouse_pointer
        else:
            self.movetowards(self.goal)


Tribble_list = {
    "Joe": pygame.sprite.GroupSingle(eval("Tribble")({"sex": ["x", "Y"], "eye_color": ["B", "u"], "spottiness": ["S", "p"], "fur_color": ["R", "U"], "spot_color": ["R", "U"], "fertility": ["F", "f"]}, "Joe")),
    "Eve": pygame.sprite.GroupSingle(eval("Tribble")({"sex": ["x", "x"], "eye_color": ["u", "u"], "spottiness": ["p", "p"], "fur_color": ["R", "w"], "spot_color": ["b", "b"], "fertility": ["F", "F"]}, "Eve"))
}



def devcheat():
    global midscreen
    global current_customer
    global mouse_pointer
    midscreen = 1
    current_customer = "Beret_Lady"
    # mouse_pointer = (500, 500)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            exit()
    mouse_pointer = pygame.mouse.get_pos()
    devcheat()

    screen.blit(images["Upper_Strip"], (0, 0))
    screen.blit(images["Hill"], (230, 107))

    screen.blit(images["Text_Box"], (0, 600))
    screen.blit(images["Option_Button"], (101, 725))
    screen.blit(images["Option_Button"], (257, 725))
    screen.blit(images["Option_Button"], (413, 725))
    screen.blit(images["Option_Button"], (569, 725))
    screen.blit(images["Left_Button"], (13, 675))
    screen.blit(images["Right_Button"], (737, 675))


    match midscreen:
        case  1:
            screen.blit(images["Field"], (0, 200))
            for tribble in Tribble_list:
                Tribble_list[tribble].update()
                Tribble_list[tribble].draw(screen)
            screen.blit(images["Food_Bowl"], (25, 230))
            screen.blit(images["Water_Bowl"], (25, 330))
        case  2:
            screen.blit(images["Office"], (0, 200))
            screen.blit(images[current_customer], (235, 249))
    pygame.display.update()
    clock.tick(60)
