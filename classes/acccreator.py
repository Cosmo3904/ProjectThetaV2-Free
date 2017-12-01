from PyQt5 import QtCore, QtGui, QtWidgets
import random
from classes.createadidas import createaccount, createv2

class createAccounts(QtCore.QThread):
    def __init__(self, email, style, maxcount):
        QtCore.QThread.__init__(self)
        self.email = email
        self.style = style
        self.maxcount = maxcount
        self.firstnames = ['james', 'john', 'robert', 'michael', 'william', 'david', 'richard', 'charles', 'joseph', 'thomas', 'christopher', 'daniel', 'paul', 'mark', 'donald', 'george', 'kenneth', 'steven', 'edward', 'brian', 'ronald', 'anthony', 'kevin', 'jason', 'matthew', 'gary', 'timothy', 'jose', 'larry', 'jeffrey', 'frank', 'scott', 'eric', 'stephen', 'andrew', 'raymond', 'gregory', 'joshua', 'jerry', 'dennis', 'walter', 'patrick', 'peter', 'harold', 'douglas', 'henry', 'carl', 'arthur', 'ryan', 'roger', 'joe', 'juan', 'jack', 'albert', 'jonathan', 'justin', 'terry', 'gerald', 'keith', 'samuel', 'willie', 'ralph', 'lawrence', 'nicholas', 'roy', 'benjamin', 'bruce', 'brandon', 'adam', 'harry', 'fred', 'wayne', 'billy', 'steve', 'louis', 'jeremy', 'aaron', 'randy', 'howard', 'eugene', 'carlos', 'russell', 'bobby', 'victor', 'martin', 'ernest', 'phillip', 'todd', 'jesse', 'craig', 'alan', 'shawn', 'clarence', 'sean', 'philip', 'chris', 'johnny', 'earl', 'jimmy', 'antonio', 'danny', 'bryan', 'tony', 'luis', 'mike', 'stanley', 'leonard', 'nathan', 'dale', 'manuel', 'rodney', 'curtis', 'norman', 'allen', 'marvin', 'vincent', 'glenn', 'jeffery', 'travis', 'jeff', 'chad', 'jacob', 'lee', 'melvin', 'alfred', 'kyle', 'francis', 'bradley', 'jesus', 'herbert', 'frederick', 'ray', 'joel', 'edwin', 'don', 'eddie', 'ricky', 'troy', 'randall', 'barry', 'alexander', 'bernard', 'mario', 'leroy', 'francisco', 'marcus', 'micheal', 'theodore', 'clifford', 'miguel', 'oscar', 'jay', 'jim', 'tom', 'calvin', 'alex', 'jon', 'ronnie', 'bill', 'lloyd', 'tommy', 'leon', 'derek', 'warren', 'darrell', 'jerome', 'floyd', 'leo', 'alvin', 'tim', 'wesley', 'gordon', 'dean', 'greg', 'jorge', 'dustin', 'pedro', 'derrick', 'dan', 'lewis', 'zachary', 'corey', 'herman', 'maurice', 'vernon', 'roberto', 'clyde', 'glen', 'hector', 'shane', 'ricardo', 'sam', 'rick', 'lester', 'brent', 'ramon', 'charlie', 'tyler', 'gilbert', 'gene', 'marc', 'reginald', 'ruben', 'brett', 'angel', 'nathaniel', 'rafael', 'leslie', 'edgar', 'milton', 'raul', 'ben', 'chester', 'cecil', 'duane', 'franklin', 'andre', 'elmer', 'brad', 'gabriel', 'ron', 'mitchell', 'roland', 'arnold', 'harvey', 'jared', 'adrian', 'karl', 'cory', 'claude', 'erik', 'darryl', 'jamie', 'neil', 'jessie', 'christian', 'javier', 'fernando', 'clinton', 'ted', 'mathew', 'tyrone', 'darren', 'lonnie', 'lance', 'cody', 'julio', 'kelly', 'kurt', 'allan', 'nelson', 'guy', 'clayton', 'hugh', 'max', 'dwayne', 'dwight', 'armando', 'felix', 'jimmie', 'everett', 'jordan', 'ian', 'wallace', 'ken', 'bob', 'jaime', 'casey', 'alfredo', 'alberto', 'dave', 'ivan', 'johnnie', 'sidney', 'byron', 'julian', 'isaac', 'morris', 'clifton', 'willard', 'daryl', 'ross', 'virgil', 'andy', 'marshall', 'salvador', 'perry', 'kirk', 'sergio', 'marion', 'tracy', 'seth', 'kent', 'terrance', 'rene', 'eduardo', 'terrence', 'enrique', 'freddie', 'wade']
        self.lastnames = ['smith', 'johnson', 'williams', 'brown', 'jones', 'miller', 'davis', 'garcia', 'rodriguez', 'wilson', 'martinez', 'anderson', 'taylor', 'thomas', 'hernandez', 'moore', 'martin', 'jackson', 'thompson', 'white', 'lopez', 'lee', 'gonzalez', 'harris', 'clark', 'lewis', 'robinson', 'walker', 'perez', 'hall', 'young', 'allen', 'sanchez', 'wright', 'king', 'scott', 'green', 'baker', 'adams', 'nelson', 'hill', 'ramirez', 'campbell', 'mitchell', 'roberts', 'carter', 'phillips', 'evans', 'turner', 'torres', 'parker', 'collins', 'edwards', 'stewart', 'flores', 'morris', 'nguyen', 'murphy', 'rivera', 'cook', 'rogers', 'morgan', 'peterson', 'cooper', 'reed', 'bailey', 'bell', 'gomez', 'kelly', 'howard', 'ward', 'cox', 'diaz', 'richardson', 'wood', 'watson', 'brooks', 'bennett', 'gray', 'james', 'reyes', 'cruz', 'hughes', 'price', 'myers', 'long', 'foster', 'sanders', 'ross', 'morales', 'powell', 'sullivan', 'russell', 'ortiz', 'jenkins', 'gutierrez', 'perry', 'butler', 'barnes', 'fisher', 'henderson', 'coleman', 'simmons', 'patterson', 'jordan', 'reynolds', 'hamilton', 'graham', 'kim', 'gonzales', 'alexander', 'ramos', 'wallace', 'griffin', 'west', 'cole', 'hayes', 'chavez', 'gibson', 'bryant', 'ellis', 'stevens', 'murray', 'ford', 'marshall', 'owens', 'mcdonald', 'harrison', 'ruiz', 'kennedy', 'wells', 'alvarez', 'woods', 'mendoza', 'castillo', 'olson', 'webb', 'washington', 'tucker', 'freeman', 'burns', 'henry', 'vasquez', 'snyder', 'simpson', 'crawford', 'jimenez', 'porter', 'mason', 'shaw', 'gordon', 'wagner', 'hunter', 'romero', 'hicks', 'dixon', 'hunt', 'palmer', 'robertson', 'black', 'holmes', 'stone', 'meyer', 'boyd', 'mills', 'warren', 'fox', 'rose', 'rice', 'moreno', 'schmidt', 'patel', 'ferguson', 'nichols', 'herrera', 'medina', 'ryan', 'fernandez', 'weaver', 'daniels', 'stephens', 'gardner', 'payne', 'kelley', 'dunn', 'pierce', 'arnold', 'tran', 'spencer', 'peters', 'hawkins', 'grant', 'hansen', 'castro', 'hoffman', 'hart', 'elliott', 'cunningham', 'knight', 'bradley', 'carroll', 'hudson', 'duncan', 'armstrong', 'berry', 'andrews', 'johnston', 'ray', 'lane', 'riley', 'carpenter', 'perkins', 'aguilar', 'silva', 'richards', 'willis', 'matthews', 'chapman', 'lawrence', 'garza', 'vargas', 'watkins', 'wheeler', 'larson', 'carlson', 'harper', 'george', 'greene', 'burke', 'guzman', 'morrison', 'munoz', 'jacobs', 'obrien', 'lawson', 'franklin', 'lynch', 'bishop', 'carr', 'salazar', 'austin', 'mendez', 'gilbert', 'jensen', 'williamson', 'montgomery', 'harvey', 'oliver', 'howell', 'dean', 'hanson', 'weber', 'garrett', 'sims', 'burton', 'fuller', 'soto', 'mccoy', 'welch', 'chen', 'schultz', 'walters', 'reid', 'fields', 'walsh', 'little', 'fowler', 'bowman', 'davidson', 'may', 'day', 'schneider', 'newman', 'brewer', 'lucas', 'holland', 'wong', 'banks', 'santos', 'curtis', 'pearson', 'delgado', 'valdez', 'pena', 'rios', 'douglas', 'sandoval', 'barrett', 'hopkins', 'keller', 'guerrero', 'stanley', 'bates', 'alvarado', 'beck', 'ortega', 'wade', 'estrada', 'contreras', 'barnett', 'caldwell', 'santiago', 'lambert', 'powers', 'chambers', 'nunez', 'craig', 'leonard', 'lowe', 'rhodes', 'byrd', 'gregory', 'shelton', 'frazier', 'becker', 'maldonado', 'fleming', 'vega', 'sutton', 'cohen', 'jennings', 'parks', 'mcdaniel', 'watts', 'barker', 'norris', 'vaughn', 'vazquez', 'holt', 'schwartz', 'steele', 'benson', 'neal', 'dominguez', 'horton', 'terry', 'wolfe', 'hale', 'lyons', 'graves', 'haynes', 'miles', 'park', 'warner', 'padilla', 'bush', 'thornton', 'mccarthy', 'mann', 'zimmerman', 'erickson', 'fletcher', 'mckinney', 'page', 'dawson', 'joseph', 'marquez', 'reeves', 'klein', 'espinoza', 'baldwin', 'moran', 'love', 'robbins', 'higgins', 'ball', 'cortez', 'le', 'griffith', 'bowen', 'sharp', 'cummings', 'ramsey', 'hardy', 'swanson', 'barber', 'acosta', 'luna', 'chandler', 'daniel', 'blair', 'cross', 'simon', 'dennis', 'oconnor', 'quinn', 'gross', 'navarro', 'moss', 'fitzgerald', 'doyle', 'mclaughlin', 'rojas', 'rodgers', 'stevenson', 'singh', 'yang', 'figueroa', 'harmon', 'newton', 'paul', 'manning', 'garner', 'mcgee', 'reese', 'francis', 'burgess', 'adkins', 'goodman', 'curry', 'brady', 'christensen', 'potter', 'walton', 'goodwin', 'mullins', 'molina', 'webster', 'fischer', 'campos', 'avila', 'sherman', 'todd', 'chang', 'blake', 'malone', 'wolf', 'hodges', 'juarez', 'gill', 'farmer', 'hines', 'gallagher', 'duran', 'hubbard', 'cannon', 'miranda', 'wang', 'saunders', 'tate', 'mack', 'hammond', 'carrillo', 'townsend', 'wise', 'ingram', 'barton', 'mejia', 'ayala', 'schroeder', 'hampton', 'rowe', 'parsons', 'frank', 'waters', 'strickland', 'osborne', 'maxwell', 'chan', 'deleon', 'norman', 'harrington', 'casey', 'patton', 'logan', 'bowers', 'mueller', 'glover', 'floyd', 'hartman', 'buchanan', 'cobb', 'french', 'kramer', 'mccormick', 'clarke', 'tyler', 'gibbs', 'moody', 'conner', 'sparks', 'mcguire', 'leon', 'bauer', 'norton', 'pope', 'flynn', 'hogan', 'robles', 'salinas', 'yates', 'lindsey', 'lloyd', 'marsh', 'mcbride', 'owen', 'solis', 'pham', 'lang', 'pratt', 'lara', 'brock', 'ballard', 'trujillo', 'shaffer', 'drake', 'roman', 'aguirre', 'morton', 'stokes', 'lamb', 'pacheco', 'patrick', 'cochran', 'shepherd', 'cain', 'burnett', 'hess', 'li', 'cervantes', 'olsen', 'briggs', 'ochoa', 'cabrera', 'velasquez', 'montoya', 'roth', 'meyers', 'cardenas', 'fuentes', 'weiss', 'wilkins', 'hoover', 'nicholson', 'underwood', 'short', 'carson', 'morrow', 'colon', 'holloway', 'summers', 'bryan', 'petersen', 'mckenzie', 'serrano', 'wilcox', 'carey', 'clayton', 'poole', 'calderon', 'gallegos', 'greer', 'rivas', 'guerra', 'decker', 'collier', 'wall', 'whitaker', 'bass', 'flowers', 'davenport', 'conley', 'houston', 'huff', 'copeland', 'hood', 'monroe', 'massey', 'roberson', 'combs', 'franco', 'larsen', 'pittman', 'randall', 'skinner', 'wilkinson', 'kirby', 'cameron', 'bridges', 'anthony', 'richard', 'kirk', 'bruce', 'singleton', 'mathis', 'bradford', 'boone', 'abbott', 'charles', 'allison', 'sweeney', 'atkinson', 'horn', 'jefferson', 'rosales', 'york', 'christian', 'phelps', 'farrell', 'castaneda', 'nash', 'dickerson', 'bond', 'wyatt', 'foley', 'chase', 'gates', 'vincent', 'mathews', 'hodge', 'garrison', 'trevino', 'villarreal', 'heath', 'dalton', 'valencia', 'callahan', 'hensley', 'atkins', 'huffman', 'roy', 'boyer', 'shields', 'lin', 'hancock', 'grimes', 'glenn', 'cline', 'delacruz', 'camacho', 'dillon', 'parrish', 'oneill', 'melton', 'booth', 'kane', 'berg', 'harrell', 'pitts', 'savage', 'wiggins', 'brennan', 'salas', 'marks', 'russo', 'sawyer', 'baxter', 'golden', 'hutchinson', 'liu', 'walter', 'mcdowell', 'wiley', 'rich', 'humphrey', 'johns', 'koch', 'suarez', 'hobbs', 'beard', 'gilmore', 'ibarra', 'keith', 'macias', 'khan', 'andrade', 'ware', 'stephenson', 'henson', 'wilkerson', 'dyer', 'mcclure', 'blackwell', 'mercado', 'tanner', 'eaton', 'clay', 'barron', 'beasley', 'oneal', 'small', 'preston', 'wu', 'zamora', 'macdonald', 'vance', 'snow', 'mcclain', 'stafford', 'orozco', 'barry', 'english', 'shannon', 'kline', 'jacobson', 'woodard', 'huang', 'kemp', 'mosley', 'prince', 'merritt', 'hurst', 'villanueva', 'roach', 'nolan', 'lam', 'yoder', 'mccullough', 'lester', 'santana', 'valenzuela', 'winters', 'barrera', 'orr', 'leach', 'berger', 'mckee', 'strong', 'conway', 'stein', 'whitehead', 'bullock', 'escobar', 'knox', 'meadows', 'solomon', 'velez', 'odonnell', 'kerr', 'stout', 'blankenship', 'browning', 'kent', 'lozano', 'bartlett', 'pruitt', 'buck', 'barr', 'gaines', 'durham', 'gentry', 'mcintyre', 'sloan', 'rocha', 'melendez', 'herman', 'sexton', 'moon', 'hendricks', 'rangel', 'stark', 'lowery', 'hardin', 'hull', 'sellers', 'ellison', 'calhoun', 'gillespie', 'mora', 'knapp', 'mccall', 'morse', 'dorsey', 'weeks', 'nielsen', 'livingston', 'leblanc', 'mclean', 'bradshaw', 'glass', 'middleton', 'buckley', 'schaefer', 'frost', 'howe', 'house', 'mcintosh', 'ho', 'pennington', 'reilly', 'hebert', 'mcfarland', 'hickman', 'noble', 'spears', 'conrad', 'arias', 'galvan', 'velazquez', 'huynh', 'frederick', 'randolph', 'cantu', 'fitzpatrick', 'mahoney', 'peck', 'villa', 'michael', 'donovan', 'mcconnell', 'walls', 'boyle', 'mayer', 'zuniga', 'giles', 'pineda', 'pace', 'hurley', 'mays', 'mcmillan', 'crosby', 'ayers', 'case', 'bentley', 'shepard', 'everett', 'pugh', 'david', 'mcmahon', 'dunlap', 'bender', 'hahn', 'harding', 'acevedo', 'raymond', 'blackburn', 'duffy', 'landry', 'dougherty', 'bautista', 'shah', 'potts', 'arroyo', 'valentine', 'meza', 'gould', 'vaughan', 'fry', 'rush', 'avery', 'herring', 'dodson', 'clements', 'sampson', 'tapia', 'bean', 'lynn', 'crane', 'farley', 'cisneros', 'benton', 'ashley', 'mckay', 'finley', 'best', 'blevins', 'friedman', 'moses', 'sosa', 'blanchard', 'huber', 'frye', 'krueger', 'bernard', 'rosario', 'rubio', 'mullen', 'benjamin', 'haley', 'chung', 'moyer', 'choi', 'horne', 'yu(s)(s)', 'woodward', 'ali', 'nixon', 'hayden', 'rivers', 'estes', 'mccarty', 'richmond', 'stuart', 'maynard', 'brandt', 'oconnell', 'hanna', 'sanford', 'sheppard', 'church', 'burch', 'levy', 'rasmussen', 'coffey', 'ponce', 'faulkner', 'donaldson', 'schmitt', 'novak', 'costa', 'montes', 'booker', 'cordova', 'waller', 'arellano', 'maddox', 'mata', 'bonilla', 'stanton', 'compton', 'kaufman', 'dudley', 'mcpherson', 'beltran', 'dickson', 'mccann', 'villegas', 'proctor', 'hester', 'cantrell', 'daugherty', 'cherry', 'bray', 'davila', 'rowland', 'madden', 'levine', 'spence', 'good', 'irwin', 'werner', 'krause', 'petty', 'whitney', 'baird', 'hooper', 'pollard', 'zavala', 'jarvis', 'holden', 'hendrix', 'haas', 'mcgrath', 'bird', 'lucero', 'terrell', 'riggs', 'joyce', 'rollins', 'mercer', 'galloway', 'duke', 'odom', 'andersen', 'downs', 'hatfield', 'benitez', 'archer', 'huerta', 'travis', 'mcneil', 'hinton', 'zhang', 'hays', 'mayo', 'fritz', 'branch', 'mooney', 'ewing', 'ritter', 'esparza', 'frey', 'braun', 'gay', 'riddle', 'haney', 'kaiser', 'holder', 'chaney', 'mcknight', 'gamble', 'vang', 'cooley', 'carney', 'cowan', 'forbes', 'ferrell', 'davies', 'barajas', 'shea', 'osborn', 'bright', 'cuevas', 'bolton', 'murillo', 'lutz', 'duarte', 'kidd', 'key', 'cooke']
    def run(self):
        if self.style == 'Gmail':
            emaillist = self.dot_trick(self.email[:self.email.find('@')])[0:int(self.maxcount)]
        else:
            count = 0
            emaillist = []
            while count < int(self.maxcount):
                emaillist.append(random.choice(self.firstnames) + random.choice(self.lastnames) + str(random.randint(0,9999)) + '@' + self.email)
                count += 1
        try:
            accounts = open('accounts.txt', 'a')
        except:
            accounts = open('accounts.txt', 'w')
        for item in emaillist:
            password = random.choice(self.firstnames) + random.choice(self.lastnames) + str(random.randint(0,9999))
            if createv2(random.choice(self.firstnames), random.choice(self.lastnames), item, password):
                print('Account Generated')
                accounts.write(item + ':' + password + '\n')
            else:
                print('Failed to Create Account')
        accounts.close()
        print('Accounts Available in accounts.txt')

    def dot_trick(self, username):
        emails = list()
        username_length = len(username)
        combinations = pow(2, username_length - 1)
        padding = "{0:0" + str(username_length - 1) + "b}"
        for i in range(0, combinations):
            bin = padding.format(i)
            full_email = ""

            for j in range(0, username_length - 1):
                full_email += (username[j]);
                if bin[j] == "1":
                    full_email += "."
            full_email += (username[j + 1])
            emails.append(full_email + "@gmail.com")
        return emails

class Ui_dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(361, 130)
        self.boxType = QtWidgets.QComboBox(Dialog)
        self.boxType.setGeometry(QtCore.QRect(220, 37, 121, 22))
        font = QtGui.QFont()
        font.setFamily("YEEZY TSTAR")
        font.setPointSize(14)
        self.boxType.setFont(font)
        self.boxType.setObjectName("boxType")
        self.boxType.addItem("")
        self.boxType.addItem("")
        self.boxMaxAccounts = QtWidgets.QSpinBox(Dialog)
        self.boxMaxAccounts.setGeometry(QtCore.QRect(220, 67, 121, 23))
        font = QtGui.QFont()
        font.setFamily("YEEZY TSTAR")
        font.setPointSize(14)
        self.boxMaxAccounts.setFont(font)
        self.boxMaxAccounts.setMaximum(999)
        self.boxMaxAccounts.setObjectName("boxMaxAccounts")
        self.txtEmail = QtWidgets.QLineEdit(Dialog)
        self.txtEmail.setGeometry(QtCore.QRect(20, 7, 321, 22))
        font = QtGui.QFont()
        font.setFamily("YEEZY TSTAR")
        font.setPointSize(14)
        self.txtEmail.setFont(font)
        self.txtEmail.setObjectName("txtEmail")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 70, 171, 16))
        font = QtGui.QFont()
        font.setFamily("YEEZY TSTAR")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btnCreate = QtWidgets.QPushButton(Dialog)
        self.btnCreate.setGeometry(QtCore.QRect(10, 97, 341, 22))
        font = QtGui.QFont()
        font.setFamily("YEEZY TSTAR")
        font.setPointSize(14)
        self.btnCreate.setFont(font)
        self.btnCreate.setAutoDefault(False)
        self.btnCreate.setObjectName("btnCreate")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 201, 16))
        font = QtGui.QFont()
        font.setFamily("YEEZY TSTAR")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.boxType.setItemText(0, _translate("Dialog", "Gmail"))
        self.boxType.setItemText(1, _translate("Dialog", "Catch All"))
        self.txtEmail.setText(_translate("Dialog", "Gmail / Domain"))
        self.label.setText(_translate("Dialog", "Accounts To Create"))
        self.btnCreate.setText(_translate("Dialog", "Create Accounts"))
        self.label_2.setText(_translate("Dialog", "Email Creation Style"))
        self.btnCreate.clicked.connect(self.createAccounts)

    def createAccounts(self):
        self.thread = createAccounts(self.txtEmail.text(), self.boxType.currentText(), self.boxMaxAccounts.text())
        self.thread.start()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
