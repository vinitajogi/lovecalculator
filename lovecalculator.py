name1=input('enter name of the first person')
name1=list(name1)
name2=input('enter name of the second person')
name2=list(name2)

def true_calc (name1,name2):
    N1=list(name1)
    N2=list(name2)
    T=['t','r','u','e']
    L=['l','o','v','e']
    U=[T,L]
    total_score_1 = 0
    total_score_2 = 0
    total_score = ''
    for u in U:
        score1 = 0
        score2 = 0
        c=0
        d=0
        e=0
        for x in u:
            print(f"{x}")
            if x == N1[d] and d < len(u):
                c+=1
            # d += 1
            print(f"count is {c}")
            if x == N2[d] and d < len(u):
                e+=1
            d += 1
            print(f"count is {e}")
        score1=score1+c
        score2=score2+e
        print(f"score in {N1} for {u} is {score1}")
        print(f"score in {N2} for {u} is {score2}")
        total_score_1=total_score_1+score1
        total_score_2= total_score_2+score2
    print(f"total_score is {total_score_1}")
    print(f"total_score is {total_score_2}")
    total_score=str(total_score_1)+str(total_score_2)
    print(f"final score is{str(total_score)}")

true_calc(name1,name2)
