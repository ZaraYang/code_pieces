# ==================================================
# Download gene from Genebank in  FASTA format 
# copy from https://www.jianshu.com/p/5e6c5df393ad  and  https://www.cnblogs.com/ailiailan/p/11850710.html
# ==================================================

from Bio import Entrez
from Bio import SeqIO
from tqdm import tqdm
import os
from multiprocessing import Pool

Entrez.email = "balabala@mails.jlu.edu.cn"
database = "nucleotide"
rettype = 'fasta'
save_path = './ICTV_fasta_data/'
if not os.path.exists(save_path):
    os.makedirs(save_path)

def  run_download(accession ,save_path =save_path ,datbase = database,rettype = rettype):
    save_name = save_name = 'ICTV_{}'.format(accession)
    hd1 = Entrez.efetch(db = database,id=accession,rettype = rettype)
    seq = SeqIO.read(hd1,'fasta')

    fw = open('{}/{}.fasta'.format(save_path,save_name),'w')
    SeqIO.write(seq,fw,'fasta')
    fw.close()
    os.getcwd()
    print('Download finish : {}'.format(accession))

#run_download('./','NC_005816',database,accession = ['NC_005816'],rettype = rettype)

def read_access_file(file_path,save_path):
    pool = Pool(10)
    input_file = open(file_path,'r')
    accession_list = input_file.readline().split(';')
    pool.map_async(run_download,accession_list)
    pool.close() 
    pool.join()
read_access_file('./seq_accession',save_path)
