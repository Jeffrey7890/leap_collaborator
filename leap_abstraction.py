import win32com.client


class LeapModel():
	def __init__(self):
		self.leap = win32com.client.Dispatch("LEAP.LEAPApplication")
		if not self.leap:
			raise("Leap not open")

	def get_branch_results(self, branch):
		result = {}
		variables = self.leap.Branch(branch).Variables
		for v in variables:
			result[v.BranchVariableName] = v.Value()
		return result

if __name__== "__main__":
	L = LeapModel()
	print(L.get_branch_results("Demand"))

