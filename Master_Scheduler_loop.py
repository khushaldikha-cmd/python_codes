# import os
# os.system("cls")
print("Starting... - Flat Tables Codes Added [Version 39] -- New Process in Every Loop - Scheduler Auto refresh code in every iteration")
while(True) : 
    print("Auto refreshing code in every iteration - as well as clearing terminal at 5 PM")
    import os
    import time
    from datetime import datetime, timedelta
    from zoneinfo import ZoneInfo
    hh = int(str(datetime.now(ZoneInfo("Asia/Kolkata")))[11:13])
    dd = int(str(datetime.now(ZoneInfo("Asia/Kolkata")))[8:10])
    ms_dir = "C:/Users/khushaldikha/Documents/Python_Codes/Master_Scheduler"
    print("Current Hour is {} , Current Date is {}".format(hh,dd))

    if( hh==17 ) | ( hh==12 ) :
        import os
        os.system("cls")
        print("Auto refreshing code in every iteration - as well as clearing terminal at 5 PM")        

        os.chdir(ms_dir)
        file = "../0009_New_Lead_Assigment_Automation/0017_Mid_Market_New_Logins.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds

    
    if (hh == 14) :
        print("Starting... Updating few columns in Flat Table ")
        ms_dir = "C:/Users/khushaldikha/Documents/Python_Codes/Master_Scheduler"
        os.chdir(ms_dir)
        file = "../0002_Lead_Data_Flat_Tables/0002_Company_Created_Flat_Tables.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds
               
        os.chdir(ms_dir)
        file = "../0002_Lead_Data_Flat_Tables/0006_Customer_Latest_Plans.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds

        os.chdir(ms_dir)
        file = "../0002_Lead_Data_Flat_Tables/0007_Company_Last_Login.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds

        os.chdir(ms_dir)
        file = "../0002_Lead_Data_Flat_Tables/0013_Failed_Payments.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds   

        os.chdir(ms_dir)
        file = "../0002_Lead_Data_Flat_Tables/0999c_Update_Last_Login.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds 


        os.chdir(ms_dir)
        file = "../0002_Lead_Data_Flat_Tables/0999d_Payment_Failed.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds 

    
    if (hh == 0) | (hh == 24) :    
        print("Starting... Logins Log")
        ms_dir = "C:/Users/khushaldikha/Documents/Python_Codes/Master_Scheduler"
        os.chdir(ms_dir)
        file = "../0002_Lead_Data_Flat_Tables/0014_Logins_Log.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds       
    
    if (hh == 11) :
        print("Starting... Renewal Campaign")
        ms_dir = "C:/Users/khushaldikha/Documents/Python_Codes/Master_Scheduler"
        os.chdir(ms_dir)
        file = "../0012_Campaign_automation/0004_renewal_direct_runner.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds        


        os.chdir(ms_dir)
        file = "../0012_Campaign_automation/0025_onboarding_demo_campaign.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds    

        
        os.chdir(ms_dir)
        file = "../Master_Scheduler/0999_Send_Log_Mail.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds 


    
    if (hh == 8) | (hh==9) | (hh==10) | (hh==11) | (hh==12) | (hh==13) | (hh == 14) | (hh==15) | (hh==16) | (hh==17) | (hh==18) | (hh==19)  :
        print("Starting... Last Login Campaign")
        ms_dir = "C:/Users/khushaldikha/Documents/Python_Codes/Master_Scheduler"
        
        os.chdir(ms_dir)
        file = "../0002_Lead_Data_Flat_Tables/0005_Sales_Assigned_Leads_Flag.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds  
        
        os.chdir(ms_dir)
        file = "../0012_Campaign_automation/0020_whatsapp_coupon_campaign_simple.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds        

    if (hh == 8) :
        
        print("Starting... D1 Campaign")
        ms_dir = "C:/Users/khushaldikha/Documents/Python_Codes/Master_Scheduler"
        os.chdir(ms_dir)
        file = "../0012_Campaign_automation/0003_Day1_WhatsApp_Campaign.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds        


        # os.chdir(ms_dir)
        # file = "../0012_Campaign_automation/0003_Day1_WhatsApp_Campaign.py"
        # print("running {}".format(file))
        # os.system("python {}".format(file))
        # time.sleep(5)  # Pause execution for 5 seconds 


        os.chdir(ms_dir)
        file = "../0012_Campaign_automation/0044_bgv_wallet_transactions_append.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds 
        
        os.chdir(ms_dir)
        file = "../0012_Campaign_automation/0003_Day1_Start_Your_Free_Trial_FCM.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds 
        
        os.chdir(ms_dir)
        file = "../0012_Campaign_automation/0003b_Day1_Trial_Started_NoUserAdded_FCM.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds 

        os.chdir(ms_dir)
        file = "../0012_Campaign_automation/0003c_Day1_Trial_Started_UserAdded_FCM.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds 

        
        os.chdir(ms_dir)
        file = "../0011_Campaign_Evaluation/0001_Campaign_Data_Pull_from_Gsheet.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds 


    
    if (hh == 9) | (hh==12) | (hh==14) | (hh==16) | (hh==18) | (hh==20) :
        print("Starting... Welcome Campaign")
        ms_dir = "C:/Users/khushaldikha/Documents/Python_Codes/Master_Scheduler"
        os.chdir(ms_dir)
        file = "../0019_FCM_Token_Master_Data/0001_Get_FCM_Token_Data.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds        

        os.chdir(ms_dir)
        file = "../0012_Campaign_automation/0002_FCM_Welcome_Campaign.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds 

        os.chdir(ms_dir)
        file = "../0011_Campaign_Evaluation/0001_Campaign_Data_Pull_from_Gsheet.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds     

        os.chdir(ms_dir)
        file = "../0011_Campaign_Evaluation/0002_Campaign_Data_Renewal.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds
        
        os.chdir(ms_dir)
        file = "../0002_Lead_Data_Flat_Tables/0013_Failed_Payments.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds  



    
    if (hh == 7) & (dd ==2) :
        os.chdir(ms_dir)
        file = "../0003_Push_Data_to_GoogleSheet_Current_Flow_for_Claude/0007_Gsheet_Tab_monthly_attendance.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds

        os.chdir(ms_dir)
        file = "../0003_Push_Data_to_GoogleSheet_Current_Flow_for_Claude/0008_Gsheet_Tab_monthly_payroll.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds

        os.chdir(ms_dir)
        file = "../0003_Push_Data_to_GoogleSheet_Current_Flow_for_Claude/0008_Gsheet_Tab_monthly_payroll.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds

    if hh == 10 :
        print("Starting... Morning 10 AM Campaign")
        ms_dir = "C:/Users/khushaldikha/Documents/Python_Codes/Master_Scheduler"
        
        os.chdir(ms_dir)
        file = "../0012_Campaign_automation/0001_whatsapp_trial_expired_Companies_simple.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds
        
    if hh == 6 :
        print("Starting... Morning 6 AM Uploads")
        ms_dir = "C:/Users/khushaldikha/Documents/Python_Codes/Master_Scheduler"
        
        os.chdir(ms_dir)
        file = "../0003_Push_Data_to_GoogleSheet_Current_Flow_for_Claude/0002_Gsheet_Tab_Contacts.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds

    
    if hh == 7 :
        print("Current Time is {} - Wake up and Run Scripts".format(str(hh)) )
        
        print("Starting... Morning Uploads")
        ms_dir = "C:/Users/khushaldikha/Documents/Python_Codes/Master_Scheduler"
        
        os.chdir(ms_dir)
        file = "../0003_Push_Data_to_GoogleSheet_Current_Flow_for_Claude/0001_Gsheet_Tab_Companies.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds
        
        os.chdir(ms_dir)
        file = "../0003_Push_Data_to_GoogleSheet_Current_Flow_for_Claude/0002_Gsheet_Tab_Contacts.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds
        
        os.chdir(ms_dir)
        file = "../0003_Push_Data_to_GoogleSheet_Current_Flow_for_Claude/0003_Gsheet_Tab_Payment_Log.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds
        
        # os.chdir(ms_dir)
        # file = "../0003_Push_Data_to_GoogleSheet_Current_Flow_for_Claude/0004_Gsheet_Tab_Trial_Expired_companies.py"
        # print("running {}".format(file))
        # os.system("python {}".format(file))
        # time.sleep(5)  # Pause execution for 5 seconds

        os.chdir(ms_dir)
        file = "../0003_Push_Data_to_GoogleSheet_Current_Flow_for_Claude/0005_Gsheet_Tab_PII_contacts.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds

        os.chdir(ms_dir)
        file = "../0003_Push_Data_to_GoogleSheet_Current_Flow_for_Claude/0006_Gsheet_Tab_PII_fcm.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds

        print("---- Flat Tables Codes ------")

        os.chdir(ms_dir)
        file = "../0002_Lead_Data_Flat_Tables/0001_Lead_Data_Flat_Tables.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds
        
        os.chdir(ms_dir)
        file = "../0002_Lead_Data_Flat_Tables/0002_Company_Created_Flat_Tables.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds
        
        os.chdir(ms_dir)
        file = "../0002_Lead_Data_Flat_Tables/0003_Email_Domain_Flat_Table.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds
        
        
        os.chdir(ms_dir)
        file = "../0002_Lead_Data_Flat_Tables/0005_Sales_Assigned_Leads_Flag.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds

        os.chdir(ms_dir)
        file = "../0002_Lead_Data_Flat_Tables/0006_Customer_Latest_Plans.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds

        os.chdir(ms_dir)
        file = "../0002_Lead_Data_Flat_Tables/0007_Company_Last_Login.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds

        os.chdir(ms_dir)
        file = "../0002_Lead_Data_Flat_Tables/0008_Company_Users_added.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds


        os.chdir(ms_dir)
        file = "../0002_Lead_Data_Flat_Tables/0009_Company_Trial_Usage.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds

        os.chdir(ms_dir)
        file = "../0002_Lead_Data_Flat_Tables/0010_Company_Trial_Attendance.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds

        os.chdir(ms_dir)
        file = "../0002_Lead_Data_Flat_Tables/0011_Company_Total_Attendance.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds        

        os.chdir(ms_dir)
        file = "../0002_Lead_Data_Flat_Tables/0012_Branch_Pincode.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds   

        os.chdir(ms_dir)
        file = "../0002_Lead_Data_Flat_Tables/0013_Failed_Payments.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds   

        
        os.chdir(ms_dir)
        file = "../0002_Lead_Data_Flat_Tables/0004_Logit_Model_Scoring.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds
        
        
        os.chdir(ms_dir)
        file = "../0002_Lead_Data_Flat_Tables/0999_Master_Flat_Table_Leads.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds        


        os.chdir(ms_dir)
        file = "../0002_Lead_Data_Flat_Tables/0999_Master_Flat_Table_Leads_Create_Index.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds     

        
        os.chdir(ms_dir)
        file = "../0002_Lead_Data_Flat_Tables/0999b_Master_Flat_Table_Daily_Data_Extract.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds        


        os.chdir(ms_dir)
        file = "../0011_Campaign_Evaluation/0001_Campaign_Data_Pull_from_Gsheet.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds        
          
        os.chdir(ms_dir)
        file = "../0027_Quotation/0027_quotation.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds      
        
        os.chdir(ms_dir)
        file = "../Master_Scheduler/0999_Send_Log_Mail.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds        
        
        print("Finished")

    if (hh == 17) | (hh == 8) |   (hh == 14)  :
        print("Starting... [SMB Data Update]")
        ms_dir = "C:/Users/khushaldikha/Documents/Python_Codes/Master_Scheduler"
        os.chdir(ms_dir)
        file = "../0006_SMB_Data_Update_on_Gsheet/0001_SMB_Data_Extract.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds

        os.chdir(ms_dir)
        file = "../0009_New_Lead_Assigment_Automation/0013_SMB_New_Lead.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds        

        os.chdir(ms_dir)
        file = "../0009_New_Lead_Assigment_Automation/0016_Mumbai_Lead.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds 
        

        # os.chdir(ms_dir)
        # file = "../0011_Campaign_Evaluation/0001_Campaign_Data_Pull_from_Gsheet.py"
        # print("running {}".format(file))
        # os.system("python {}".format(file))
        # time.sleep(5)  # Pause execution for 5 seconds    

        
        os.chdir(ms_dir)
        file = "../Master_Scheduler/0999_Send_Log_Mail.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds  

    if  (hh == 10) |   (hh == 19)  :
        print("Starting.. [Support Renewal Update]")
        file = "../0010_renewal_ticket_payment_data_automation/0014_Renewal_Support_tickets_renewal.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds

        os.chdir(ms_dir)
        file = "../Master_Scheduler/0999_Send_Log_Mail.py"
        print("running {}".format(file))
        os.system("python {}".format(file))
        time.sleep(5)  # Pause execution for 5 seconds    
        
        
    print("going back to sleep for {} minutes ".format(str((61- int(str(datetime.now(ZoneInfo("Asia/Kolkata")))[14:16])))))
    from datetime import datetime, timedelta
    time.sleep((61- int(str( datetime.now(ZoneInfo("Asia/Kolkata"))   )[14:16]))*60)
    # time.sleep(3*60)
    import os 
    import sys
    os.execv(
        sys.executable,
        [sys.executable] + sys.argv
    )    