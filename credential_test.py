import unittest
from Credential import Credential

class TestCredential(unittest.TestCase):
        '''
        Test class that defines test cases for the user class behaviours.
        Args:
        unittest.TestCase: helps in creating test cases
        '''
        def setUp(self):
            '''
            Function to create a user account before each test
            '''
            self.new_credential = Credential("Protus","Bantan","psswd")

        def test_init(self):
            '''
            Test to if check the initialization/creation of user instances is properly done
            '''
            self.assertEqual(self.new_credential.first_name,'Protus')
            self.assertEqual(self.new_credential.last_name,'Bantan')
            self.assertEqual(self.new_credential.password,'psswd')

        def test_save_Credential(self):
            '''
            test_save_contact test case to test if the contact object is saved into
            the contact list
            '''
            self.new_credential.save_credential() # saving the new contact
            self.assertEqual(len(Credential.credential_list),1)

class TestCredentials(unittest.TestCase):
        '''
        Test class that defines test cases for the credentials class behaviours.
        Args:
            unittest.TestCase: helps in creating test cases
        '''
        def test_check_credential(self):
                '''
                Function to test whether the login in function check_user works as expected
                '''
                self.new_credential = Credential('Protus','Bantan','psswd')
                self.new_credential.save_credential()
                credential2 = Credential('Protus','Oduor','psswd')
                credential2.save_credential()

                for credential in Credential.credential_list:
                    if credential.first_name == credential2.first_name and credential.password == credential2.password:
                        current_credential= credential.first_name
                return current_credential

                self.assertEqual(current_credential,Credential.check_credential(credential2.password,credential2.first_name))

        def setUp(self):
                '''
                Function to create an account's credentials before each test
                '''
                self.new_credential = Credential('Mary','Facebook','maryjoe','pswd100')

if __name__ ==  '__main__':
    unittest.main()
