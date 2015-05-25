package capstone.cs.holeinone;

import android.app.Activity;
import android.app.NotificationManager;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.media.AudioManager;
import android.os.Bundle;
import android.speech.tts.TextToSpeech;
import android.support.v4.app.NotificationCompat;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.TextView;
import android.widget.Toast;


import java.util.Locale;

/**
 * Created by shinjiung on 15. 5. 17..
 */
public class MainActivity extends Activity implements
        TextToSpeech.OnInitListener {

    private TextView txtView;
    public NotificationKakao nKakao;
    public NotificationMessage nMessage;
    private TextToSpeech tts;
    private String temp;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_kakao);

        final CheckBox option1 = (CheckBox) findViewById(R.id.option1);
        final CheckBox option2 = (CheckBox) findViewById(R.id.option2);
        Button setupBtn = (Button) findViewById(R.id.setup_button);
        Button canReadBtn = (Button) findViewById(R.id.canReadBtn);
        setVolumeControlStream(AudioManager.STREAM_MUSIC);
        tts = new TextToSpeech(this,this);

        canReadBtn.setOnClickListener(new Button.OnClickListener() {
            public void onClick(View v) {
                Intent intent = new Intent("android.settings.ACTION_NOTIFICATION_LISTENER_SETTINGS");
                startActivity(intent);
            }
        });

        setupBtn.setOnClickListener(new Button.OnClickListener() {
            public void onClick(View v) {

                if(option1.isChecked()) {
                    nKakao = new NotificationKakao();
                    IntentFilter filter = new IntentFilter();
                    filter.addAction("com.example.shinjiung.notificationtest.NOTIFICATION_LISTENER_EXAMPLE.Kakaotalk");
                    registerReceiver(nKakao,filter);
                }
                else {
                   onDestroyKakao();
                }
                if(option2.isChecked()) {
                    nMessage = new NotificationMessage();
                    IntentFilter filter = new IntentFilter();
                    filter.addAction("com.example.shinjiung.notificationtest.NOTIFICATION_LISTENER_EXAMPLE.Message");
                    registerReceiver(nMessage,filter);
                }
                else {
                    onDestroyMessage();
                }
                Toast.makeText(getApplicationContext(), "설정이 완료되었습니다.", Toast.LENGTH_SHORT).show();

            }
        });


    }

    protected void onDestroyKakao() {
        super.onDestroy();
        if (nKakao!=null) {
            unregisterReceiver(nKakao);
            nKakao=null;
        }
    }
    protected void onDestroyMessage() {
        super.onDestroy();
        if (nMessage!=null) {
            unregisterReceiver(nMessage);
            nMessage=null;
        }
    }



    @Override
    public void onInit(int status) {

        if (status == TextToSpeech.SUCCESS) {

            int result = tts.setLanguage(Locale.KOREAN);

            if (result == TextToSpeech.LANG_MISSING_DATA
                    || result == TextToSpeech.LANG_NOT_SUPPORTED) {
                Log.e("TTS", "This Language is not supported");
            } else {
                speakOut();
            }

        } else {
            Log.e("TTS", "Initilization Failed!");
        }

    }

    private void speakOut() {

        tts.speak(temp, TextToSpeech.QUEUE_ADD, null);
    }

    public class NotificationKakao extends BroadcastReceiver {

        @Override
        public void onReceive(Context context, Intent intent) {
            temp = intent.getStringExtra("notification_kakao");
            Log.d("test", "temp" +":" +temp);
            speakOut();

        }
    }
    public class NotificationMessage extends BroadcastReceiver {

        @Override
        public void onReceive(Context context, Intent intent) {
            temp = intent.getStringExtra("notification_message");
            Log.d("test", "temp" +":" +temp);
            speakOut();
        }
    }



}