x=int(input("enter your value"))
match x:
    case 0:
     print("x is zero.")
    case 4:
      print("x is four")
    case _ if x==99:
      print("x is  equal to 99")
      
    case _ if x==100:
      print("x is equal to 100")