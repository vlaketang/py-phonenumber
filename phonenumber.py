# -*- coding:UTF-8 -*-
import xlrd
import sys
from optparse import OptionParser
phonefile="F:/GlobalRoam_Address_book.xls"

def getphonenumber(name):
    bk = xlrd.open_workbook(phonefile)
    shxrange = range(bk.nsheets)
    ret = []
    try:
        #打开Sheet1工作表
        sh = bk.sheet_by_name("Sheet1")
    except:
        print("no sheet in %s named Sheet1",phonefile)
    #获取行数
    nrows = sh.nrows
    #print(nrows)
    ncols = sh.ncols
    # print("nrows %d, ncols %d" % (nrows,ncols))

    for x in range(1,nrows):
        cell_value = sh.cell_value(x,1)

        # print(cell_value.replace(" ", ""),type(cell_value))
        ron = cell_value.replace(" ", "").find(name)
        if ron >= 0:
            ret.append([cell_value,sh.cell_value(x,2).replace(" ", ""),sh.cell_value(x,3)])
            # for y in range(1,sh.ncols):
            #     print(sh.cell_value(x,y))
    return ret

def main(argv):
    parser = OptionParser()
    parser.add_option('-n', '--name',dest='phone_name',type=str,default=None,
                      help = 'phone name')
    (options,args) = parser.parse_args()
    checkname = options.phone_name
    ret = getphonenumber(checkname)
    if len(ret) == 0:
        print(checkname,"没有找到")
        return
    for x in ret:
        print(x[0],x[1])
if __name__ == "__main__":
    main(sys.argv)