from PIL import Image
import numpy as np

class Profiles:
    def __init__(self, id, actList, image, name, description, active):
        self.id = id
        self.actList = actList
        self.image = image
        self.name = name 
        self.description = description
        self.active = active
      
    def setInactive(active):
        active = False

    def setActive(active):
        active = True

    def getImage(self):
        return self.image
    
    def getDescription(self):
        return self.description
    
    def getName(self):
        return self.name

    def getID(self):
        return self.id
    
    def getActList(self):
        return self.actList

    def getActive(self):
        return self.active
    
    
    def convertImage(self, image):
        img = Image.open(image)
        ary = np.array(img)

        for i in range(img.size[0]):    # For every pixel:
          for j in range(img.size[1]):
            ary[i,j] = (i, j, 100) # Set the colour accordingly
        img.save(image)


    def writeEntry(id, actList, image, name, description, active):
        #if it is not already there write the entry, otherwise change entry
        with open('profiles.txt', 'a') as f:
            f.write("")
        lines = set(open('profiles.txt').readlines())
        inLine = False
        
        newLine = [str(id), ', ', actList, ', ', str(image),  ', ', name,  ', ', description,  ', ', active]
    
        for line in lines:
            if str(id) in line:
                line = line.replace(line, str(newLine))
                inLine = True
        
        if inLine == False:
            with open('profiles.txt', 'a') as f:
                for word in newLine:
                    f.write(str(word))
                f.write('\n')
        else: 
            with open('profiles.txt', 'w') as f:
                for line in lines:
                    f.write(line)
                    f.write('\n')
        
p = Profiles(id, "whiteList", 'handsome-cheerful-man-with-happy-smile_176420-18028.png', "genericus", "for the glory of Rome", True)
p.convertImage('handsome-cheerful-man-with-happy-smile_176420-18028.png')
p.writeEntry("whiteList", p.getImage(), "genericus", "for the glory of Rome", True)