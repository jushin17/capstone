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
            Toast.makeText(this, "��� �Է��� �ּ���", Toast.LENGTH_SHORT).show();
        }
    }
    

    public void sendSMS(String smsNumber, String smsText){
 
    	PendingIntent sentIntent = PendingIntent.getBroadcast(this, 0, new Intent("SMS_SENT_ACTION"), 0); //SMS ���� ���� ���θ� �˱� ���� ���, ��� Ȯ��
        PendingIntent deliveredIntent = PendingIntent.getBroadcast(this, 0, new Intent("SMS_DELIVERED_ACTION"), 0); //���� ���� ��� Ȯ��
        
       //SMS ���۽�
        registerReceiver(new BroadcastReceiver() { //BroadcastReceiver�� ���� ��� Ȯ��
            
        	//CallBack method, ������ �޽����� ������ �����ߴ��� �ľ�
        	//��Ÿ����κ��� ���� �ܸ��Ⱑ �޽����� �޾Ҵٴ� Ȯ�� ������ ���� �������� ȣ��
        	@Override
            public void onReceive(Context context, Intent intent) {
            	           	            	
                switch(getResultCode()){
                    case Activity.RESULT_OK:
                        // ���� ����
                        Toast.makeText(mContext, "���� �Ϸ�", Toast.LENGTH_SHORT).show();
                        break;
                    case SmsManager.RESULT_ERROR_GENERIC_FAILURE:
                        // ���� ����
                        Toast.makeText(mContext, "���� ����", Toast.LENGTH_SHORT).show();
                        break;
                    case SmsManager.RESULT_ERROR_NO_SERVICE:
                        // ���� ���� �ƴ�
                        Toast.makeText(mContext, "���� ������ �ƴմϴ�", Toast.LENGTH_SHORT).show();
                        break;
                    case SmsManager.RESULT_ERROR_RADIO_OFF:
                        // ���� ����
                        Toast.makeText(mContext, "����(Radio)�� �����ֽ��ϴ�", Toast.LENGTH_SHORT).show();
                        break;
                    case SmsManager.RESULT_ERROR_NULL_PDU:
                        // PDU ����
                        Toast.makeText(mContext, "PDU Null", Toast.LENGTH_SHORT).show();
                        break;
                }
            }
        }, new IntentFilter("SMS_SENT_ACTION"));
        
        
        //SMS ������
        registerReceiver(new BroadcastReceiver() {
            @Override
            public void onReceive(Context context, Intent intent) {
                switch (getResultCode()){
                    case Activity.RESULT_OK:
                        // ���� �Ϸ�
                        Toast.makeText(mContext, "SMS ���� �Ϸ�", Toast.LENGTH_SHORT).show();
                        break;
                    case Activity.RESULT_CANCELED:
                        // ���� �ȵ�
                        Toast.makeText(mContext, "SMS ���� ����", Toast.LENGTH_SHORT).show();
                        break;
                }
            }
        }, new IntentFilter("SMS_DELIVERED_ACTION"));
      
        
      SmsManager mSmsManager = SmsManager.getDefault();
      mSmsManager.sendTextMessage(smsNumber, null, smsText, sentIntent, deliveredIntent); //SMS ����

    }

}