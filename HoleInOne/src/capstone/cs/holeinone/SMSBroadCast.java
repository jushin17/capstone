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
    		  //메시지 파싱		
    		Log.d("onReceive()","문자가 수신되었습니다!");
 
    		Bundle bundle = intent.getExtras();
    		Object messages[] = (Object[])bundle.get("pdus");
    		SmsMessage smsMessage[] = new SmsMessage[messages.length];

    		for(int i = 0; i < messages.length; i++) { //PDU포맷 형식의 메시지를 복원
    		    smsMessage[i] = SmsMessage.createFromPdu((byte[])messages[i]);
    		}
    		
    		Date curDate = new Date(smsMessage[0].getTimestampMillis());  	
    		Log.d("문자 수신 시간", curDate.toString());
    		
    		SimpleDateFormat mDateFormat = new SimpleDateFormat(
    				"yyyy년 MM월 dd일 HH시 mm분 ss초",Locale.KOREA);
    		String originDate = mDateFormat.format(curDate);
    		
    		String origNumber = smsMessage[0].getOriginatingAddress();
    		
    		 //발신번호를 연락처에 저장된 이름으로 변경
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
    		Log.d("문자 내용", "발신자 : "+origNumber+", 내용 : "+Message);
    		
    		
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
	 * 수신된 메시지를 단말기에 저장합니다
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