out_fname = 'ex_module/sample_write_csv.csv'

with open(out_fname,'w') as out_fd:
    out_fd.write('name,age,id,phone_no,address')
    
# 작업 종료 메시지를 출력합니다.
print("output file :", out_fname)
    
