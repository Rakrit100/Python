def world_war():
    a_w_r= input("Which alliance won World War 2?: ")
    w_w_e_y=input("When did World War end?: ")
    return a_w_r,w_w_e_y
def main():
        alliance,war_end_year=world_war()
        print(f"The war was won by {alliance} and the war ended in {war_end_year}")
if __name__=="__main__":
    main()
