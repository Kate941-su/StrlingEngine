
"""自作関数たち"""

"""listの平均をとる関数"""

def average_list(Target_list,Moving_Average):
    sum=0
    count=0
    ave_lis=[]
    for i in Target_list:
        sum+=i
        count+=1
        if count%Moving_Average==0:
            ave=sum/Moving_Average
            ave_lis.append(ave)
            sum=0

    return ave_lis

"""横軸の時間リストを作る"""


def make_Timelist(Length,between_step):
    time_list=[]
    for i in range(Length):
        time_list.append(5*i*between_step)
    
    return time_list

"""データを間引く"""

"""引数：Array:対象配列,Interval：間引く間隔,EndTime,EndTime以降のデータは配列に追加しない"""

"""戻り値：配列"""



def cull_data(Array,Interval,EndTime):
    ReturnList=[]
    for i in range(len(Array)):
        if i%Interval==0:
            ReturnList.append(Array[i])
        
        if i >=EndTime:
            break
    return ReturnList
