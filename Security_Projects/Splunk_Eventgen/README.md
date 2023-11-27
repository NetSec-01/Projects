# **Overview:**

> Used to generate security events as per the sample file using Splunk Eventgen.
> The events can be outputted to splunk and analyzed using SPL(Search  Processing Language) query. 

-***********************************************************************************-

# **Installation Requirements:**

> Splunk and Eventgen has to be installed on the local system.

-***********************************************************************************-

# **File Placements:**

> To ensure zero issues, make sure to place the files in the below mentioned folders.
> Sample Files; which includes below mentioned files has to be placed into 'samples'   direcroty under SA-Eventgen (path: /opt/splunk/etc/apps/SA-Eventgen/samples) 
> As a best practice for this project, ensure to install the 'splunk' application in '/opt' directory.

> > Files to be placed in samples folder, 
> > 1) security_log.sample
> > 2) action.sample
> > 3) countries.sample
> > 4) companies.sample
> > 5) ip_address_1.sample
> > 6) usernames.sample

-***********************************************************************************-

# **Files Description:**

> This section describes the information contained in the sample files and eventgen.conf file. 
    
> ## I) SampleFiles: 

> > > ### 1) security_log.sample:
        
        This file contains the structure of the event in key,value pairs .json format. The eventgen.conf file is used to change the 'values'of this security_log.sample file by randomly picking the the inputs provided from the other sample values.

        ─$ cat security_log.sample 
        { "Event_Time":"2023-11-23 16:30:20", "src_ip":"100.40.50.10", "UserName":"sa           muel", "Action":"Success",  "Source_Country":"Spain", "Company":"Cyber_Tec          h", "Protocol":"tcp", "Port":"443" }

> > > ### 2) action.sample:

        This file has the values of 'Success' and  'Failed'.

        Note: If you want to see more failed events, edit the file with more 'Failed'           vales, vice-versa.
            
                └─$ cat action.sample 
                Failed
                Failed
                Failed
                Failed
                Failed
                Success

> > > ### 3) countries.sample:

        This file has the different country names that would be distributed aross events. 

                └─$ cat countries.sample 
                South Korea
                Spain
                Australia
                Mexico
                Brazil
                Germany
                Russia
                China
                North Korea
                Austria

> > > ### 4) companies.sample:

        This file has different company names.

                └─$ cat companies.sample 
                Cyber Tek
                Massive Dynamic
                Office Communications

> > > ### 5) ip_address_1.sample
        
        This file has different ip-addresses that would be randomly distributed across the events.


        └─$ cat ip_address_1.sample 
        100.30.45.12
        160.100.150.223
        9.6.90.198
        20.56.89.196
                       

> > > ### 6) usernames.sample:

         This file has the different usernames.

        └─$ cat usernames.sample   
        samuel123
        Mimi065
        John987


> ## II) eventgen.conf File:

        This file has all the configuration that's used to drive the generator in generating the events as per the selected sample file. 

        Note: The parameter definations and supporting values can be referred from below link.

        https://splunk.github.io/eventgen/REFERENCE.html#eventgenconfspec

        ─$ cat eventgen.conf
        [security_log.sample]
        index = security
        mode = sample
        interval = 10
        earliest = -10s
        latest = now
        count = 20
        hourOfDayRate = { "0": 0.8, "1": 0.8, "2": 0.8, "3": 0.7, "4": 0.2, "5": 0.8, "6": 0.8, "7": 0.8, "8": 0.8, "9": 0.8, "10": 0.8, "11": 0.8, "12": 0.8, "13": 0.8, "1                            4": 0.8, "15": 0.8, "16": 0.8, "17": 1, "18": 1.2, "19": 0.8, "20": 0.8, "21": 0.8, "22": 0.8, "23": 0.8, "24": 2 }
        dayOfWeekRate = { "0": 0.7, "1": 0.8, "2": 0.7, "3": 0.5, "4": 1.0, "5":1.0, "6":1.0 }
        randomizeCount = 0.2
        randomizeEvents = true
        outputMode = modinput
        sourcetype = networksecurity
        source = devices
        ##Change the Timestamp to today's date
        token.0.token = \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}
        token.0.replacementType = timestamp
        token.0.replacement = %Y-%m-%d %H:%M:%S

        ##Change the source_IP to a list of addresses saved onto ip_address_1.sample
        token.1.token = "src_ip":"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\"
        token.1.replacementType = file
        token.1.replacement = /opt/splunk/etc/apps/SA-Eventgen/samples/ip_address_1.sample

        ##Change the Source_Country to a list of addresses saved onto Countries File.
        token.2.token = "Source_Country"\:\"(\w+)\"
        token.2.replacementType = file
        token.2.replacement = /opt/splunk/etc/apps/SA-Eventgen/samples/countries.sample

        ## Randomly select the user name from username.sample file
        token.3.token = "UserName"\:\"(\w+)\"
        token.3.replacementType = file
        token.3.replacement = /opt/splunk/etc/apps/SA-Eventgen/samples/usernames.sample

        ## Randomly select the company name from companies.sample file
        token.4.token = "Company"\:\"(\w+)\"
        token.4.replacementType = file
        token.4.replacement = /opt/splunk/etc/apps/SA-Eventgen/samples/companies.sample


        ## Randonly select the action status from action.sample file
        token.5.token = "Action":\"(\w+)\"
        token.5.replacementType = file
        token.5.replacement = /opt/splunk/etc/apps/SA-Eventgen/samples/action.sample
