import sys
class handydandy:
  def quit():
    sys.close
  class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    def printc(text, color):
      print(f'{color}{text}{handydandy.colors.ENDC}')
  class input:
    def pause():
      input("press enter to continue\n")
    def quitpause():
      input("press enter to quit\n")
      quit() 
    def quitask():
      quitaskv1 = input("do you want to quit:  (y/n)\n")
      if quitaskv1 == "y":
        handydandy.quit()
      else:
        return()
    def ask(question):
      input(question)