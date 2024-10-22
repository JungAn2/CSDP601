import rsa

def displaySteps(user):
    if user == 0:
        print("************\nAlice:\n************")
        print("step 1: p and q\np: ", alice.p, "\nq: ", alice.q)
        print("step 2: n\nn: ", alice.n)
        print("step 3: phi\nphi: ", alice.phi)
        print("step 4: e by gcd(e, phi) = 1\ne: ", alice.e)
        print("step 5: d by mod_inverse(e, phi)\nd: ", alice.d)
        print("Public Key: ", alice.public_key)
        print("Private Key: ", alice.private_key)
    elif user == 1:
        print("************\nMike:\n************")
        print("step 1: p and q\np: ", mike.p, "\nq: ", mike.q)
        print("step 2: n\nn: ", mike.n)
        print("step 3: phi\nphi: ", mike.phi)
        print("step 4: e by gcd(e, phi) = 1\ne: ", mike.e)
        print("step 5: d by mod_inverse(e, phi)\nd: ", mike.d)
        print("Public Key: ", mike.public_key)
        print("Private Key: ", mike.private_key)
    elif user == 2:
        print("************\nGreg:\n************")
        print("step 1: p and q\np: ", greg.p, "\nq: ", greg.q)
        print("step 2: n\nn: ", greg.n)
        print("step 3: phi\nphi: ", greg.phi)
        print("step 4: e by gcd(e, phi) = 1\ne: ", greg.e)
        print("step 5: d by mod_inverse(e, phi)\nd: ", greg.d)
        print("Public Key: ", greg.public_key)
        print("Private Key: ", greg.private_key)

def menu():
    while(True):
        print("Select a user to send the message to: ")
        print("1. Alice")
        print("2. Mike")
        print("3. Greg")
        print("4. Exit")
        user = int(input("Select user: "))
        print()

        if user == 1:
            displaySteps(0)
        elif user == 2:
            displaySteps(1)
        elif user == 3:
            displaySteps(2)
        elif user == 4:
            break

        print()
        print("Type in the message: ")
        message = input()
        print("Encrypted message: ", alice.encrypt(message))
        print("Decrypted message: ", alice.decrypt(alice.encrypt(message)))
        print()

alice = rsa.rsa()
mike = rsa.rsa()
greg = rsa.rsa()

menu()