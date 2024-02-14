# Pirate's Plunder Password Simulator
# Author: Ahmed Ali
# Date: 09/02/2024
# Revision: 1

import random
import string

class PasswordSimulator:
    """
    Class to simulate generation and validation of random passwords.
    """
    def __init__(self):
        """
        Initialize PasswordSimulator object.
        """
        self.accepted_passwords = []
        self.dictionary = set(["password", "123456", "qwerty", "letmein"])  # Example dictionary list

    def generate_random_password(self, length=10):
        """
        Generate a random password with the specified length.
        
        Args:
            length (int): Length of the password to generate. Default is 10.
        
        Returns:
            str: Randomly generated password.
        """
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    def is_acceptable_password(self, password):
        """
        Check if the given password meets the acceptance criteria.
        
        Args:
            password (str): Password to validate.
        
        Returns:
            bool: True if the password is acceptable, False otherwise.
        """
        # Check if the password contains special symbols
        if not any(char in string.punctuation for char in password):
            return False
        
        # Check if the password is in the dictionary list
        if password.lower() in self.dictionary:
            return False

        return True

    def simulate_passwords(self, iterations=40):
        """
        Simulate generating passwords and archive acceptable passwords.
        
        Args:
            iterations (int): Number of password simulation iterations. Default is 40.
        """
        for i in range(iterations):
            password = self.generate_random_password()
            if self.is_acceptable_password(password):
                self.accepted_passwords.append(password)
                print("Accepted password:", password)
            else:
                print("Rejected password:", password)

# Main function
def main():
    # Create an instance of PasswordSimulator
    simulator = PasswordSimulator()

    # Simulate passwords for at least 40 iterations
    simulator.simulate_passwords(iterations=40)

if __name__ == "__main__":
    main()
