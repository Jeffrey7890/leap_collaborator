import win32com.client
import json
from enum import Enum

class OBJType(Enum):
	BRANCH = 'Branch'
	SCENARIO = 'Scenario'



class LEAPObject:
	def __init__(self, COMObject, ObjType):
		self.object = COMObject
		self.type = ObjType

	def __repr__(self):
		return f"<LEAPObject <{self.type}: {self.object.Name}>>"
	
	def name(self):
		return self.object.Name

	def get_variables(self, BaseYear=2020, EndYear=2040):
		result = {}
		variables = self.object.Variables
		for v in variables:
			value_by_years = [v.Value(year) for year in range(BaseYear, EndYear+10, 10)]
			units = v.DefaultResultUnit
			if units is not None:
				result[v.Name] = (value_by_years, units.Name)
			else:
				units = v.DataUnitText
				result[v.Name] = (value_by_years, units)
			# try:
			# 	result[v.Name] = (value_by_years, v.DefaultResultUnit.Name)
			# except:
			# 	result[v.Name] = (value_by_years, v.DataUnitText)
		return result



class LeapModel():
	def __init__(self):
		self.leap = win32com.client.Dispatch("LEAP.LEAPApplication")
		if not self.leap:
			raise("Leap not open")

	def __repr__(self):
		return "<<LEAPObject>>"

	def get_branch(self, branch_path):
		branch = self.leap.Branch(branch_path)
		return LEAPObject(branch, "Branch")

	def get_subbranch(self, branch_path):
		branch = self.leap.Branch(branch_path)
		branch_list = []
		def crawl(branch):
			for b in branch.Children:
				branch_list.append(b.FullName)
				crawl(b)
		crawl(branch);
		return branch_list



	def get_current_scenario_results(self, branch_path="Demand"):
		branch = self.get_branch(branch_path)
		BaseYear = self.leap.BaseYear
		EndYear = self.leap.EndYear
		branch_result = branch.get_variables(BaseYear, EndYear)
		return {"years":[year for year in range(BaseYear, EndYear+10, 10)],
				"Scenario":self.leap.ActiveScenario.Name, branch_path:branch_result}

	def get_scenario_results(self, scenario, branch_path):
		self.leap.ActiveScenario = scenario
		return self.get_current_scenario_results(branch_path)
	
	def get_multiple_scenario_results(self, scenarios:list, branch_paths='Demand'):
		"""
			get_multiple_scenario_results: get data for the given list of scenarios
			@scenarios: list of scenarios
			@branch_paths: should be list [leave as Demand for now
			returns: a list of all scenario data
		"""
		result = []
		self.leap.Calculate()
		for scenario in scenarios:
			result.append(self.get_scenario_results(scenario, branch_paths))
		return result



def save_json(data, name):
	with open(name+ ".json", 'w')as f:
		json.dump(data, f, indent=4)

if __name__ == "__main__":
	leap = LeapModel()
	sub_branches = leap.get_subbranch("Transformation")
	SCD = leap.get_multiple_scenario_results(scenarios = ['Baseline', 'Mitigation'])
	save_json(SCD, 'Transformation')

	# lighting_existing = leap.get_branch("Demand\\Household\\Urban\\Electrified\\Lighting\\Existing")
	# var = lighting_existing.get_variables()
	# print(var)

