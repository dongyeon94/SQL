from collections import *
import pymysql
connection = pymysql.connect(                               ###   ---------
host = '****************',                                  ###   database server url
user = '**********',                                        ###   database server user id
password = '*********',                                     ###   database server user password
db = '******',                                              ###   database name(scema name)
                                                            ###   ----------    
charset = 'utf8',                                             
cursorclass = pymysql.cursors.DictCursor)                  ## cusor 


def mainframe():
    ##action = input('Select your action:')
    ##cm,buil_id, name, location, capacity,assigned='', [],[],[],[],[]
    while True:
        action = input('Select your action:')

        #### 1 function
        if action == '1':
            try:
                with connection.cursor() as cursor:   ## cursor handling sql
                    
                    sql = 'select * from building'
                    cursor.execute(sql)
                    all_building = cursor.fetchall()
                    buil_id, b_name, b_location, b_capacity, = [], [], [], []
                    for i in range(len(all_building)):
                        b_cm = ChainMap(all_building[i])
                        buil_id.append(b_cm['building_id'])
                        b_name.append(b_cm['building_name'])
                        b_location.append(b_cm['building_location'])
                        b_capacity.append(b_cm['capacity'])

                    print('-' * 100)
                    print('id', ' ' * 9, 'name', ' ' * 20, 'location', ' ' * 20, 'capacity', ' ' * 10)
                    print('-' * 100)
                    for j in range(len(buil_id)):
                        print(buil_id[j], ' ' * 5, b_name[j], ' ' * (31-int(len(b_name[j]))), b_location[j], ' ' * (30-int(len(b_location[j]))), b_capacity[j], ' ')
                    print('-' * 100)
                    print('\n')

            except:
                print('error')
                
                
        ##### 2 function
        if action == '2':
            try:
                with connection.cursor() as cursor:  ## cursor handling sql
                    sql = 'select p.performance_id , p.performance_name, p.performance_type, p.price ,count(seat.audience_id) as booked ' + \
                          'from performance p  left join seat using(performance_id) group by (p.performance_id) '

                    cursor.execute(sql)
                    all_performance = cursor.fetchall()

                    perfor_id, p_name, p_price, p_type, p_booked = [], [], [], [], []
                    for i in range(len(all_performance)):
                        p_cm = ChainMap(all_performance[i])
                        perfor_id.append(p_cm['performance_id'])
                        p_name.append(p_cm['performance_name'])
                        p_price.append(p_cm['price'])
                        p_type.append(p_cm['performance_type'])
                        p_booked.append(p_cm['booked'])

                    print('-' * 100)
                    print('id', ' ' * 9, 'name', ' ' * 20, 'tpye', ' ' * 20, 'price', ' ' * 10, 'booked')
                    print('-' * 100)
                    for j in range(len(perfor_id)):
                        ccc = str(p_price[j])
                        print(perfor_id[j], ' ' * 5, p_name[j], ' ' * (28-int(len(p_name[j]))), p_type[j], ' ' * (24-int(len(p_type[j]))), ccc, ' '*(19-int(len(ccc))), p_booked[j])
                    print('-' * 100)
                    print('\n')

            except:
                print('error')

                ### 3번 function
        ##### 3번 function
        if action == '3':
            try:
                with connection.cursor() as cursor:
                    sql = 'SELECT * FROM audience'
                    cursor.execute(sql)
                    all_audience = cursor.fetchall()

                    audience_id, gender, age, audience_name = [], [], [], []
                    for i in range(len(all_audience)):
                        a_cm = ChainMap(all_audience[i])
                        audience_id.append(a_cm['audience_id'])
                        gender.append(a_cm['gender'])
                        age.append(a_cm['age'])
                        audience_name.append(a_cm['audience_name'])

                    print('-' * 100)
                    print('id', ' ' * 9, 'name', ' ' * 20, 'gender', ' ' * 20, 'age', ' ' * 10)
                    print('-' * 100)
                    for j in range(len(audience_id)):
                        print(audience_id[j], ' ' * 5, audience_name[j], ' ' * (30-int(len(audience_name[j]))), gender[j], ' ' * (26-int(len(gender[j]))), age[j])
                    print('-' * 100)
                    print('\n')

            except:
                print('error')

                ####  4번 function
        ##### 4번 function
        if action == '4':
            try:
                with connection.cursor() as cursor:
                    int_capa = 0
                    build_name, build_locatoin, build_capacity = input('Building name:'), input(
                        'Building locatoin:'), input('Building capacity:')
                    int_capa = int(build_capacity)
                    sql = ' insert into building(building_name,building_location,capacity) values(%s,%s,%s) '

                    cursor.execute(sql, (build_name, build_locatoin, int_capa))

                connection.commit()

            except:
                print('error')
        #### 5 번 function
        if action == '5':
            try:
                with connection.cursor() as cursor:
                    remove_name = input('Building ID')
                    sql = 'delete from building where building_id  = %s '
                    cursor.execute(sql, (remove_name))

                connection.commit()

            except:
                print('error')
        ### 6 번 function
        if action == '6':
            try:
                with connection.cursor() as cursor:
                    int_price = 0
                    per_name, p_type, price = input('Performance name:'), input('Performance type:'), input(
                        'Performance price:')
                    int_price = int(price)
                    sql = ' insert into performance(performance_name,price,performance_type) values(%s,%s,%s) '

                    cursor.execute(sql, (per_name, int_price, p_type))

                connection.commit()

            except:
                print('error')

                #### 7 번 function
        ##### 7번 function
        if action == '7':
            try:
                with connection.cursor() as cursor:
                    remove_name = input('Performance ID')
                    sql = 'delete from performance where performance_id = %s  '
                    cursor.execute(sql, (remove_name))

                connection.commit()

            except:
                print('error')
        ### 8 번 function
        if action == '8':
            try:
                with connection.cursor() as cursor:
                    int_age = 0
                    a_name, gender, age = input('Audience name:'), input('Audience gender:'), input('Audience age:')
                    int_age = int(age)
                    sql = ' insert into audience(audience_name,gender,age) values(%s,%s,%s); '

                    cursor.execute(sql, (a_name, gender, age))

                connection.commit()

            except:
                print('error')

                #### 9 번 function
        ##### 9번 function
        if action == '9':
            try:
                with connection.cursor() as cursor:
                    remove_name = input('Audience ID : ')
                    sql = 'delete from audience where audience_id =%s '
                    cursor.execute(sql, (remove_name))

                connection.commit()

            except:
                print('error')
        ##### 10번 function
        if action == '10':
            try:
                with connection.cursor() as cursor:
                    build_id, perfor_id = input('Building ID:'), input('Performance ID:')
                    int_b, int_p = int(build_id), int(perfor_id)
                    sql = 'update performance set building_id= %s where  performance_id =%s'
                    cursor.execute(sql, (int_b, int_p))

                connection.commit()


            except:
                print('error')
        ##### 11번 function
        if action == '11':
            try:
                with connection.cursor() as cursor:
                    per_id, aud_id, seat_num1 = input('Performance ID: '), input('Audience ID: '), input('Seat number : ')

                    int_per, int_aud = int(per_id), int(aud_id)
                    c = seat_num1.split(',')
                    b = []
                    for j in range(len(c)):
                        b.append(int(c[j]))


                    ###  capacity  범위 확인
                    sql = 'select building.capacity  from building , performance where  performance.building_id = building.building_id and performance.performance_id = %s'
                    cursor.execute(sql, (int_per))
                    cap = cursor.fetchall()
                    cap_nu = 0

                    for i in range(len(cap)):
                        p_cm1 = ChainMap(cap[i])
                        cap_nu = int(p_cm1['capacity'])

                    ## seat num 이 없는지 확인하자   %s
                    sql2 = 'select seat_num , performance_id   from seat where performance_id = %s '
                    cursor.execute(sql2, (int_per))
                    seat_n = cursor.fetchall()


                    ## audience 있는것도 만들어 줘야 될라나 조건엔 없는데 ㅡㅡ..

                    ## se_nu 에 좌석 번호 들었음  여기 번호 있으면 좌석 있는거임 에러 출력해야됨
                    se_nu, per = [], []
                    for i in range(len(seat_n)):
                        p_cm3 = ChainMap(seat_n[i])
                        se_nu.append(p_cm3['seat_num'])
                        per.append(p_cm3['performance_id'])

                    sql4 = 'select seat.audience_id,seat.performance_id, count(performance_id)*price as price ' +\
                          'from seat join performance using(performance_id)' +\
                          'where seat.audience_id = %s group by seat.audience_id,seat.performance_id'
                    cursor.execute(sql4, (int_aud))
                    pr = cursor.fetchall()
                    audid, pric=[],[]
                    for i in range(len(pr)):
                        p_cm3 = ChainMap(pr[i])
                        audid.append(p_cm3['audience_id'])
                        pric.append(p_cm3['price'])




                    int_pez, in_se = [], []
                    for j in range(len(per)):
                        int_pez.append(int(per[j]))

                    for k in range(len(se_nu)):
                        in_se.append(int(se_nu[k]))




                    if cap_nu == 0:
                        print('Sorry not assign performance')
                    elif cap_nu < max(b):
                        print('Sorry is overflow')
                    else:
                        ss = True
                        for m in range(len(b)):
                            if b[m] in in_se:
                                print('Sorry already assign')
                                ss = False

                        if ss == True:
                            c3 = len(b)
                            ## DB 삽입
                            for n in range(c3):
                                a=1
                                sql3 = 'insert into seat(seat_num,performance_id,audience_id) values(%s,%s,%s) '
                                cursor.execute(sql3, (b[n], int_per, int_aud))
                        connection.commit()




                    sql4 = 'select seat.audience_id,seat.performance_id, count(performance_id)*price as price ' + \
                             'from seat join performance using(performance_id)' + \
                             'where seat.audience_id = %s group by seat.audience_id,seat.performance_id'
                    cursor.execute(sql4, (int_aud))
                    pr = cursor.fetchall()
                    audid, pric ,it_pir= [], [] ,[]
                    for i in range(len(pr)):
                        p_cm3 = ChainMap(pr[i])
                        audid.append(p_cm3['audience_id'])
                        pric.append(p_cm3['price'])

                    for m in range(len(pric)):
                        it_pir.append(int(pric[m]))
                    ccc= sum(it_pir)
                    print(ccc)



            except:
                print('error')

                ### 12번 function
        ##### 12번 function
        if action == '12':
            try:
                with connection.cursor() as cursor:  ## 이게 커서 내용임 아래 접근을 할 수 있게 핸들링 해줌
                    perd = input('Building ID :')
                    inperd = int(perd)

                    sql = 'select p.performance_id , p.performance_name, p.performance_type, p.price ,count(seat.audience_id) as booked ' +\
                          'from performance p  left join seat using(performance_id)  where p.building_id =%s group by (p.performance_id) '

                    cursor.execute(sql,(inperd))
                    all_performance = cursor.fetchall()

                    perfor_id, p_name, p_price, p_type, p_booked = [], [], [], [], []
                    for i in range(len(all_performance)):
                        p_cm = ChainMap(all_performance[i])
                        perfor_id.append(p_cm['performance_id'])
                        p_name.append(p_cm['performance_name'])
                        p_price.append(p_cm['price'])
                        p_type.append(p_cm['performance_type'])
                        p_booked.append(p_cm['booked'])

                    print('-' * 100)
                    print('id', ' ' * 9, 'name', ' ' * 20, 'tpye', ' ' * 20, 'price', ' ' * 10, 'booked')
                    print('-' * 100)
                    for j in range(len(perfor_id)):
                        sss= str(p_price[j])
                        print(perfor_id[j], ' ' * 5, p_name[j], ' ' * (28-int(len(p_name[j]))), p_type[j], ' ' * (25- int(len(p_type[j]))), sss, ' ' * (15-int(len(sss))), p_booked[j])
                    print('-' * 100)
                    print('\n')

            except:
                print('error')

                ### 13번
        ##### 13번 function
        if action == '13':
            try:
                with connection.cursor() as cursor:
                    per_id1 = input('Performance ID:')
                    int_per_id = int(per_id1)

                    sql =  'select * from audience where audience_id in (select audience_id '  +\
                            'from seat  where performance_id = %s)'
                    cursor.execute(sql, (int_per_id))
                    all_boo = cursor.fetchall()

                    aud_id, aud_name, gender, age, = [], [], [], []
                    for i in range(len(all_boo)):
                        b_cm = ChainMap(all_boo[i])
                        aud_id.append(b_cm['audience_id'])
                        aud_name.append(b_cm['audience_name'])
                        gender.append(b_cm['gender'])
                        age.append(b_cm['age'])

                    print('-' * 100)
                    print('ID', ' ' * 9, 'audience_name', ' ' * 20, ' ',  'gender', ' ' * 30, 'age')
                    print('-' * 100)
                    for j in range(len(aud_id)):
                        print(aud_id[j], ' ' * 10, aud_name[j], ' ' * (37-int(len(aud_name[j]))), gender[j], ' ' * (35-int(len(gender[j]))), age[j])
                    print('-' * 100)
                    print('\n')

            except:
                print('error')

                ###  14번
        ##### 14번 function
        if action == '14':
            try:
                with connection.cursor() as cursor:
                    per_id = input('Performance ID:')
                    int_per_id = int(per_id)
                    sql = 'select capacity from building where building_id in (select building_id ' +\
                          'from performance where performance_id =%s)'
                    cursor.execute(sql, (int_per_id))
                    all_booked = cursor.fetchall()
                    cap_nu = 0
                    for i in range(len(all_booked)):
                        p_cm1 = ChainMap(all_booked[i])
                        cap_nu = int(p_cm1['capacity'])

                    sql2 =  'select seat_num, audience_id from seat where performance_id = %s'
                    cursor.execute(sql2, (int_per_id))
                    seat_nu = cursor.fetchall()
                    sat_nu , adid = [],[]
                    for i in range(len(seat_nu)):
                        p_cm1 = ChainMap(seat_nu[i])
                        sat_nu.append(int(p_cm1['seat_num']))
                        adid.append(int(p_cm1['audience_id']))


                    print('-' * 100)
                    print('seat_num', ' ' * 9, '', ' ' * 20, '', ' ' * 20, '', ' ' * 10, 'audien_id')
                    print('-' * 100)
                    for j in range(1,cap_nu+1):
                        aas  = ''
                        for k in range(len(sat_nu)):
                            if j == sat_nu[k]:
                                aas = adid[k]

                        print(j, ' ' * 5, ' ' * 15, ' ' * 25, ' ' * 25, aas)
                    print('-' * 100)
                    print('\n')

            except:
                print('error')
        ##### 15번 function
        if action == '15':
            print('exit')
            print('\n')
            connection.close()
            break


mainframe()
