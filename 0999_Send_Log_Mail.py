try : 
    #!/usr/bin/env python
    # coding: utf-8
    
    # In[1]:
    
    print("Running 0999_Send_Log_Mail.py [Version 3] ")
    import pandas as pd
    
    
    # In[2]:
    
    
    import os
    dir_list = os.listdir("../Script_Logs/")
    print(dir_list)
    
    
    # In[3]:
    
    
    df = pd.DataFrame()
    for file in dir_list : 
        print(file)
        temp = pd.read_csv("../Script_Logs/"+file)
        df = pd.concat([df,temp] , ignore_index=True )
    
    
    df.sort_values("timestamp", ascending = False  , inplace = True )
    df['timestamp'] = pd.to_datetime(df['timestamp']) + pd.Timedelta(hours=5.5)

    df['error'] = df['error'].apply(lambda x : str(x)[:30])
    
    from datetime import datetime
    ref_date = str(datetime.now())[:16]
    print(ref_date)
    
    
    # In[5]:
    
    
    import pickle
    import base64
    from email.mime.text import MIMEText
    from googleapiclient.discovery import build
    from google.auth.transport.requests import Request
    
    
    # In[6]:
    
    
    from pretty_html_table import build_table
    import pandas as pd
    
    
    # In[7]:
    
    
    token_file = "../0000_Creds/khushal_token.pickle"
    
    
    # In[8]:
    
    
    # Load OAuth token
    with open(token_file, "rb") as token:
        creds = pickle.load(token)
    
    
    # In[9]:
    
    
    service = build(
        "gmail",
        "v1",
        credentials=creds
    )
    
    
    # In[10]:
    
    
    html_table = build_table(
        df,
        "blue_light"
    )
    
    html_body = '''
    <h2>Report as of {0} </h2>
    {1}
    '''.format(ref_date, html_table )
    
    message = MIMEText(html_body, "html")
    
    message["to"] = "khushal.dikha@salarybox.in , jatin@salarybox.in , jayveer.singh@salarybox.in "
    message["subject"] = "Script_Scuccess_Falied_Log {0}".format(ref_date[:10])
    
    
    raw_message = base64.urlsafe_b64encode(
        message.as_bytes()
    ).decode()
    
    
    service.users().messages().send(
        userId="me",
        body={
            "raw": raw_message
        }
    ).execute()
    
    print("Email sent successfully")
    
except Exception as e : 
    print("Error in Send Mail Log Script {}".format(e))
