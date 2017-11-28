import os
import shutil

root = '/mnt/sdd1/mingzhang/qujing_vehicle_data/'

inputlist = root + '2016-12-14_2017-08-29_new/distractor/query_f5000.list'

dir0 = root +'2016-12-14_2017-08-29_new/distractor/query_f5000_imgs/'



filetxt = open(inputlist,'r')
filetxt2 = open('query_f5000_noplate.list','w+')
for oneline in filetxt:
    oneline = oneline.replace('\n','')
    tmp = oneline.split(',')
#    print oneline
    print tmp[0]+'/'+tmp[1]
#    print tmp[1]
#    print tmp[2]

    shutil.copy(tmp[0]+'/'+tmp[1],dir0)
    filetxt2.write(tmp[0]+','+tmp[1]+'_noplate.jpg'+','+tmp[2]+'\n')

filetxt2.close()
