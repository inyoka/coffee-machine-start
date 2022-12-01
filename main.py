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

def process_order(drink):
  print(f"Please pay : £{DRINKS[drink]['cost']}")
  check_resources(DRINKS[drink])
  payment = coin_payment()
  if payment >= DRINKS[drink]['cost']:
    print('Payment accepted, thank you.')
  else :
    print('Not enough funds to proceed, your money has been returned.')


def order_drink():
  while True :
    order = input("What would you like? (espresso/latte/cappuccino) ☕: ")
    if order not in DRINKS:
      print('Please enter a valid drink name.')
    elif order in DRINKS:
      process_order(order)
    elif order == "off":
      print("Shutting down ...")
      break
    else :
      pass


if __name__ == '__main__':
    order_drink()