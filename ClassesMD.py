from ast import Continue
import xml.etree.ElementTree as ET
import os
import shutil
from tkinter import *
from tkinter import ttk, messagebox

global ModuleCollection




class ModuleMD (object):
    def __init__ (self):
        self.ModuleName = "DefaultModule"
        self.VendorName = "MARELLI"
        self.ModuleDescription = "Generic Module"
        self.SipVersion = ""
        self.SipPath = ""
        self.xmlFile = ""
        self.root_ARXML =""
        self.LowMultiplicity = 0
        self.UppMultiplicity = 0
        self.NumContainers = 0
        self.dict_Containers = {}
    
    def SetModule (self, ModuleName, VendorName, ModuleDescription, SipVersion, SipPath, LowMultiplicity = 0, UppMultiplicity = 0, NumContainers = 0):
        self.ModuleName = ModuleName
        self.VendorName = VendorName
        self.ModuleDescription = ModuleDescription
        self.SipVersion = SipVersion        
        self.SipPath = SipPath
        self.Set_ModulePath()
        self.LowMultiplicity = str (LowMultiplicity)
        self.UppMultiplicity = str (UppMultiplicity)
        
        try:
            self.NumContainers = str(len (self.dict_Containers.keys()))

        except:
             self.NumContainers = str(0)
        
        
    def GetModule (self):
        dict_Module = {}
        dict_Module ["Module"] = self.ModuleName
        dict_Module ["Vendor"] = self.VendorName
        dict_Module ["Description"] = self.ModuleDescription
        dict_Module ["SipVersion"] = self.SipVersion
        dict_Module ["SipPath"] = self.SipPath
        dict_Module ["ARXML Path"] = self.xmlFile
        dict_Module ["LowMult"] = self.LowMultiplicity
        dict_Module ["UppMult"] = self.UppMultiplicity
        dict_Module ["NumContainers"] = len(self.dict_Containers)
        dict_Module ["DictionaryContainers"] = self.dict_Containers
        return dict_Module
    
    def SetFileXml (self, file):
        self.xmlFile = file
        self.GetPath_VersionSip()
    
    def GetPath_VersionSip (self):
        file = os.path.split(self.xmlFile)
        BMSMD_Dir = os.path.split(file[0])
        Module_Dir = os.path.split(BMSMD_Dir[0])
        Components_Dir = os.path.split(Module_Dir[0])
        SipPath = os.path.split(Components_Dir[0])
        self.SipPath = Components_Dir[0]
        self.SipVersion = SipPath[1]
    
    def printModule (self):
        print ("Module Name: " + self.ModuleName + "\n")
        print ("Vendor: " + self.VendorName + "\n")
        print ("Description: " + self.ModuleDescription + "\n")
        print ("Sip Version: " + self.SipVersion + "\n")
        print ("Sip Path: " + self.SipPath + "\n")
        print ("Low Multiplicity: " + str(self.LowMultiplicity) + "\n")
        print ("Upper Multiplicity: " + str(self.UppMultiplicity) + "\n")
        print ("Number Containers: " + str(self.NumContainers) + "\n")

        for each_container in self.dict_Containers.values():
            each_container.PrintContainer()
            
    #Create the Module inside the SIP
    def CreateModule_Sip (self, TreeView):
        
        returnVal = "MS_NOT_OK"
        #Check if the path of the SIP exists
        if not self.CheckSipPath():
            messagebox.showinfo(message="Error Path or SIP not exist")
            return returnVal
        
        #Check if the Module exist
        if self.FindModule_Sip():
            messagebox.showinfo(message="The File Arxml is already exist")
            return returnVal
        
        #Create the file in case the the SIP exists and the ARXML does not exist
        if (self.CheckSipPath()) and not (self.FindModule_Sip()):
            
            try:
              TreeView.insert('', 'end', self.ModuleName, text=self.ModuleName, values = (None, self)) 

            except:
                messagebox.showinfo(message='The Module is already exist') 
                return returnVal  
                        
            #Create Directory of the Module Inside the SIP
            PathModule = os.path.join(self.SipPath, "Components", self.ModuleName)
            os.mkdir(PathModule)
            #Create Directory BSWMD inside the Module
            PathModule = os.path.join(PathModule, "BSWMD")
            os.mkdir(PathModule)
            #Create the file ARXML inside BSWMD 
            PathModule = os.path.join(PathModule, self.ModuleName + "_bswmd.arxml")
            #PathModule = PathModule + "\\" + InModuleName + "_bswmd.arxml"
            fp = open(PathModule, 'x')
            fp.close()   
            
            self.xmlFile = PathModule
            
            self.CreateFirstBSWMD()
            
            
            returnVal = "MS_OK"
            return returnVal
        
        #Generic Error
        return returnVal

    def DeleteModule_Sip (self):
        
        #Check if the path of the SIP exists
        if not self.CheckSipPath():
            return "Error Path or SIP not exist"
        
        else:
            #Create Directory of the Module Inside the SIP
            PathModule = os.path.join(self.SipPath, "Components", self.ModuleName)
            try:
                shutil.rmtree(PathModule)
                print ("Module has been deleted inside the Sip")
            except:
                print("Module Not exist inside the Sip")
        
    def Set_ModulePath (self):
        self.xmlFile = os.path.join(self.SipPath, "Components", self.ModuleName, "BSWMD", self.ModuleName + "_bswmd.arxml")
    
    def CheckSipPath (self):
        CheckDirectory = os.path.exists(self.SipPath)
        return CheckDirectory
    
    #Check if the Module Exist inside the SIP
    def FindModule_Sip (self):
        
        PathModule = os.path.join(self.SipPath, "Components", self.ModuleName, "BSWMD", self.ModuleName + "_bswmd.arxml")
        CheckDirectory = os.path.exists(PathModule)    
        return CheckDirectory

    def removeNamespace(self, doc, namespace):
        #print("Removes XML namespace in place."
        #print (namespace)
        ns = namespace
        #print (ns)
        nsl = len(ns)
        for elem in doc.iter():
            if elem.tag.startswith(ns):
                elem.tag = elem.tag[nsl:]

    def parseXMLFile(self,namespace=None):
        arxml_tree = ET.ElementTree()
        arxml_tree.parse(self.xmlFile)
        arxml_root = arxml_tree.getroot()
        if namespace is not None:
            self.removeNamespace(arxml_root, namespace)
        return arxml_root
    
    def SetRootArxml (self):
        self.root_ARXML = self.parseXMLFile("{http://autosar.org/schema/r4.0}")
       
    def GetRootArxml (self):
        return self.root_ARXML
    
    #Create Structure ARXML
    def CreateFirstBSWMD (self, Modify = 0):
        self.CreateArxmlStructure (Modify)
        # Write the file(self, xmlFile, ModuleName, VendorName, ModuleDescription)
        myfile = open(self.xmlFile, "w")
        myfile.write('<?xml version="1.0" encoding="UTF-8"?>\n')   
        myfile.write(self.root_ARXML)   
        myfile.close()

    # create the file structure
    def CreateArxmlStructure (self, Modify = 0):
        print("------------------------------------")
        self.printModule()
        #Root Autosar
        root_arxml_AUTOSAR = ET.Element('AUTOSAR')
        root_arxml_AUTOSAR.set ('xsi:schemaLocation', 'http://autosar.org/schema/r4.0 AUTOSAR_4-0-3.xsd')
        root_arxml_AUTOSAR.set ('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
        root_arxml_AUTOSAR.set ('xmlns', "http://autosar.org/schema/r4.0")
        
        #Branch AR-PACKAGES
        arxml_PACKAGES = ET.Element('AR-PACKAGES')
        root_arxml_AUTOSAR.append (arxml_PACKAGES)
        
        #Branch AR-PACKAGE with Vendor's Name
        arxml_PACKAGE = ET.Element('AR-PACKAGE')
        arxml_PACKAGE_NAME = ET.SubElement (arxml_PACKAGE,'SHORT-NAME')
        arxml_PACKAGE_NAME.text = self.VendorName
        arxml_PACKAGES.append (arxml_PACKAGE)
        
        #Branch ELEMENTS      
        arxml_ELEMENTS = ET.Element('ELEMENTS')
        arxml_PACKAGE.append (arxml_ELEMENTS)
        
        #Branch Definition of ECUC Module
        arxml_ECUC_MODULE = ET.Element('ECUC-MODULE-DEF')
        ECUC_MODULE_NAME = ET.SubElement (arxml_ECUC_MODULE,'SHORT-NAME')
        ECUC_MODULE_NAME.text = self.ModuleName
        arxml_ELEMENTS.append (arxml_ECUC_MODULE)
        
        ECUC_MODULE_DESC = ET.Element('DESC')
        ECUC_MODULE_DESC_TEXT = ET.SubElement (ECUC_MODULE_DESC,'L-2')
        ECUC_MODULE_DESC_TEXT.set ("L", "EN")
        ECUC_MODULE_DESC_TEXT.text = self.ModuleDescription
        arxml_ECUC_MODULE.append (ECUC_MODULE_DESC)

        ECUC_LOW_MULT = ET.SubElement (arxml_ECUC_MODULE,'LOWER-MULTIPLICITY')
        ECUC_LOW_MULT.text = self.LowMultiplicity
        ECUC_UPP_MULT = ET.SubElement (arxml_ECUC_MODULE,'UPPER-MULTIPLICITY')
        ECUC_UPP_MULT.text = self.UppMultiplicity
        
        #Containers
        if int(self.NumContainers) == 0:
            self.NumContainers = str(len(self.dict_Containers.keys()))

        if int (self.NumContainers) > 0 or len(self.dict_Containers.keys()):
            
            CONTAINER_ROOT = ET.SubElement (arxml_ECUC_MODULE, 'CONTAINERS')

            if (Modify == 0):
                for each_container in range (0, self.NumContainers):
                    objContainer = ContainerMD ()
                    objContainer.Menu2CreateContainer (NumContainer = str(each_container))
                    objContainer.SetContainer (self, CONTAINER_ROOT)
            else:
                for each_container in self.dict_Containers.values():
                    each_container.SetContainer (self, CONTAINER_ROOT)      
                              
        # create a new XML
        ET.indent(root_arxml_AUTOSAR, '	')
        self.root_ARXML = ET.tostring(root_arxml_AUTOSAR)
        self.root_ARXML = self.root_ARXML.decode('utf-8')
        
    def ReadArxmlStructure (self):

        self.SetRootArxml()
        root = self.GetRootArxml()
        ArPackages = root.find ('AR-PACKAGES')
        ArPackage = ArPackages.find ('AR-PACKAGE')
        self.VendorName = ArPackage.find ('SHORT-NAME').text
        
        Elements = ArPackage.find ('ELEMENTS')
        EcuCModuleDef = Elements.find ('ECUC-MODULE-DEF')
        self.ModuleName = EcuCModuleDef.find ('SHORT-NAME').text
        self.ModuleDescription = ((EcuCModuleDef.find('DESC')).find ('L-2')).text
        self.LowMultiplicity = EcuCModuleDef.find ('LOWER-MULTIPLICITY').text
        self.UppMultiplicity = EcuCModuleDef.find ('UPPER-MULTIPLICITY').text
        
        ContainerRoot = EcuCModuleDef.find ('CONTAINERS')
        
        try:
            for each_container in ContainerRoot:
                print (each_container)
                Container_obj = ContainerMD ()
                Container_obj.GetContainer (self, each_container)
                self.dict_Containers[Container_obj.Name] = Container_obj
                self.NumContainers = self.NumContainers + 1
        except:
            pass

    def ModifyArxmlStructure (self):
        
        #self.ReadArxmlStructure()
        
        #Modify Containers
        #self.Menu2CreateOrModOrDelContainer()
        self.printModule()
        self.CreateFirstBSWMD(Modify = 1)
        print ("Container has been modified")
            
    def Menu2CreateOrModOrDelContainer (self):
        
        while (1):
            print("---------------------------------------------")
            print ("---------------Modifying Module--------------")
            print("---------------------------------------------")
            print("1. Create a container ")
            print("2. Modify a container ")
            print("3. Delete a container ")
            print("4. Print a container")
            print("5. Save and Exit ")
            print("---------------------------------------------")
            Option = int(input("Choose an option: "))

            print("\n")
            print ("------------- Modifying Container ------------")
            print ()
            #Create Container
            if Option == 1:
                ContainerName = input("Write the Name of the New Container: ")
                if ContainerName in self.dict_Containers.keys():
                    print ("The Container is alredy exist")
                else:
                    New_Container = ContainerMD()
                    New_Container.Menu2CreateContainer(NameContainer = ContainerName)
                    self.NumContainers = int (self.NumContainers) + 1
                    self.dict_Containers[New_Container.Name] = New_Container
            #Modify Container
            elif Option == 2:
                if len (self.dict_Containers) == 0:
                    print ("Not exist any container to be modified")
                else:
                    print ()
                    ContainerName = input("Write the Name of the Container to be modified: ")
                    if not ContainerName in self.dict_Containers.keys():
                        print ("The Container is not exist")
                    else:
                        New_Container = self.dict_Containers[ContainerName]
                        New_Container.Menu2ModifyContainer()
                        del self.dict_Containers[ContainerName]
                        self.dict_Containers[New_Container.Name] = New_Container
            
            #Delete Container
            elif Option == 3:

                if len (self.dict_Containers) == 0:
                    print ("Not exist any container to be removed")
                else:
                    print ("Write the Name of the Container to be removed: ")
                    ContainerName = input()
                    if not ContainerName in self.dict_Containers.keys():
                        print ("The Container is not exist")
                    else:
                        del self.dict_Containers[ContainerName]

            elif Option == 4:
                
                if len (self.dict_Containers) == 0:
                    print ("Not exist any container to be printed")
                else:
                    print ("Write the Name of the Container to be printed: ")
                    ContainerName = input()
                    if not ContainerName in self.dict_Containers.keys():
                        print ("The Container is not exist")
                    else:
                        self.dict_Containers[ContainerName].PrintContainer()
            
            elif Option ==5:
                break

    def AddContainer (self, ContainerObj):
        self.dict_Containers[ContainerObj.Name] = ContainerObj
        self.NumContainers = str(len (self.dict_Containers.keys()))

    def DelContainer (self, ContainerObj):
        del self.dict_Containers[ContainerObj.Name] 
        self.NumContainers = str(len (self.dict_Containers.keys()))
        

class ContainerMD (object):
   
    def __init__ (self):
        self.ModuleObj = "Deafault Module"
        self.Name = ""
        self.Description = "Description"
        self.minMultiplicity = 0
        self.maxMultiplicity = 0
        self.dict_Parameters = {}
        self.NumParameters = 0
        self.dict_subcontainers = {}
        self.NumSubContainer = 0
        self.dict_reference = {}
        self.NumReference = 0
    
    def InitContainer (self, Module, ContainerName, ContainerDescription, LowMultiplicity = 0, UppMultiplicity = 0):
        self.ModuleObj = Module
        self.Name = ContainerName
        self.Description = ContainerDescription
        self.minMultiplicity = LowMultiplicity
        self.maxMultiplicity = UppMultiplicity
        
    def SetContainer (self, Module, ContainerElement, index = None):            
        
        self.ModuleObj = Module
        
        ContainerConfig = ET.Element ("ECUC-PARAM-CONF-CONTAINER-DEF")
        if index == None:
            ContainerElement.append(ContainerConfig)
        else:
            ContainerElement.insert(index, ContainerConfig)
            
        ContainerName = ET.SubElement (ContainerConfig, "SHORT-NAME")
        ContainerName.text = self.Name
    
        ContainerDescription = ET.Element ("DESC")
        DescriptionText = ET.SubElement (ContainerDescription, "L-2")
        DescriptionText.set ("L", "EN")
        DescriptionText.text = self.Description
        ContainerConfig.append (ContainerDescription)
    
        ContainerLowerMult = ET.SubElement (ContainerConfig, "LOWER-MULTIPLICITY")
        ContainerLowerMult.text = str(self.minMultiplicity) 

        ContainerMaxMult = ET.SubElement (ContainerConfig, "UPPER-MULTIPLICITY")
        ContainerMaxMult.text = str(self.maxMultiplicity)     

        if len(self.dict_Parameters) > 0:
            ContainerParameters = ET.SubElement (ContainerConfig, "PARAMETERS")
            for each_parameter in self.dict_Parameters.values():
                each_parameter.SetParameter (ContainerParameters)
 
        if len(self.dict_reference) > 0:
            ContainerReference = ET.SubElement (ContainerConfig, "REFERENCES")
            for each_reference in self.dict_reference.values():
                each_reference.Set_ReferenceXml (ContainerReference)
 
 
        if len(self.dict_subcontainers) > 0:
            ContainerSubContainers = ET.SubElement (ContainerConfig, "SUB-CONTAINERS")
            print(self.dict_subcontainers)
            print (self.dict_subcontainers)
            for each_subcontainer in (self.dict_subcontainers.values()):
                each_subcontainer.ObjContainer.SetContainer (Module, ContainerSubContainers)                
        
        
        
        ET.indent(ContainerElement, '	')
             
    def GetContainer (self, ModuleObj, ContainerConfig):
        
        #ET.dump (ContainerElement)
        #ContainerConfig = ContainerElement.find ('ECUC-PARAM-CONF-CONTAINER-DEF')
        
        self.ModuleObj = ModuleObj
        
        #Name
        ContainerName = ContainerConfig.find ("SHORT-NAME")
        self.Name = ContainerName.text

        #Description
        ContainerDescription = ContainerConfig.find ("DESC")
        DescriptionText = ContainerDescription.find ("L-2")
        self.Description = DescriptionText.text

        #Lower Mult
        ContainerLowerMult = ContainerConfig.find ("LOWER-MULTIPLICITY")
        self.minMultiplicity = ContainerLowerMult.text
   
        #Upper Mult
        ContainerLowerMult = ContainerConfig.find ("UPPER-MULTIPLICITY")
        self.maxMultiplicity  = ContainerLowerMult.text
        
        #Parameters
        
        ContainerParameters = ContainerConfig.find ("PARAMETERS")
        try:
            for each_Parameter in ContainerParameters:
                Parameter_obj = ParameterMD()
                Parameter_obj.Get_ParameterFromXml (each_Parameter)
                self.dict_Parameters [Parameter_obj.Name] = Parameter_obj
        except:
            pass
        
        
        #References

        ContainerReferences = ContainerConfig.find ("REFERENCES")
        try:
            for each_reference in ContainerReferences:
                Reference_obj = ReferencesMD()
                Reference_obj.Get_ReferenceFromXml (each_reference)
                self.dict_reference [Reference_obj.Name] = Reference_obj
        except:
            pass
        
        #Subcontainers
        
        ContainerSubContainer = ContainerConfig.find("SUB-CONTAINERS")
        #print (self.Name)
        try:
            for each_Subcontainer in ContainerSubContainer:
                Subcontainer_obj = SubContainerMD()
                Subcontainer_obj.ObjContainer.GetContainer (ModuleObj, each_Subcontainer)
                self.dict_subcontainers [Subcontainer_obj.ObjContainer.Name] = Subcontainer_obj
        except Exception as error:
            print (error)
            print (self.Name)
    
    def PrintContainer (self, space = 0):
        print ((space* "   ") + "Module Name: " + self.ModuleObj.ModuleName)
        print ((space* "   ") + "Container Name: " + self.Name)
        print ((space* "   ") + "Container Description: " + self.Description)
        print ((space* "   ") + "Container Lower Multiplicity: " + str(self.minMultiplicity))
        print ((space* "   ") + "Container Lower Multiplicity: " + str(self.maxMultiplicity))
        print ((space* "   ") + "----------Parameters----------")
        print ((space* "   ") + "Number of parameters: " + str(self.NumParameters))
        print ((space* "   ") + "Parameters: ")
        for each_parameter in self.dict_Parameters.values():
            print ((space* "   ") + "----------------Parameter-----------------")
            each_parameter.PrintParameter(space)
        
        print ((space* "   ") + "Number of Subcontainers: " + str(self.NumSubContainer))
        space = space + 3
        for each_subcontainer in self.dict_subcontainers.values():
            print ((space* "   ") + "-------------Subcontainer-------------")
            each_subcontainer.PrintSubcontainer(space)
              
    def find_Container (self, NameContainer, ContainerElement):
        index = 0
        for each_container in ContainerElement.findall('ECUC-PARAM-CONF-CONTAINER-DEF'):
            if each_container.find ("SHORT-NAME").text == NameContainer:
                return [each_container, index]
            index = index + 1
        return None
    
    def Remove_Container (self, NameContainer, ContainerElement):

        for each_container in ContainerElement.findall('ECUC-PARAM-CONF-CONTAINER-DEF'):
            if each_container.find ("SHORT-NAME").text == NameContainer:
                ContainerElement.remove (each_container)
        
        return None
  
    def Menu2CreateContainer(self, NameContainer = "", NumContainer = ""):
        
        print ("\n------------------- Creating Container ----------------------")
        
        #Name
        if NameContainer == "":
            print ("")
            NameContainer = input ("Write the name of the Container" + NumContainer + ": ") 
        self.Name = NameContainer
        
        #Description
        print()
        self.Description = input ("Write the description of the Container" + NumContainer + ": ") 
        
        #Lower Multiplicity
        print()
        self.minMultiplicity = input ("Write the lower multiplicity of the Container" + NumContainer + ": ") 
        
        #Upper Multiplicity
        print()
        self.maxMultiplicity = input ("Write the upper multiplicity of the Container" + NumContainer + ": ") 

        #Parameters
        print()
        self.NumParameters = int (input("Write the number of parameters to be defined in the Container" + NumContainer + ": "))

        #Subcontainers
        print ()
        self.NumSubContainer = int (input("Write the number of subcontainers to be defined in the Container" + NumContainer + ": "))
        
        #Parameters
        for each_parameter in range (0, self.NumParameters):
            parameter_obj = ParameterMD()
            parameter_obj.Menu2CreateParameter(NumParameter2Defined = str(each_parameter))
            self.dict_Parameters [parameter_obj.Name] = parameter_obj

        #Subcontainers
        if self.NumSubContainer > 0:
            for each_subcontainer in range (0, self.NumSubContainer):
                SubContainer_obj = SubContainerMD()
                SubContainer_obj.Menu2CreateSubContainer(str(each_subcontainer))
                self.dict_subcontainers [SubContainer_obj.ObjContainer.Name] = SubContainer_obj

    def Menu2ModifyContainer(self):                   
        print ("Container: " + self.Name)
        while (1):
            print ("------------------------------------------")
            print ("-------- Menu to modify Container --------")
            print ("1. Change the Name")
            print ("2. Change the Description")
            print ("3. Change the Lower Mult")
            print ("4. Change the Upper Mult")
            print ("5. Add, Modify or Remove parameters")
            print ("6. Add, Modify or Remove Subcontainer")
            print ("7. Back to principal Menu")
            print ("------------------------------------------")
            choose_modify = int(input ("Choose one option: "))
            print("\n")
            if choose_modify == 1:
                self.Name = input ("Write the new name: ")
            elif choose_modify == 2:
                self.Description = input ("Write the new description: ")
            elif choose_modify == 3:               
                self.minMultiplicity = str(input ("Define the new lower multiplicity: "))
            elif choose_modify == 4: 
                self.maxMultiplicity = str(input ("Define the new upper multiplicity: "))
            elif choose_modify == 5:
                while (1):
                    print ("\n---------------------------------------------------")
                    print ("-------------- Modifying Parameter ----------------")
                    print ("---------------------------------------------------")
                    print ("Container: " + self.Name)
                    print ("\n")
                    print ("1. Add parameter")
                    print ("2. Modify paramenter")
                    print ("3. Remove parameter") 
                    print ("4. Exit ")
                    print ("---------------------------------------------------")
                    option = int(input("Choose one option: "))
                    if option == 1:
                        parameter_obj = ParameterMD()
                        parameter_obj.Menu2CreateParameter()
                        self.dict_Parameters [parameter_obj.Name] = parameter_obj
                    elif option == 2:
                        if len (self.dict_Parameters.keys()) == 0:
                            print ("No parameters exist to be modified")
                        else:
                            print("\n")
                            ParameterName = input("Write the name of the parameter to be modified: ")
                            if not ParameterName in self.dict_Parameters.keys():
                                print ("Parameter does not exit")
                            else:
                                parameter_obj = self.dict_Parameters [ParameterName]
                                parameter_obj.Menu2ModifyParameter()
                                print ("The parameter has been modified\n")
                    
                    elif option == 3:
                        if len (self.dict_Parameters.keys()) == 0:
                            print ("No parameters exist to be removed")
                        else:
                            print ("\nWrite the name of the parameter to be remove: ")
                            ParameterName = input()
                            if not ParameterName in self.dict_Parameters.keys():
                                print ("Parameter does not exit")
                            else:
                                del self.dict_Parameters [ParameterName]
                                print ("The parameter has been removed\n")
                    elif option == 4:
                        break
            
            elif choose_modify == 6:
                while (1):
                    print ("\n---------------------------------------------------")
                    print ("-------------- Modifying Container ----------------")
                    print ("---------------------------------------------------")
                    print ("Container: " + self.Name)
                    print ("\n")
                    print ("1. Add Subcontainer")
                    print ("2. Modify Subcontainer")
                    print ("3. Remove Subcontainer") 
                    print ("4. Exit ")
                    print ("---------------------------------------------------")
                    option = int(input("Choose one option: "))
                    if option == 1:
                        subcontainer_obj = SubContainerMD()
                        subcontainer_obj.Menu2CreateSubContainer()
                        self.dict_subcontainers[subcontainer_obj.ObjContainer.Name] = subcontainer_obj
                    
                    elif option == 2:
                        if len (self.dict_subcontainers.keys()) == 0:
                            print ("Not exist any subcontainer to be modified")
                        else:
                            print ()
                            SubcontainerName = input("Write the name of the subcontainer to be modified: ")
                            print()
                            if not SubcontainerName in self.dict_subcontainers.keys():
                                print ("Subcontainer does not exit")
                            else:
                                self.dict_subcontainers[SubcontainerName].Menu2ModifySubcontainer()               
                                print ("The Subcontainer has been modified\n")                        
                    
                    elif option == 3:
                        if len (self.dict_subcontainers.keys()) == 0:
                            print ("Not exist any subcontainer to be removed")
                        else:
                            print ()
                            SubcontainerName = input("Write the name of the subcontainer to be removed: ")
                            print ()
                            if not SubcontainerName in self.dict_subcontainers.keys():
                                print ("Subcontainer does not exit")
                            else:
                                del self.dict_subcontainers [SubcontainerName]
                                print ("The Subcontainer has been removed\n")     
                    elif option == 4:
                        break
            elif choose_modify == 7:
                break        

    def setParameterInContainer (self, ParameterName, ParameterDescription, ParameterMinMultiplicity, ParameterMaxMultiplicity, ParameterType, IndexInput, SymbolicNameInput, DefaultValueInput, MaxValue=0, MinValue=0, enum_list=[]):
        
        ParameterObj = ParameterMD ()
        ParameterObj.InitParameterValues (ParameterName, ParameterDescription, ParameterMinMultiplicity, ParameterMaxMultiplicity, ParameterType, IndexInput, SymbolicNameInput, DefaultValueInput, MaxValue, MinValue, enum_list, Container = self)
        self.dict_Parameters [ParameterName] = ParameterObj
        self.NumParameters = str (len (self.dict_Parameters))

    def delParameterInContainer (self, ParameterName):
        del self.dict_Parameters [ParameterName]
        self.NumParameters = str (len (self.dict_Parameters))

    def setSubcontainerInContainer (self, ContainerName, ContainerDescription, LowerMultiplicity, UpperMultiplicity):
        
        SubcontainerObj = SubContainerMD ()
        SubcontainerObj.ObjContainer.InitContainer (self.ModuleObj, ContainerName, ContainerDescription, LowerMultiplicity, UpperMultiplicity)
        self.dict_subcontainers [ContainerName] = SubcontainerObj
        self.NumSubContainer = str (len (self.dict_subcontainers))

    def delSubcontainerInContainer (self):
        pass
  
    def setReferenceInContainer (self, ReferenceName, ReferenceDescription, ReferenceLowMultiplicity, ReferenceUppMultiplicity, ReferenceOrigin, ReferenceDestination):
        
        ReferenceObj = ReferencesMD ()
        ReferenceObj.InitParameterValues (ReferenceName, ReferenceDescription, ReferenceLowMultiplicity, ReferenceUppMultiplicity, ReferenceOrigin, ReferenceDestination)
        self.dict_reference [ReferenceName] = ReferenceObj
        self.NumReference = str (len (self.dict_reference))

    def delReferenceInContainer (self, ReferenceName):
        del self.dict_reference [ReferenceName]
        self.NumReference = str (len (self.dict_reference))
  
    
class ParameterMD (object):
    
    def __init__ (self):
        self.ContainerObj = None
        self.Name = ""
        self.Description = ""
        self.minMultiplicity = 0
        self.maxMultiplicity = 0
        self.ParameterXML = ""
        self.Parameter = ""
        self.Index = "false"
        self.Symbolic = "false"
        self.DefaultValue = None
        self.MaxValue = None
        self.MinValue = None
        self.EnumListName = []

    def InitParameterValues (self, ParameterName, ParameterDescription, ParameterMinMultiplicity, ParameterMaxMultiplicity, ParameterType, IndexInput, SymbolicNameInput, DefaultValueInput, MaxValue, MinValue, enum_list, Container = None):
        self.ContainerObj = Container
        self.Name = ParameterName
        self.Description = ParameterDescription
        self.minMultiplicity = str(ParameterMinMultiplicity)
        self.maxMultiplicity = str(ParameterMaxMultiplicity)
        self.DefineParameters (ParameterType.upper())
        self.Index = IndexInput
        self.Symbolic = SymbolicNameInput
        self.DefaultValue = str(DefaultValueInput)
        self.MaxValue = str(MaxValue)
        self.MinValue = str(MinValue)
        self.EnumListName = enum_list        

    def DefineParameters (self, typeParameter):
        
        if typeParameter == 1 or typeParameter == "ECUC-BOOLEAN-PARAM-DEF" or typeParameter == "BOOLEAN":
            self.ParameterXML = "ECUC-BOOLEAN-PARAM-DEF"
            self.Parameter = "BOOLEAN"
        
        elif typeParameter == 2 or typeParameter == "ECUC-ENUMERATION-PARAM-DEF" or typeParameter == "ENUMERATION":
            self.ParameterXML = "ECUC-ENUMERATION-PARAM-DEF"
            self.Parameter = "ENUMERATION"
        
        elif typeParameter == 3 or typeParameter == "ECUC-INTEGER-PARAM-DEF" or typeParameter == "INTEGER":
            self.ParameterXML = "ECUC-INTEGER-PARAM-DEF"
            self.Parameter = "INTEGER"

        elif typeParameter == 4 or typeParameter == "ECUC-FLOAT-PARAM-DEF" or typeParameter == "FLOAT":
            self.ParameterXML = "ECUC-FLOAT-PARAM-DEF"
            self.Parameter = "FLOAT"

        elif typeParameter == 5 or "ECUC-STRING-PARAM-DEF" or typeParameter == "STRING":
            self.ParameterXML = "ECUC-STRING-PARAM-DEF"
            self.Parameter = "STRING"
        
        elif typeParameter == 6 or "ECUC-FUNCTION-NAME-DEF" or typeParameter == "FUNCTION":
            self.ParameterXML = "ECUC-FUNCTION-NAME-DEF"
            self.Parameter = "FUNCTION"
   
    def ReturnTypeParameter (self, typeParameter):
        if typeParameter == 1 or typeParameter == "ECUC-BOOLEAN-PARAM-DEF":
            return "BOOLEAN"
        
        elif typeParameter == 2 or typeParameter == "ECUC-ENUMERATION-PARAM-DEF":
            return "ENUMERATION"
        
        elif typeParameter == 3 or typeParameter == "ECUC-INTEGER-PARAM-DEF":
            return "INTEGER"

        elif typeParameter == 4 or typeParameter == "ECUC-FLOAT-PARAM-DEF":
            return "FLOAT"

        elif typeParameter == 5 or "ECUC-STRING-PARAM-DEF":
            return "STRING"
        
        elif typeParameter == 6 or "ECUC-FUNCTION-NAME-DEF":
            return "FUNCTION"        
            
    def SetParameter (self, ParameterElement):
        ParameterConfig = ET.Element (self.ParameterXML)      
        
        ParameterElement.append (ParameterConfig)
        
        ParameterName = ET.SubElement (ParameterConfig, "SHORT-NAME")
        ParameterName.text = self.Name
    
        ParameterDescription = ET.Element ("DESC")
        DescriptionText = ET.SubElement (ParameterDescription, "L-2")
        DescriptionText.set ("L", "EN")
        DescriptionText.text = self.Description
        ParameterConfig.append (ParameterDescription)

        
        ParameterLowerMult = ET.SubElement (ParameterConfig, "LOWER-MULTIPLICITY")
        ParameterLowerMult.text = self.minMultiplicity       

        ParameterMaxMult = ET.SubElement (ParameterConfig, "UPPER-MULTIPLICITY")
        ParameterMaxMult.text = self.maxMultiplicity  
   
        ParameterReqIndex = ET.SubElement (ParameterConfig, "REQUIRES-INDEX")
        ParameterReqIndex.text = self.Index
        
        ParameterSymbolic = ET.SubElement (ParameterConfig, "SYMBOLIC-NAME-VALUE")
        ParameterSymbolic.text = self.Symbolic

        if self.Parameter == "INTEGER" or self.Parameter == "FLOAT" or self.Parameter == "BOOLEAN":
            ParameterDefaultValue = ET.SubElement (ParameterConfig, "DEFAULT-VALUE")
            ParameterDefaultValue.text = self.DefaultValue
        
        if self.Parameter == "INTEGER" or self.Parameter == "FLOAT":
            ParameterMaxValue = ET.SubElement (ParameterConfig, "MAX")
            ParameterMaxValue.text = self.MaxValue
            
            ParameterMinValue = ET.SubElement (ParameterConfig, "MIN")
            ParameterMinValue.text = self.MinValue
        
        if self.Parameter == "ENUMERATION":
            ParameterLiterals = ET.Element ("LITERALS")
            ParameterConfig.append (ParameterLiterals)
            
            for each_enum in self.EnumListName:
                ParameterEnum = ET.Element("ECUC-ENUMERATION-LITERAL-DEF")
                ParameterLiterals.append (ParameterEnum)
                EnumName = ET.SubElement (ParameterEnum, "SHORT-NAME")
                EnumName.text = each_enum
                EnumName = ET.SubElement (ParameterEnum, "ORIGIN")
                EnumName.text = "Marelli"               
            
        ET.indent(ParameterElement, '	')
    
    def Dict_Parameters (self, ParametersConfig):
        dict_parameters = {}

        for each_parameter in ParametersConfig:
            print (each_parameter)
            self.DefineParameters(each_parameter.tag)
            self.Get_ParameterFromXml (each_parameter)
            dict_parameters [self.Name] = self
        return dict_parameters
    
    def Get_ParameterFromXml (self, ParameterConfig):
        
        #ET.dump (ContainerElement)
        #ContainerConfig = ContainerElement.find ('ECUC-PARAM-CONF-CONTAINER-DEF')
        
        #Type Parameter
        #ET.dump (ParameterConfig)
        self.DefineParameters (ParameterConfig.tag)
        #Name
        ParameterName = ParameterConfig.find ("SHORT-NAME")
        self.Name = ParameterName.text

        #Description
        ParameterDescription = ParameterConfig.find ("DESC")
        DescriptionText = ParameterDescription.find ("L-2")
        self.Description = DescriptionText.text

        #Lower Mult
        ParameterLowerMult = ParameterConfig.find ("LOWER-MULTIPLICITY")
        self.minMultiplicity = ParameterLowerMult.text
   
        #Upper Mult
        ParameterUpperMult = ParameterConfig.find ("UPPER-MULTIPLICITY")
        self.maxMultiplicity = ParameterUpperMult.text
        
        #Requiere Index
        ParameterReqIndex = ParameterConfig.find ("REQUIRES-INDEX")
        self.Index = ParameterReqIndex.text
        
        #Symbolic
        ParameterSymbolic = ParameterConfig.find ("SYMBOLIC-NAME-VALUE")
        self.Symbolic = ParameterSymbolic.text
        
        ###################################################################################
        
        if self.Parameter == "INTEGER" or self.Parameter == "FLOAT" or self.Parameter == "BOOLEAN":
            self.DefaultValue = (ParameterConfig.find ("DEFAULT-VALUE")).text
            
        if self.Parameter == "INTEGER" or self.Parameter == "FLOAT":
            self.MaxValue = (ParameterConfig.find ("MAX")).text
            self.MinValue = (ParameterConfig.find ("MIN")).text

        if self.Parameter == "ENUMERATION":
 
            ParameterLiterals = ParameterConfig.find ("LITERALS")
            
            self.EnumListName = []
            for each_element in ParameterLiterals.findall ("ECUC-ENUMERATION-LITERAL-DEF"):
                NameEnum = each_element.find ("SHORT-NAME")
                self.EnumListName.append (NameEnum.text)

    def PrintParameter (self, space = 0):
        print ((space* "   ") + "Name Parameter: "+ self.Name)
        print ((space* "   ") + "Description Parameter: " + self.Description)
        print ((space* "   ") + "Lower Multiplicity : " + str(self.minMultiplicity))
        print ((space* "   ") + "Upper Multiplicity : " + str(self.maxMultiplicity))
        print ((space* "   ") + "Type Parameter: " + self.Parameter)
        print ((space* "   ") + "Index Parameter Requiered: " + self.Index)
        print ((space* "   ") + "Index Symbolic Name Requiered: " + self.Symbolic)
        
        if self.Parameter == "INTEGER" or self.Parameter == "FLOAT" or self.Parameter == "BOOLEAN":
            print ((space* "   ") + "Default Value: " + self.DefaultValue)
        if self.Parameter == "INTEGER" or self.Parameter == "FLOAT": 
            print ((space* "   ") + "Max Value: " + self.MaxValue)
            print ((space* "   ") + "Min Value: " + self.MinValue)   
        
        if self.Parameter == "ENUMERATION":
            print ((space* "   ") + "Enum List: ")
            for each_Enum in self.EnumListName:
                print ((space* "   ") + each_Enum)

    def Menu2CreateParameter (self, NumParameter2Defined = ""):
        print ("\n")
        print ("------------ Defining Parameters -----------------")
        print ("Parameter #: " + NumParameter2Defined)
        print ("Types of parameters")
        print ("1)Bool \n2)Enum \n3)Integer \n4)Float \n5)String \n6)Function\n")

        type_parameter_obj = int(input("Choose one type: "))
        self.DefineParameters (type_parameter_obj)
        
        print ("Type Parameter: ", self.Parameter)
        
        #Name
        self.Name = input ("Write the Name of the Parameter: ") 
        #Description
        self.Description = input ("Write the description of the parameter: ")
        #Lower Multiplicity
        self.minMultiplicity = str(input ("define the lower multiplicity: "))
        #Upper Multiplicity
        self.maxMultiplicity = str(input ("define the upper multiplicity: "))
        #Index
        self.Index = input ("Define true or false if Index is requiered: ")
        #Symbolic
        self.Symbolic = input ("Define true or false if Symbolic name is requiered: ")
                     
        #Parameters according to the type
        if self.Parameter == "BOOLEAN":
            self.DefaultValue = input ("Define the default value of the boolean parameter: ")
            self.MaxValue = None
            self.MinValue = None
            self.EnumListName = None
            
        elif self.Parameter == "INTEGER" or self.Parameter == "FLOAT":
            self.DefaultValue = input ("Define the default value of the integer parameter: ")       
            self.MinValue = input ("Define the min value: ")      
            self.MaxValue = input ("Define the max value: ")
            self.EnumListName = None
                          
        elif self.Parameter == "ENUMERATION":
            self.DefaultValue = None
            self.MaxValue = None
            self.MinValue = None
            enum_num = int(input("How many elements to be add: "))
            for each_enum in range (0, enum_num):
                print("")
                print ("List of elements: ")
                enum_name = input("Write the name of the element " + str (each_enum) + ":")
                self.EnumListName.append (enum_name)
        else:
            self.DefaultValue = None
            self.MaxValue = None
            self.MinValue = None
            self.EnumListName = None

        print ("------ Parameter has been Created----------")
        print ()
        
    def Menu2ModifyParameter (self):
        
         while (1):
            print()
            print ("--------------Modifying Paramater---------------------")
            print ("1. Change the Name")
            print ("2. Change the Description")
            print ("3. Change the Lower Mult")
            print ("4. Change the Upper Mult")
            print ("5. Change the Index requiered")
            print ("6. Change the Symbolic requiered")
            print ("7. Change the type")
            print ("8. Back to principal Menu")
            print ("------------------------------------------------------")
            choose_modify = int(input ("Choose one option: "))
            print ()  
            if choose_modify == 1:
                self.Name = input ("Write the new name: ")
            elif choose_modify == 2:
                self.Description = input ("Write the new description: ")
            elif choose_modify == 3:               
                self.minMultiplicity = str(input ("Define the new lower multiplicity: "))
            elif choose_modify == 4: 
                self.maxMultiplicity = str(input ("Define the new upper multiplicity: "))         
            elif choose_modify == 5:
                self.Index = str(input ("Define true or false if the new Index is requiered: "))                           
            elif choose_modify == 6:
                self.Symbolic = str(input ("Define true or false if the new Symbolic name is requiered: "))          
            elif choose_modify == 7:
                print ("Choose the new parameter type:")
                print ("1)Bool \n2)Enum \n3)Integer \n4)Float \n5)String \n6)Function\n")
                patameterType = int(input("Choose one type: "))
                patameterType = self.ReturnTypeParameter (patameterType)
                
                if patameterType == self.Parameter:
                    print ("The new parameter type is the same to previous parameter type")
 
                else:
                    self.DefineParameters (patameterType)
                    #Parameters according to Parameter Type

                    if self.Parameter == "BOOLEAN":
                        self.DefaultValue = input ("Define the default value of the boolean parameter: ")
                        self.MaxValue = None
                        self.MinValue = None
                        self.EnumListName = None
            
                    elif self.Parameter == "INTEGER" or self.Parameter == "FLOAT":
                        self.DefaultValue = input ("Define the default value of the integer parameter: ")       
                        self.MinValue = input ("Define the min value: ")      
                        self.MaxValue = input ("Define the max value: ")
                        self.EnumListName = None
                                    
                    elif self.Parameter == "ENUMERATION":
                        self.DefaultValue = None
                        self.MaxValue = None
                        self.MinValue = None
                        enum_num = int(input("How many elements to be add: "))
                        for each_enum in range (0, enum_num):
                            print("")
                            print ("List of elements: ")
                            enum_name = input("Write the name of the element " + str (each_enum) + ":")
                            self.EnumListName.append (enum_name)
                    else:
                        self.DefaultValue = None
                        self.MaxValue = None
                        self.MinValue = None
                        self.EnumListName = None                
            
            elif choose_modify == 8:
                return 
            
class SubContainerMD (object):
    def __init__ (self):
        self.ObjContainer = ContainerMD ()
        
    def PrintSubcontainer (self, space = 0):
        print ((space* "   ") + "Subcontainer Name: " + self.ObjContainer.Name)
        print ((space* "   ") + "Subcontainer Description: " + self.ObjContainer.Description)
        print ((space* "   ") + "Subcontainer Lower Multiplicity: " + str(self.ObjContainer.minMultiplicity))
        print ((space* "   ") + "Subcontainer Lower Multiplicity: " + str(self.ObjContainer.maxMultiplicity))
        print ((space* "   ") + "Number of parameters: " + str(self.ObjContainer.NumParameters))
        print ((space* "   ") + "Parameters: ")
        for each_parameter in self.ObjContainer.dict_Parameters.values():
            
            each_parameter.PrintParameter()
        
        print ((space* "   ") + "Number of Subcontainers: " + str(len(self.ObjContainer.dict_subcontainers)))
        space = space + 3
        for each_subcontainer in self.ObjContainer.dict_subcontainers.values():
            each_subcontainer.PrintSubcontainer(space)
              
               
    def Menu2CreateSubContainer(self, NumSubContainer = ""):

        print ("\n")
        print ("------------ Defining SubContainer -----------------")
        if NumSubContainer != "":
            print ("Subcontainer #: " + NumSubContainer)
        print ("")
        #Name
        self.ObjContainer.Name = input ("Write the name of the subcontainer: ") 
        #Description
        self.ObjContainer.Description = input ("Write the description of the subcontainer: ")
        #Lower Multiplicity
        self.ObjContainer.minMultiplicity = str(input ("Define the lower multiplicity: "))
        #Upper Multiplicity
        self.ObjContainer.maxMultiplicity = str(input ("Define the upper multiplicity: "))

        #Number of Parameters
        self.ObjContainer.NumParameters = int (input("Write the number of parameters to be defined: "))

        #Number of Subcontainers
        self.ObjContainer.NumSubContainer = int (input("Write the number of subcontainers to be defined: "))
        
        #Parameters
        for each_parameter in range (0, self.ObjContainer.NumParameters):
            parameter_obj = ParameterMD()
            parameter_obj.Menu2CreateParameter(NumParameter2Defined = str (each_parameter))
            self.ObjContainer.dict_Parameters [parameter_obj.Name] = parameter_obj

        #Subcontainers
        
        if self.ObjContainer.NumSubContainer > 0:
            for each_subcontainer in range (0, self.ObjContainer.NumSubContainer):
                SubContainerSubContainer = SubContainerMD()
                SubContainerSubContainer.Menu2CreateSubContainer(NumSubContainer = str (each_subcontainer))
                self.ObjContainer.dict_subcontainers [SubContainerSubContainer.ObjContainer.Name] = SubContainerSubContainer
        
    def Menu2ModifySubcontainer(self):                    
                
        while (1):
            print()
            print ("--------------Modifying SubContainer---------------------")
            print ("Container: " + self.ObjContainer.Name)
            print ("1. Change the Name")
            print ("2. Change the Description")
            print ("3. Change the Lower Mult")
            print ("4. Change the Upper Mult")
            print ("5. Add, Modify or Remove parameters")
            print ("6. Add, Modify or Remove Subcontainer")
            print ("7. Back to principal Menu")
            print ("------------------------------------------------------")
            choose_modify = int(input ("Choose one option: "))
            print ()  
            

            if choose_modify == 1:
                self.ObjContainer.Name = input ("Write the new name: ")
            elif choose_modify == 2:
                self.ObjContainer.Description = input ("Write the new description: ")
            elif choose_modify == 3:               
                self.ObjContainer.minMultiplicity = str(input ("Define the new lower multiplicity: "))
            elif choose_modify == 4: 
                self.ObjContainer.maxMultiplicity =  str(input ("Define the new upper multiplicity: "))  
            elif choose_modify == 5:
                while (1):

                    print ("\n---------------------------------------------------")
                    print ("-------------- Modifying Parameter ----------------")
                    print ("---------------------------------------------------")
                    print ("Subcontainer: " + self.ObjContainer.Name)
                    print ("\n")
                    print ("1. Add parameter")
                    print ("2. Modify paramenter")
                    print ("3. Remove parameter") 
                    print ("4. Exit ")
                    print ("---------------------------------------------------")
                    option = int(input("Choose one option: "))

                    if option == 1:
                        parameter_obj = ParameterMD()
                        parameter_obj.Menu2CreateParameter()
                        self.ObjContainer.dict_Parameters [parameter_obj.Name] = parameter_obj
                    elif option == 2:
                        if len (self.ObjContainer.dict_Parameters.keys()) == 0:
                            print ("No parameters exist to be modified")
                        else:
                            print ()
                            ParameterName = input("Write the name of the parameter to be modified: ")
                            print ()
                            if not ParameterName in self.ObjContainer.dict_Parameters.keys():
                                print ("Parameter does not exit")
                            else:
                                parameter_obj = ParameterMD()
                                parameter_obj.Menu2ModifyParameter()
                                del self.ObjContainer.dict_Parameters [ParameterName]
                                self.ObjContainer.dict_Parameters [parameter_obj.Name] = parameter_obj
                                print ("The parameter has been modified\n")
                    
                    elif option == 3:
                        if len (self.ObjContainer.dict_Parameters.keys()) == 0:
                            print ("No parameters exist to be removed")
                        else:
                            print ()
                            ParameterName = input("Write the name of the parameter to be remove: ")
                            print ()
                            if not ParameterName in self.ObjContainer.dict_Parameters.keys():
                                print ("Parameter does not exit")
                            else:
                                del self.ObjContainer.dict_Parameters [ParameterName]
                                print ("The parameter has been removed\n")
                    elif option == 4:
                        break
            
            elif choose_modify == 6:
                while (1): 
                    print ("\n---------------------------------------------------")
                    print ("-------------- Modifying SubContainer ----------------")
                    print ("---------------------------------------------------")
                    print ("Subcontainer: " + self.ObjContainer.Name)
                    print ("\n")
                    print ("1. Add subcontainer")
                    print ("2. Modify subcontainer")
                    print ("3. Remove subcontainer") 
                    print ("4. Print Subcontainer")
                    print ("5. Exit ")
                    print ("---------------------------------------------------")
                    option = int(input("Choose one option: "))

                    if option == 1:
                        subcontainer_obj = SubContainerMD()
                        subcontainer_obj.Menu2CreateSubContainer()
                        self.ObjContainer.dict_subcontainers[subcontainer_obj.ObjContainer.Name] = subcontainer_obj
                    
                    elif option == 2:
                        if len (self.ObjContainer.dict_subcontainers.keys()) == 0:
                            print ("Not exist any subcontainer to be modified")
                        else:
                            print ()
                            SubcontainerName = input("Write the name of the subcontainer to be modified: ")
                            print()
                            if not SubcontainerName in self.ObjContainer.dict_subcontainers.keys():
                                print ("Subcontainer does not exit")
                            else:
                                self.ObjContainer.dict_subcontainers[SubcontainerName].Menu2ModifySubcontainer()
                                print ("The Subcontainer has been modified\n")                        
                    
                    elif option == 3:
                        if len (self.ObjContainer.dict_subcontainers.keys()) == 0:
                            print ("Not exist any subcontainer to be removed")
                        else:
                            print ()
                            SubcontainerName = input("Write the name of the subcontainer to be removed: ")
                            print ()
                            if not SubcontainerName in self.ObjContainer.dict_subcontainers.keys():
                                print ("Subcontainer does not exit")
                            else:
                                del self.ObjContainer.dict_subcontainers [SubcontainerName]
                                print ("The Subcontainer has been removed\n")     
                    
                    elif option == 4:
                        self.PrintSubcontainer()
                                
                    elif option ==5:
                        break
                    
            elif choose_modify == 7:
                break       
        
class Modules:
    def __init__ (self):
        self.dict_Modules = {}
        
    def AddModule (self, Module):
        self.dict_Modules [Module.ModuleName] = Module

    def PrintModules (self):
        for each_module in self.dict_Modules.keys():
            print (each_module)
            
    def FindModule (self, ModuleName):
        return self.dict_Modules [ModuleName]

class ReferencesMD (object):

    def __init__ (self):
        self.Name = ""
        self.Description = ""
        self.lowMultiplicity = 0
        self.uppMultiplicity = 0
        self.Origin = ""
        self.Destination = ""
 
    def InitParameterValues (self, Name, Description, lowMultiplicity, uppMultiplicity, Origin, Destination):
        self.Name = Name
        self.Description = Description
        self.lowMultiplicity = str (lowMultiplicity)
        self.uppMultiplicity = str (uppMultiplicity)
        self.Origin = Origin
        self.Destination = Destination

    def Get_ReferenceFromXml (self, ReferenceXml):
        
        #Name
        ReferenceNameXml = ReferenceXml.find ("SHORT-NAME")
        ReferenceName = ReferenceNameXml.text

        #Description
        ReferenceDescriptionDescXml = ReferenceXml.find ("DESC")
        ReferenceDescriptionL2Xml = ReferenceDescriptionDescXml.find ("L-2")
        ReferenceDescription = ReferenceDescriptionL2Xml.text

        #Lower Mult
        ReferenceLowMultXml = ReferenceXml.find ("LOWER-MULTIPLICITY")
        ReferenceLowMult = ReferenceLowMultXml.text
   
        #Upper Mult
        ReferenceUppMultXml = ReferenceXml.find ("UPPER-MULTIPLICITY")
        ReferenceUppMult = ReferenceUppMultXml.text

        #Origin
        ReferenceOriginXml = ReferenceXml.find ("ORIGIN")
        ReferenceOrigin = ReferenceOriginXml.text
        
        #Destination
        ReferenceDestinationXml = ReferenceXml.find ("DESTINATION-REF")
        ReferenceDestination = ReferenceDestinationXml.text         
    
        self.InitParameterValues (ReferenceName, ReferenceDescription, ReferenceLowMult, ReferenceUppMult, ReferenceOrigin, ReferenceDestination)

    def Set_ReferenceXml (self, ReferenceElement):
        
        ReferenceConfig = ET.Element ("ECUC-SYMBOLIC-NAME-REFERENCE-DEF")      
        
        ReferenceElement.append (ReferenceConfig)
        
        ReferenceName = ET.SubElement (ReferenceConfig, "SHORT-NAME")
        ReferenceName.text = self.Name
    
        ReferenceDescription = ET.Element ("DESC")
        DescriptionText = ET.SubElement (ReferenceDescription, "L-2")
        DescriptionText.set ("L", "EN")
        DescriptionText.text = self.Description
        ReferenceConfig.append (ReferenceDescription)

        
        ReferenceLowerMult = ET.SubElement (ReferenceConfig, "LOWER-MULTIPLICITY")
        ReferenceLowerMult.text = self.lowMultiplicity       

        ReferenceMaxMult = ET.SubElement (ReferenceConfig, "UPPER-MULTIPLICITY")
        ReferenceMaxMult.text = self.uppMultiplicity  
   
        ReferenceOrigin = ET.SubElement (ReferenceConfig, "ORIGIN")
        ReferenceOrigin.text = self.Origin 

        ReferenceDest = ET.SubElement (ReferenceConfig, "DESTINATION-REF")
        ReferenceDest.attrib = {"DEST":"ECUC-PARAM-CONF-CONTAINER-DEF"}
        ReferenceDest.text = self.Destination         
            
            
        ET.indent(ReferenceElement, '	')

ModuleCollection = Modules()