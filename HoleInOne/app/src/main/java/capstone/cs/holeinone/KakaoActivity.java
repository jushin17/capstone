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


import java.util.Locale;

/**
 * Created by shinjiung on 15. 5. 17..
 */
public class KakaoActivity extends Activity implements
        TextToSpeech.OnInitListener {

    private TextView txtView;
    public NotificationShow nShow;
    public NotificationSpeech nSpeech;
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
        /*
        nReceiver = new NotificationReceiver();
        IntentFilter filter = new IntentFilter();
        filter.addAction("com.example.shinjiung.notificationtest.NOTIFICATION_LISTENER_EXAMPLE");
        registerReceiver(nReceiver,filter);
        tts = new TextToSpeech(this,this);*/
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
                    nSpeech = new NotificationSpeech();
                    IntentFilter filter = new IntentFilter();
                    filter.addAction("com.example.shinjiung.notificationtest.NOTIFICATION_LISTENER_EXAMPLE");
                    registerReceiver(nSpeech,filter);
                }
                else {
                    onDestroySpeech();
                }
                if(option2.isChecked()) {
                    nShow = new NotificationShow();
                    IntentFilter filter = new IntentFilter();
                    filter.addAction("com.example.shinjiung.notificationtest.NOTIFICATION_LISTENER_EXAMPLE");
                    registerReceiver(nShow,filter);
                }
                else {
                    onDestroyShow();
                }

            }
        });


    }

    protected void onDestroySpeech() {
        super.onDestroy();
        if (nSpeech!=null) {
            unregisterReceiver(nSpeech);
            nSpeech=null;
        }
    }
    protected void onDestroyShow() {
        super.onDestroy();
        if (nShow!=null) {
            unregisterReceiver(nShow);
            nShow=null;
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

    public class NotificationShow extends BroadcastReceiver {

        @Override
        public void onReceive(Context context, Intent intent) {
            temp = intent.getStringExtra("notification_event");
            Log.d("test", "temp" +":" +temp);

            //라즈베리파이로 보내는 부분 적용하면 될듯

        }
    }
    public class NotificationSpeech extends BroadcastReceiver {

        @Override
        public void onReceive(Context context, Intent intent) {
            temp = intent.getStringExtra("notification_event");
            Log.d("test", "temp" +":" +temp);
            speakOut();
        }
    }



}