import json
from pprint import pprint
import glob, os

header = "apkName,accessed_file,recvsaction_android.intent.action.UMS_DISCONNECTED,recvsaction_android.intent.action.ACTION_POWER_CONNECTED,recvsaction_android.intent.action.ACTION_SHUTDOWN,recvsaction_android.provider.Telephony.SMS_RECEIVED,recvsaction_android.intent.action.SIG_STR,recvsaction_com.android.vending.INSTALL_REFERRER,recvsaction_android.intent.action.NEW_OUTGOING_CALL,recvsaction_android.provider.Telephony.WAP_PUSH_RECEIVED,recvsaction_android.intent.action.BOOT_COMPLETED,recvsaction_android.intent.action.PHONE_STATE,recvsaction_android.intent.action.PACKAGE_REMOVED,recvsaction_android.intent.action.USER_PRESENT,data_leaks_count,tag_count,servicestart_found_com.android.mms.transaction.SmsReceiverService,servicestart_found_com.android.contacts.ViewNotificationService,servicestart_found_com.android.battery.BridgeProvider,servicestart_found_com.safetest.tractor.UpdateService,servicestart_found_com.android.providers.downloads.DownloadService,servicestart_found_com.android.contacts.calllog.CallLogNotificationsService,servicestart_found_com.safetest.five.SoundService,servicestart_found_com.geinimi.custom.GoogleKeyboard,tag_name_TAINT_LOCATION,tag_name_TAINT_CONTACTS,tag_name_TAINT_MIC,tag_name_TAINT_PHONE_NUMBER,tag_name_TAINT_LOCATION_GPS,tag_name_TAINT_LOCATION_NET,tag_name_TAINT_LOCATION_LAST,tag_name_TAINT_CAMERA,tag_name_TAINT_ACCELEROMETER,tag_name_TAINT_SMS,tag_name_TAINT_IMEI,tag_name_TAINT_IMSI,tag_name_TAINT_ICCID,tag_name_TAINT_DEVICE_SN,tag_name_TAINT_ACCOUNT,tag_name_TAINT_BROWSER,tag_name_TAINT_OTHERDB,tag_name_TAINT_FILECONTENT,tag_name_TAINT_PACKAGE,tag_name_TAINT_CALL_LOG,tag_name_TAINT_EMAIL,tag_name_TAINT_CALENDAR,tag_name_TAINT_SETTINGS,fdaccess_pipe,fdaccess_cmdline,fdaccess_shared_prefs,fdaccess_dat,fdaccess_sdcard,fdaccess_info,fdaccess_jar,fdaccess_db,fdaccess_txt,fdaccess_urandom,fdaccess_if_inet6,phonecalls,sendsms,label"
#header = "apkName,recvsaction_android.intent.action.UMS_DISCONNECTED,recvsaction_android.intent.action.ACTION_POWER_CONNECTED,recvsaction_android.intent.action.ACTION_SHUTDOWN,recvsaction_android.provider.Telephony.SMS_RECEIVED,recvsaction_android.intent.action.SIG_STR,recvsaction_com.android.vending.INSTALL_REFERRER,recvsaction_android.intent.action.NEW_OUTGOING_CALL,recvsaction_android.provider.Telephony.WAP_PUSH_RECEIVED,recvsaction_android.intent.action.BOOT_COMPLETED,recvsaction_android.intent.action.PHONE_STATE,recvsaction_android.intent.action.PACKAGE_REMOVED,recvsaction_android.intent.action.USER_PRESENT,data_leaks_count,tag_count,servicestart_found_com.android.mms.transaction.SmsReceiverService,servicestart_found_com.android.contacts.ViewNotificationService,servicestart_found_com.android.battery.BridgeProvider,servicestart_found_com.safetest.tractor.UpdateService,servicestart_found_com.android.providers.downloads.DownloadService,servicestart_found_com.android.contacts.calllog.CallLogNotificationsService,servicestart_found_com.safetest.five.SoundService,servicestart_found_com.geinimi.custom.GoogleKeyboard,tag_name_TAINT_LOCATION,tag_name_TAINT_CONTACTS,tag_name_TAINT_MIC,tag_name_TAINT_PHONE_NUMBER,tag_name_TAINT_LOCATION_GPS,tag_name_TAINT_LOCATION_NET,tag_name_TAINT_LOCATION_LAST,tag_name_TAINT_CAMERA,tag_name_TAINT_ACCELEROMETER,tag_name_TAINT_SMS,tag_name_TAINT_IMEI,tag_name_TAINT_IMSI,tag_name_TAINT_ICCID,tag_name_TAINT_DEVICE_SN,tag_name_TAINT_ACCOUNT,tag_name_TAINT_BROWSER,tag_name_TAINT_OTHERDB,tag_name_TAINT_FILECONTENT,tag_name_TAINT_PACKAGE,tag_name_TAINT_CALL_LOG,tag_name_TAINT_EMAIL,tag_name_TAINT_CALENDAR,tag_name_TAINT_SETTINGS,fdaccess_pipe,fdaccess_cmdline,fdaccess_shared_prefs,fdaccess_dat,fdaccess_sdcard,fdaccess_info,fdaccess_jar,fdaccess_db,fdaccess_txt,fdaccess_urandom,fdaccess_if_inet6,phonecalls,sendsms,label"

#print header

log_dir = "/media/waqar/store/android-sdk/DroidBox_4.1.1/Malicious-Logs/log-summaries" 
store = open("values.csv", "w+");
store.write(header+"\n")

#result = []

print "\nPlease wait... Converting data from JSON to CSV....\n"

os.chdir(log_dir)
for jsonlog in glob.glob("*.log"):
#	print jsonlog
	with open(jsonlog) as data_file:    
		data = json.load(data_file)
#		pprint(data)

		store.write("\n")
		for key,value in data.items():

			if key == str("apkName"):
				x = value[51:-4]
				store.write(x+",")
	
			elif key == str("count_accessed_file"):
				if str(value) == 0:
					store.write(str("0")+",")
				else:
					store.write(str("1")+",")
					
			elif key == str("data_leaks_count"):
				if value == -1:
					store.write(str(0)+",")
				else:
					store.write(str(value)+",")
	
			elif key == str("fdaccess"):
		
				if str(value).find("pipe") != -1:
					store.write("1"+",")
				else:
					store.write("0"+",")

				if str(value).find("cmdline") != -1:
					store.write("1"+",")
				else:
					store.write("0"+",")

				if str(value).find("prefs") != -1:			
					store.write("1"+",")
				else:
					store.write("0"+",")

				if str(value).find("dat") != -1:			
					store.write("1"+",")
				else:
					store.write("0"+",")

				if str(value).find("sdcard") != -1:			
					store.write("1"+",")
				else:
					store.write("0"+",")

				if str(value).find("info") != -1:			
					store.write("1"+",")
				else:
					store.write("0"+",")

				if str(value).find("jar") != -1:			
					store.write("1"+",")
				else:
					store.write("0"+",")

				if str(value).find("db") != -1:			
					store.write("1"+",")
				else:
					store.write("0"+",")

				if str(value).find("txt") != -1:			
					store.write("1"+",")
				else:
					store.write("0"+",")

				if str(value).find("urandom") != -1:			
					store.write("1"+",")
				else:
					store.write("0"+",")

				if str(value).find("if_inet6") != -1:
					store.write("1"+",")
				else:
					store.write("0"+",")

			elif key == str("recvsaction"):
#				print value

				if str(value).find("UMS_DISCONNECTED") != -1:
					store.write("1"+",")
				else:
					store.write("0"+",")
		
				if str(value).find("ACTION_POWER_CONNECTED") != -1:
					store.write("1"+",")
				else:
					store.write("0"+",")

				if str(value).find("ACTION_SHUTDOWN") != -1:
					store.write("1"+",")
				else:
					store.write("0"+",")

				if str(value).find("SMS_RECEIVED") != -1:
					store.write("1"+",")
				else:
					store.write("0"+",")

				if str(value).find("SIG_STR") != -1:
					store.write("1"+",")
				else:
					store.write("0"+",")

				if str(value).find("INSTALL_REFERRER") != -1:
					store.write("1"+",")
				else:
					store.write("0"+",")

				if str(value).find("NEW_OUTGOING_CALL") != -1:
					store.write("1"+",")
				else:
					store.write("0"+",")

				if str(value).find("WAP_PUSH_RECEIVED") != -1:
					store.write("1"+",")
				else:
					store.write("0"+",")

				if str(value).find("BOOT_COMPLETED") != -1:
					store.write("1"+",")
				else:
					store.write("0"+",")

				if str(value).find("PHONE_STATE") != -1:
					store.write("1"+",")
				else:
					store.write("0"+",")

				if str(value).find("PACKAGE_REMOVED") != -1:
					store.write("1"+",")
				else:
					store.write("0"+",")

				if str(value).find("USER_PRESENT") != -1:
					store.write("1"+",")
				else:
					store.write("0"+",")

			elif key == str("phonecalls"):
				if str(value) == "{}":
					store.write(str("0")+",")
				else:
					store.write(str("1")+",")

			elif key == str("sendsms"):
				if str(value) == "{}":
					store.write(str("0")+",")
				else:
					store.write(str("1")+",")
					
			elif key == str("servicestart_found"):
				if str(value).find("SmsReceiverService") != -1:			
					store.write("1"+",")
				else:
					store.write("0"+",")
			
				if str(value).find("ViewNotificationService") != -1:		
					store.write("1"+",")
				else:
					store.write("0"+",")

				if str(value).find("BridgeProvider") != -1:		
					store.write("1"+",")
				else:
					store.write("0"+",")

				if str(value).find("UpdateService") != -1:		
					store.write("1"+",")
				else:
					store.write("0"+",")

				if str(value).find("DownloadService") != -1:		
					store.write("1"+",")
				else:
					store.write("0"+",")

				if str(value).find("CallLogNotificationsService") != -1:		
					store.write("1"+",")
				else:
					store.write("0"+",")

				if str(value).find("SoundService") != -1:		
					store.write("1"+",")
				else:
					store.write("0"+",")

				if str(value).find("GoogleKeyboard") != -1:		
					store.write("1"+",")
				else:
					store.write("0"+",")

			elif key == str("tag_count"):
				if value == -1:
					store.write(str(0)+",")
				else:
					store.write(str(value)+",")

			elif key == str("tag_name"):
				if str(value).find("TAINT_LOCATION") != -1:
					store.write("1"+",")
				else:
					store.write("0"+",")

				if str(value).find("TAINT_CONTACTS") != -1:		
					store.write("1"+",")
				else:
					store.write("0"+",")
				if str(value).find("TAINT_MIC") != -1:		
					store.write("1"+",")
				else:
					store.write("0"+",")
				if str(value).find("TAINT_PHONE_NUMBER") != -1:		
					store.write("1"+",")
				else:
					store.write("0"+",")
				if str(value).find("TAINT_LOCATION_GPS") != -1:		
					store.write("1"+",")
				else:
					store.write("0"+",")
				if str(value).find("TAINT_LOCATION_NET") != -1:		
					store.write("1"+",")
				else:
					store.write("0"+",")
				if str(value).find("TAINT_LOCATION_LAST") != -1:		
					store.write("1"+",")
				else:
					store.write("0"+",")
				if str(value).find("TAINT_CAMERA") != -1:		
					store.write("1"+",")
				else:
					store.write("0"+",")
				if str(value).find("TAINT_ACCELEROMETER") != -1:		
					store.write("1"+",")
				else:
					store.write("0"+",")
				if str(value).find("TAINT_SMS") != -1:		
					store.write("1"+",")
				else:
					store.write("0"+",")
				if str(value).find("TAINT_IMEI") != -1:		
					store.write("1"+",")
				else:
					store.write("0"+",")
				if str(value).find("TAINT_IMSI") != -1:		
					store.write("1"+",")
				else:
					store.write("0"+",")
				if str(value).find("TAINT_ICCID") != -1:		
					store.write("1"+",")
				else:
					store.write("0"+",")
				if str(value).find("TAINT_DEVICE_SN") != -1:		
					store.write("1"+",")
				else:
					store.write("0"+",")
				if str(value).find("TAINT_ACCOUNT") != -1:		
					store.write("1"+",")
				else:
					store.write("0"+",")
				if str(value).find("TAINT_BROWSER") != -1:		
					store.write("1"+",")
				else:
					store.write("0"+",")
				if str(value).find("TAINT_OTHERDB") != -1:		
					store.write("1"+",")
				else:
					store.write("0"+",")
				if str(value).find("TAINT_FILECONTENT") != -1:		
					store.write("1"+",")
				else:
					store.write("0"+",")
				if str(value).find("TAINT_PACKAGE") != -1:		
					store.write("1"+",")
				else:
					store.write("0"+",")
				if str(value).find("TAINT_CALL_LOG") != -1:		
					store.write("1"+",")
				else:
					store.write("0"+",")
				if str(value).find("TAINT_EMAIL") != -1:		
					store.write("1"+",")
				else:
					store.write("0"+",")
				if str(value).find("TAINT_CALENDAR") != -1:		
					store.write("1"+",")
				else:
					store.write("0"+",")
				if str(value).find("TAINT_SETTINGS") != -1:		
					store.write("1"+",")
				else:
					store.write("0"+",")

		store.write("1"+",")
store.close()

print "All Done..."
