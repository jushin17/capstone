package capstone.cs.holeinone;

import capstone.cs.holeinone.R;
import android.app.Activity;
import android.app.PendingIntent;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.os.Bundle;
import android.telephony.SmsManager;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends Activity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
    	// TODO Auto-generated method stub
    	super.onCreate(savedInstanceState);
    	setContentView(R.layout.activity_main);
    	
    	Button nextB = (Button)findViewById(R.id.next_button);
    	nextB.setOnClickListener(new Button.OnClickListener() {
    		public void onClick(View v) {
    			Intent intent = new Intent(MainActivity.this, SendSMSActivity.class);
    			startActivity(intent);
    		}
    	});
    }
}
