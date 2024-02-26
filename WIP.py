import pandas as pd

# This class will be populated by the GUI
class Person:
    def __init__(self, name=None, email=None, userid=None, model=None, role=None, sf_role=None, country=None, manager=None, service=False):
        self.name = name
        self.email = email
        self.userid = userid
        self.model = model
        self.role = role
        self.sf_role = sf_role
        self.country = country
        self.manager = manager
        self.service = service
        
    #Setters
    def setName(self, name):
        self.name = name    
                
    def setEmail(self, email):
        self.email = email
    
    def setUserid(self, userid):
        self.userid = userid
        
    def setModel(self, model):
        self.model = model    
                
    def setRole(self, role):
        self.role = role
        
    def setSF(self, sf_role):
        self.sf_role = sf_role
    
    def setCountry(self, country):
        self.country = country
        
    def setManager(self, manager):
        self.manager = manager
        
    def setService(self, service):
        self.service = service
       
# This class will read the Person data and extract the correct text from the database
class Write:
    def __init__(self, person, data_frame):
        self.person = person
        self.data_frame = data_frame
        self.subject = "New User: "
        self.intro = "Please create a new user for " + person.name + " with the following permissions:\n"
        self.permissions = "\nPermission Set Assignments:\n"
        self.queues = "\nQueue Membership:\n"
        self.configit = "\nConfigit Tool:\n"
        self.basic = ""
    
    #Helpers
    def _fetch(self, rows, col): #Note the rows will be a tuple
        local_output = ""
        for i in range(abs(rows[0] - rows[1])):
            current = str(self.data_frame.iloc[i, col])
            if current != "nan":
                local_output += current + '\n'
        return local_output
    
    def _country_org(self, n):
        orgs = {
            "Brasil":"H200",
            "Chile":"H300",
            "Colombia":"H400",
            "Argentina":"H500",
            "Mexico":"F800"
            }
        return orgs.get(n, "Exception in Country")
    
    def _find_rows(self, key):
        ret = [-1, -1]
        col_name = self.data_frame.columns[0] 
        for i, value in self.data_frame[col_name].items():
            if value == key:
                ret[0] = i
            if value != key and pd.isna(value) == False and ret[0] != -1:
                ret[1] = i
                return ret
    
    #Setters
    def _set_permissions(self):
        r = self._find_rows("Permission")
        self.permissions += "Title: "
        if self.person.role == "Sales Engineer":
            self.permissions += self._fetch(r, 1)
        elif self.person.role == "Internal Sales":
            self.permissions += self._fetch(r, 2)
        elif self.person.role == "Intern":
            self.permissions += self._fetch(r, 3)
        elif self.service:
            self.permissions += self._fetch(r, 4)
            
    def _set_queues(self):
        self.queues = self._fetch((23, 45), 2)
    
    def _set_configit(self):
        configit_rows = self._find_rows("Configit") #dont forget to subtract 2
        if self.person.role == "Sales Engineer":
            self.configit += self._fetch(configit_rows, 1)
        elif self.person.role == "Internal Sales":
            self.configit += self._fetch(configit_rows, 2)
        elif self.person.role == "Intern":
            self.configit += self._fetch(configit_rows, 3)
        elif self.service:
            self.configit += self._fetch(configit_rows, 4)
    
    def _set_country(self):
        org = "CRM P01 - Plant " + self._country_org(self.person.country)
        self.configit += org
        
    def _set_basic(self):
        split_names = self.person.name.split()
        self.basic += "\nFirst Name: " + split_names[0]
        self.basic += "\nLast Name: " + " ".join(split_names[1:])
        self.basic += "\nTitle: " + self.person.role
        self.basic += "\nSalesforce Role: " + self.person.sf_role
        self.basic += "\nTeam:"
        self.basic += "\nManager: " + self.person.manager
        self.basic += "\nUserID: " + self.person.userid
        self.basic += "\nUser Country: " + self.person.country
        self.basic += "\nRegion: LAM"
        self.basic += "\nSub Region: LAM - " + self.person.country
        self.basic += "\nBusiness Unit: DDS - AC Drives"
        self.basic += "\nMy Pipeline Role: " + self.person.role
        if self.person.role == "Sales Engineer":
            self.basic += "\nMy Pipeline Manager NWT: True"
        else:
            self.basic += "\nMy Pipeline Manager NWT: False"
        self.basic += "\nSalesforce Outlook Sync: false\nEnvironment User Needs Modified: P01"
        self.basic += "\nCurrency: USD\n"

    def populate(self):
        self._set_permissions()
        self._set_queues()
        self._set_country()
        self._set_configit()
        self._set_basic()
    
    def get_subject(self):
        output = ""
        output += self.subject
        output += self.person.name
        return output
    
    def get_description(self):
        output = ""
        output += self.intro
        if self.person.model != None:
            output += "Model User: " + self.person.model + "\n"
        if self.person.role == "Sales Engineer":
            output += "\nAllow Forecasting: Yes\n"
        output += self.basic
        output += self.permissions
        output += self.configit
        output += self.queues
        
        return output
        
"""
planilha = "C:\\Users\\U429604\\OneDrive - Danfoss\\Desktop\\Python\\NewUser\\UserPermissions.xlsx"
pagina = 'Sheet1'
df = pd.read_excel(planilha, sheet_name=pagina)

notepad = "C:\\Users\\U429604\\OneDrive - Danfoss\\Desktop\\Python\\NewUser\\Output.txt"
"""
"""
Col A -> index 1
Row 2 -> index 0

test = Person("Fulano Ciclano da Silva", "Fulano@gmail.com", "9876543210", None, "Internal Sales", "CRM - Fulano", "Brasil", "Carluxo")
writing_test = Write(test, df)
writing_test.populate()

with open(notepad, 'w') as file:
    file.write('')

with open(notepad, "a") as file:
    file.write(writing_test.get_subject())
    file.write("\n\n\n")
    file.write(writing_test.get_description())
"""
            
