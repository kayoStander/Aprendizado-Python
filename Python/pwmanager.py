from cryptography.fernet import Fernet

class PwManager:

    def __init__(self):
        self.key = None
        self.password_File = None
        self.password_dict = {}

    def create_Key(self, path):
        self.key = Fernet.generate_key()
        with open(path,'wb') as f:
            f.write(self.key)

    def load_key(self,path):
        with open(path, 'rb') as f:
            self.key = f.read()

    def create_pw_file(self, path, initial_value=None):
        self.password_File = path

        if initial_value is not None:
            for k,v in initial_value.items():
                self.add_pw(k,v)

    def load_pw_file(self,path):
        self.password_File = path

        with open(path,'r') as f:
            for line in f:
                site, encrypt = line.split(':')
                self.password_dict[site] = Fernet(self.key).decrypt(encrypt.encode()).decode()

    def add_pw(self,site,pw):
        self.password_dict[site] = pw

        if self.password_File is not None:
            with open(self.password_File,'a') as f:
                encrytped = Fernet(self.key).encrypt(pw.encode())
                f.write(site + ':' + encrytped.decode() + '\n')

    def get_pw(self,site):
        return self.password_dict[site]

def main():
    password = {'email': 'nls196824',
                'facebook': 'nl196824'}
    
    pm = PwManager()

    print("""what do you wanna do?
          (1) create a new key
          (2) load a existing key
          (3) create a password file
          (4) load existing file
          (5) add new password
          (6) get a password
          (q) quiting
          """)
    
    done = False

    while not done:

        choice = input('choice: ')
        if choice == '1':
            path = input('enter path: ')
            pm.create_Key(path)
        elif choice == '2':
            path = input('enter path: ')
            pm.load_key(path)
        elif choice == '3':
            path = input('enter path: ')
            pm.create_pw_file(path, password)
        elif choice == '4':
            path = input('enter path: ')
            pm.load_pw_file(path)
        elif choice == '5':
            site = input('enter site: ')
            password = input('enter the password: ')
            pm.add_pw(site,password)
        elif choice == '6':
            site = input('what site do you want: ')
            print(f'password for {site} is {pm.get_pw(site)}')
        elif choice == '7':
            done = True
            print('bye')
        else:
            print('invalid choice')
            
main()