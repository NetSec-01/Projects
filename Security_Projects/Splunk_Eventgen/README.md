Overview:

-Used to generate security events as per the sample file using Splunk Eventgen.
-The events can be outputted to splunk and analyzed using SPL(Search  Processing Language) query. 

-***********************************************************************************-

Installation Requirements:

Splunk and Eventgen has to be installed on the local system.

-***********************************************************************************-

File Placements:

-To ensure zero issues, make sure to place the files in the below mentioned folders.
-Sample Files; which includes below mentioned files has to be placed into 'samples'   direcroty under SA-Eventgen (path: /opt/splunk/etc/apps/SA-Eventgen/samples) 
 ensure to isntall the 'splunk' application in '/opt' directory.
 Files to be placed in samples folder, 
 1) security_log.sample
 2) action.sample
 3) countries.sample
 4) companies.sample
 5) ip_address_1.sample
 6) usernames.sample

-***********************************************************************************-

Files Description:

This section describes the information contained in the sample files and eventgen.conf file. 
    
 I) SampleFiles: 
    
    1) security_log.sample:
        
        This file contains the structure of the event in key,value pairs .json format. The eventgen.conf file is used to change the 'values'of this security_log.sample file by randomly picking the the inputs provided from the other sample values.

      Output of security_log.sample: 
        { "Event_Time":"2023-11-23 16:30:20", "src_ip":"100.40.50.10", "UserName":"sa           muel", "Action":"Success",  "Source_Country":"Spain", "Company":"Cyber_Tec          h", "Protocol":"tcp", "Port":"443" }

    2) action.sample:

        This file has the values of 'Success' and  'Failed'.

        Note: If you want to see more failed events, edit the file with more 'Failed'           vales, vice-versa.
            
                └─$ cat action.sample 
                Failed
                Failed
                Failed
                Failed
                Failed
                Success
