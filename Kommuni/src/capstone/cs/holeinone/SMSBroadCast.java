package capstone.cs.holeinone;


import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.database.Cursor;
import android.net.Uri;
import android.os.Bundle;
import android.os.Environment;
import android.provider.ContactsContract;
import android.telephony.SmsMessage;
import android.util.Log;
import android.widget.Toast;


public class SMSBroadCast extends BroadcastReceiver {

    @Override
    public void onReceive(Context mContext, Intent intent) {
    	String action =  intent.getAction();
    	
    	if("android.provider.Telephony.SMS_RECEIVED".equals(action)){
    		  //�޽��� �Ľ�		
    		Log.d("onReceive()","���ڰ� ���ŵǾ����ϴ�!");
 
    		Bundle bundle = intent.getExtras();
    		Object messages[] = (Object[])bundle.get("pdus");
    		SmsMessage smsMessage[] = new SmsMessage[messages.length];

    		for(int i = 0; i < messages.length; i++) { //PDU���� ������ �޽����� ����
    		    smsMessage[i] = SmsMessage.createFromPdu((byte[])messages[i]);
    		}
    		
    		Date curDate = new Date(smsMessage[0].getTimestampMillis());  	
    		Log.d("���� ���� �ð�", curDate.toString());
    		
    		SimpleDateFormat mDateFormat = new SimpleDateFormat(
    				"yyyy�� MM�� dd�� HH�� mm�� ss��",Locale.KOREA);
    		String originDate = mDateFormat.format(curDate);
    		
    		String origNumber = smsMessage[0].getOriginatingAddress();
    		
    		 //�߽Ź�ȣ�� ����ó�� ����� �̸����� ����
            Uri uri = Uri.withAppendedPath(ContactsContract.PhoneLookup.CONTENT_FILTER_URI, Uri.encode(origNumber));
            String[] projection = new String[] {ContactsContract.PhoneLookup.DISPLAY_NAME};
            String displayName = "";
                      
            Cursor cursor = mContext.getContentResolver().query(uri, projection, null, null, null);
            if (cursor != null) {
                if (cursor.moveToFirst()){
                    displayName = cursor.getString(0);              
                }        

                cursor.close();
            }
            
    		String Message = smsMessage[0].getMessageBody().toString();
    		Log.d("���� ����", "�߽��� : "+origNumber+", ���� : "+Message);
    		
    		
    		saveFile(Message);
    		
    		
    		Intent showSMSIntent = new Intent(mContext, ShowSMSActivity.class);
    		showSMSIntent.putExtra("originNum", displayName);
    		showSMSIntent.putExtra("smsDate", originDate);
    		showSMSIntent.putExtra("originText", Message);
    		
    		showSMSIntent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
    		
    		mContext.startActivity(showSMSIntent);
    	}
    }
    
    /**
	 * ���ŵ� �޽����� �ܸ��⿡ �����մϴ�
	 */
    public void saveFile(String message){
    	
		 File file;
         String path = Environment.getExternalStorageDirectory().getAbsolutePath()+"/Download/";
         file = new File(path+"output.txt");
         
         FileOutputStream fos = null;
         try{
        	 
         	fos = new FileOutputStream(file);
         	fos.write((message).getBytes());
         	fos.close();
         	
         	
         }catch(IOException e){
         	e.printStackTrace();
         }
         
         
    }

}