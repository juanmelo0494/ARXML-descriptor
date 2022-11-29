import os
import xml.etree.ElementTree as ET
import ClassesMD as MD


    


def CreateFileMDArxml(TreeView, ModuleName, VendorName, ModuleDescription, SipVersion, SipPath, LowerMultiplicity, UpperMultiplicity, NumContainers2Create):
    Module = MD.ModuleMD()
    Module.SetModule (ModuleName, VendorName, ModuleDescription, SipVersion, SipPath, LowerMultiplicity, UpperMultiplicity, NumContainers = NumContainers2Create)
    #Module.printModule()
    ReturnVal = Module.CreateModule_Sip(TreeView)
    print(Module)
    MD.ModuleCollection.AddModule (Module)
    MD.ModuleCollection.PrintModules()
    return ReturnVal
    
def ModifileFileMDArxml (ModuleName, VendorName, ModuleDescription, SipVersion, SipPath, LowerMultiplicity, UpperMultiplicity):
    BSWMD_Mol = MD.ModuleCollection.FindModule(ModuleName)

    BSWMD_Mol.SetModule (ModuleName, VendorName, ModuleDescription, SipVersion, SipPath, LowerMultiplicity, UpperMultiplicity)
    print ("---------------------Module--------------------")
    BSWMD_Mol.printModule()
    
    if BSWMD_Mol.CheckSipPath() and BSWMD_Mol.FindModule_Sip():
        print("Hello")
        BSWMD_Mol.ModifyArxmlStructure()
        return "MS_OK"

def DeleteFileMDArxml(ModuleName, VendorName, ModuleDescription, SipVersion, SipPath):
    BSWMD_Mol = MD.ModuleMD()
    BSWMD_Mol.SetModule (ModuleName, VendorName, ModuleDescription, SipVersion, SipPath)
    BSWMD_Mol.DeleteModule_Sip()

#ModifileFileMDArxml()
#CreateFileMDArxml(ModuleName, VendorName, ModuleDescription, SipVersion, SipPath, NumContainers)








    
    
  


