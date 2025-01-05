# radiology_scenario_factory.py
from medical_products import MedicalEnvironment, XRayMachine, AdjustRadiationExposure
from industrial_products import IndustrialEnvironment, ProtectiveSuit, MonitorRadiationLevels

class RadiologyScenarioFactory:
    def create_environment(self):
        pass

    def create_equipment(self):
        pass

    def create_task(self):
        pass

class MedicalScenarioFactory(RadiologyScenarioFactory):
    def create_environment(self):
        return MedicalEnvironment()

    def create_equipment(self):
        return XRayMachine()

    def create_task(self):
        return AdjustRadiationExposure()

class IndustrialScenarioFactory(RadiologyScenarioFactory):
    def create_environment(self):
        return IndustrialEnvironment()

    def create_equipment(self):
        return ProtectiveSuit()

    def create_task(self):
        return MonitorRadiationLevels()
