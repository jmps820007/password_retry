###密碼重試程式

#先在程式碼中 設定好 password = 'a123456'
#讓使用者[最多輸入3次密碼]
#不對的話, 就印出"密碼錯誤! 還有__次機會"
#對的話,就印出"登入成功!"

password = 'a123456'
times = 3
while times <= 3:
    enter = input('請輸入密碼: ')
    if enter == password:
        print('登入成功')
        break
    elif enter != password:
        times -= 1
        if times <= 0:
            print('帳戶鎖定，請至分行解鎖')
            break
        print('密碼輸入錯誤! 還有 %d 次機會' %times)
