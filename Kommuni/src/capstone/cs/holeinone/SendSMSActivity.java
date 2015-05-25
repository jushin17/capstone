package capstone.cs.holeinone;

import android.app.Activity;
import android.app.PendingIntent;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.database.Cursor;
import android.net.Uri;
import android.os.Bundle;
import android.provider.ContactsContract;
import android.telephony.SmsManager;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

public class SendSMSActivity extends Activity{
	Context mContext;
    EditText smsNumber, smsTextContext;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_sendsms);
        
        mContext = this;
        
        smsNumber = (EditText) findViewById(R.id.smsNumber);
        smsTextContext = (EditText) findViewById(R.id.smsText);
    }
    
    public void sendSMS(View v){
        String smsNum = smsNumber.getText().toString();
        String smsText = smsTextContext.getText().toString();
        
        if (smsNum.length()>0 && smsText.length()>0){
            sendSMS(smsNum, smsText);
        }else{
            Toast.makeText(this, "모두 입력해 주세요", Toast.LENGTH_SHORT).show();
        }
    }
    

    public void sendSMS(String smsNumber, String smsText){
 
    	PendingIntent sentIntent = PendingIntent.getBroadcast(this, 0, new Intent("SMS_SENT_ACTION"), 0); //SMS 전송 성공 여부를 알기 위해 등록, 결과 확인
        PendingIntent deliveredIntent = PendingIntent.getBroadcast(this, 0, new Intent("SMS_DELIVERED_ACTION"), 0); //문자 도착 결과 확인
        
       //SMS 전송시
        registerReceiver(new BroadcastReceiver() { //BroadcastReceiver를 통해 결과 확인
            
        	//CallBack method, 상대방이 메시지를 실제로 수신했는지 파악
        	//통신망으로부터 상대방 단말기가 메시지를 받았다는 확인 통지를 받은 시점에서 호출
        	@Override
            public void onReceive(Context context, Intent intent) {
            	           	            	
                switch(getResultCode()){
                    case Activity.RESULT_OK:
                        // 전송 성공
                        Toast.makeText(mContext, "전송 완료", Toast.LENGTH_SHORT).show();
                        break;
                    case SmsManager.RESULT_ERROR_GENERIC_FAILURE:
                        // 전송 실패
                        Toast.makeText(mContext, "전송 실패", Toast.LENGTH_SHORT).show();
                        break;
                    case SmsManager.RESULT_ERROR_NO_SERVICE:
                        // 서비스 지역 아님
                        Toast.makeText(mContext, "서비스 지역이 아닙니다", Toast.LENGTH_SHORT).show();
                        break;
                    case SmsManager.RESULT_ERROR_RADIO_OFF:
                        // 무선 꺼짐
                        Toast.makeText(mContext, "무선(Radio)가 꺼져있습니다", Toast.LENGTH_SHORT).show();
                        break;
                    case SmsManager.RESULT_ERROR_NULL_PDU:
                        // PDU 실패
                        Toast.makeText(mContext, "PDU Null", Toast.LENGTH_SHORT).show();
                        break;
                }
            }
        }, new IntentFilter("SMS_SENT_ACTION"));
        
        
        //SMS 도착시
        registerReceiver(new BroadcastReceiver() {
            @Override
            public void onReceive(Context context, Intent intent) {
                switch (getResultCode()){
                    case Activity.RESULT_OK:
                        // 도착 완료
                        Toast.makeText(mContext, "SMS 도착 완료", Toast.LENGTH_SHORT).show();
                        break;
                    case Activity.RESULT_CANCELED:
                        // 도착 안됨
                        Toast.makeText(mContext, "SMS 도착 실패", Toast.LENGTH_SHORT).show();
                        break;
                }
            }
        }, new IntentFilter("SMS_DELIVERED_ACTION"));
      
        
      SmsManager mSmsManager = SmsManager.getDefault();
      mSmsManager.sendTextMessage(smsNumber, null, smsText, sentIntent, deliveredIntent); //SMS 전송

    }

}
