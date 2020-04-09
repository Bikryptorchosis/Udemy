for x in range(10):
    for y in range(10):
        for z in range(10):
            print(x, y, z)
            if x*y*z == 30:
                print("breaking z")
                break
        else:
            continue
        print("breaking y")
        break
    else:
        continue
    print("breaking x")
    break
