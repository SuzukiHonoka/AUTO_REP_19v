#Some statement
print('Hi guys,\nwelcome to use this py based program!\nThis program is made by Starx and written in py3 format.\nPlease notice this program is used for test only,\nDO NOT USE IT FOR UNUSUAL PURPOSE.\nPLEASE USE IT AT YOUR OWN RISK.\nDO NOT USE IT TO FAKE REPORT!')
#import some needed packages
import requests
#API
login_p = 'https://cz.yoya.com/user_block/do?action=cz/h5/login&start=login&start=login&user_code=user_id&app_type=Android&action=cz/h5/login&user_pwd=user_pa&client_code=user_imei'
base_p = 'https://jkjc.yoya.com/fzjdxx/do?action=tzjc/h5/gzbdreport&start=getPreviousReport&user_id=uu_id'
report_p = 'https://jkjc.yoya.com/fzjdxx/do?action=tzjc/h5/gzbdreport&start=saveReport'
#Account
user_bl = 'school'
user_id = 'student_id'
user_pa = '123456' #unencrypted password text is very stupid.
user_im = 'Ive cracked you.\nQQ:1787074172'
#These below could be auto saved by using APP.
user_id_type = '1'
real_id = '000000000000000000'
user_real_addr = 'Paradise'
user_tel = '10010'
user_back_time = 'How long will you survive?' 

#mixed
user_f = login_p.replace('user_block',user_bl).replace('user_id',user_id).replace('user_pa',user_pa).replace('user_imei',user_im)
#Start a session by using requests
s = requests.session()
#Get backend resp
req1 = s.get(user_f).json()
#Check if login success or not
if not req1['code'] == 200 :
    print('Login Failed')
    print('Response:',req1['msg'])
    exit()
#After success
print('Login Success')
#Collect the useful datas
data_g = req1['data']
data_u = data_g['user']
#Split datas to single var
block = data_g['siteInfo']['site_code']
last_time = data_u['last_login_time']
name = data_u['user_name']
n_name = data_u['user_code']
#Say Hello to client
print('Last_Login_Time:',last_time,'\nName:',name,'\nNick Name:',n_name,'\nSchool:',block)
#Get ready for post datas
uu_id = data_u['user_id']
#Get base info
base_f = base_p.replace('uu_id',uu_id)
base_dict = s.get(base_f).json()
if base_dict['data'] != 'None':
    base_dict = base_dict['data']
    user_id_type = base_dict['id_type']
    real_id = base_dict['identity_code']
    user_real_addr = base_dict['address']
    user_tel = base_dict['telephone']
    user_back_time = base_dict['back_time']
#mixed
post_format = {'user_id':uu_id,'id_type':'1','identity_code':real_id,'address':user_real_addr,'telephone':user_tel,'user_back_time':user_back_time,'go_where':'None','contact_type':'1','es':'1','health_status':'2','is_diagnosis':'','is_fever':'0','temperature':'36','is_cough':'0','isolate':'0','isolate_type':'','isolate_time':'','remark':''}
#Finally post out
result = s.post(report_p,data=post_format).json()
print(result)
