r=int(input("enter the rows:\n"))
c = int(input("enter the columns:\n"))

x = '-'*3
y = ' '*3

for i in range(1,(2*r+2)):
    for j in range(1,c+1):

        match i%2:
            case 1:
                match j%2:

                    case 1:print(' '+x,end='')
                    case 0:print(' '+y,end='')

            case 0:
                match j%2:
                    case 1:print(' '+y,end='')
                    case 0:print(' '+x,end='')

    print()
    


#/ setting

    if i<=(c+1):
        for j in range(1,c+2):

            match i%2:
                case 1:
                    match j%2:
                        case 1:print('/'+y,end='')
                        case 0:print(chr(92)+y,end='')
                case 0:
                    match j%2:
                        case 1:print(chr(92)+y,end='')
                        case 0:print('/'+y,end='')

        print()
