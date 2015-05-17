package capstone.cs.holeinone;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

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
     	    	
    	Button blue = (Button)findViewById(R.id.blue_button);
    	blue.setOnClickListener(new Button.OnClickListener() {
    		public void onClick(View v) {
    			Intent intent2 = new Intent(MainActivity.this, KakaoActivity.class);
    			startActivity(intent2);
    		}
    	});
    }
}
