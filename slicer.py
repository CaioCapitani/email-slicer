# email do usuário

email = input("Qual o seu email? ").strip()

# slice do nome de usário

username = email[:email.index("@")]

# slice do domain

domain = email[email.index("@") + 1 :]

# formatar mensagem

output = "Seu nome de usuário é {} e seu domain é {}".format(username, domain)

# display da mensagem de output

print(output)