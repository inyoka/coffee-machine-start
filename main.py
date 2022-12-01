from menu import DRINKS, resources

    
def check_resources(drink):
  for ingredient in drink['ingredients']:
    if drink['ingredients'][ingredient] <= resources[ingredient]:
      print(f"Enough {ingredient}")
    else:
      print(f"Sorry, there is not enough {ingredient}.")
      return False

def coin_payment():
  payment = 0.0
  print("Please insert coins.")
  quarters = input("how many quarters?: ")
  payment += float(quarters) * 0.25
  dimes = input("how many dimes?: ")
  payment += float(dimes) * 0.10
  nickles = input("how many nickles?: ")
  payment += float(nickles) * 0.05
  pennies = input("how many pennies?: ")
  payment += float(pennies) * 0.01
  print(f"You entered : £ {payment}")
  return payment

def order_drink():
  while True :
    order = input("What would you like? (espresso/latte/cappuccino) ☕: ")
    if order == "espresso":
      print(f"Please pay : £{DRINKS['espresso']['cost']}")
      check_resources(DRINKS['espresso'])
      if coin_payment() >= {DRINKS['espresso']['cost']:
        print('Payment accepted, thank you.')
      else :
        print('Not enough funds to proceed, your money has been returned.')
    elif order == "latte":
      print("latte")
      return
    elif order == "cappuccino":
      print("cappuccino")
      return
    elif order == "off":
      print("Shutting down ...")
      break
    else :
      return


if __name__ == '__main__':
    order_drink()