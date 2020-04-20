

from invoice_extraction import InvoiceExtraction
import sys
import os
from optparse import OptionParser
import pandas as pd
from progressbar import progressbar

print('None;')
if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-i', '--input', dest='input', help='输入文件夹，含pdf电子发票', default='./')
    parser.add_option('-o', '--output', dest='output', help='输出各发票字段表格', default='output.xlsx')
    parser.add_option('-r', '--recursive', dest='recursive', help='是否递归查找子文件夹中的发票', action='store_true')
    parser.add_option('-n', '--normalize', dest='normalize', help='是否重命名发票，格式：[发票号码]_[价税合计（小写）].pdf', action='store_true')
    opts, args = parser.parse_args()
    ie = InvoiceExtraction()

    df = []
    file_index=[]
    for root, folders, files in os.walk(opts.input):
        for file_name in files:
            if file_name.endswith('.pdf'):
                src_pdf = os.path.join(root, file_name)
                ret = ie.extract(src_pdf)
                #if opts.normalize and '发票号码' in ret and '价税合计(小写)' in ret:
                if True:
                    ret['fileName'] = 'Jiafu_%s_%s.pdf'%(ret['发票号码'], ret['金额'])
                    #ret['文件名'] = '%s_%s.pdf'%(ret['发票号码'], ret['价税合计(小写)'])
                    dst_pdf = os.path.join(root, ret['fileName'])
                    os.rename(src_pdf, dst_pdf)
                    #file_index.append(dst_pdf)

                #if file_index.count(dst_pdf):
                if dst_pdf not in file_index:
                    file_index.append(dst_pdf)
                    print(dst_pdf)
                    df.append(ret)
                else:
                    print('Duplicated pdf, abaondaon it')
    print(df)
    print(file_index)
    print(len(file_index))
    pd.DataFrame(df).to_excel(opts.output, index=False)
    #pd.DataFrame(df).to_excel(opts.output, index=False)

    # monitor folder, watch dog
    

    # process pdf and create index file


    # create new output folder
    
