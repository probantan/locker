class Credential:
        """
        Class that generates new instances of contacts
        """
        credential_list = [] # Empty contact list

        def __init__(self,first_name,last_name,password):

            # docstring removed for simplicity

            
                self.first_name = first_name
                self.last_name = last_name
                self.password = password
        
        def save_credential(self):
    		'''
		Function to save a newly created user instance
		'''
		Credential.credential_list.append(self)

class Credential:
    	'''
	Class to create  account credentials, generate passwords and save their information
	'''
	# Class Variables
	credential_list =[]
	credential_credential_list = []
	@classmethod
	def check_credential(cls,first_name,password):
		'''
		Method that checks if the name and password entered match entries in the users_list
		'''
		current_credential = ''
		for credential in Credential.credential_list:
			if (credential.first_name == first_name and credential.password == password):
				current_credential = credential.first_name
		return current_credential

        def __init__(self,credential_name,site_name,account_name,password):
    		'''
		Method to define the properties for each user object will hold.
		'''

		# instance variables
		self.credential_name = credential_name
		self.site_name = site_name
		self.account_name = account_name
		self.password = password