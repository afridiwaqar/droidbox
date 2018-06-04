Intro
========

DroidBox is developed to offer dynamic analysis of Android applications. The following information is described in the results, generated when analysis is complete:

- Hashes for the analyzed package
- Incoming/outgoing network data
- File read and write operations
- Started services and loaded classes through DexClassLoader
- Information leaks via the network, file and SMS
- Circumvented permissions
- Cryptographic operations performed using Android API
- Listing broadcast receivers
- Sent SMS and phone calls

Working
========

1. An APK is passed to droidbox as a parameter along with the amount of time the APK should run.
2. The Droidbox launches Android's Virtual Machine 
3. Droidbox then installs the APK on Android's virtual machine using MonkeyRunner
4. The App then begin execution for the specied amount of time
5. The App start running on the virtual machine and all the information is gathered using logcat
6. During the time of App execution, certain events are injected to android's virtual machine as there may have been some malicious apps that might be waiting for certain event to occur in order to perform some malicious task.
7. The gathered activity log is then forward to droidbox where it is parsed and useful information is extracted and given the json format and then converted to a CSV.
8. The information is CSV is used to train and test various machine learning algorithms
9. Based on the trained and tested algorithm, new fresh information regarding an App is given to the machine learning algorithm where is predicts whether the App is malicious or benign.

How to Run
==========

1. Download Android System Images from the link (https://drive.google.com/open?id=17otDE8U7eNHj2I-_LeDK8vCdZc0cu1Jw) and place them in "images" folder. Create folder if not already exisits.
2. Run the setupenv.sh script to setup envirnoment variables.
3. Next, Everyhting is automated, Just Run the analyze.sh
