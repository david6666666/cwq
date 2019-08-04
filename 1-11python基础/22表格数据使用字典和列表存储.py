r1 = {'name':"陈炜青", 'age':'25','salary':'66666', 'city':'sd'}
r2 = {'name':"陈炜青1", 'age':'24','salary':'77777', 'city':'fj'}
r3 = {'name':"陈炜青2", 'age':'23','salary':'88888', 'city':'js'}

tb = [r1, r2, r3]
for i in range(len(tb)):
    print(tb[i].get('name'), tb[i].get('age'), tb[i].get('salary'), tb[i].get('city'))