import pyjokes
import cowsay
import helper

print(helper.VERSION)
helper.greet("Chris")
cowsay.stegosaurus(pyjokes.get_joke())
