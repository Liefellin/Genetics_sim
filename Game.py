import pygame
from sys import exit
import random

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Tribble Farm")
clock = pygame.time.Clock()
mouse_pointer = ()
midscreen = 1
current_customer = ""
black = (0, 0, 0)
white = (255, 255, 255)
text1 = ""
text2 = ""
clickimmunity = False
paused = False
tribbledraw = screen
Sex_partner = None
Money = 0


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
    "Blue_eyes_left": pygame.image.load(
        "Art/Tribbles/Tribble Parts/Eye colors/Sky_Blue_Irises_Looking_left.png").convert_alpha(),
    "Blue_eyes_right": pygame.image.load(
        "Art/Tribbles/Tribble Parts/Eye colors/Sky_Blue_Irises_Looking_right.png").convert_alpha(),
    "Blue_eyes_forward": pygame.image.load(
        "Art/Tribbles/Tribble Parts/Eye colors/Sky_Blue_Irises_Looking_forward.png").convert_alpha(),
    "Brown_eyes_forward": pygame.image.load(
        "Art/Tribbles/Tribble Parts/Eye colors/Brown_Irises_Looking_forward.png").convert_alpha(),
    "Brown_eyes_left": pygame.image.load(
        "Art/Tribbles/Tribble Parts/Eye colors/Brown_Irises_Looking_left.png").convert_alpha(),
    "Brown_eyes_right": pygame.image.load(
        "Art/Tribbles/Tribble Parts/Eye colors/Brown_Irises_Looking_right.png").convert_alpha(),
    "Red_eyes_right": pygame.image.load(
        "Art/Tribbles/Tribble Parts/Eye colors/Red_Irises_Looking_right.png").convert_alpha(),
    "Red_eyes_left": pygame.image.load(
        "Art/Tribbles/Tribble Parts/Eye colors/Red_Irises_Looking_left.png").convert_alpha(),
    "Red_eyes_forward": pygame.image.load(
        "Art/Tribbles/Tribble Parts/Eye colors/Red_Irises_Looking_forward.png").convert_alpha(),
    "Eyes_look_forward": pygame.image.load(
        "Art/Tribbles/Tribble Parts/Gaze Direction/Eyes_Looking_Forward.png").convert_alpha(),
    "Eyes_look_left": pygame.image.load(
        "Art/Tribbles/Tribble Parts/Gaze Direction/Eyes_Looking_Left.png").convert_alpha(),
    "Eyes_look_right": pygame.image.load(
        "Art/Tribbles/Tribble Parts/Gaze Direction/Eyes_Looking_Right.png").convert_alpha(),
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
    "Hill": pygame.image.load("Art/Top_Screen_Hill.png").convert_alpha(),
    "Love_Hut": pygame.image.load("Art/Love_Hut.png").convert_alpha(),
    "Text_Area": pygame.image.load("Art/UI/Text_Area.png").convert_alpha(),
    "Paused": pygame.image.load("Art/UI/Paused.png").convert_alpha()
}

Traits = ("sex", "fur_color", "spottiness", "spot_color", "eye_color", "longevity", "sturdiness", "fertility", "alopecia")
colors = {"R": "red", "Y": "yellow", "U": "blue", "B": "black", "W": "white"}
partials = {("blue", "red"): "purple", ("blue", "yellow"): "green", ("red", "yellow"): "orange",
            ("black", "white"): "grey"}

field_rect = images["Field"].get_rect(topleft=(0, 200))
mytext = pygame.font.Font("freesansbold.ttf", 20)
tbspace = images["Text_Area"].get_rect(topleft=(101, 630))
Active_Tribble = None
cars = {"Beret_Lady":images["Beret_Lady's_Car"]}
Todays_customers = ["Beret_Lady"]
lot = []

def onedge(rect):
    edge = random.choice(["top", "bottom", "left", "right"])
    match edge:
        case "top":
            return random.randint(rect.topleft[0], rect.topright[0]), rect.top
        case "bottom":
            return random.randint(rect.bottomleft[0], rect.bottomright[0]), rect.bottom
        case "left":
            return rect.left, random.randint(rect.topleft[1], rect.bottomleft[1])
        case "right":
            return rect.right, random.randint(rect.topright[1], rect.bottomright[1])


def text_objects(text, font):
    textsurface = font.render(text, True, black)
    return textsurface, textsurface.get_rect()


def domrec_alleles(alleles2):
    allelex = []
    alleley = []
    for a in alleles2:
        alleley.append(a)
    for allele in alleles2:
        if allele.isupper():
            allelex.append(allele)
            alleley.remove(allele)
    return [allelex, alleley]


def name_babies(babies):
    pass


def customer_entrance(customers):
    for customer in customers:
        lot.append(cars[customer])



class Button:
    def __init__(self, location):
        self.location = location
        self.clicked = False


    def draw(self):
        screen.blit(self.image, self.location)


class Tribble(Button):
    namecount=0
    def __init__(self, genecode, name=""):
        self.image = images["Tribble_skeleton"]
        self.rect = self.image.get_rect(topleft=(300, 300))
        super().__init__(self.rect.center)
        if len(genecode) != len(Traits):
            pass
        self.genecode = genecode
        self.name = name or self.generate_name()
        self.phenotypes = {}
        self.age = 0
        self.looking = "forward"
        self.goal = ()
        self.image = images["Tribble_skeleton"]
        self.rect = self.image.get_rect(topleft=(300, 300))
        self.collisions = False
        self.breedmode = False
        self.sex_partner = None
        self.value = 10

        for gene in self.genecode:
            if gene not in Traits:
                print(f"Houston, we have a problem. {self.name} has an unlisted gene named {gene}")
            alleles = domrec_alleles(genecode[gene])

            match gene:
                case "eye_color":
                    print(alleles)
                    if len(alleles[0]) == 0:
                        match alleles[1][0]:
                            case "u":
                                self.eye_color = "sky blue"
                                self.value += 5
                    else:
                        print(alleles[0][0])
                        match alleles[0][0]:
                            case "B":
                                self.eye_color = "brown"

                case "sex":
                    if len(alleles[0]) == 0:
                        match alleles[1][0]:
                            case "x":
                                self.sex = "female"
                    else:
                        match alleles[0][0]:
                            case "Y":
                                self.sex = "male"
                case "fur_color":
                    if len(alleles[0]) == 2 and (alleles[0][0]) != (alleles[0][1]) or (
                            len(alleles[1]) == 2 and (alleles[1][0]) != (alleles[1][1])):
                        mixer = []
                        if len(alleles[0]) == 2:
                            alleles = alleles[0]
                        elif len(alleles[1]) == 2:
                            alleles = alleles[1]
                        else:
                            print("Houston, we have a problem. Logic is broken.")
                        for color in alleles:
                            print(color)
                            color = colors[color]
                            mixer.append(color)
                        self.fur_color = partials[tuple(sorted(mixer))]
                    elif len(alleles[0]) == 0:
                        self.fur_color = colors[alleles[1][0].upper()]
                    else:
                        self.fur_color = colors[alleles[0][0].upper()]

                case "spottiness":
                    print(alleles)
                    if len(alleles[0]) == 0:
                        match alleles[1][0]:
                            case "p":
                                self.spots = False
                    else:
                        print("f", alleles[0][0])
                        match alleles[0][0]:
                            case "S":
                                self.spots = True
                case "spot_color":
                    if len(alleles[0]) == 2 and (alleles[0][0]) != (alleles[0][1]) or (
                            len(alleles[1]) == 2 and (alleles[1][0]) != (alleles[1][1])):
                        mixer = []
                        if len(alleles[0]) == 2:
                            alleles = alleles[0]
                        elif len(alleles[1]) == 2:
                            alleles = alleles[1]
                        else:
                            print("Houston, we have a problem. Logic is broken.")
                        for color in alleles:
                            color = colors[color.upper()]
                            mixer.append(color)
                        self.spot_color = partials[tuple(sorted(mixer))]
                    elif len(alleles[0]) == 0:
                        self.spot_color = colors[alleles[1][0].upper()]
                    else:
                        self.spot_color = colors[alleles[0][0]]
                case "fertility":
                    self.fertility = len(alleles[0])
                    if self.fertility > 0:
                        self.fertility -= len(alleles[1])
        if self.fur_color == "white" or self.fur_color == "black":
            self.value += 5
        if self.eye_color == "sky blue":
            self.value += 5
        if self.fur_color != self.spot_color and self.spots and self.value>0:
            self.value -= 5

    @classmethod
    def generate_name(cls):
        cls.namecount += 1
        return f"c{cls.namecount}"

    def breed(self, partner):
        if partner.sex == self.sex:
            return "breed_fail:same_sex"
        childcode = {}
        babies = []
        fertbonus = max(self.fertility, partner.fertility)
        broodsize = random.randint(1, 5 + fertbonus)
        for i in range(broodsize):
            for trait in self.genecode:
                partnergene = partner.genecode[trait]
                selfgene = self.genecode[trait]
                childcode[trait] = [random.choice(selfgene), random.choice(partnergene)]
            child=Tribble(childcode)
            Tribble_list[child.name]=(child)
            print(child.name)
            print (child.genecode)
            print(" -- ")
        self.breedmode = True
        partner.breedmode = True
        return babies

    def description(self):
        desc2=""
        desc = f" This is {self.name}. {self.name} is a {self.fur_color} {self.sex} tribble with {self.eye_color} eyes."
        if self.spots and self.spot_color != self.fur_color:
            desc2 = f" {self.name} has {self.spot_color} spots."
        return [desc, desc2]

    def move(self, xy):
        self.rect = self.rect.move(xy[0], xy[1])

    def moveto(self, coords):
        self.rect.center = coords

    def set_eyes(self, aim):
        if self.breedmode:
            self.looking = "right"
        elif aim:
            if aim[0] < self.rect.left:
                self.looking = "left"
            elif aim[0] > self.rect.right:
                self.looking = "right"
        else:
            self.looking = "forward"

    def movetowards(self, goal):
        xcoord = 0
        ycoord = 0
        if self.rect.left >= goal[0]:
            xcoord -= 1
        elif self.rect.right <= goal[0]:
            xcoord += 1
        if self.rect.top >= goal[1]:
            ycoord -= 1
        elif self.rect.bottom <= goal[1]:
            ycoord += 1
        self.move((xcoord, ycoord))

    def draw(self, location):
        screen.blit(self.image, location)
        match self.eye_color:
            case "brown":
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
                screen.blit(images["Black_fur"], location)

        if self.spots:
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

    def update(self):
        tribblerects = []
        self.set_eyes(self.goal)

        global Sex_partner, Active_Tribble
        if self == Active_Tribble:
            self.looking = "forward"
        for t in Tribble_list:
            if Tribble_list[t] != self:
                tribblerects.append(Tribble_list[t].rect)
        if self.breedmode:
            self.movetowards(lovehuts[0].rect.midbottom)
            self.collisions=False
            self.set_eyes((lovehuts[0].rect.midbottom))
        if not self.breedmode:
            if self.goal == () or self.rect.collidepoint(self.goal):
                self.goal = onedge(field_rect)
            elif not field_rect.contains(self.rect) and not self == Active_Tribble:
                self.goal = onedge(field_rect)
                self.movetowards(self.goal)
            elif not self.rect.collidelistall(obstacles) == [] or self.rect.collidelistall(
                    tribblerects) and self.collisions and not self == Active_Tribble:
                self.collisions = False
                self.goal = onedge(field_rect)
                self.movetowards(self.goal)
            elif not self.rect.collidelistall(obstacles) and not self.rect.collidelistall(tribblerects) and not self == Active_Tribble:
                self.collisions = True
                self.movetowards(self.goal)
            elif self == Active_Tribble:
                pass
            else:
                self.movetowards(self.goal)
        if self.clicked and not left:
            print(self.name)
            if self.rect.collidepoint(mouse_pointer):
                if Active_Tribble:
                    print(Active_Tribble.name)
                    Sex_partner = Active_Tribble

                Active_Tribble = self
            self.clicked = False



class Lovehut:
    def __init__(self, location, name):
        super().__init__()
        self.image = images["Love_Hut"]
        self.location = location
        self.rect = self.image.get_rect(topleft=self.location)

    def draw(self):
        screen.blit(self.image, self.location)


class option_Button(Button):
    def __init__(self, txt, location):
        super().__init__(location)
        self.txt = txt
        self.image = images["Option_Button"]
        self.rect = self.image.get_rect(topleft=self.location)
        self.textsurf = text_objects(self.txt, mytext)[0]

    def draw_text(self):
        screen.blit(self.textsurf, self.location)

    def update(self):
        self.textsurf = text_objects(self.txt, mytext)[0]


class direc_Button(Button):
    def __init__(self, direc, location):
        super().__init__(location)
        self.direc = direc
        if self.direc == "left":
            self.image = images["Left_Button"]
        elif self.direc == "right":
            self.image = images["Right_Button"]
        else:
            print("Houston, we have a problem. A direction button has been misnamed.")
        self.rect = self.image.get_rect(topleft=self.location)


class sustenance(Button):
    def __init__(self, forw, location):
        super().__init__(location)
        self.name = forw
        if self.name == "food":
            self.image = images["Food_Bowl"]
        elif self.name == "water":
            self.image = images["Water_Bowl"]
        else:
            print("Houston, we have a problem. A sustenance bowl has been misnamed.")
        self.rect = self.image.get_rect(topleft=self.location)


Tribble_list = {
    "Joe": Tribble({"sex": ["x", "Y"], "eye_color": ["B", "u"], "spottiness": ["S", "p"], "fur_color": ["R", "U"],
                    "spot_color": ["R", "U"], "fertility": ["F", "f"]}, "Joe"),
    "Eve": Tribble({"sex": ["x", "x"], "eye_color": ["u", "u"], "spottiness": ["p", "p"], "fur_color": ["R", "w"],
                    "spot_color": ["b", "b"], "fertility": ["F", "F"]}, "Eve")
}
Table_Tribbles = []

opbuttons = {
    "1": option_Button("option 1", (101, 725)),
    "2": option_Button("option 2", (257, 725)),
    "3": option_Button("option 3", (413, 725)),
    "4": option_Button("option 4", (569, 725))
}

direc_Buttons = [
    direc_Button("left", (13, 675)),
    direc_Button("right", (737, 675))
]

sust = [
    sustenance("food", (25, 230)),
    sustenance("water", (25, 330))
]

lovehuts = [
    Lovehut((600, 225), "LH1")
]

obstacles = [
]

for x in lovehuts:
    obstacles.append(x.rect)
for x in sust:
    obstacles.append(x.rect)
'''
def choosetribbledropdown():
    screen.blit(frame, placeholder)
    screen.blit(choicefield)
    arrow.draw()
    if Active_Tribble:
        screen.blit(Active_Tribble, nexttothechoicefield(right))
    else:
        screen.blit(Active_Tribble, nexttothechoicefield(right))
    confirmbutton.draw()
    screen.blit(textobjects(confirmbuttontext, mytext)[0](placeholder))
    if arrow is clicked:
        start clickimmunity
        dd = "open":
    if dd == "open":
        for tribble in tribblelist:
            if counter<5
                counter+=1
                menuop.draw()
                screen.blit(textobjects(tribble.name, mytext)[0](placeholder, placeholder+50*counter))
                screen.blit(tribble, (placeholder+100, placeholder+50*counter))


'''
text1_1=""
text2_1=""
def devcheat():
    global midscreen, current_customer, mouse_pointer, options, text1, text1_1, text2, text2_1
    # mouse_pointer = (500, 500)
options = [["???", "??????", "???", "???"], ["???", "???", "???", "???"], ["???", "???", "???", "???"]]

text3 = "Today I am selling a bumblebee tribble."
text2 = "I will need three red tribbles. No spots."
text1 = "Click a tribble!"
text3_1 = "Only $5!"
current_customer = "Beret_Lady"
satisfied=False
visited=[]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONUP:
            clickimmunity = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            paused = not paused
            pausetext = "Game Paused"
    left, middle, right = pygame.mouse.get_pressed()
    mouse_pointer = pygame.mouse.get_pos()

    devcheat()

    screen.blit(images["Upper_Strip"], (0, 0))
    screen.blit(images["Hill"], (230, 107))
    screen.blit(images["Text_Box"], (0, 600))

    if not paused:
        match midscreen:
            case 1:
                options[0] = [f"{'Breed ' + Sex_partner.name if Sex_partner else '???'}", f"{'Sell (Table)' if Active_Tribble else '???'}", f"{'Sell (Market)' if Active_Tribble else '???'}", "???"]
                screen.blit(images["Field"], (0, 200))


                for lovehut in lovehuts:
                    lovehut.draw()
                for sus in sust:
                    sus.draw()

                for tribble in Tribble_list:
                    button = Tribble_list[tribble]
                    button.update()
                    button.draw(button.rect.topleft)
                    if button.clicked and not left:
                        button.clicked = False
                    if left and button.rect.collidepoint(mouse_pointer) and not button.clicked:
                        button.clicked = True
                        text1, text1_1 = button.description()

                if opbuttons["1"].clicked and Sex_partner != Active_Tribble and Active_Tribble:
                    if len(Tribble_list)>21:
                        text1 = "The field cannot hold any more tribbles!"
                        text1_1 = "Try selling some off."
                    Active_Tribble.breedmode = True
                    Sex_partner.breedmode = True
                    Active_Tribble.sex_partner = Sex_partner
                    Sex_partner.sex_partner = Active_Tribble
                    Active_Tribble = False
                    Sex_partner = False
                    text1 = ""
                    text1_1 = ""
                    options[0][0] = "???"
                elif opbuttons["2"].clicked and Active_Tribble:
                    for trib in Tribble_list:
                        Tribble_list[trib].breedmode = False
                    Table_Tribbles.append(Active_Tribble)
                    print("table:")
                    for tribble in Table_Tribbles:
                        print(tribble.name)

                    Tribble_list.pop(Active_Tribble.name, None)
                    Active_Tribble = None
                elif opbuttons["3"].clicked and Active_Tribble:
                    Money+=Active_Tribble.value
                    Tribble_list.pop(Active_Tribble.name, None)
                    Active_Tribble=None
                    text1 = ""
                    text1_1 = ""

                for tribble in Tribble_list:
                    tribble = Tribble_list[tribble]
                    if tribble.breedmode == True and tribble.sex_partner.rect.colliderect(lovehuts[0]) and tribble.rect.colliderect(lovehuts[0]) and tribble.sex_partner.sex_partner == tribble and len(Tribble_list)<21:
                        tribble.breed(tribble.sex_partner)
                        tribble.sex_partner.breedmode = False
                        tribble.breedmode = False
                        break
                screen.blit(text_objects(text1, mytext)[0], (101, 630))
                screen.blit(text_objects(text1_1, mytext)[0], (101, 650))

            case 2:
                screen.blit(images["Office"], (0, 200))
                if current_customer and not satisfied:
                    screen.blit(images[current_customer], (235, 249))
                    options[1] = ["Offer Table", "'Later'", "'Get out.'", "Return Table"]
                    screen.blit(text_objects(text2, mytext)[0], (101, 630))
                    screen.blit(text_objects(text2_1, mytext)[0], (101, 650))
                    if opbuttons["1"].clicked:
                        Acceptables = []
                        tribcolors={'red':[]}
                        tribbletally = f"{len(Table_Tribbles)} tribbles."
                        for trib in Table_Tribbles:
                            try:
                                tribcolors[trib.fur_color].append(trib)
                            except KeyError:
                                tribcolors[trib.fur_color]=[trib]
                            counter=0
                            tribbletally=''
                        for color in tribcolors:
                            counter+=1
                            if counter== len(tribcolors)-1:
                                tribbletally += str(len(tribcolors[color])) + ' ' + color + ' tribble'+('s' if len(tribcolors[color])!=1 else '')+(f' with {trib.spot_color} spots') if trib.spots else '' +', and '
                            elif counter==len(tribcolors):
                                tribbletally += str(len(tribcolors[color])) + ' ' + color + ' tribble'+('s' if len(tribcolors[color])!=1 else '')+(f' with {trib.spot_color} spots') if trib.spots else ''+'.'
                            else:
                                tribbletally+=str(len(tribcolors[color]))+' '+color +' tribble'+('s' if len(tribcolors[color])!=1 else '')+(f' with {trib.spot_color} spots') if trib.spots else ''+', '
                        for tribble in Table_Tribbles:
                            print(tribble.name)
                            if tribble.fur_color=="red" and (tribble.spots==False or tribble.spot_color=='red'):
                                Acceptables.append(tribble)
                        print(tribbletally)
                        print(tribcolors)
                        if len(Acceptables)>3 and len (Table_Tribbles<7):
                            text2 = "'I appreciate your generosity. Here is a little extra.'"
                            Table_Tribbles = []
                            options[1] = ["???", "???", "???", "???"]
                            satisfied=True
                            Money+=500
                        elif len(Acceptables)==3:
                            text2 = "'Magnifique! Here is your pay.'"
                            Table_Tribbles = []
                            satisfied=True
                            Money+=300
                            options[1] = ["???", "???", "???", "???"]
                        else:
                            text2 = f"'I wanted THREE RED tribbles. You gave me "
                            text2_1 = "far too many tribbles" if len(Table_Tribbles)>6 else "the wrong kind of tribbles."
                    elif opbuttons["2"].clicked:
                        text2 = "'I will return in four days.'"
                        current_customer = None
                        options[1] = ["???", "???", "???", "???"]
                    elif opbuttons["3"].clicked:
                        text2 = "'I see I have been wasting my time here.'"
                        current_customer = None
                        options[1]=["???","???","???","???"]
                    elif opbuttons["4"].clicked:
                        for trib in Table_Tribbles:
                            text2 = f"Table cleared. {len(Table_Tribbles)} tribbles have been returned to the field"
                            text2_1 =""
                            Tribble_list[trib.name] = trib
                        Table_Tribbles = []
                screen.blit(text_objects(text2, mytext)[0], (101, 630))
                screen.blit(text_objects(text2_1, mytext)[0], (101, 650))

            case 3:
                screen.fill(white)
                screen.blit(images["Upper_Strip"], (0, 0))
                screen.blit(images["Hill"], (230, 107))
                screen.blit(images["Text_Box"], (0, 600))

                screen.blit(text_objects(text3, mytext)[0], (101, 630))
                screen.blit(text_objects(text3_1, mytext)[0], (101, 650))
        screen.blit(text_objects(f"${Money}", mytext)[0], (600, 10))

    else:
        match midscreen:
            case 1:
                screen.blit(images["Field"], (0, 200))
                for lovehut in lovehuts:
                    lovehut.draw()
                for sus in sust:
                    sus.draw()
                for tribble in Tribble_list:
                    Tribble_list[tribble].draw(Tribble_list[tribble].rect.topleft)
            case 2:
                screen.blit(images["Office"], (0, 200))
                screen.blit(images[current_customer], (235, 249))
            case 3:
                screen.fill(white)
                screen.blit(images["Upper_Strip"], (0, 0))
                screen.blit(images["Hill"], (230, 107))
                screen.blit(images["Text_Box"], (0, 600))
        screen.blit(text_objects(pausetext, mytext)[0], (101, 630))
        screen.blit(images["Paused"], (300, 280))
        screen.blit(text_objects(f"${Money}", mytext)[0], (600, 10))


    for option in opbuttons:
        button = opbuttons[option]
        button.txt = options[midscreen - 1][int(option) - 1]
        button.update()
        button.draw()
        button.draw_text()
        if button.clicked and not left:
            button.clicked = False
        if left and button.rect.collidepoint(mouse_pointer) and not button.clicked:
            button.clicked = True

    for button in direc_Buttons:
        button.draw()
        if left and button.rect.collidepoint(mouse_pointer) and not button.clicked:
            button.clicked = True
    if direc_Buttons[0].clicked and not left:
            visited.append(midscreen)
            midscreen -= 1
            if midscreen <= 0:
                midscreen = 3

            direc_Buttons[0].clicked = False
    elif direc_Buttons[1].clicked and not left:
            visited.append(midscreen)
            midscreen += 1
            if midscreen >= 4:
                midscreen = 1

            direc_Buttons[1].clicked = False

            for page in range(4):
                if page in visited:
                    match page:
                        case 1:
                            text1 = "Click a tribble!"
                            text1_1 = ""
                        case 2:
                            text2 = "I'm still waiting on my three red tribbles."
                            text2_1 = ""
                        case 3:
                            text3 = "Are you here to buy a bumblebee tribble?"
                            text3_1 = "Only $5!"
            button.clicked = False
            if left and button.rect.collidepoint(mouse_pointer) and not button.clicked:
                button.clicked = True
    pygame.display.update()
    clock.tick(60)
