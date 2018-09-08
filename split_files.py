import sys,os
'''
UPDATES ON 2018/5/14
1. User can input chunksize in MB.
2. Will not return incomplete lines. (Only limited to situation where every linesize is same)
'''
kilobytes = 1024
megabytes = kilobytes*1000

def split(fromfile,todir,chunksize=20*megabytes):
    if not os.path.exists(todir):#check whether todir exists or not
        os.mkdir(todir)          
    else:    # if the directory has already existed, delete every file under the directory
        for fname in os.listdir(todir):
            os.remove(os.path.join(todir,fname))
    inputfile = open(fromfile,'rb')
    partnum = 0
    line = inputfile.readline()
    line_size = inputfile.tell() # get the size of one line
    residule = chunksize % line_size # reading without break complete line
    inputfile.close()
    inputfile = open(fromfile,'rb')
    while True:
        chunk = inputfile.read(chunksize - residule)
        if not chunk:
            break
        partnum += 1
        out_file_name = os.path.join(todir,('part%04d.txt'%partnum))
        outputfile = open(out_file_name, 'wb')   
        outputfile.write(chunk)
        outputfile.close()
    return partnum

if __name__=='__main__':
        fromfile  = raw_input('File to be split?')
        todir     = raw_input('Directory to store part files?')
        chunksize_mb = int(raw_input('Chunksize to be split（in MB)?'))
        chunksize = int(chunksize_mb * megabytes)
        absfrom,absto = map(os.path.abspath,[fromfile,todir])
        print('Splitting',absfrom,'to',absto,'by',chunksize)
        try:
            parts = split(absfrom,absto,chunksize)
        except:
            print('Error during split:')
            print(sys.exc_info()[0],sys.exc_info()[1])
        else:
            print('split finished:',parts,'parts are in',absto)

# how to use
# fromfile = JD_3C_IDFA_MD5.txt
# todir = ./JD_3C_IDFA_MD5
# chunksize = 50000000  bytes < 20MB

# fromfile = 'JD_luxury_IDFA_MD5.txt'
# todir = './JD_luxury_IDFA_MD5'
# chunksize = 9000000  bytes < 9MB


